from zim.actions import action
from zim.plugins import PluginClass, WindowExtension, extends


class HorizontalRule(PluginClass):
    plugin_info = {
        'name': _('Horizontal Rule'),  # T: plugin name
        'description': _('`<Ctrl> + <Shift> + R` Short cut for insert horizontal rule..'),  # T: plugin description
        'author': 'Viacheslav Wolf',
        'help': 'Plugins:Horizontal Rule',
    }

@extends('MainWindow')
class MainWindowExtension(WindowExtension):
    uimanager_xml = '''
        <ui>
            <menubar name='menubar'>
                <menu action='insert_menu'>
                    <placeholder name='plugin_items'>
                        <menuitem action='insert_hr'/>
                    </placeholder>
                </menu>
            </menubar>
        </ui>
    '''

    def __init__(self, plugin, window):
        WindowExtension.__init__(self, plugin, window)

        # Define the bugtracker object as global, for the performance purpose
        plugin.bt = Mantis()

    @action(
            _('Horizontal Rule'),
            readonly=True,
            accelerator='<Control><Shift>R'
    )  # T: menu item
    def insert_hr(self):
        buffer = self.window.pageview.view.get_buffer()
        buffer.insert_at_cursor("\n________________________________________________\n")