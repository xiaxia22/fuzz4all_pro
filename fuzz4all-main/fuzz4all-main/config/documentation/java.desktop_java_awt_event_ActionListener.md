# Interface ActionListener

**Source:** `java.desktop\java\awt\event\ActionListener.html`

### Class Description

```java
public interface
ActionListener

extends
EventListener
```

The listener interface for receiving action events.
The class that is interested in processing an action event
implements this interface, and the object created with that
class is registered with a component, using the component's

addActionListener

method. When the action event
occurs, that object's

actionPerformed

method is
invoked.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void actionPerformed​(
ActionEvent
e)

Invoked when an action occurs.

**Parameters:**
- e

- the event to be processed

---

### Additional Sections

#### Interface ActionListener

**All Superinterfaces:** EventListener

**All Known Subinterfaces:** Action

**All Known Implementing Classes:** AbstractAction

,

AWTEventMulticaster

,

BasicDesktopPaneUI.CloseAction

,

BasicDesktopPaneUI.MaximizeAction

,

BasicDesktopPaneUI.MinimizeAction

,

BasicDesktopPaneUI.NavigateAction

,

BasicDesktopPaneUI.OpenAction

,

BasicFileChooserUI.ApproveSelectionAction

,

BasicFileChooserUI.CancelSelectionAction

,

BasicFileChooserUI.ChangeToParentDirectoryAction

,

BasicFileChooserUI.GoHomeAction

,

BasicFileChooserUI.NewFolderAction

,

BasicFileChooserUI.UpdateAction

,

BasicInternalFrameTitlePane.CloseAction

,

BasicInternalFrameTitlePane.IconifyAction

,

BasicInternalFrameTitlePane.MaximizeAction

,

BasicInternalFrameTitlePane.MoveAction

,

BasicInternalFrameTitlePane.RestoreAction

,

BasicInternalFrameTitlePane.SizeAction

,

BasicOptionPaneUI.ButtonActionListener

,

BasicScrollBarUI.ScrollListener

,

BasicSliderUI.ActionScroller

,

BasicSliderUI.ScrollListener

,

BasicSplitPaneUI.KeyboardDownRightHandler

,

BasicSplitPaneUI.KeyboardEndHandler

,

BasicSplitPaneUI.KeyboardHomeHandler

,

BasicSplitPaneUI.KeyboardResizeToggleHandler

,

BasicSplitPaneUI.KeyboardUpLeftHandler

,

BasicTreeUI.ComponentHandler

,

BasicTreeUI.TreeCancelEditingAction

,

BasicTreeUI.TreeHomeAction

,

BasicTreeUI.TreeIncrementAction

,

BasicTreeUI.TreePageAction

,

BasicTreeUI.TreeToggleAction

,

BasicTreeUI.TreeTraverseAction

,

DefaultCellEditor.EditorDelegate

,

DefaultEditorKit.BeepAction

,

DefaultEditorKit.CopyAction

,

DefaultEditorKit.CutAction

,

DefaultEditorKit.DefaultKeyTypedAction

,

DefaultEditorKit.InsertBreakAction

,

DefaultEditorKit.InsertContentAction

,

DefaultEditorKit.InsertTabAction

,

DefaultEditorKit.PasteAction

,

DefaultTreeCellEditor

,

DropTarget.DropTargetAutoScroller

,

FormView

,

HTMLEditorKit.HTMLTextAction

,

HTMLEditorKit.InsertHTMLTextAction

,

JComboBox

,

List.AccessibleAWTList

,

MetalFileChooserUI.DirectoryComboBoxAction

,

StyledEditorKit.AlignmentAction

,

StyledEditorKit.BoldAction

,

StyledEditorKit.FontFamilyAction

,

StyledEditorKit.FontSizeAction

,

StyledEditorKit.ForegroundAction

,

StyledEditorKit.ItalicAction

,

StyledEditorKit.StyledTextAction

,

StyledEditorKit.UnderlineAction

,

TextAction

,

ToolTipManager.insideTimerAction

,

ToolTipManager.outsideTimerAction

,

ToolTipManager.stillInsideTimerAction

```java
public interface
ActionListener

extends
EventListener
```

The listener interface for receiving action events.
The class that is interested in processing an action event
implements this interface, and the object created with that
class is registered with a component, using the component's

addActionListener

method. When the action event
occurs, that object's

actionPerformed

method is
invoked.

**Since:** 1.1
**See Also:** ActionEvent

,

How to Write an Action Listener

public interface

ActionListener

extends

EventListener

The listener interface for receiving action events.
The class that is interested in processing an action event
implements this interface, and the object created with that
class is registered with a component, using the component's

addActionListener

method. When the action event
occurs, that object's

actionPerformed

method is
invoked.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

actionPerformed

​(

ActionEvent

e)

Invoked when an action occurs.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

actionPerformed

​(

ActionEvent

e)

Invoked when an action occurs.

---

#### Method Summary

Invoked when an action occurs.

============ METHOD DETAIL ==========

- Method Detail

- actionPerformed

```java
void actionPerformed​(
ActionEvent
e)
```

Invoked when an action occurs.

**Parameters:** e

- the event to be processed

Method Detail

- actionPerformed

```java
void actionPerformed​(
ActionEvent
e)
```

Invoked when an action occurs.

**Parameters:** e

- the event to be processed

---

#### Method Detail

actionPerformed

```java
void actionPerformed​(
ActionEvent
e)
```

Invoked when an action occurs.

**Parameters:** e

- the event to be processed

---

#### actionPerformed

void actionPerformed​(

ActionEvent

e)

Invoked when an action occurs.

---

