
import  wx

#---------------------------------------------------------------------------

class TestSashWindow(wx.Panel):

    def __init__(self, parent, log):
        wx.Panel.__init__(self, parent, -1)

        self.log = log
        winids = []

        # Create some layout windows
        # A window like a toolbar
        topwin = wx.SashLayoutWindow(
            self, -1, wx.DefaultPosition, (200, 30), 
            wx.NO_BORDER|wx.SW_3D
            )

        topwin.SetDefaultSize((1000, 30))
        topwin.SetOrientation(wx.LAYOUT_HORIZONTAL)
        topwin.SetAlignment(wx.LAYOUT_TOP)
        topwin.SetBackgroundColour(wx.Colour(255, 0, 0))
        topwin.SetSashVisible(wx.SASH_BOTTOM, True)

        self.topWindow = topwin
        winids.append(topwin.GetId())

        # A window like a statusbar
        bottomwin = wx.SashLayoutWindow(
                self, -1, wx.DefaultPosition, (200, 30), 
                wx.NO_BORDER|wx.SW_3D
                )

        bottomwin.SetDefaultSize((1000, 30))
        bottomwin.SetOrientation(wx.LAYOUT_HORIZONTAL)
        bottomwin.SetAlignment(wx.LAYOUT_BOTTOM)
        bottomwin.SetBackgroundColour(wx.Colour(0, 0, 255))
        bottomwin.SetSashVisible(wx.SASH_TOP, True)

        self.bottomWindow = bottomwin
        winids.append(bottomwin.GetId())

        # A window to the left of the client window
        leftwin1 =  wx.SashLayoutWindow(
                self, -1, wx.DefaultPosition, (200, 30), 
                wx.NO_BORDER|wx.SW_3D
                )

        leftwin1.SetDefaultSize((120, 1000))
        leftwin1.SetOrientation(wx.LAYOUT_VERTICAL)
        leftwin1.SetAlignment(wx.LAYOUT_LEFT)
        leftwin1.SetBackgroundColour(wx.Colour(0, 255, 0))
        leftwin1.SetSashVisible(wx.SASH_RIGHT, True)
        leftwin1.SetExtraBorderSize(10)
        textWindow = wx.TextCtrl(
                        leftwin1, -1, "", wx.DefaultPosition, wx.DefaultSize, 
                        wx.TE_MULTILINE|wx.SUNKEN_BORDER
                        )

        textWindow.SetValue("A sub window")

        self.leftWindow1 = leftwin1
        winids.append(leftwin1.GetId())


        # Another window to the left of the client window
        leftwin2 = wx.SashLayoutWindow(
                self, -1, wx.DefaultPosition, (200, 30), 
                wx.NO_BORDER|wx.SW_3D
                )

        leftwin2.SetDefaultSize((120, 1000))
        leftwin2.SetOrientation(wx.LAYOUT_VERTICAL)
        leftwin2.SetAlignment(wx.LAYOUT_LEFT)
        leftwin2.SetBackgroundColour(wx.Colour(0, 255, 255))
        leftwin2.SetSashVisible(wx.SASH_RIGHT, True)

        self.leftWindow2 = leftwin2
        winids.append(leftwin2.GetId())

        # will occupy the space not used by the Layout Algorithm
        self.remainingSpace = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)

        self.Bind(
            wx.EVT_SASH_DRAGGED_RANGE, self.OnSashDrag,
            id=min(winids), id2=max(winids)
            )

        self.Bind(wx.EVT_SIZE, self.OnSize)


    def OnSashDrag(self, event):
        if event.GetDragStatus() == wx.SASH_STATUS_OUT_OF_RANGE:
            self.log.write('drag is out of range')
            return

        eobj = event.GetEventObject()

        if eobj is self.topWindow:
            self.log.write('topwin received drag event')
            self.topWindow.SetDefaultSize((1000, event.GetDragRect().height))

        elif eobj is self.leftWindow1:
            self.log.write('leftwin1 received drag event')
            self.leftWindow1.SetDefaultSize((event.GetDragRect().width, 1000))


        elif eobj is self.leftWindow2:
            self.log.write('leftwin2 received drag event')
            self.leftWindow2.SetDefaultSize((event.GetDragRect().width, 1000))

        elif eobj is self.bottomWindow:
            self.log.write('bottomwin received drag event')
            self.bottomWindow.SetDefaultSize((1000, event.GetDragRect().height))

        wx.LayoutAlgorithm().LayoutWindow(self, self.remainingSpace)
        self.remainingSpace.Refresh()

    def OnSize(self, event):
        wx.LayoutAlgorithm().LayoutWindow(self, self.remainingSpace)

#---------------------------------------------------------------------------

def runTest(frame, nb, log):
    win = TestSashWindow(nb, log)
    return win

#---------------------------------------------------------------------------


overview = """\
wx.SashLayoutWindow responds to OnCalculateLayout events generated by 
wxLayoutAlgorithm. It allows the application to use simple accessors to 
specify how the window should be laid out, rather than having to respond 
to events. The fact that the class derives from wx.SashWindow allows sashes 
to be used if required, to allow the windows to be user-resizable.

The documentation for wx.LayoutAlgorithm explains the purpose of this class 
in more detail.

"""


if __name__ == '__main__':
    import sys,os
    import run
    run.main(['', os.path.basename(sys.argv[0])] + sys.argv[1:])
