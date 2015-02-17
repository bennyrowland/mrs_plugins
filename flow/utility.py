__author__ = 'ben'

from PySide import QtCore, QtGui


def ps2pdf_step(index, params_dict=None):
    # set the name
    index.model().setData(index.model().index(index.row(), 0, index.parent()), "PS to PDF")
    # add the "PS" input
    input_list_index = index.model().index(1, 0, index)
    index.model().insertRow(0, input_list_index)
    index.model().setData(index.model().index(0, 0, input_list_index), "PS")
    index.model().setData(index.model().index(0, 1, input_list_index), 2)
    # add the "PDF" output
    output_list_index = index.model().index(0, 0, index)
    index.model().insertRow(0, output_list_index)
    index.model().setData(index.model().index(0, 0, output_list_index), "PDF")
    index.model().setData(index.model().index(0, 1, output_list_index), 4)
    if params_dict is not None:
        if "pos" in params_dict:
            position = QtCore.QPointF(params_dict["pos"]["x"], params_dict["pos"]["y"])
            index.model().setData(index.model().index(index.row(), 1, index.parent()), position)


def ps2pdf_dict(index):
    return {}


def mail_step(index, params_dict=None):
    # set the name
    index.model().setData(index.model().index(index.row(), 0, index.parent()), "Mail")
    # add the "Attachments" input
    input_list_index = index.model().index(1, 0, index)
    index.model().insertRow(0, input_list_index)
    index.model().setData(index.model().index(0, 0, input_list_index), "Attachments")
    index.model().setData(index.model().index(0, 1, input_list_index), 4)
    # build the auxiliary widget
    widget = QtGui.QWidget()
    widget.setMinimumWidth(178)
    index.model().setData(index.model().index(index.row(), 2, index.parent()), widget)
    layout = QtGui.QFormLayout()
    layout.setContentsMargins(4, 4, 4, 4)
    recipient_edit = QtGui.QLineEdit()
    recipient_edit.setObjectName("recipients")
    layout.addRow("To", recipient_edit)
    widget.setLayout(layout)
    if params_dict is not None:
        if "pos" in params_dict:
            position = QtCore.QPointF(params_dict["pos"]["x"], params_dict["pos"]["y"])
            print "setting pos to %s" % str(position)
            index.model().setData(index.model().index(index.row(), 1, index.parent()), position)
        if "send_to" in params_dict:
            recipient_edit.setText(";".join(params_dict["send_to"]))


def mail_dict(index):
    auxiliary_widget = index.model().data(index.model().index(index.row(), 2, index.parent()), QtCore.Qt.UserRole)
    recipient_edit = auxiliary_widget.findChild(QtGui.QLineEdit, "recipients")
    recipient_string = recipient_edit.text()
    recipients = recipient_string.split(";")
    # get the number of attachments connected to our first input
    input_list_index = index.model().index(1, 0, index)
    num_attachments = index.model().rowCount(index.model().index(0, 0, input_list_index))
    return {"send_to": [recipient.strip() for recipient in recipients],
            "attachments": num_attachments}


def wref_step(index, params_dict=None):
    # set the name
    index.model().setData(index.model().index(index.row(), 0, index.parent()), "Add Water Ref")
    # add the "Data" input
    input_list_index = index.model().index(1, 0, index)
    index.model().insertRow(0, input_list_index)
    index.model().setData(index.model().index(0, 0, input_list_index), "Data")
    index.model().setData(index.model().index(0, 1, input_list_index), 1)
    # add the "Wref" input
    input_list_index = index.model().index(1, 0, index)
    index.model().insertRow(1, input_list_index)
    index.model().setData(index.model().index(1, 0, input_list_index), "Water Ref")
    index.model().setData(index.model().index(1, 1, input_list_index), 1)
    # add the "Data" output
    output_list_index = index.model().index(0, 0, index)
    index.model().insertRow(0, output_list_index)
    index.model().setData(index.model().index(0, 0, output_list_index), "Data")
    index.model().setData(index.model().index(0, 1, output_list_index), 1)
    if params_dict is not None:
        if "pos" in params_dict:
            position = QtCore.QPointF(params_dict["pos"]["x"], params_dict["pos"]["y"])
            index.model().setData(index.model().index(index.row(), 1, index.parent()), position)


def wref_dict(index):
    return {}