import ttkbootstrap as tb

from config.definitions import *
from .. components.frames import RefreshMixin, AutoLayoutFrame


class DetailView(AutoLayoutFrame, RefreshMixin):
    """A generic class to depict objects in great detail.

    Parameters
    ----------
    layout : dict
        A dictionary defining the layout of the component. Has to
        contain the variables specified below:
        - rowconfigure : dict(row_idx, weight)
        - columnconfigure : dict(col_idx, weight)
        - labels : dict
    """
    def __init__(self, master, layout):
        super().__init__(
            master=master,
            config=layout['grid-config'],
            labels=layout['labels']
        )

        btn = VIEW_BTN_EDIT
        btn_edit = tb.Button(
            self,
            text=btn['text'])
        btn_edit.bind('<Button-1>', self.open_edit_form)
        btn_edit.place(
            relx=btn['relx'],
            rely=btn['rely'],
            anchor=btn['anchor']
        )

    def open_edit_form(self, *_args):
        """Open a form for editing the selected entity.
        """
        print('Open edit form')


class ProjectDetailView(DetailView):
    def __init__(self, master):
        super().__init__(
            master=master,
            layout=VIEW_PROJECT_DETAIL
        )
        self.build_gui_components()

    def build_gui_components(self):
        dict_name = VIEW_PROJECT_DETAIL['lbl_name']
        tb.Label(
            self,
            text='Project Name',
            font=dict_name['font']
        ).grid(
            row=dict_name['row'],
            column=dict_name['col'],
            rowspan=dict_name['rowspan'],
            columnspan=dict_name['columnspan'],
            sticky=dict_name['sticky'],
            padx=dict_name['padx'],
            pady=dict_name['pady']
        )