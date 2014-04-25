# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from multichoice import TextCtrlAutoComplete
import wx
import wx.grid

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Chow Chow", pos = wx.DefaultPosition, size = wx.Size( 400,120 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		main_bsizer = wx.BoxSizer( wx.VERTICAL )
		
		self.panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		main_panel_bsizer = wx.BoxSizer( wx.VERTICAL )
		
		controls_fg_sizer = wx.FlexGridSizer( 2, 2, 0, 0 )
		controls_fg_sizer.AddGrowableCol( 1 )
		controls_fg_sizer.SetFlexibleDirection( wx.BOTH )
		controls_fg_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self.panel, wx.ID_ANY, u"Insert your task:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		controls_fg_sizer.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.task_multi_choice_text_ctrl = TextCtrlAutoComplete( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		controls_fg_sizer.Add( self.task_multi_choice_text_ctrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		main_panel_bsizer.Add( controls_fg_sizer, 1, wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		main_panel_bsizer.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		bsizer_buttons = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn_ok = wx.Button( self.panel, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		bsizer_buttons.Add( self.btn_ok, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.btn_cancel = wx.Button( self.panel, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bsizer_buttons.Add( self.btn_cancel, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		main_panel_bsizer.Add( bsizer_buttons, 0, wx.ALIGN_RIGHT, 5 )
		
		self.panel.SetSizer( main_panel_bsizer )
		self.panel.Layout()
		main_panel_bsizer.Fit( self.panel )
		main_bsizer.Add( self.panel, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.SetSizer( main_bsizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.on_close )
		self.task_multi_choice_text_ctrl.Bind( wx.EVT_KEY_DOWN, self.cmb_task_key_down )
		self.task_multi_choice_text_ctrl.Bind( wx.EVT_KEY_UP, self.cmb_task_key_up )
		self.btn_ok.Bind( wx.EVT_BUTTON, self.btn_ok_click )
		self.btn_cancel.Bind( wx.EVT_BUTTON, self.btn_cancel_click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_close( self, event ):
		event.Skip()
	
	def cmb_task_key_down( self, event ):
		event.Skip()
	
	def cmb_task_key_up( self, event ):
		event.Skip()
	
	def btn_ok_click( self, event ):
		event.Skip()
	
	def btn_cancel_click( self, event ):
		event.Skip()
	

###########################################################################
## Class TasksBaseFrame
###########################################################################

class TasksBaseFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tasks Detail", pos = wx.DefaultPosition, size = wx.Size( 610,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		tasks_frame_bsizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_toolBar1 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"Export to CSV", wx.Bitmap( u"icons/filesave16.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Export to CSV", wx.EmptyString ) 
		self.m_toolBar1.Realize()
		
		tasks_frame_bsizer.Add( self.m_toolBar1, 0, wx.EXPAND, 5 )
		
		self.tasks_grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.tasks_grid.CreateGrid( 1, 3 )
		self.tasks_grid.EnableEditing( False )
		self.tasks_grid.EnableGridLines( True )
		self.tasks_grid.EnableDragGridSize( False )
		self.tasks_grid.SetMargins( 0, 0 )
		
		# Columns
		self.tasks_grid.SetColSize( 0, 250 )
		self.tasks_grid.SetColSize( 1, 110 )
		self.tasks_grid.SetColSize( 2, 150 )
		self.tasks_grid.EnableDragColMove( False )
		self.tasks_grid.EnableDragColSize( True )
		self.tasks_grid.SetColLabelSize( 30 )
		self.tasks_grid.SetColLabelValue( 0, u"Task" )
		self.tasks_grid.SetColLabelValue( 1, u"Time (minutes)" )
		self.tasks_grid.SetColLabelValue( 2, u"Start Date" )
		self.tasks_grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.tasks_grid.EnableDragRowSize( True )
		self.tasks_grid.SetRowLabelSize( 80 )
		self.tasks_grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.tasks_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		tasks_frame_bsizer.Add( self.tasks_grid, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.SetSizer( tasks_frame_bsizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_TOOL, self.on_tool_export_csv_click, id = wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_tool_export_csv_click( self, event ):
		event.Skip()
	

###########################################################################
## Class ConfigFrame
###########################################################################

class ConfigFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Configuration", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		config_bsizer = wx.BoxSizer( wx.VERTICAL )
		
		self.config_scrolledwindow = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.config_scrolledwindow.SetScrollRate( 5, 5 )
		config_bsizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.config_panel = wx.Panel( self.config_scrolledwindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		config_fgsizer = wx.FlexGridSizer( 2, 2, 0, 0 )
		config_fgsizer.AddGrowableCol( 1 )
		config_fgsizer.SetFlexibleDirection( wx.BOTH )
		config_fgsizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.st_redmine = wx.StaticText( self.config_panel, wx.ID_ANY, u"Redmine", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_redmine.Wrap( -1 )
		config_fgsizer.Add( self.st_redmine, 0, wx.ALL, 5 )
		
		self.staticline2 = wx.StaticLine( self.config_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		config_fgsizer.Add( self.staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.st_redmine_user = wx.StaticText( self.config_panel, wx.ID_ANY, u"user", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_redmine_user.Wrap( -1 )
		config_fgsizer.Add( self.st_redmine_user, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_redmine_user = wx.TextCtrl( self.config_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		config_fgsizer.Add( self.txt_redmine_user, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.st_redmine_password = wx.StaticText( self.config_panel, wx.ID_ANY, u"password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_redmine_password.Wrap( -1 )
		config_fgsizer.Add( self.st_redmine_password, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_redmine_password = wx.TextCtrl( self.config_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		config_fgsizer.Add( self.txt_redmine_password, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.config_panel.SetSizer( config_fgsizer )
		self.config_panel.Layout()
		config_fgsizer.Fit( self.config_panel )
		config_bsizer2.Add( self.config_panel, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.config_scrolledwindow.SetSizer( config_bsizer2 )
		self.config_scrolledwindow.Layout()
		config_bsizer2.Fit( self.config_scrolledwindow )
		config_bsizer.Add( self.config_scrolledwindow, 1, wx.EXPAND |wx.ALL, 5 )
		
		bsizer_buttons = wx.BoxSizer( wx.HORIZONTAL )
		
		self.config_btn_ok = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		bsizer_buttons.Add( self.config_btn_ok, 0, wx.ALL, 5 )
		
		self.config_btn_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bsizer_buttons.Add( self.config_btn_cancel, 0, wx.ALL, 5 )
		
		config_bsizer.Add( bsizer_buttons, 0, wx.ALIGN_RIGHT, 5 )
		
		self.SetSizer( config_bsizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.config_btn_ok.Bind( wx.EVT_BUTTON, self.config_btn_ok_on_click )
		self.config_btn_cancel.Bind( wx.EVT_BUTTON, self.config_btn_cancel_on_click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def config_btn_ok_on_click( self, event ):
		event.Skip()
	
	def config_btn_cancel_on_click( self, event ):
		event.Skip()
	

