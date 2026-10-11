import csv
import io
import tempfile
import unittest
from pathlib import Path
from service import Product

class PipelineChecks(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.app=Product(Path(self.temp.name))
    def tearDown(self):
        self.temp.cleanup()
    def test_trained_model_excludes_scored_day(self):
        state=self.app.state()
        self.assertEqual(state['model']['training_rows'],1008)
        self.assertGreater(state['model']['training_rows'],len(state['measures']))
        anomalies=[row for row in state['measures'] if row['anomaly']]
        self.assertTrue(any(row['station_id']=='central' for row in anomalies))
        self.assertTrue(all(len(model['coefficients'])==3 for model in state['model']['stations'].values()))
    def test_rerun_is_idempotent_and_raw_file_persists(self):
        before=self.app.state()['warehouse_rows']
        result=self.app.action('run',{'csv':self.app.fixture('observations.csv'),'label':'repeat'})
        self.assertEqual(result['accepted'],0)
        self.assertEqual(result['duplicates'],144)
        self.assertEqual(self.app.state()['warehouse_rows'],before)
        self.assertTrue((Path(self.temp.name)/result['raw_file']).is_file())
    def test_bad_rows_are_quarantined_without_entering_ods(self):
        result=self.app.action('run',{'csv':'station_id,observed_at,count\ncentral,invalid,-4\n','label':'bad'})
        self.assertEqual(result['rejected'],1)
        self.assertEqual(result['accepted'],0)
        self.assertEqual(self.app.state()['runs'][0]['status'],'quality warning')
    def test_model_and_data_survive_restart(self):
        initial=self.app.state()
        fresh=Product(Path(self.temp.name)).state()
        self.assertEqual(fresh['model']['sha256'],initial['model']['sha256'])
        self.assertEqual(fresh['warehouse_rows'],initial['warehouse_rows'])
    def test_export_has_actual_predictions_and_flags(self):
        result=self.app.action('export',{'station_id':'central'})
        rows=list(csv.DictReader(io.StringIO(result['content'])))
        self.assertEqual(len(rows),24)
        self.assertIn('predicted',rows[0])
        self.assertTrue(any(row['anomaly']=='True' for row in rows))

if __name__=='__main__':
    unittest.main()
