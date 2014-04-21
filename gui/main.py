# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from extra import PromptingComboBox
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
		
		cmb_taskChoices = [ u"Breakfast", u"Lunch" ]
		self.cmb_task = PromptingComboBox( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cmb_taskChoices, 0 )
		controls_fg_sizer.Add( self.cmb_task, 0, wx.ALL|wx.EXPAND, 5 )
		
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
		self.cmb_task.Bind( wx.EVT_KEY_DOWN, self.cmb_task_key_down )
		self.cmb_task.Bind( wx.EVT_KEY_UP, self.cmb_task_key_up )
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tasks Detail", pos = wx.DefaultPosition, size = wx.Size( 515,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		tasks_frame_bsizer = wx.BoxSizer( wx.VERTICAL )
		
		self.tasks_grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.tasks_grid.CreateGrid( 1, 2 )
		self.tasks_grid.EnableEditing( False )
		self.tasks_grid.EnableGridLines( True )
		self.tasks_grid.EnableDragGridSize( False )
		self.tasks_grid.SetMargins( 0, 0 )
		
		# Columns
		self.tasks_grid.SetColSize( 0, 300 )
		self.tasks_grid.SetColSize( 1, 120 )
		self.tasks_grid.EnableDragColMove( False )
		self.tasks_grid.EnableDragColSize( True )
		self.tasks_grid.SetColLabelSize( 30 )
		self.tasks_grid.SetColLabelValue( 0, u"Task" )
		self.tasks_grid.SetColLabelValue( 1, u"Time (seconds)" )
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
	
	def __del__( self ):
		pass
	

