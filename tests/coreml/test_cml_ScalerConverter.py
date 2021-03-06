"""
Tests CoreML Scaler converter.
"""
import unittest
import numpy
import coremltools
from sklearn.preprocessing import StandardScaler
from onnxmltools.convert.coreml.convert import convert
from onnxmltools.utils import dump_data_and_model


class TestCoreMLScalerConverter(unittest.TestCase):

    def test_scaler(self):
        model = StandardScaler()
        data = numpy.array([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]], dtype=numpy.float32)
        model.fit(data)
        model_coreml = coremltools.converters.sklearn.convert(model)
        model_onnx = convert(model_coreml.get_spec())
        self.assertTrue(model_onnx is not None)
        dump_data_and_model(data, model, model_onnx, basename="CmlStandardScalerFloat32")

        
if __name__ == "__main__":
    unittest.main()
