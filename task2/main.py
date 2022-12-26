from ccalc import Calc_block as ccalc
from logger import result_logger as write_log
import datatransformation as d_t
import consoleui as c_ui


def button_click():
    j = d_t.data_formatting(c_ui.input_data())
    calc_result = ccalc(j)
    c_ui.view_data(calc_result, 'Ответ:')
    write_log(j, calc_result)

button_click()