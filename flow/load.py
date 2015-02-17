__author__ = 'ben'

from PySide import QtCore, QtGui


class EditButton(QtGui.QPushButton):
    index = None

    def set_index(self, new_index):
        self.index = QtCore.QPersistentModelIndex(new_index)

    def edit(self):
        print "editing %s" % self.index


def twix_load_step(index, params_dict=None):
    # set the name of the step
    index.model().setData(index.model().index(index.row(), 0, index.parent()), "TWIX")
    # build and set the auxiliary widget
    #widget = QtGui.QWidget()
    #widget.setMinimumWidth(178)
    #layout = QtGui.QHBoxLayout()
    #layout.setContentsMargins(4, 4, 4, 4)
    #layout.addStretch()
    #edit_button = EditButton("Edit")
    #edit_button.set_index(index)
    #edit_button.clicked.connect(edit_button.edit)
    #layout.addWidget(edit_button)
    #widget.setLayout(layout)
    #index.model().setData(index.model().index(index.row(), 2, index.parent()), widget)
    if params_dict is not None:
        if "pos" in params_dict:
            position = QtCore.QPointF(params_dict["pos"]["x"], params_dict["pos"]["y"])
            index.model().setData(index.model().index(index.row(), 1, index.parent()), position)
        if "protocols" in params_dict:
            for protocol_name in params_dict["protocols"]:
                # add a sample output
                output_list_index = index.model().index(0, 0, index)
                index.model().insertRow(index.model().rowCount(output_list_index), output_list_index)
                # name the sample output
                output_index = index.model().index(index.model().rowCount(output_list_index) - 1, 0, output_list_index)
                index.model().setData(output_index, protocol_name)
        else:
            # add a sample output
            output_list_index = index.model().index(0, 0, index)
            index.model().insertRow(0, output_list_index)
            # name the sample output
            output_index = index.model().index(0, 0, output_list_index)
            index.model().setData(output_index, "filename.dat")


def twix_load_dict(index):
    save_dict = {}
    output_list_index = index.model().index(0, 0, index)
    number_of_outputs = index.model().rowCount(output_list_index)
    protocol_list = []
    for i in range(number_of_outputs):
        output_name = index.model().data(index.model().index(i, 0, output_list_index), QtCore.Qt.DisplayRole)
        protocol_list.append(output_name)
    save_dict["protocols"] = protocol_list
    return save_dict


def rda_load_step(index, params_dict=None):
    # set the name of the step
    index.model().setData(index.model().index(index.row(), 0, index.parent()), "RDA")
    if params_dict is not None:
        if "pos" in params_dict:
            position = QtCore.QPointF(params_dict["pos"]["x"], params_dict["pos"]["y"])
            index.model().setData(index.model().index(index.row(), 1, index.parent()), position)
        if "protocols" in params_dict:
            output_list_index = index.model().index(0, 0, index)
            for protocol_name in params_dict["protocols"]:
                index.model().insertRow(index.model().rowCount(output_list_index), output_list_index)
                output_index = index.model().index(index.model().rowCount(output_list_index) - 1, 0, output_list_index)
                index.model().setData(output_index, protocol_name)
                # set the type to 1
                index.model().setData(index.model().index(index.model().rowCount(output_list_index) - 1, 1, output_list_index), 1)
        else:
            # add a sample output
            output_list_index = index.model().index(0, 0, index)
            index.model().insertRow(0, output_list_index)
            # name the sample output
            output_index = index.model().index(0, 0, output_list_index)
            index.model().setData(output_index, "filename.dat")


def rda_load_dict(index):
    save_dict = {}
    output_list_index = index.model().index(0, 0, index)
    number_of_outputs = index.model().rowCount(output_list_index)
    protocol_list = []
    for i in range(number_of_outputs):
        output_name = index.model().data(index.model().index(i, 0, output_list_index), QtCore.Qt.DisplayRole)
        protocol_list.append(output_name)
    save_dict["protocols"] = protocol_list
    return save_dict