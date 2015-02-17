__author__ = 'ben'

from PySide import QtCore


def twix_svs_step(index, params_dict=None):
    # set the name
    index.model().setData(index.model().index(index.row(), 0, index.parent()), "SVS Recon")
    # add the "Data" input
    input_list_index = index.model().index(1, 0, index)
    index.model().insertRow(0, input_list_index)
    index.model().setData(index.model().index(0, 0, input_list_index), "Data")
    # add the "WRef" input
    index.model().insertRow(1, input_list_index)
    index.model().setData(index.model().index(1, 0, input_list_index), "Water Ref")
    # add the "Data" output
    output_list_index = index.model().index(0, 0, index)
    index.model().insertRow(0, output_list_index)
    index.model().setData(index.model().index(0, 0, output_list_index), "Data")
    index.model().setData(index.model().index(0, 1, output_list_index), 1)
    if params_dict is not None:
        if "pos" in params_dict:
            position = QtCore.QPointF(params_dict["pos"]["x"], params_dict["pos"]["y"])
            index.model().setData(index.model().index(index.row(), 1, index.parent()), position)


def twix_svs_dict(index):
    return {}