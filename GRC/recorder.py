#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Recorder
# Generated: Sat Sep 26 01:34:28 2020
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import ieee802_11
import osmosdr
import sip
import sys
import time
from gnuradio import qtgui


class recorder(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Recorder")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Recorder")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "recorder")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.window_size = window_size = 960
        self.sync_length = sync_length = 320
        self.samp_rate = samp_rate = 20000000
        self.rf_gain = rf_gain = 14
        self.lo_offset = lo_offset = 0
        self.if_gain = if_gain = 24
        self.freq = freq = 2437000000
        self.chan_est = chan_est = 0
        self.bb_gain = bb_gain = 30

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_options = (5000000, 10000000, 20000000, )
        self._samp_rate_labels = (str(self._samp_rate_options[0]), str(self._samp_rate_options[1]), str(self._samp_rate_options[2]), )
        self._samp_rate_tool_bar = Qt.QToolBar(self)
        self._samp_rate_tool_bar.addWidget(Qt.QLabel("samp_rate"+": "))
        self._samp_rate_combo_box = Qt.QComboBox()
        self._samp_rate_tool_bar.addWidget(self._samp_rate_combo_box)
        for label in self._samp_rate_labels: self._samp_rate_combo_box.addItem(label)
        self._samp_rate_callback = lambda i: Qt.QMetaObject.invokeMethod(self._samp_rate_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._samp_rate_options.index(i)))
        self._samp_rate_callback(self.samp_rate)
        self._samp_rate_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_samp_rate(self._samp_rate_options[i]))
        self.top_layout.addWidget(self._samp_rate_tool_bar)
        self._rf_gain_range = Range(0, 14, 7, 14, 200)
        self._rf_gain_win = RangeWidget(self._rf_gain_range, self.set_rf_gain, "rf_gain", "counter_slider", float)
        self.top_grid_layout.addWidget(self._rf_gain_win, 2, 1, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(2,3)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(1,2)]
        self._if_gain_range = Range(0, 40, 8, 24, 200)
        self._if_gain_win = RangeWidget(self._if_gain_range, self.set_if_gain, "if_gain", "counter_slider", float)
        self.top_grid_layout.addWidget(self._if_gain_win, 3, 0, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(3,4)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,1)]
        self._freq_options = [2412000000.0, 2417000000.0, 2422000000.0, 2427000000.0, 2432000000.0, 2437000000.0, 2442000000.0, 2447000000.0, 2452000000.0, 2457000000.0, 2462000000.0, 2467000000.0, 2472000000.0, 2484000000.0, 5170000000.0, 5180000000.0, 5190000000.0, 5200000000.0, 5210000000.0, 5220000000.0, 5230000000.0, 5240000000.0, 5250000000.0, 5260000000.0, 5270000000.0, 5280000000.0, 5290000000.0, 5300000000.0, 5310000000.0, 5320000000.0, 5500000000.0, 5510000000.0, 5520000000.0, 5530000000.0, 5540000000.0, 5550000000.0, 5560000000.0, 5570000000.0, 5580000000.0, 5590000000.0, 5600000000.0, 5610000000.0, 5620000000.0, 5630000000.0, 5640000000.0, 5660000000.0, 5670000000.0, 5680000000.0, 5690000000.0, 5700000000.0, 5710000000.0, 5720000000.0, 5745000000.0, 5755000000.0, 5765000000.0, 5775000000.0, 5785000000.0, 5795000000.0, 5805000000.0, 5825000000.0, 5860000000.0, 5870000000.0, 5880000000.0, 5890000000.0, 5900000000.0, 5910000000.0, 5920000000.0]
        self._freq_labels = ['  1 | 2412.0 | 11g', '  2 | 2417.0 | 11g', '  3 | 2422.0 | 11g', '  4 | 2427.0 | 11g', '  5 | 2432.0 | 11g', '  6 | 2437.0 | 11g', '  7 | 2442.0 | 11g', '  8 | 2447.0 | 11g', '  9 | 2452.0 | 11g', ' 10 | 2457.0 | 11g', ' 11 | 2462.0 | 11g', ' 12 | 2467.0 | 11g', ' 13 | 2472.0 | 11g', ' 14 | 2484.0 | 11g', ' 34 | 5170.0 | 11a', ' 36 | 5180.0 | 11a', ' 38 | 5190.0 | 11a', ' 40 | 5200.0 | 11a', ' 42 | 5210.0 | 11a', ' 44 | 5220.0 | 11a', ' 46 | 5230.0 | 11a', ' 48 | 5240.0 | 11a', ' 50 | 5250.0 | 11a', ' 52 | 5260.0 | 11a', ' 54 | 5270.0 | 11a', ' 56 | 5280.0 | 11a', ' 58 | 5290.0 | 11a', ' 60 | 5300.0 | 11a', ' 62 | 5310.0 | 11a', ' 64 | 5320.0 | 11a', '100 | 5500.0 | 11a', '102 | 5510.0 | 11a', '104 | 5520.0 | 11a', '106 | 5530.0 | 11a', '108 | 5540.0 | 11a', '110 | 5550.0 | 11a', '112 | 5560.0 | 11a', '114 | 5570.0 | 11a', '116 | 5580.0 | 11a', '118 | 5590.0 | 11a', '120 | 5600.0 | 11a', '122 | 5610.0 | 11a', '124 | 5620.0 | 11a', '126 | 5630.0 | 11a', '128 | 5640.0 | 11a', '132 | 5660.0 | 11a', '134 | 5670.0 | 11a', '136 | 5680.0 | 11a', '138 | 5690.0 | 11a', '140 | 5700.0 | 11a', '142 | 5710.0 | 11a', '144 | 5720.0 | 11a', '149 | 5745.0 | 11a (SRD)', '151 | 5755.0 | 11a (SRD)', '153 | 5765.0 | 11a (SRD)', '155 | 5775.0 | 11a (SRD)', '157 | 5785.0 | 11a (SRD)', '159 | 5795.0 | 11a (SRD)', '161 | 5805.0 | 11a (SRD)', '165 | 5825.0 | 11a (SRD)', '172 | 5860.0 | 11p', '174 | 5870.0 | 11p', '176 | 5880.0 | 11p', '178 | 5890.0 | 11p', '180 | 5900.0 | 11p', '182 | 5910.0 | 11p', '184 | 5920.0 | 11p']
        self._freq_tool_bar = Qt.QToolBar(self)
        self._freq_tool_bar.addWidget(Qt.QLabel("freq"+": "))
        self._freq_combo_box = Qt.QComboBox()
        self._freq_tool_bar.addWidget(self._freq_combo_box)
        for label in self._freq_labels: self._freq_combo_box.addItem(label)
        self._freq_callback = lambda i: Qt.QMetaObject.invokeMethod(self._freq_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._freq_options.index(i)))
        self._freq_callback(self.freq)
        self._freq_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_freq(self._freq_options[i]))
        self.top_layout.addWidget(self._freq_tool_bar)
        self._chan_est_options = [ieee802_11.LS, ieee802_11.LMS, ieee802_11.STA, ieee802_11.COMB]
        self._chan_est_labels = ["LS", "LMS", "STA", "Linear Comb"]
        self._chan_est_group_box = Qt.QGroupBox("chan_est")
        self._chan_est_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._chan_est_button_group = variable_chooser_button_group()
        self._chan_est_group_box.setLayout(self._chan_est_box)
        for i, label in enumerate(self._chan_est_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._chan_est_box.addWidget(radio_button)
        	self._chan_est_button_group.addButton(radio_button, i)
        self._chan_est_callback = lambda i: Qt.QMetaObject.invokeMethod(self._chan_est_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._chan_est_options.index(i)))
        self._chan_est_callback(self.chan_est)
        self._chan_est_button_group.buttonClicked[int].connect(
        	lambda i: self.set_chan_est(self._chan_est_options[i]))
        self.top_layout.addWidget(self._chan_est_group_box)
        self._bb_gain_range = Range(0, 60, 2, 30, 200)
        self._bb_gain_win = RangeWidget(self._bb_gain_range, self.set_bb_gain, "bb_gain", "counter_slider", float)
        self.top_grid_layout.addWidget(self._bb_gain_win, 3, 1, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(3,4)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(1,2)]
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	48*10, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(rf_gain, 0)
        self.osmosdr_source_0.set_if_gain(if_gain, 0)
        self.osmosdr_source_0.set_bb_gain(bb_gain, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self._lo_offset_options = (0, 6e6, 11e6, )
        self._lo_offset_labels = (str(self._lo_offset_options[0]), str(self._lo_offset_options[1]), str(self._lo_offset_options[2]), )
        self._lo_offset_tool_bar = Qt.QToolBar(self)
        self._lo_offset_tool_bar.addWidget(Qt.QLabel("lo_offset"+": "))
        self._lo_offset_combo_box = Qt.QComboBox()
        self._lo_offset_tool_bar.addWidget(self._lo_offset_combo_box)
        for label in self._lo_offset_labels: self._lo_offset_combo_box.addItem(label)
        self._lo_offset_callback = lambda i: Qt.QMetaObject.invokeMethod(self._lo_offset_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._lo_offset_options.index(i)))
        self._lo_offset_callback(self.lo_offset)
        self._lo_offset_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_lo_offset(self._lo_offset_options[i]))
        self.top_layout.addWidget(self._lo_offset_tool_bar)
        self.ieee802_11_sync_short_0 = ieee802_11.sync_short(0.56, 2, False, False)
        self.ieee802_11_sync_long_0 = ieee802_11.sync_long(sync_length, True, False)
        self.ieee802_11_parse_mac_0 = ieee802_11.parse_mac(True, True)
        self.ieee802_11_moving_average_xx_1 = ieee802_11.moving_average_ff(window_size + 16)
        self.ieee802_11_moving_average_xx_0 = ieee802_11.moving_average_cc(window_size)
        self.ieee802_11_frame_equalizer_0 = ieee802_11.frame_equalizer(chan_est, freq, samp_rate, False, False)
        self.ieee802_11_decode_mac_0 = ieee802_11.decode_mac(True, False)
        self.fft_vxx_0 = fft.fft_vcc(64, True, (window.rectangular(64)), True, 1)
        self.fft_filter_xxx_0 = filter.fft_filter_ccc(1, ([3.475465564406477e-05, 3.921664392692037e-05, 4.3666452256729826e-05, 4.810490281670354e-05, 5.253248309600167e-05, 5.694930223398842e-05, 6.135496369097382e-05, 6.574857980012894e-05, 7.012864807620645e-05, 7.449306576745585e-05, 7.88389952504076e-05, 8.3162885857746e-05, 8.746036473894492e-05, 9.172626596409827e-05, 9.595452866051346e-05, 0.00010013821156462654, 0.00010426943481434137, 0.00010833935084519908, 0.00011233818077016622, 0.00011625513434410095, 0.00012007846817141399, 0.0001237954420503229, 0.0001273923262488097, 0.00013085441605653614, 0.00013416614092420787, 0.00013731095532421023, 0.00014027139695826918, 0.0001430292468285188, 0.00014556545647792518, 0.00014786020619794726, 0.00014989302144385874, 0.00015164281649049371, 0.00015308793808799237, 0.00015420628187712282, 0.00015497540880460292, 0.0001553725014673546, 0.00015537462604697794, 0.00015495868865400553, 0.0001541016681585461, 0.0001527806743979454, 0.000150972991832532, 0.00014865631237626076, 0.0001458088227082044, 0.00014240926248021424, 0.00013843717169947922, 0.00013387289072852582, 0.00012869780766777694, 0.00012289444566704333, 0.00011644652840914205, 0.00010933926387224346, 0.00010155932977795601, 9.309507731813937e-05, 8.393668395001441e-05, 7.407623343169689e-05, 6.350783951347694e-05, 5.2227820560801774e-05, 4.023476139991544e-05, 2.7529658837011084e-05, 1.4116030797595158e-05, -1.1277033424057267e-19, -1.4809590538789053e-05, -3.03010965581052e-05, -4.645998342311941e-05, -6.32687660981901e-05, -8.070691546890885e-05, -9.875082469079643e-05, -0.00011737374734366313, -0.00013654578651767224, -0.00015623382932972163, -0.00017640153237152845, -0.00019700932898558676, -0.00021801443654112518, -0.00023937092919368297, -0.000261029606917873, -0.00028293815557844937, -0.00030504129244945943, -0.00032728054793551564, -0.0003495945711620152, -0.00037191930459812284, -0.0003941877803299576, -0.0004163304402027279, -0.00043827531044371426, -0.0004599479725584388, -0.00048127182526513934, -0.0005021682009100914, -0.0005225568311288953, -0.0005423553520813584, -0.0005614803521893919, -0.0005798469064757228, -0.0005973691586405039, -0.0006139606120996177, -0.0006295338971540332, -0.000644001760520041, -0.0006572765414603055, -0.0006692712777294219, -0.0006798990070819855, -0.0006890740478411317, -0.0006967115914449096, -0.000702728284522891, -0.0007070426363497972, -0.0007095747860148549, -0.0007102476083673537, -0.0007089864229783416, -0.0007057195180095732, -0.0007003784994594753, -0.0006928984075784683, -0.0006832184735685587, -0.000671281770337373, -0.000657036027405411, -0.0006404338637366891, -0.0006214328459464014, -0.0005999959539622068, -0.000576091930270195, -0.0005496952799148858, -0.0005207868525758386, -0.0004893539007753134, -0.00045539034181274474, -0.0004188970779068768, -0.0003798819670919329, -0.00033836046350188553, -0.00029435535543598235, -0.00024789711460471153, -0.0001990241144085303, -0.0001477827172493562, -9.422734729014337e-05, -3.842059595626779e-05, 1.9566638002288528e-05, 7.965514669194818e-05, 0.0001417573803337291, 0.00020577735267579556, 0.0002716107410378754, 0.00033914492814801633, 0.0004082589002791792, 0.00047882343642413616, 0.000550701399333775, 0.0006237471825443208, 0.0006978079327382147, 0.0007727226475253701, 0.0008483228739351034, 0.0009244330576620996, 0.0010008704848587513, 0.0010774459224194288, 0.0011539628030732274, 0.0012302196118980646, 0.0013060078490525484, 0.0013811138924211264, 0.0014553191140294075, 0.0015284003457054496, 0.00160012929700315, 0.001670274417847395, 0.0017386004328727722, 0.0018048692727461457, 0.0018688400741666555, 0.0019302699947729707, 0.001988915028050542, 0.0020445294212549925, 0.002096867887303233, 0.0021456845570355654, 0.0021907349582761526, 0.0022317746188491583, 0.002268562326207757, 0.002300858497619629, 0.002328426344320178, 0.002351032802835107, 0.002368449466302991, 0.0023804516531527042, 0.002386821433901787, 0.0023873455356806517, 0.002381817903369665, 0.0023700387682765722, 0.0023518172092735767, 0.0023269695229828358, 0.0022953213192522526, 0.0022567075211554766, 0.002210972597822547, 0.0021579712629318237, 0.002097569638863206, 0.0020296447910368443, 0.001954086124897003, 0.001870793872512877, 0.0017796827014535666, 0.001680679153650999, 0.0015737236244603992, 0.001458770246244967, 0.0013357873540371656, 0.0012047573691233993, 0.0010656777303665876, 0.0009185601375065744, 0.0007634324138052762, 0.0006003368180245161, 0.00042933132499456406, 0.0002504894800949842, 6.390033377101645e-05, -0.0001303313038079068, -0.0003320850373711437, -0.0005412247264757752, -0.0007575987838208675, -0.0009810400661081076, -0.0012113659176975489, -0.0014483786653727293, -0.001691865618340671, -0.0019415994174778461, -0.002197337569668889, -0.002458824310451746, -0.0027257895562797785, -0.002997949253767729, -0.0032750072423368692, -0.00355665385723114, -0.0038425675593316555, -0.004132415167987347, -0.004425852559506893, -0.004722523968666792, -0.005022064782679081, -0.005324100144207478, -0.0056282468140125275, -0.005934113170951605, -0.006241301074624062, -0.006549403537064791, -0.006858009845018387, -0.007166701834648848, -0.007475059013813734, -0.007782654836773872, -0.008089061826467514, -0.0083938492462039, -0.008696584962308407, -0.008996834978461266, -0.009294169023633003, -0.009588155895471573, -0.009878363460302353, -0.010164367966353893, -0.01044574473053217, -0.010722074657678604, -0.010992946103215218, -0.011257949285209179, -0.011516684666275978, -0.011768758296966553, -0.012013785541057587, -0.012251392006874084, -0.012481208890676498, -0.01270288322120905, -0.012916072271764278, -0.013120441697537899, -0.013315673917531967, -0.013501462526619434, -0.013677516020834446, -0.013843556866049767, -0.013999324291944504, -0.014144569635391235, -0.014279062859714031, -0.014402593486011028, -0.014514961279928684, -0.014615988358855247, -0.014705514535307884, -0.014783395454287529, -0.014849507249891758, -0.014903743751347065, -0.01494601834565401, -0.014976263046264648, -0.014994428493082523, 0.9850320219993591, -0.014994428493082523, -0.014976263046264648, -0.01494601834565401, -0.014903743751347065, -0.014849507249891758, -0.014783395454287529, -0.014705514535307884, -0.014615988358855247, -0.014514961279928684, -0.014402593486011028, -0.014279062859714031, -0.014144569635391235, -0.013999324291944504, -0.013843556866049767, -0.013677516020834446, -0.013501462526619434, -0.013315673917531967, -0.013120441697537899, -0.012916072271764278, -0.01270288322120905, -0.012481208890676498, -0.012251392006874084, -0.012013785541057587, -0.011768758296966553, -0.011516684666275978, -0.011257949285209179, -0.010992946103215218, -0.010722074657678604, -0.01044574473053217, -0.010164367966353893, -0.009878363460302353, -0.009588155895471573, -0.009294169023633003, -0.008996834978461266, -0.008696584962308407, -0.0083938492462039, -0.008089061826467514, -0.007782654836773872, -0.007475059013813734, -0.007166701834648848, -0.006858009845018387, -0.006549403537064791, -0.006241301074624062, -0.005934113170951605, -0.0056282468140125275, -0.005324100144207478, -0.005022064782679081, -0.004722523968666792, -0.004425852559506893, -0.004132415167987347, -0.0038425675593316555, -0.00355665385723114, -0.0032750072423368692, -0.002997949253767729, -0.0027257895562797785, -0.002458824310451746, -0.002197337569668889, -0.0019415994174778461, -0.001691865618340671, -0.0014483786653727293, -0.0012113659176975489, -0.0009810400661081076, -0.0007575987838208675, -0.0005412247264757752, -0.0003320850373711437, -0.0001303313038079068, 6.390033377101645e-05, 0.0002504894800949842, 0.00042933132499456406, 0.0006003368180245161, 0.0007634324138052762, 0.0009185601375065744, 0.0010656777303665876, 0.0012047573691233993, 0.0013357873540371656, 0.001458770246244967, 0.0015737236244603992, 0.001680679153650999, 0.0017796827014535666, 0.001870793872512877, 0.001954086124897003, 0.0020296447910368443, 0.002097569638863206, 0.0021579712629318237, 0.002210972597822547, 0.0022567075211554766, 0.0022953213192522526, 0.0023269695229828358, 0.0023518172092735767, 0.0023700387682765722, 0.002381817903369665, 0.0023873455356806517, 0.002386821433901787, 0.0023804516531527042, 0.002368449466302991, 0.002351032802835107, 0.002328426344320178, 0.002300858497619629, 0.002268562326207757, 0.0022317746188491583, 0.0021907349582761526, 0.0021456845570355654, 0.002096867887303233, 0.0020445294212549925, 0.001988915028050542, 0.0019302699947729707, 0.0018688400741666555, 0.0018048692727461457, 0.0017386004328727722, 0.001670274417847395, 0.00160012929700315, 0.0015284003457054496, 0.0014553191140294075, 0.0013811138924211264, 0.0013060078490525484, 0.0012302196118980646, 0.0011539628030732274, 0.0010774459224194288, 0.0010008704848587513, 0.0009244330576620996, 0.0008483228739351034, 0.0007727226475253701, 0.0006978079327382147, 0.0006237471825443208, 0.000550701399333775, 0.00047882343642413616, 0.0004082589002791792, 0.00033914492814801633, 0.0002716107410378754, 0.00020577735267579556, 0.0001417573803337291, 7.965514669194818e-05, 1.9566638002288528e-05, -3.842059595626779e-05, -9.422734729014337e-05, -0.0001477827172493562, -0.0001990241144085303, -0.00024789711460471153, -0.00029435535543598235, -0.00033836046350188553, -0.0003798819670919329, -0.0004188970779068768, -0.00045539034181274474, -0.0004893539007753134, -0.0005207868525758386, -0.0005496952799148858, -0.000576091930270195, -0.0005999959539622068, -0.0006214328459464014, -0.0006404338637366891, -0.000657036027405411, -0.000671281770337373, -0.0006832184735685587, -0.0006928984075784683, -0.0007003784994594753, -0.0007057195180095732, -0.0007089864229783416, -0.0007102476083673537, -0.0007095747860148549, -0.0007070426363497972, -0.000702728284522891, -0.0006967115914449096, -0.0006890740478411317, -0.0006798990070819855, -0.0006692712777294219, -0.0006572765414603055, -0.000644001760520041, -0.0006295338971540332, -0.0006139606120996177, -0.0005973691586405039, -0.0005798469064757228, -0.0005614803521893919, -0.0005423553520813584, -0.0005225568311288953, -0.0005021682009100914, -0.00048127182526513934, -0.0004599479725584388, -0.00043827531044371426, -0.0004163304402027279, -0.0003941877803299576, -0.00037191930459812284, -0.0003495945711620152, -0.00032728054793551564, -0.00030504129244945943, -0.00028293815557844937, -0.000261029606917873, -0.00023937092919368297, -0.00021801443654112518, -0.00019700932898558676, -0.00017640153237152845, -0.00015623382932972163, -0.00013654578651767224, -0.00011737374734366313, -9.875082469079643e-05, -8.070691546890885e-05, -6.32687660981901e-05, -4.645998342311941e-05, -3.03010965581052e-05, -1.4809590538789053e-05, -1.1277033424057267e-19, 1.4116030797595158e-05, 2.7529658837011084e-05, 4.023476139991544e-05, 5.2227820560801774e-05, 6.350783951347694e-05, 7.407623343169689e-05, 8.393668395001441e-05, 9.309507731813937e-05, 0.00010155932977795601, 0.00010933926387224346, 0.00011644652840914205, 0.00012289444566704333, 0.00012869780766777694, 0.00013387289072852582, 0.00013843717169947922, 0.00014240926248021424, 0.0001458088227082044, 0.00014865631237626076, 0.000150972991832532, 0.0001527806743979454, 0.0001541016681585461, 0.00015495868865400553, 0.00015537462604697794, 0.0001553725014673546, 0.00015497540880460292, 0.00015420628187712282, 0.00015308793808799237, 0.00015164281649049371, 0.00014989302144385874, 0.00014786020619794726, 0.00014556545647792518, 0.0001430292468285188, 0.00014027139695826918, 0.00013731095532421023, 0.00013416614092420787, 0.00013085441605653614, 0.0001273923262488097, 0.0001237954420503229, 0.00012007846817141399, 0.00011625513434410095, 0.00011233818077016622, 0.00010833935084519908, 0.00010426943481434137, 0.00010013821156462654, 9.595452866051346e-05, 9.172626596409827e-05, 8.746036473894492e-05, 8.3162885857746e-05, 7.88389952504076e-05, 7.449306576745585e-05, 7.012864807620645e-05, 6.574857980012894e-05, 6.135496369097382e-05, 5.694930223398842e-05, 5.253248309600167e-05, 4.810490281670354e-05, 4.3666452256729826e-05, 3.921664392692037e-05, 3.475465564406477e-05]), 1)
        self.fft_filter_xxx_0.declare_sample_delay(0)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 64)
        self.blocks_pdu_to_tagged_stream_1 = blocks.pdu_to_tagged_stream(blocks.complex_t, 'packet_len')
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_file_sink_2 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/kishow/RFTool/recorded_frame.txt', False)
        self.blocks_file_sink_2.set_unbuffered(True)
        self.blocks_divide_xx_0 = blocks.divide_ff(1)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*1, 16)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, sync_length)
        self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.ieee802_11_decode_mac_0, 'out'), (self.ieee802_11_parse_mac_0, 'in'))
        self.msg_connect((self.ieee802_11_frame_equalizer_0, 'symbols'), (self.blocks_pdu_to_tagged_stream_1, 'pdus'))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_divide_xx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.ieee802_11_moving_average_xx_1, 0))
        self.connect((self.blocks_conjugate_cc_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_delay_0, 0), (self.ieee802_11_sync_long_0, 1))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_conjugate_cc_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.ieee802_11_sync_short_0, 0))
        self.connect((self.blocks_divide_xx_0, 0), (self.ieee802_11_sync_short_0, 2))
        self.connect((self.blocks_divide_xx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.ieee802_11_moving_average_xx_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_1, 0), (self.blocks_file_sink_2, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_1, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.fft_filter_xxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.fft_filter_xxx_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.fft_filter_xxx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.ieee802_11_frame_equalizer_0, 0))
        self.connect((self.ieee802_11_frame_equalizer_0, 0), (self.ieee802_11_decode_mac_0, 0))
        self.connect((self.ieee802_11_moving_average_xx_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.ieee802_11_moving_average_xx_0, 0), (self.ieee802_11_sync_short_0, 1))
        self.connect((self.ieee802_11_moving_average_xx_1, 0), (self.blocks_divide_xx_0, 1))
        self.connect((self.ieee802_11_sync_long_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.ieee802_11_sync_short_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.ieee802_11_sync_short_0, 0), (self.ieee802_11_sync_long_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.fft_filter_xxx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "recorder")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_window_size(self):
        return self.window_size

    def set_window_size(self, window_size):
        self.window_size = window_size
        self.ieee802_11_moving_average_xx_1.set_length(self.window_size + 16)
        self.ieee802_11_moving_average_xx_0.set_length(self.window_size)

    def get_sync_length(self):
        return self.sync_length

    def set_sync_length(self, sync_length):
        self.sync_length = sync_length
        self.blocks_delay_0.set_dly(self.sync_length)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self._samp_rate_callback(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.ieee802_11_frame_equalizer_0.set_bandwidth(self.samp_rate)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self.osmosdr_source_0.set_gain(self.rf_gain, 0)

    def get_lo_offset(self):
        return self.lo_offset

    def set_lo_offset(self, lo_offset):
        self.lo_offset = lo_offset
        self._lo_offset_callback(self.lo_offset)

    def get_if_gain(self):
        return self.if_gain

    def set_if_gain(self, if_gain):
        self.if_gain = if_gain
        self.osmosdr_source_0.set_if_gain(self.if_gain, 0)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_callback(self.freq)
        self.osmosdr_source_0.set_center_freq(self.freq, 0)
        self.ieee802_11_frame_equalizer_0.set_frequency(self.freq)

    def get_chan_est(self):
        return self.chan_est

    def set_chan_est(self, chan_est):
        self.chan_est = chan_est
        self._chan_est_callback(self.chan_est)
        self.ieee802_11_frame_equalizer_0.set_algorithm(self.chan_est)

    def get_bb_gain(self):
        return self.bb_gain

    def set_bb_gain(self, bb_gain):
        self.bb_gain = bb_gain
        self.osmosdr_source_0.set_bb_gain(self.bb_gain, 0)


def main(top_block_cls=recorder, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
