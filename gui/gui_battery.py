#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2018 Julius Susanto. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

"""
CENTAUR: Hybrid Power System Simulation

Battery Tab

Authors: Julius Susanto
Last edited: January 2018
"""

from PyQt5 import QtGui, QtWidgets
import numpy as np
import gui.globals as globals
import gui.utility as utility
                      
class battery_ui(QtWidgets.QWidget): 
    
    def setup(self, window):   
        """Set up and initialise battery tab"""
        
        self.main_window = window        
        
        title1 = QtWidgets.QLabel('Battery configuration')
        title1.setFont(QtGui.QFont('arial', weight=QtGui.QFont.Bold))
        
        label1 = QtWidgets.QLabel('No. batteries:')
        label1.setFixedWidth(100)
        
        self.edit_nBatt = QtWidgets.QLineEdit()
        self.edit_nBatt.setFixedWidth(100)
        
        label2a = QtWidgets.QLabel('Nominal capacity:')
        label2a.setFixedWidth(100)
        label2b = QtWidgets.QLabel('Ah')
        
        self.edit_Cnom = QtWidgets.QLineEdit()
        self.edit_Cnom.setFixedWidth(100)
        
        label3a = QtWidgets.QLabel('Nominal voltage:')
        label3a.setFixedWidth(100)
        label3b = QtWidgets.QLabel('Vdc')
        label3b.setFixedWidth(50)
        
        self.edit_Vdc = QtWidgets.QLineEdit()
        self.edit_Vdc.setFixedWidth(100)
        
        title2 = QtWidgets.QLabel('Battery discharge characteristics')
        title2.setFont(QtGui.QFont('arial', weight=QtGui.QFont.Bold))
        
        headings = ['Time (hours)', 'Capacity (A)']
        self.tableWidget = SolarTable(window, headings = headings, alternatingRowColors = True)
        #self.tableWidget.setMinimumHeight(200)
        
        vline = QtWidgets.QFrame()
        vline.setFrameStyle(QtWidgets.QFrame.VLine | QtWidgets.QFrame.Sunken)
        
        title3 = QtWidgets.QLabel('Battery charge parameters')
        title3.setFont(QtGui.QFont('arial', weight=QtGui.QFont.Bold))
        
        label4a = QtWidgets.QLabel('Battery converter / inverter efficiency:')
        label4b = QtWidgets.QLabel('%')
        
        self.edit_effConv = QtWidgets.QLineEdit()
        self.edit_effConv.setFixedWidth(100)
        
        label5a = QtWidgets.QLabel('Battery initial state of charge:')
        label5b = QtWidgets.QLabel('%')
        
        self.edit_initSOC = QtWidgets.QLineEdit()
        self.edit_initSOC.setFixedWidth(100)
        
        label6a = QtWidgets.QLabel('Battery minimum state of charge:')
        label6b = QtWidgets.QLabel('%')
        
        self.edit_minSOC = QtWidgets.QLineEdit()
        self.edit_minSOC.setFixedWidth(100)
        
        title4 = QtWidgets.QLabel('Battery ramp control parameters')
        title4.setFont(QtGui.QFont('arial', weight=QtGui.QFont.Bold))
        
        label7a = QtWidgets.QLabel('PV output setpoint for ramp control:')
        label7b = QtWidgets.QLabel('W')
        
        self.edit_Pset = QtWidgets.QLineEdit()
        self.edit_Pset.setFixedWidth(100)
        
        label8a = QtWidgets.QLabel('Ramp control start time:')
        label8b = QtWidgets.QLabel('hour')
        
        self.edit_Ton = QtWidgets.QLineEdit()
        self.edit_Ton.setFixedWidth(100)
        
        label9a = QtWidgets.QLabel('Ramp control stop time:')
        label9b = QtWidgets.QLabel('hour')
        
        self.edit_Toff = QtWidgets.QLineEdit()
        self.edit_Toff.setFixedWidth(100)
        
        label10a = QtWidgets.QLabel('Cycle charging SOC setpoint:')
        label10b = QtWidgets.QLabel('%')
        
        self.edit_SOC_cyc = QtWidgets.QLineEdit()
        self.edit_SOC_cyc.setFixedWidth(100)
        
        layout = QtWidgets.QGridLayout()
        layout.addWidget(title1, 0, 0)
        layout.addWidget(label1, 1, 0)
        layout.addWidget(self.edit_nBatt, 1, 1)
        layout.addWidget(label2a, 2, 0)
        layout.addWidget(self.edit_Cnom, 2, 1)
        layout.addWidget(label2b, 2, 2)
        layout.addWidget(label3a, 3, 0)
        layout.addWidget(self.edit_Vdc, 3, 1)
        layout.addWidget(label3b, 3, 2)
        layout.addWidget(title2, 4, 0, 1, 2)
        layout.addWidget(self.tableWidget, 5, 0, 10, 3)
        layout.addWidget(vline, 0, 3, 15, 3)
        layout.addWidget(title3, 0, 4)
        layout.addWidget(label4a, 1, 4)
        layout.addWidget(self.edit_effConv, 1, 5)
        layout.addWidget(label4b, 1, 6)
        layout.addWidget(label5a, 2, 4)
        layout.addWidget(self.edit_initSOC, 2, 5)
        layout.addWidget(label5b, 2, 6)
        layout.addWidget(label6a, 3, 4)
        layout.addWidget(self.edit_minSOC, 3, 5)
        layout.addWidget(label6b, 3, 6)
        layout.addWidget(label10a, 4, 4)
        layout.addWidget(self.edit_SOC_cyc, 4, 5)
        layout.addWidget(label10b, 4, 6)
        layout.addWidget(title4, 5, 4)
        layout.addWidget(label7a, 6, 4)
        layout.addWidget(self.edit_Pset, 6, 5)
        layout.addWidget(label7b, 6, 6)
        layout.addWidget(label8a, 7, 4)
        layout.addWidget(self.edit_Ton, 7, 5)
        layout.addWidget(label8b, 7, 6)
        layout.addWidget(label9a, 8, 4)
        layout.addWidget(self.edit_Toff, 8, 5)
        layout.addWidget(label9b, 8, 6)
        self.setLayout(layout)

        self.edit_nBatt.editingFinished.connect(utility.create_validation_hook(self, self.edit_nBatt, "Number of batteries", 0, 99999))
        
        self.edit_Cnom.editingFinished.connect(utility.create_validation_hook(self, self.edit_Cnom, "Nominal capacity", 0, 99999))
        self.edit_Vdc.editingFinished.connect(utility.create_validation_hook(self, self.edit_Vdc, "Nominal DC voltage", 0, 99999))
        self.edit_effConv.editingFinished.connect(utility.create_validation_hook(self, self.edit_effConv, "Battery converter / inverter efficiency", 0, 100))
        self.edit_initSOC.editingFinished.connect(utility.create_validation_hook(self, self.edit_initSOC, "Battery initial state of charge", 0, 100))
        self.edit_minSOC.editingFinished.connect(utility.create_validation_hook(self, self.edit_minSOC, "Battery minimum state of charge", 0, 100))
        self.edit_SOC_cyc.editingFinished.connect(utility.create_validation_hook(self, self.edit_SOC_cyc, "Cycle charging SOC setpoint", 0, 100))
        self.edit_Pset.editingFinished.connect(utility.create_validation_hook(self, self.edit_Pset, "PV output setpoint for ramp control", 0, 9999999))
        self.edit_Ton.editingFinished.connect(utility.create_validation_hook(self, self.edit_Ton, "Ramp control start time", 0, 23))
        self.edit_Toff.editingFinished.connect(utility.create_validation_hook(self, self.edit_Toff, "Ramp control stop time", 0, 23))
        
        self.tableWidget.itemChanged.connect(self.update_data_matrix)

        self.refresh_data()  
    
    def update_data(self):
        """Update global variables to match GUI fields"""
        globals.batt_data['n_batt'] = int(self.edit_nBatt.text())
        globals.batt_data['C_nom'] = float(self.edit_Cnom.text())
        globals.batt_data['v_dc'] = float(self.edit_Vdc.text())
        globals.batt_data['eff_conv'] = float(self.edit_effConv.text())
        globals.batt_data['SOC_0'] = float(self.edit_initSOC.text())
        globals.batt_data['SOC_min'] = float(self.edit_minSOC.text())
        globals.batt_data['SOC_cyc'] = float(self.edit_SOC_cyc.text())
        globals.batt_data['p_set'] = float(self.edit_Pset.text())
        globals.batt_data['t_set'][0] = int(self.edit_Ton.text())
        globals.batt_data['t_set'][1] = int(self.edit_Toff.text())
        
    def update_data_matrix(self, tableWidgetItem): 
        """Update battery constants whenever table data is changed"""
        value = 0.0
        if tableWidgetItem.column() == 0:
            element = "Discharge Time"
            lower_bound = 0.0
            upper_bound = 999999
            value = utility.validate(tableWidgetItem.text(), lower_bound, upper_bound, l_inclusive = True, u_inclusive = False)
        elif tableWidgetItem.column() == 1:
            element = "Discharge Current"
            lower_bound = 0.0
            upper_bound = 999999
            value = utility.validate(tableWidgetItem.text(), lower_bound, upper_bound, l_inclusive = True, u_inclusive = False)
        
        if value is not False:   
            columns = [0,1]            
            column = columns[tableWidgetItem.column()]
            update_mapping = (globals.batt_char[tableWidgetItem.row(), column] != value)            
            globals.batt_char[tableWidgetItem.row(), column] = value
            #tableWidgetItem.setText(str(value))
            
        else:
            self.main_window.show_status_message(element + " Row " + str(tableWidgetItem.row() + 1) + ": Input value '" + tableWidgetItem.text() + "' out of bounds. (" + str(lower_bound) + " to " + str(upper_bound) + "). Value not set.", error = True, beep = True)
            self.tableWidget.itemChanged.disconnect()
            self.refresh_data()          
            self.tableWidget.itemChanged.connect(self.update_data_matrix)            
        
    def refresh_data(self):
        """Update GUI fields to match global variables"""
        self.edit_nBatt.setText(str(globals.batt_data['n_batt']))
        self.edit_Cnom.setText(str(globals.batt_data['C_nom']))
        self.edit_Vdc.setText(str(globals.batt_data['v_dc']))
        self.edit_effConv.setText(str(globals.batt_data['eff_conv']))
        self.edit_initSOC.setText(str(globals.batt_data['SOC_0']))
        self.edit_minSOC.setText(str(globals.batt_data['SOC_min']))
        self.edit_SOC_cyc.setText(str(globals.batt_data['SOC_cyc']))
        self.edit_Pset.setText(str(globals.batt_data['p_set']))
        self.edit_Ton.setText(str(globals.batt_data['t_set'][0]))
        self.edit_Toff.setText(str(globals.batt_data['t_set'][1]))
        
        self.tableWidget.fill_table(globals.batt_char)
            
class SolarTable(utility.CentaurTable): 
    """Modified version of LowFi table specifically for the Right Of Way tab."""

    def signal_mapping(signal_mapper):
        self.signal_mapper = signal_mapper

    def fill_table(self, data):
        """Fill table from 2D list or numpy array."""
        if len(data) > 0:
            if isinstance(data, np.ndarray):
                data = data.tolist()
            data_rows = len(data)
            data_columns = len(data[0])
            
            if data_columns > 0:
                self.setRowCount(data_rows)
                for r in range(0, data_rows):
                    # Update real columns
                    for c in range(2):
                        item = QtWidgets.QTableWidgetItem()                        
                        item.setText(str(data[r][c]))      
                        self.setItem(r, c, item)