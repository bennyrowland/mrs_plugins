__author__ = 'ben'

from PySide import QtCore, QtGui
import os


lcmodel_basis_dir = "/home/spectre/.lcmodel/basis-sets/provencher"


class LCModelAuxiliary(QtGui.QWidget):
    def __init__(self, params_dict=None):
        QtGui.QWidget.__init__(self)
        self.setMinimumWidth(178)
        layout = QtGui.QVBoxLayout()
        layout.setContentsMargins(4, 4, 4, 4)
        basis_set_layout = QtGui.QHBoxLayout()
        basis_set_label = QtGui.QLabel("Basis Set")
        basis_set_layout.addWidget(basis_set_label)
        self.basis_set_combo = QtGui.QComboBox()
        self.basis_set_combo.setMaximumWidth(120)
        basis_set_layout.addWidget(self.basis_set_combo)
        # populate the basis set combo box with the standard basis sets
        for filename in os.listdir(lcmodel_basis_dir):
            full_name = os.path.join(lcmodel_basis_dir, filename)
            name, extension = os.path.splitext(filename)
            if os.path.isfile(full_name) and extension.lower() == ".basis":
                self.basis_set_combo.addItem(filename)
        if params_dict is not None and "FILBAS" in params_dict:
            current_basis_set = params_dict["FILBAS"]
            if os.path.commonprefix([current_basis_set, lcmodel_basis_dir]) == lcmodel_basis_dir:
                current_basis_set = os.path.basename(current_basis_set)
            for i in range(self.basis_set_combo.count()):
                if self.basis_set_combo.itemText(i) == current_basis_set:
                    self.basis_set_combo.setCurrentIndex(i)
                    break
            else:
                self.basis_set_combo.addItem(current_basis_set)
                self.basis_set_combo.setCurrentIndex(self.basis_set_combo.count() - 1)

        basis_set_browse = QtGui.QPushButton()
        icon = QtGui.QIcon.fromTheme("system-file-manager")
        basis_set_browse.setIcon(icon)
        basis_set_browse.setIconSize(QtCore.QSize(16, 16))
        basis_set_browse.setFixedSize(QtCore.QSize(24, 24))
        basis_set_layout.addWidget(basis_set_browse)
        layout.addLayout(basis_set_layout)
        #ecc_layout = QtGui.QHBoxLayout()
        self.ecc_checkbox = QtGui.QCheckBox("Do ECC")
        if params_dict is not None and "DOECC" in params_dict:
            if params_dict["DOECC"] == 'T':
                self.ecc_checkbox.setChecked(True)
            else:
                self.ecc_checkbox.setChecked(False)
        layout.addWidget(self.ecc_checkbox)
        self.setLayout(layout)

    def get_basis_set(self):
        if os.path.isfile(self.basis_set_combo.currentText()):
            return self.basis_set_combo.currentText()
        elif os.path.isfile(os.path.join(lcmodel_basis_dir, self.basis_set_combo.currentText())):
            return os.path.join(lcmodel_basis_dir, self.basis_set_combo.currentText())
        else:
            return os.path.join(lcmodel_basis_dir, self.basis_set_combo.itemText(0))


def lcmodel_process_step(index, params_dict=None):
    # set the name of the step
    index.model().setData(index.model().index(index.row(), 0, index.parent()), "LCModel Analysis")
    # build the auxiliary widget
    #widget = QtGui.QWidget()
    #widget.setMinimumWidth(178)
    widget = LCModelAuxiliary(params_dict)
    index.model().setData(index.model().index(index.row(), 2, index.parent()), widget)
    # add the "Data" input
    input_list_index = index.model().index(1, 0, index)
    index.model().insertRow(0, input_list_index)
    index.model().setData(index.model().index(0, 0, input_list_index), "Data")
    index.model().setData(index.model().index(0, 1, input_list_index), 1)
    # add the "Plot" output
    output_list_index = index.model().index(0, 0, index)
    index.model().insertRow(0, output_list_index)
    index.model().setData(index.model().index(0, 0, output_list_index), "Plot")
    index.model().setData(index.model().index(0, 1, output_list_index), 2)
    # add the "Concentrations" output
    output_list_index = index.model().index(0, 0, index)
    index.model().insertRow(1, output_list_index)
    index.model().setData(index.model().index(1, 0, output_list_index), "Concentrations")
    index.model().setData(index.model().index(1, 1, output_list_index), 3)
    if params_dict is not None:
        if "pos" in params_dict:
            print "setting pos"
            position = QtCore.QPointF(params_dict["pos"]["x"], params_dict["pos"]["y"])
            print position
            index.model().setData(index.model().index(index.row(), 1, index.parent()), position)


def lcmodel_process_dict(index):
    # get the auxiliary widget
    aux = index.model().data(index.model().index(index.row(), 2, index.parent()), QtCore.Qt.UserRole)
    return {"FILBAS": aux.get_basis_set(),
            "DOECC": 'T' if aux.ecc_checkbox.isChecked() else 'F'}