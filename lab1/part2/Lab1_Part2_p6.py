#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: LAB1_Part2_p6
# Author: Karen_Valencia_Victor_Rodriguez_L1B_G3
# GNU Radio version: 3.10.5.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class Lab1_Part2_p6(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "LAB1_Part2_p6", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("LAB1_Part2_p6")
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

        self.settings = Qt.QSettings("GNU Radio", "Lab1_Part2_p6")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 200000
        self.fc = fc = 1500
        self.f_corte = f_corte = 1500
        self.audio_rate = audio_rate = 44100
        self.Inter = Inter = 10000
        self.De = De = 10000
        self.Const = Const = 1
        self.BW = BW = 1500

        ##################################################
        # Blocks
        ##################################################

        self._samp_rate_range = Range(1000, 300000, 1000, 200000, 200)
        self._samp_rate_win = RangeWidget(self._samp_rate_range, self.set_samp_rate, "frecuencia de muestreo", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._samp_rate_win)
        self._fc_range = Range(100, 21000, 10, 1500, 200)
        self._fc_win = RangeWidget(self._fc_range, self.set_fc, "frecuencia central", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fc_win)
        self._f_corte_range = Range(100, 50000, 10, 1500, 200)
        self._f_corte_win = RangeWidget(self._f_corte_range, self.set_f_corte, "frecuencia de corte", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._f_corte_win)
        self._Const_range = Range(0, 5, 0.1, 1, 200)
        self._Const_win = RangeWidget(self._Const_range, self.set_Const, "Constante", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Const_win)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=48000,
                decimation=200000,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=200000,
                decimation=48000,
                taps=[],
                fractional_bw=0)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            2,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.high_pass_filter_1 = filter.interp_fir_filter_fff(
            1,
            firdes.high_pass(
                1,
                samp_rate,
                f_corte,
                10,
                window.WIN_HAMMING,
                6.76))
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/labcom/lab_comu_I_L1B/session52_quevedobzrp.wav-20230412T155609Z-001/session52_quevedobzrp.wav', True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(Const)
        self.audio_sink_0 = audio.sink(44100, '', True)
        self._Inter_range = Range(10000, 300000, 10000, 10000, 200)
        self._Inter_win = RangeWidget(self._Inter_range, self.set_Inter, "Interpolation", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Inter_win)
        self._De_range = Range(10000, 300000, 10000, 10000, 200)
        self._De_win = RangeWidget(self._De_range, self.set_De, "Decimacion", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._De_win)
        self._BW_range = Range(10, 50000, 10, 1500, 200)
        self._BW_win = RangeWidget(self._BW_range, self.set_BW, "Ancho de banda", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._BW_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.high_pass_filter_1, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.high_pass_filter_1, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.high_pass_filter_1, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_throttle_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Lab1_Part2_p6")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.high_pass_filter_1.set_taps(firdes.high_pass(1, self.samp_rate, self.f_corte, 10, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc

    def get_f_corte(self):
        return self.f_corte

    def set_f_corte(self, f_corte):
        self.f_corte = f_corte
        self.high_pass_filter_1.set_taps(firdes.high_pass(1, self.samp_rate, self.f_corte, 10, window.WIN_HAMMING, 6.76))

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate

    def get_Inter(self):
        return self.Inter

    def set_Inter(self, Inter):
        self.Inter = Inter

    def get_De(self):
        return self.De

    def set_De(self, De):
        self.De = De

    def get_Const(self):
        return self.Const

    def set_Const(self, Const):
        self.Const = Const
        self.blocks_multiply_const_vxx_0.set_k(self.Const)

    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW




def main(top_block_cls=Lab1_Part2_p6, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
