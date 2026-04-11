# Class AccessibleRole

**Source:** `java.desktop\javax\accessibility\AccessibleRole.html`

### Class Description

```java
public class
AccessibleRole

extends
AccessibleBundle
```

Class

AccessibleRole

determines the role of a component. The role of
a component describes its generic function. (E.G., "push button," "table," or
"list.")

The

AccessibleBundle.toDisplayString()

method allows you to obtain the localized
string for a locale independent key from a predefined

ResourceBundle

for the keys defined in this class.

The constants in this class present a strongly typed enumeration of common
object roles. A public constructor for this class has been purposely omitted
and applications should use one of the constants from this class. If the
constants in this class are not sufficient to describe the role of an object,
a subclass should be generated from this class and it should provide
constants in a similar manner.

---

### Field Details

#### public static final
AccessibleRole
ALERT

Object is used to alert the user about something.

---

#### public static final
AccessibleRole
COLUMN_HEADER

The header for a column of data.

---

#### public static final
AccessibleRole
CANVAS

Object that can be drawn into and is used to trap events.

**See Also:**
- FRAME

,

GLASS_PANE

,

LAYERED_PANE

---

#### public static final
AccessibleRole
COMBO_BOX

A list of choices the user can select from. Also optionally allows the
user to enter a choice of their own.

---

#### public static final
AccessibleRole
DESKTOP_ICON

An iconified internal frame in a

DESKTOP_PANE

.

**See Also:**
- DESKTOP_PANE

,

INTERNAL_FRAME

---

#### public static final
AccessibleRole
HTML_CONTAINER

An object containing a collection of

Accessibles

that together
represents

HTML

content. The child

Accessibles

would
include objects implementing

AccessibleText

,

AccessibleHypertext

,

AccessibleIcon

, and other
interfaces.

**See Also:**
- HYPERLINK

,

AccessibleText

,

AccessibleHypertext

,

AccessibleHyperlink

,

AccessibleIcon

**Since:**
- 1.6

---

#### public static final
AccessibleRole
INTERNAL_FRAME

A frame-like object that is clipped by a desktop pane. The desktop pane,
internal frame, and desktop icon objects are often used to create
multiple document interfaces within an application.

**See Also:**
- DESKTOP_ICON

,

DESKTOP_PANE

,

FRAME

---

#### public static final
AccessibleRole
DESKTOP_PANE

A pane that supports internal frames and iconified versions of those
internal frames.

**See Also:**
- DESKTOP_ICON

,

INTERNAL_FRAME

---

#### public static final
AccessibleRole
OPTION_PANE

A specialized pane whose primary use is inside a

DIALOG

.

**See Also:**
- DIALOG

---

#### public static final
AccessibleRole
WINDOW

A top level window with no title or border.

**See Also:**
- FRAME

,

DIALOG

---

#### public static final
AccessibleRole
FRAME

A top level window with a title bar, border, menu bar, etc. It is often
used as the primary window for an application.

**See Also:**
- DIALOG

,

CANVAS

,

WINDOW

---

#### public static final
AccessibleRole
DIALOG

A top level window with title bar and a border. A dialog is similar to a
frame, but it has fewer properties and is often used as a secondary
window for an application.

**See Also:**
- FRAME

,

WINDOW

---

#### public static final
AccessibleRole
COLOR_CHOOSER

A specialized pane that lets the user choose a color.

---

#### public static final
AccessibleRole
DIRECTORY_PANE

A pane that allows the user to navigate through and select the contents
of a directory. May be used by a file chooser.

**See Also:**
- FILE_CHOOSER

---

#### public static final
AccessibleRole
FILE_CHOOSER

A specialized dialog that displays the files in the directory and lets
the user select a file, browse a different directory, or specify a
filename. May use the directory pane to show the contents of a directory.

**See Also:**
- DIRECTORY_PANE

---

#### public static final
AccessibleRole
FILLER

An object that fills up space in a user interface. It is often used in
interfaces to tweak the spacing between components, but serves no other
purpose.

---

#### public static final
AccessibleRole
HYPERLINK

A hypertext anchor.

---

#### public static final
AccessibleRole
ICON

A small fixed size picture, typically used to decorate components.

---

#### public static final
AccessibleRole
LABEL

An object used to present an icon or short string in an interface.

---

#### public static final
AccessibleRole
ROOT_PANE

A specialized pane that has a glass pane and a layered pane as its
children.

**See Also:**
- GLASS_PANE

,

LAYERED_PANE

---

#### public static final
AccessibleRole
GLASS_PANE

A pane that is guaranteed to be painted on top of all panes beneath it.

**See Also:**
- ROOT_PANE

,

CANVAS

---

#### public static final
AccessibleRole
LAYERED_PANE

A specialized pane that allows its children to be drawn in layers,
providing a form of stacking order. This is usually the pane that holds
the menu bar as well as the pane that contains most of the visual
components in a window.

**See Also:**
- GLASS_PANE

,

ROOT_PANE

---

#### public static final
AccessibleRole
LIST

An object that presents a list of objects to the user and allows the user
to select one or more of them. A list is usually contained within a
scroll pane.

**See Also:**
- SCROLL_PANE

,

LIST_ITEM

---

#### public static final
AccessibleRole
LIST_ITEM

An object that presents an element in a list. A list is usually contained
within a scroll pane.

**See Also:**
- SCROLL_PANE

,

LIST

---

#### public static final
AccessibleRole
MENU_BAR

An object usually drawn at the top of the primary dialog box of an
application that contains a list of menus the user can choose from. For
example, a menu bar might contain menus for "File," "Edit," and "Help."

**See Also:**
- MENU

,

POPUP_MENU

,

LAYERED_PANE

---

#### public static final
AccessibleRole
POPUP_MENU

A temporary window that is usually used to offer the user a list of
choices, and then hides when the user selects one of those choices.

**See Also:**
- MENU

,

MENU_ITEM

---

#### public static final
AccessibleRole
MENU

An object usually found inside a menu bar that contains a list of actions
the user can choose from. A menu can have any object as its children, but
most often they are menu items, other menus, or rudimentary objects such
as radio buttons, check boxes, or separators. For example, an application
may have an "Edit" menu that contains menu items for "Cut" and "Paste."

**See Also:**
- MENU_BAR

,

MENU_ITEM

,

SEPARATOR

,

RADIO_BUTTON

,

CHECK_BOX

,

POPUP_MENU

---

#### public static final
AccessibleRole
MENU_ITEM

An object usually contained in a menu that presents an action the user
can choose. For example, the "Cut" menu item in an "Edit" menu would be
an action the user can select to cut the selected area of text in a
document.

**See Also:**
- MENU_BAR

,

SEPARATOR

,

POPUP_MENU

---

#### public static final
AccessibleRole
SEPARATOR

An object usually contained in a menu to provide a visual and logical
separation of the contents in a menu. For example, the "File" menu of an
application might contain menu items for "Open," "Close," and "Exit," and
will place a separator between "Close" and "Exit" menu items.

**See Also:**
- MENU

,

MENU_ITEM

---

#### public static final
AccessibleRole
PAGE_TAB_LIST

An object that presents a series of panels (or page tabs), one at a time,
through some mechanism provided by the object. The most common mechanism
is a list of tabs at the top of the panel. The children of a page tab
list are all page tabs.

**See Also:**
- PAGE_TAB

---

#### public static final
AccessibleRole
PAGE_TAB

An object that is a child of a page tab list. Its sole child is the panel
that is to be presented to the user when the user selects the page tab
from the list of tabs in the page tab list.

**See Also:**
- PAGE_TAB_LIST

---

#### public static final
AccessibleRole
PANEL

A generic container that is often used to group objects.

---

#### public static final
AccessibleRole
PROGRESS_BAR

An object used to indicate how much of a task has been completed.

---

#### public static final
AccessibleRole
PASSWORD_TEXT

A text object used for passwords, or other places where the text contents
is not shown visibly to the user.

---

#### public static final
AccessibleRole
PUSH_BUTTON

An object the user can manipulate to tell the application to do
something.

**See Also:**
- CHECK_BOX

,

TOGGLE_BUTTON

,

RADIO_BUTTON

---

#### public static final
AccessibleRole
TOGGLE_BUTTON

A specialized push button that can be checked or unchecked, but does not
provide a separate indicator for the current state.

**See Also:**
- PUSH_BUTTON

,

CHECK_BOX

,

RADIO_BUTTON

---

#### public static final
AccessibleRole
CHECK_BOX

A choice that can be checked or unchecked and provides a separate
indicator for the current state.

**See Also:**
- PUSH_BUTTON

,

TOGGLE_BUTTON

,

RADIO_BUTTON

---

#### public static final
AccessibleRole
RADIO_BUTTON

A specialized check box that will cause other radio buttons in the same
group to become unchecked when this one is checked.

**See Also:**
- PUSH_BUTTON

,

TOGGLE_BUTTON

,

CHECK_BOX

---

#### public static final
AccessibleRole
ROW_HEADER

The header for a row of data.

---

#### public static final
AccessibleRole
SCROLL_PANE

An object that allows a user to incrementally view a large amount of
information. Its children can include scroll bars and a viewport.

**See Also:**
- SCROLL_BAR

,

VIEWPORT

---

#### public static final
AccessibleRole
SCROLL_BAR

An object usually used to allow a user to incrementally view a large
amount of data. Usually used only by a scroll pane.

**See Also:**
- SCROLL_PANE

---

#### public static final
AccessibleRole
VIEWPORT

An object usually used in a scroll pane. It represents the portion of the
entire data that the user can see. As the user manipulates the scroll
bars, the contents of the viewport can change.

**See Also:**
- SCROLL_PANE

---

#### public static final
AccessibleRole
SLIDER

An object that allows the user to select from a bounded range. For
example, a slider might be used to select a number between 0 and 100.

---

#### public static final
AccessibleRole
SPLIT_PANE

A specialized panel that presents two other panels at the same time.
Between the two panels is a divider the user can manipulate to make one
panel larger and the other panel smaller.

---

#### public static final
AccessibleRole
TABLE

An object used to present information in terms of rows and columns. An
example might include a spreadsheet application.

---

#### public static final
AccessibleRole
TEXT

An object that presents text to the user. The text is usually editable by
the user as opposed to a label.

**See Also:**
- LABEL

---

#### public static final
AccessibleRole
TREE

An object used to present hierarchical information to the user. The
individual nodes in the tree can be collapsed and expanded to provide
selective disclosure of the tree's contents.

---

#### public static final
AccessibleRole
TOOL_BAR

A bar or palette usually composed of push buttons or toggle buttons. It
is often used to provide the most frequently used functions for an
application.

---

#### public static final
AccessibleRole
TOOL_TIP

An object that provides information about another object. The

accessibleDescription

property of the tool tip is often displayed
to the user in a small "help bubble" when the user causes the mouse to
hover over the object associated with the tool tip.

---

#### public static final
AccessibleRole
AWT_COMPONENT

An AWT component, but nothing else is known about it.

**See Also:**
- SWING_COMPONENT

,

UNKNOWN

---

#### public static final
AccessibleRole
SWING_COMPONENT

A Swing component, but nothing else is known about it.

**See Also:**
- AWT_COMPONENT

,

UNKNOWN

---

#### public static final
AccessibleRole
UNKNOWN

The object contains some

Accessible

information, but its role is
not known.

**See Also:**
- AWT_COMPONENT

,

SWING_COMPONENT

---

#### public static final
AccessibleRole
STATUS_BAR

A

STATUS_BAR

is an simple component that can contain multiple
labels of status information to the user.

---

#### public static final
AccessibleRole
DATE_EDITOR

A

DATE_EDITOR

is a component that allows users to edit

java.util.Date

and

java.util.Time

objects.

---

#### public static final
AccessibleRole
SPIN_BOX

A

SPIN_BOX

is a simple spinner component and its main use is for
simple numbers.

---

#### public static final
AccessibleRole
FONT_CHOOSER

A

FONT_CHOOSER

is a component that lets the user pick various
attributes for fonts.

---

#### public static final
AccessibleRole
GROUP_BOX

A

GROUP_BOX

is a simple container that contains a border around
it and contains components inside it.

---

#### public static final
AccessibleRole
HEADER

A text header.

**Since:**
- 1.5

---

#### public static final
AccessibleRole
FOOTER

A text footer.

**Since:**
- 1.5

---

#### public static final
AccessibleRole
PARAGRAPH

A text paragraph.

**Since:**
- 1.5

---

#### public static final
AccessibleRole
RULER

A ruler is an object used to measure distance.

**Since:**
- 1.5

---

#### public static final
AccessibleRole
EDITBAR

A role indicating the object acts as a formula for calculating a value.
An example is a formula in a spreadsheet cell.

**Since:**
- 1.5

---

#### public static final
AccessibleRole
PROGRESS_MONITOR

A role indicating the object monitors the progress of some operation.

**Since:**
- 1.5

---

### Constructor Details

#### protected AccessibleRole​(
String
key)

Creates a new

AccessibleRole

using the given locale independent
key. This should not be a public method. Instead, it is used to create
the constants in this file to make it a strongly typed enumeration.
Subclasses of this class should enforce similar policy.

The key

String

should be a locale independent key for the role.
It is not intended to be used as the actual

String

to display to
the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

**Parameters:**
- key

- the locale independent name of the role

**See Also:**
- AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

---

### Method Details

*No entries found.*

### Additional Sections

#### Class AccessibleRole

java.lang.Object

- javax.accessibility.AccessibleBundle
- - javax.accessibility.AccessibleRole

javax.accessibility.AccessibleBundle

- javax.accessibility.AccessibleRole

javax.accessibility.AccessibleRole

```java
public class
AccessibleRole

extends
AccessibleBundle
```

Class

AccessibleRole

determines the role of a component. The role of
a component describes its generic function. (E.G., "push button," "table," or
"list.")

The

AccessibleBundle.toDisplayString()

method allows you to obtain the localized
string for a locale independent key from a predefined

ResourceBundle

for the keys defined in this class.

The constants in this class present a strongly typed enumeration of common
object roles. A public constructor for this class has been purposely omitted
and applications should use one of the constants from this class. If the
constants in this class are not sufficient to describe the role of an object,
a subclass should be generated from this class and it should provide
constants in a similar manner.

public class

AccessibleRole

extends

AccessibleBundle

Class

AccessibleRole

determines the role of a component. The role of
a component describes its generic function. (E.G., "push button," "table," or
"list.")

The

AccessibleBundle.toDisplayString()

method allows you to obtain the localized
string for a locale independent key from a predefined

ResourceBundle

for the keys defined in this class.

The constants in this class present a strongly typed enumeration of common
object roles. A public constructor for this class has been purposely omitted
and applications should use one of the constants from this class. If the
constants in this class are not sufficient to describe the role of an object,
a subclass should be generated from this class and it should provide
constants in a similar manner.

The

AccessibleBundle.toDisplayString()

method allows you to obtain the localized
string for a locale independent key from a predefined

ResourceBundle

for the keys defined in this class.

The constants in this class present a strongly typed enumeration of common
object roles. A public constructor for this class has been purposely omitted
and applications should use one of the constants from this class. If the
constants in this class are not sufficient to describe the role of an object,
a subclass should be generated from this class and it should provide
constants in a similar manner.

The constants in this class present a strongly typed enumeration of common
object roles. A public constructor for this class has been purposely omitted
and applications should use one of the constants from this class. If the
constants in this class are not sufficient to describe the role of an object,
a subclass should be generated from this class and it should provide
constants in a similar manner.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

AccessibleRole

ALERT

Object is used to alert the user about something.

static

AccessibleRole

AWT_COMPONENT

An AWT component, but nothing else is known about it.

static

AccessibleRole

CANVAS

Object that can be drawn into and is used to trap events.

static

AccessibleRole

CHECK_BOX

A choice that can be checked or unchecked and provides a separate
indicator for the current state.

static

AccessibleRole

COLOR_CHOOSER

A specialized pane that lets the user choose a color.

static

AccessibleRole

COLUMN_HEADER

The header for a column of data.

static

AccessibleRole

COMBO_BOX

A list of choices the user can select from.

static

AccessibleRole

DATE_EDITOR

A

DATE_EDITOR

is a component that allows users to edit

java.util.Date

and

java.util.Time

objects.

static

AccessibleRole

DESKTOP_ICON

An iconified internal frame in a

DESKTOP_PANE

.

static

AccessibleRole

DESKTOP_PANE

A pane that supports internal frames and iconified versions of those
internal frames.

static

AccessibleRole

DIALOG

A top level window with title bar and a border.

static

AccessibleRole

DIRECTORY_PANE

A pane that allows the user to navigate through and select the contents
of a directory.

static

AccessibleRole

EDITBAR

A role indicating the object acts as a formula for calculating a value.

static

AccessibleRole

FILE_CHOOSER

A specialized dialog that displays the files in the directory and lets
the user select a file, browse a different directory, or specify a
filename.

static

AccessibleRole

FILLER

An object that fills up space in a user interface.

static

AccessibleRole

FONT_CHOOSER

A

FONT_CHOOSER

is a component that lets the user pick various
attributes for fonts.

static

AccessibleRole

FOOTER

A text footer.

static

AccessibleRole

FRAME

A top level window with a title bar, border, menu bar, etc.

static

AccessibleRole

GLASS_PANE

A pane that is guaranteed to be painted on top of all panes beneath it.

static

AccessibleRole

GROUP_BOX

A

GROUP_BOX

is a simple container that contains a border around
it and contains components inside it.

static

AccessibleRole

HEADER

A text header.

static

AccessibleRole

HTML_CONTAINER

An object containing a collection of

Accessibles

that together
represents

HTML

content.

static

AccessibleRole

HYPERLINK

A hypertext anchor.

static

AccessibleRole

ICON

A small fixed size picture, typically used to decorate components.

static

AccessibleRole

INTERNAL_FRAME

A frame-like object that is clipped by a desktop pane.

static

AccessibleRole

LABEL

An object used to present an icon or short string in an interface.

static

AccessibleRole

LAYERED_PANE

A specialized pane that allows its children to be drawn in layers,
providing a form of stacking order.

static

AccessibleRole

LIST

An object that presents a list of objects to the user and allows the user
to select one or more of them.

static

AccessibleRole

LIST_ITEM

An object that presents an element in a list.

static

AccessibleRole

MENU

An object usually found inside a menu bar that contains a list of actions
the user can choose from.

static

AccessibleRole

MENU_BAR

An object usually drawn at the top of the primary dialog box of an
application that contains a list of menus the user can choose from.

static

AccessibleRole

MENU_ITEM

An object usually contained in a menu that presents an action the user
can choose.

static

AccessibleRole

OPTION_PANE

A specialized pane whose primary use is inside a

DIALOG

.

static

AccessibleRole

PAGE_TAB

An object that is a child of a page tab list.

static

AccessibleRole

PAGE_TAB_LIST

An object that presents a series of panels (or page tabs), one at a time,
through some mechanism provided by the object.

static

AccessibleRole

PANEL

A generic container that is often used to group objects.

static

AccessibleRole

PARAGRAPH

A text paragraph.

static

AccessibleRole

PASSWORD_TEXT

A text object used for passwords, or other places where the text contents
is not shown visibly to the user.

static

AccessibleRole

POPUP_MENU

A temporary window that is usually used to offer the user a list of
choices, and then hides when the user selects one of those choices.

static

AccessibleRole

PROGRESS_BAR

An object used to indicate how much of a task has been completed.

static

AccessibleRole

PROGRESS_MONITOR

A role indicating the object monitors the progress of some operation.

static

AccessibleRole

PUSH_BUTTON

An object the user can manipulate to tell the application to do
something.

static

AccessibleRole

RADIO_BUTTON

A specialized check box that will cause other radio buttons in the same
group to become unchecked when this one is checked.

static

AccessibleRole

ROOT_PANE

A specialized pane that has a glass pane and a layered pane as its
children.

static

AccessibleRole

ROW_HEADER

The header for a row of data.

static

AccessibleRole

RULER

A ruler is an object used to measure distance.

static

AccessibleRole

SCROLL_BAR

An object usually used to allow a user to incrementally view a large
amount of data.

static

AccessibleRole

SCROLL_PANE

An object that allows a user to incrementally view a large amount of
information.

static

AccessibleRole

SEPARATOR

An object usually contained in a menu to provide a visual and logical
separation of the contents in a menu.

static

AccessibleRole

SLIDER

An object that allows the user to select from a bounded range.

static

AccessibleRole

SPIN_BOX

A

SPIN_BOX

is a simple spinner component and its main use is for
simple numbers.

static

AccessibleRole

SPLIT_PANE

A specialized panel that presents two other panels at the same time.

static

AccessibleRole

STATUS_BAR

A

STATUS_BAR

is an simple component that can contain multiple
labels of status information to the user.

static

AccessibleRole

SWING_COMPONENT

A Swing component, but nothing else is known about it.

static

AccessibleRole

TABLE

An object used to present information in terms of rows and columns.

static

AccessibleRole

TEXT

An object that presents text to the user.

static

AccessibleRole

TOGGLE_BUTTON

A specialized push button that can be checked or unchecked, but does not
provide a separate indicator for the current state.

static

AccessibleRole

TOOL_BAR

A bar or palette usually composed of push buttons or toggle buttons.

static

AccessibleRole

TOOL_TIP

An object that provides information about another object.

static

AccessibleRole

TREE

An object used to present hierarchical information to the user.

static

AccessibleRole

UNKNOWN

The object contains some

Accessible

information, but its role is
not known.

static

AccessibleRole

VIEWPORT

An object usually used in a scroll pane.

static

AccessibleRole

WINDOW

A top level window with no title or border.

- Fields declared in class javax.accessibility.

AccessibleBundle

key

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AccessibleRole

​(

String

key)

Creates a new

AccessibleRole

using the given locale independent
key.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class javax.accessibility.

AccessibleBundle

toDisplayString

,

toDisplayString

,

toDisplayString

,

toString

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Field Summary

Fields

Modifier and Type

Field

Description

static

AccessibleRole

ALERT

Object is used to alert the user about something.

static

AccessibleRole

AWT_COMPONENT

An AWT component, but nothing else is known about it.

static

AccessibleRole

CANVAS

Object that can be drawn into and is used to trap events.

static

AccessibleRole

CHECK_BOX

A choice that can be checked or unchecked and provides a separate
indicator for the current state.

static

AccessibleRole

COLOR_CHOOSER

A specialized pane that lets the user choose a color.

static

AccessibleRole

COLUMN_HEADER

The header for a column of data.

static

AccessibleRole

COMBO_BOX

A list of choices the user can select from.

static

AccessibleRole

DATE_EDITOR

A

DATE_EDITOR

is a component that allows users to edit

java.util.Date

and

java.util.Time

objects.

static

AccessibleRole

DESKTOP_ICON

An iconified internal frame in a

DESKTOP_PANE

.

static

AccessibleRole

DESKTOP_PANE

A pane that supports internal frames and iconified versions of those
internal frames.

static

AccessibleRole

DIALOG

A top level window with title bar and a border.

static

AccessibleRole

DIRECTORY_PANE

A pane that allows the user to navigate through and select the contents
of a directory.

static

AccessibleRole

EDITBAR

A role indicating the object acts as a formula for calculating a value.

static

AccessibleRole

FILE_CHOOSER

A specialized dialog that displays the files in the directory and lets
the user select a file, browse a different directory, or specify a
filename.

static

AccessibleRole

FILLER

An object that fills up space in a user interface.

static

AccessibleRole

FONT_CHOOSER

A

FONT_CHOOSER

is a component that lets the user pick various
attributes for fonts.

static

AccessibleRole

FOOTER

A text footer.

static

AccessibleRole

FRAME

A top level window with a title bar, border, menu bar, etc.

static

AccessibleRole

GLASS_PANE

A pane that is guaranteed to be painted on top of all panes beneath it.

static

AccessibleRole

GROUP_BOX

A

GROUP_BOX

is a simple container that contains a border around
it and contains components inside it.

static

AccessibleRole

HEADER

A text header.

static

AccessibleRole

HTML_CONTAINER

An object containing a collection of

Accessibles

that together
represents

HTML

content.

static

AccessibleRole

HYPERLINK

A hypertext anchor.

static

AccessibleRole

ICON

A small fixed size picture, typically used to decorate components.

static

AccessibleRole

INTERNAL_FRAME

A frame-like object that is clipped by a desktop pane.

static

AccessibleRole

LABEL

An object used to present an icon or short string in an interface.

static

AccessibleRole

LAYERED_PANE

A specialized pane that allows its children to be drawn in layers,
providing a form of stacking order.

static

AccessibleRole

LIST

An object that presents a list of objects to the user and allows the user
to select one or more of them.

static

AccessibleRole

LIST_ITEM

An object that presents an element in a list.

static

AccessibleRole

MENU

An object usually found inside a menu bar that contains a list of actions
the user can choose from.

static

AccessibleRole

MENU_BAR

An object usually drawn at the top of the primary dialog box of an
application that contains a list of menus the user can choose from.

static

AccessibleRole

MENU_ITEM

An object usually contained in a menu that presents an action the user
can choose.

static

AccessibleRole

OPTION_PANE

A specialized pane whose primary use is inside a

DIALOG

.

static

AccessibleRole

PAGE_TAB

An object that is a child of a page tab list.

static

AccessibleRole

PAGE_TAB_LIST

An object that presents a series of panels (or page tabs), one at a time,
through some mechanism provided by the object.

static

AccessibleRole

PANEL

A generic container that is often used to group objects.

static

AccessibleRole

PARAGRAPH

A text paragraph.

static

AccessibleRole

PASSWORD_TEXT

A text object used for passwords, or other places where the text contents
is not shown visibly to the user.

static

AccessibleRole

POPUP_MENU

A temporary window that is usually used to offer the user a list of
choices, and then hides when the user selects one of those choices.

static

AccessibleRole

PROGRESS_BAR

An object used to indicate how much of a task has been completed.

static

AccessibleRole

PROGRESS_MONITOR

A role indicating the object monitors the progress of some operation.

static

AccessibleRole

PUSH_BUTTON

An object the user can manipulate to tell the application to do
something.

static

AccessibleRole

RADIO_BUTTON

A specialized check box that will cause other radio buttons in the same
group to become unchecked when this one is checked.

static

AccessibleRole

ROOT_PANE

A specialized pane that has a glass pane and a layered pane as its
children.

static

AccessibleRole

ROW_HEADER

The header for a row of data.

static

AccessibleRole

RULER

A ruler is an object used to measure distance.

static

AccessibleRole

SCROLL_BAR

An object usually used to allow a user to incrementally view a large
amount of data.

static

AccessibleRole

SCROLL_PANE

An object that allows a user to incrementally view a large amount of
information.

static

AccessibleRole

SEPARATOR

An object usually contained in a menu to provide a visual and logical
separation of the contents in a menu.

static

AccessibleRole

SLIDER

An object that allows the user to select from a bounded range.

static

AccessibleRole

SPIN_BOX

A

SPIN_BOX

is a simple spinner component and its main use is for
simple numbers.

static

AccessibleRole

SPLIT_PANE

A specialized panel that presents two other panels at the same time.

static

AccessibleRole

STATUS_BAR

A

STATUS_BAR

is an simple component that can contain multiple
labels of status information to the user.

static

AccessibleRole

SWING_COMPONENT

A Swing component, but nothing else is known about it.

static

AccessibleRole

TABLE

An object used to present information in terms of rows and columns.

static

AccessibleRole

TEXT

An object that presents text to the user.

static

AccessibleRole

TOGGLE_BUTTON

A specialized push button that can be checked or unchecked, but does not
provide a separate indicator for the current state.

static

AccessibleRole

TOOL_BAR

A bar or palette usually composed of push buttons or toggle buttons.

static

AccessibleRole

TOOL_TIP

An object that provides information about another object.

static

AccessibleRole

TREE

An object used to present hierarchical information to the user.

static

AccessibleRole

UNKNOWN

The object contains some

Accessible

information, but its role is
not known.

static

AccessibleRole

VIEWPORT

An object usually used in a scroll pane.

static

AccessibleRole

WINDOW

A top level window with no title or border.

- Fields declared in class javax.accessibility.

AccessibleBundle

key

---

#### Field Summary

Object is used to alert the user about something.

An AWT component, but nothing else is known about it.

Object that can be drawn into and is used to trap events.

A choice that can be checked or unchecked and provides a separate
indicator for the current state.

A specialized pane that lets the user choose a color.

The header for a column of data.

A list of choices the user can select from.

A

DATE_EDITOR

is a component that allows users to edit

java.util.Date

and

java.util.Time

objects.

An iconified internal frame in a

DESKTOP_PANE

.

A pane that supports internal frames and iconified versions of those
internal frames.

A top level window with title bar and a border.

A pane that allows the user to navigate through and select the contents
of a directory.

A role indicating the object acts as a formula for calculating a value.

A specialized dialog that displays the files in the directory and lets
the user select a file, browse a different directory, or specify a
filename.

An object that fills up space in a user interface.

A

FONT_CHOOSER

is a component that lets the user pick various
attributes for fonts.

A text footer.

A top level window with a title bar, border, menu bar, etc.

A pane that is guaranteed to be painted on top of all panes beneath it.

A

GROUP_BOX

is a simple container that contains a border around
it and contains components inside it.

A text header.

An object containing a collection of

Accessibles

that together
represents

HTML

content.

A hypertext anchor.

A small fixed size picture, typically used to decorate components.

A frame-like object that is clipped by a desktop pane.

An object used to present an icon or short string in an interface.

A specialized pane that allows its children to be drawn in layers,
providing a form of stacking order.

An object that presents a list of objects to the user and allows the user
to select one or more of them.

An object that presents an element in a list.

An object usually found inside a menu bar that contains a list of actions
the user can choose from.

An object usually drawn at the top of the primary dialog box of an
application that contains a list of menus the user can choose from.

An object usually contained in a menu that presents an action the user
can choose.

A specialized pane whose primary use is inside a

DIALOG

.

An object that is a child of a page tab list.

An object that presents a series of panels (or page tabs), one at a time,
through some mechanism provided by the object.

A generic container that is often used to group objects.

A text paragraph.

A text object used for passwords, or other places where the text contents
is not shown visibly to the user.

A temporary window that is usually used to offer the user a list of
choices, and then hides when the user selects one of those choices.

An object used to indicate how much of a task has been completed.

A role indicating the object monitors the progress of some operation.

An object the user can manipulate to tell the application to do
something.

A specialized check box that will cause other radio buttons in the same
group to become unchecked when this one is checked.

A specialized pane that has a glass pane and a layered pane as its
children.

The header for a row of data.

A ruler is an object used to measure distance.

An object usually used to allow a user to incrementally view a large
amount of data.

An object that allows a user to incrementally view a large amount of
information.

An object usually contained in a menu to provide a visual and logical
separation of the contents in a menu.

An object that allows the user to select from a bounded range.

A

SPIN_BOX

is a simple spinner component and its main use is for
simple numbers.

A specialized panel that presents two other panels at the same time.

A

STATUS_BAR

is an simple component that can contain multiple
labels of status information to the user.

A Swing component, but nothing else is known about it.

An object used to present information in terms of rows and columns.

An object that presents text to the user.

A specialized push button that can be checked or unchecked, but does not
provide a separate indicator for the current state.

A bar or palette usually composed of push buttons or toggle buttons.

An object that provides information about another object.

An object used to present hierarchical information to the user.

The object contains some

Accessible

information, but its role is
not known.

An object usually used in a scroll pane.

A top level window with no title or border.

Fields declared in class javax.accessibility.

AccessibleBundle

key

---

#### Fields declared in class javax.accessibility. AccessibleBundle

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AccessibleRole

​(

String

key)

Creates a new

AccessibleRole

using the given locale independent
key.

---

#### Constructor Summary

Creates a new

AccessibleRole

using the given locale independent
key.

Method Summary

- Methods declared in class javax.accessibility.

AccessibleBundle

toDisplayString

,

toDisplayString

,

toDisplayString

,

toString

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Methods declared in class javax.accessibility.

AccessibleBundle

toDisplayString

,

toDisplayString

,

toDisplayString

,

toString

---

#### Methods declared in class javax.accessibility. AccessibleBundle

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- ALERT

```java
public static final
AccessibleRole
ALERT
```

Object is used to alert the user about something.

- COLUMN_HEADER

```java
public static final
AccessibleRole
COLUMN_HEADER
```

The header for a column of data.

- CANVAS

```java
public static final
AccessibleRole
CANVAS
```

Object that can be drawn into and is used to trap events.

**See Also:** FRAME

,

GLASS_PANE

,

LAYERED_PANE

- COMBO_BOX

```java
public static final
AccessibleRole
COMBO_BOX
```

A list of choices the user can select from. Also optionally allows the
user to enter a choice of their own.

- DESKTOP_ICON

```java
public static final
AccessibleRole
DESKTOP_ICON
```

An iconified internal frame in a

DESKTOP_PANE

.

**See Also:** DESKTOP_PANE

,

INTERNAL_FRAME

- HTML_CONTAINER

```java
public static final
AccessibleRole
HTML_CONTAINER
```

An object containing a collection of

Accessibles

that together
represents

HTML

content. The child

Accessibles

would
include objects implementing

AccessibleText

,

AccessibleHypertext

,

AccessibleIcon

, and other
interfaces.

**Since:** 1.6
**See Also:** HYPERLINK

,

AccessibleText

,

AccessibleHypertext

,

AccessibleHyperlink

,

AccessibleIcon

- INTERNAL_FRAME

```java
public static final
AccessibleRole
INTERNAL_FRAME
```

A frame-like object that is clipped by a desktop pane. The desktop pane,
internal frame, and desktop icon objects are often used to create
multiple document interfaces within an application.

**See Also:** DESKTOP_ICON

,

DESKTOP_PANE

,

FRAME

- DESKTOP_PANE

```java
public static final
AccessibleRole
DESKTOP_PANE
```

A pane that supports internal frames and iconified versions of those
internal frames.

**See Also:** DESKTOP_ICON

,

INTERNAL_FRAME

- OPTION_PANE

```java
public static final
AccessibleRole
OPTION_PANE
```

A specialized pane whose primary use is inside a

DIALOG

.

**See Also:** DIALOG

- WINDOW

```java
public static final
AccessibleRole
WINDOW
```

A top level window with no title or border.

**See Also:** FRAME

,

DIALOG

- FRAME

```java
public static final
AccessibleRole
FRAME
```

A top level window with a title bar, border, menu bar, etc. It is often
used as the primary window for an application.

**See Also:** DIALOG

,

CANVAS

,

WINDOW

- DIALOG

```java
public static final
AccessibleRole
DIALOG
```

A top level window with title bar and a border. A dialog is similar to a
frame, but it has fewer properties and is often used as a secondary
window for an application.

**See Also:** FRAME

,

WINDOW

- COLOR_CHOOSER

```java
public static final
AccessibleRole
COLOR_CHOOSER
```

A specialized pane that lets the user choose a color.

- DIRECTORY_PANE

```java
public static final
AccessibleRole
DIRECTORY_PANE
```

A pane that allows the user to navigate through and select the contents
of a directory. May be used by a file chooser.

**See Also:** FILE_CHOOSER

- FILE_CHOOSER

```java
public static final
AccessibleRole
FILE_CHOOSER
```

A specialized dialog that displays the files in the directory and lets
the user select a file, browse a different directory, or specify a
filename. May use the directory pane to show the contents of a directory.

**See Also:** DIRECTORY_PANE

- FILLER

```java
public static final
AccessibleRole
FILLER
```

An object that fills up space in a user interface. It is often used in
interfaces to tweak the spacing between components, but serves no other
purpose.

- HYPERLINK

```java
public static final
AccessibleRole
HYPERLINK
```

A hypertext anchor.

- ICON

```java
public static final
AccessibleRole
ICON
```

A small fixed size picture, typically used to decorate components.

- LABEL

```java
public static final
AccessibleRole
LABEL
```

An object used to present an icon or short string in an interface.

- ROOT_PANE

```java
public static final
AccessibleRole
ROOT_PANE
```

A specialized pane that has a glass pane and a layered pane as its
children.

**See Also:** GLASS_PANE

,

LAYERED_PANE

- GLASS_PANE

```java
public static final
AccessibleRole
GLASS_PANE
```

A pane that is guaranteed to be painted on top of all panes beneath it.

**See Also:** ROOT_PANE

,

CANVAS

- LAYERED_PANE

```java
public static final
AccessibleRole
LAYERED_PANE
```

A specialized pane that allows its children to be drawn in layers,
providing a form of stacking order. This is usually the pane that holds
the menu bar as well as the pane that contains most of the visual
components in a window.

**See Also:** GLASS_PANE

,

ROOT_PANE

- LIST

```java
public static final
AccessibleRole
LIST
```

An object that presents a list of objects to the user and allows the user
to select one or more of them. A list is usually contained within a
scroll pane.

**See Also:** SCROLL_PANE

,

LIST_ITEM

- LIST_ITEM

```java
public static final
AccessibleRole
LIST_ITEM
```

An object that presents an element in a list. A list is usually contained
within a scroll pane.

**See Also:** SCROLL_PANE

,

LIST

- MENU_BAR

```java
public static final
AccessibleRole
MENU_BAR
```

An object usually drawn at the top of the primary dialog box of an
application that contains a list of menus the user can choose from. For
example, a menu bar might contain menus for "File," "Edit," and "Help."

**See Also:** MENU

,

POPUP_MENU

,

LAYERED_PANE

- POPUP_MENU

```java
public static final
AccessibleRole
POPUP_MENU
```

A temporary window that is usually used to offer the user a list of
choices, and then hides when the user selects one of those choices.

**See Also:** MENU

,

MENU_ITEM

- MENU

```java
public static final
AccessibleRole
MENU
```

An object usually found inside a menu bar that contains a list of actions
the user can choose from. A menu can have any object as its children, but
most often they are menu items, other menus, or rudimentary objects such
as radio buttons, check boxes, or separators. For example, an application
may have an "Edit" menu that contains menu items for "Cut" and "Paste."

**See Also:** MENU_BAR

,

MENU_ITEM

,

SEPARATOR

,

RADIO_BUTTON

,

CHECK_BOX

,

POPUP_MENU

- MENU_ITEM

```java
public static final
AccessibleRole
MENU_ITEM
```

An object usually contained in a menu that presents an action the user
can choose. For example, the "Cut" menu item in an "Edit" menu would be
an action the user can select to cut the selected area of text in a
document.

**See Also:** MENU_BAR

,

SEPARATOR

,

POPUP_MENU

- SEPARATOR

```java
public static final
AccessibleRole
SEPARATOR
```

An object usually contained in a menu to provide a visual and logical
separation of the contents in a menu. For example, the "File" menu of an
application might contain menu items for "Open," "Close," and "Exit," and
will place a separator between "Close" and "Exit" menu items.

**See Also:** MENU

,

MENU_ITEM

- PAGE_TAB_LIST

```java
public static final
AccessibleRole
PAGE_TAB_LIST
```

An object that presents a series of panels (or page tabs), one at a time,
through some mechanism provided by the object. The most common mechanism
is a list of tabs at the top of the panel. The children of a page tab
list are all page tabs.

**See Also:** PAGE_TAB

- PAGE_TAB

```java
public static final
AccessibleRole
PAGE_TAB
```

An object that is a child of a page tab list. Its sole child is the panel
that is to be presented to the user when the user selects the page tab
from the list of tabs in the page tab list.

**See Also:** PAGE_TAB_LIST

- PANEL

```java
public static final
AccessibleRole
PANEL
```

A generic container that is often used to group objects.

- PROGRESS_BAR

```java
public static final
AccessibleRole
PROGRESS_BAR
```

An object used to indicate how much of a task has been completed.

- PASSWORD_TEXT

```java
public static final
AccessibleRole
PASSWORD_TEXT
```

A text object used for passwords, or other places where the text contents
is not shown visibly to the user.

- PUSH_BUTTON

```java
public static final
AccessibleRole
PUSH_BUTTON
```

An object the user can manipulate to tell the application to do
something.

**See Also:** CHECK_BOX

,

TOGGLE_BUTTON

,

RADIO_BUTTON

- TOGGLE_BUTTON

```java
public static final
AccessibleRole
TOGGLE_BUTTON
```

A specialized push button that can be checked or unchecked, but does not
provide a separate indicator for the current state.

**See Also:** PUSH_BUTTON

,

CHECK_BOX

,

RADIO_BUTTON

- CHECK_BOX

```java
public static final
AccessibleRole
CHECK_BOX
```

A choice that can be checked or unchecked and provides a separate
indicator for the current state.

**See Also:** PUSH_BUTTON

,

TOGGLE_BUTTON

,

RADIO_BUTTON

- RADIO_BUTTON

```java
public static final
AccessibleRole
RADIO_BUTTON
```

A specialized check box that will cause other radio buttons in the same
group to become unchecked when this one is checked.

**See Also:** PUSH_BUTTON

,

TOGGLE_BUTTON

,

CHECK_BOX

- ROW_HEADER

```java
public static final
AccessibleRole
ROW_HEADER
```

The header for a row of data.

- SCROLL_PANE

```java
public static final
AccessibleRole
SCROLL_PANE
```

An object that allows a user to incrementally view a large amount of
information. Its children can include scroll bars and a viewport.

**See Also:** SCROLL_BAR

,

VIEWPORT

- SCROLL_BAR

```java
public static final
AccessibleRole
SCROLL_BAR
```

An object usually used to allow a user to incrementally view a large
amount of data. Usually used only by a scroll pane.

**See Also:** SCROLL_PANE

- VIEWPORT

```java
public static final
AccessibleRole
VIEWPORT
```

An object usually used in a scroll pane. It represents the portion of the
entire data that the user can see. As the user manipulates the scroll
bars, the contents of the viewport can change.

**See Also:** SCROLL_PANE

- SLIDER

```java
public static final
AccessibleRole
SLIDER
```

An object that allows the user to select from a bounded range. For
example, a slider might be used to select a number between 0 and 100.

- SPLIT_PANE

```java
public static final
AccessibleRole
SPLIT_PANE
```

A specialized panel that presents two other panels at the same time.
Between the two panels is a divider the user can manipulate to make one
panel larger and the other panel smaller.

- TABLE

```java
public static final
AccessibleRole
TABLE
```

An object used to present information in terms of rows and columns. An
example might include a spreadsheet application.

- TEXT

```java
public static final
AccessibleRole
TEXT
```

An object that presents text to the user. The text is usually editable by
the user as opposed to a label.

**See Also:** LABEL

- TREE

```java
public static final
AccessibleRole
TREE
```

An object used to present hierarchical information to the user. The
individual nodes in the tree can be collapsed and expanded to provide
selective disclosure of the tree's contents.

- TOOL_BAR

```java
public static final
AccessibleRole
TOOL_BAR
```

A bar or palette usually composed of push buttons or toggle buttons. It
is often used to provide the most frequently used functions for an
application.

- TOOL_TIP

```java
public static final
AccessibleRole
TOOL_TIP
```

An object that provides information about another object. The

accessibleDescription

property of the tool tip is often displayed
to the user in a small "help bubble" when the user causes the mouse to
hover over the object associated with the tool tip.

- AWT_COMPONENT

```java
public static final
AccessibleRole
AWT_COMPONENT
```

An AWT component, but nothing else is known about it.

**See Also:** SWING_COMPONENT

,

UNKNOWN

- SWING_COMPONENT

```java
public static final
AccessibleRole
SWING_COMPONENT
```

A Swing component, but nothing else is known about it.

**See Also:** AWT_COMPONENT

,

UNKNOWN

- UNKNOWN

```java
public static final
AccessibleRole
UNKNOWN
```

The object contains some

Accessible

information, but its role is
not known.

**See Also:** AWT_COMPONENT

,

SWING_COMPONENT

- STATUS_BAR

```java
public static final
AccessibleRole
STATUS_BAR
```

A

STATUS_BAR

is an simple component that can contain multiple
labels of status information to the user.

- DATE_EDITOR

```java
public static final
AccessibleRole
DATE_EDITOR
```

A

DATE_EDITOR

is a component that allows users to edit

java.util.Date

and

java.util.Time

objects.

- SPIN_BOX

```java
public static final
AccessibleRole
SPIN_BOX
```

A

SPIN_BOX

is a simple spinner component and its main use is for
simple numbers.

- FONT_CHOOSER

```java
public static final
AccessibleRole
FONT_CHOOSER
```

A

FONT_CHOOSER

is a component that lets the user pick various
attributes for fonts.

- GROUP_BOX

```java
public static final
AccessibleRole
GROUP_BOX
```

A

GROUP_BOX

is a simple container that contains a border around
it and contains components inside it.

- HEADER

```java
public static final
AccessibleRole
HEADER
```

A text header.

**Since:** 1.5

- FOOTER

```java
public static final
AccessibleRole
FOOTER
```

A text footer.

**Since:** 1.5

- PARAGRAPH

```java
public static final
AccessibleRole
PARAGRAPH
```

A text paragraph.

**Since:** 1.5

- RULER

```java
public static final
AccessibleRole
RULER
```

A ruler is an object used to measure distance.

**Since:** 1.5

- EDITBAR

```java
public static final
AccessibleRole
EDITBAR
```

A role indicating the object acts as a formula for calculating a value.
An example is a formula in a spreadsheet cell.

**Since:** 1.5

- PROGRESS_MONITOR

```java
public static final
AccessibleRole
PROGRESS_MONITOR
```

A role indicating the object monitors the progress of some operation.

**Since:** 1.5

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AccessibleRole

```java
protected AccessibleRole​(
String
key)
```

Creates a new

AccessibleRole

using the given locale independent
key. This should not be a public method. Instead, it is used to create
the constants in this file to make it a strongly typed enumeration.
Subclasses of this class should enforce similar policy.

The key

String

should be a locale independent key for the role.
It is not intended to be used as the actual

String

to display to
the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

**Parameters:** key

- the locale independent name of the role
**See Also:** AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

Field Detail

- ALERT

```java
public static final
AccessibleRole
ALERT
```

Object is used to alert the user about something.

- COLUMN_HEADER

```java
public static final
AccessibleRole
COLUMN_HEADER
```

The header for a column of data.

- CANVAS

```java
public static final
AccessibleRole
CANVAS
```

Object that can be drawn into and is used to trap events.

**See Also:** FRAME

,

GLASS_PANE

,

LAYERED_PANE

- COMBO_BOX

```java
public static final
AccessibleRole
COMBO_BOX
```

A list of choices the user can select from. Also optionally allows the
user to enter a choice of their own.

- DESKTOP_ICON

```java
public static final
AccessibleRole
DESKTOP_ICON
```

An iconified internal frame in a

DESKTOP_PANE

.

**See Also:** DESKTOP_PANE

,

INTERNAL_FRAME

- HTML_CONTAINER

```java
public static final
AccessibleRole
HTML_CONTAINER
```

An object containing a collection of

Accessibles

that together
represents

HTML

content. The child

Accessibles

would
include objects implementing

AccessibleText

,

AccessibleHypertext

,

AccessibleIcon

, and other
interfaces.

**Since:** 1.6
**See Also:** HYPERLINK

,

AccessibleText

,

AccessibleHypertext

,

AccessibleHyperlink

,

AccessibleIcon

- INTERNAL_FRAME

```java
public static final
AccessibleRole
INTERNAL_FRAME
```

A frame-like object that is clipped by a desktop pane. The desktop pane,
internal frame, and desktop icon objects are often used to create
multiple document interfaces within an application.

**See Also:** DESKTOP_ICON

,

DESKTOP_PANE

,

FRAME

- DESKTOP_PANE

```java
public static final
AccessibleRole
DESKTOP_PANE
```

A pane that supports internal frames and iconified versions of those
internal frames.

**See Also:** DESKTOP_ICON

,

INTERNAL_FRAME

- OPTION_PANE

```java
public static final
AccessibleRole
OPTION_PANE
```

A specialized pane whose primary use is inside a

DIALOG

.

**See Also:** DIALOG

- WINDOW

```java
public static final
AccessibleRole
WINDOW
```

A top level window with no title or border.

**See Also:** FRAME

,

DIALOG

- FRAME

```java
public static final
AccessibleRole
FRAME
```

A top level window with a title bar, border, menu bar, etc. It is often
used as the primary window for an application.

**See Also:** DIALOG

,

CANVAS

,

WINDOW

- DIALOG

```java
public static final
AccessibleRole
DIALOG
```

A top level window with title bar and a border. A dialog is similar to a
frame, but it has fewer properties and is often used as a secondary
window for an application.

**See Also:** FRAME

,

WINDOW

- COLOR_CHOOSER

```java
public static final
AccessibleRole
COLOR_CHOOSER
```

A specialized pane that lets the user choose a color.

- DIRECTORY_PANE

```java
public static final
AccessibleRole
DIRECTORY_PANE
```

A pane that allows the user to navigate through and select the contents
of a directory. May be used by a file chooser.

**See Also:** FILE_CHOOSER

- FILE_CHOOSER

```java
public static final
AccessibleRole
FILE_CHOOSER
```

A specialized dialog that displays the files in the directory and lets
the user select a file, browse a different directory, or specify a
filename. May use the directory pane to show the contents of a directory.

**See Also:** DIRECTORY_PANE

- FILLER

```java
public static final
AccessibleRole
FILLER
```

An object that fills up space in a user interface. It is often used in
interfaces to tweak the spacing between components, but serves no other
purpose.

- HYPERLINK

```java
public static final
AccessibleRole
HYPERLINK
```

A hypertext anchor.

- ICON

```java
public static final
AccessibleRole
ICON
```

A small fixed size picture, typically used to decorate components.

- LABEL

```java
public static final
AccessibleRole
LABEL
```

An object used to present an icon or short string in an interface.

- ROOT_PANE

```java
public static final
AccessibleRole
ROOT_PANE
```

A specialized pane that has a glass pane and a layered pane as its
children.

**See Also:** GLASS_PANE

,

LAYERED_PANE

- GLASS_PANE

```java
public static final
AccessibleRole
GLASS_PANE
```

A pane that is guaranteed to be painted on top of all panes beneath it.

**See Also:** ROOT_PANE

,

CANVAS

- LAYERED_PANE

```java
public static final
AccessibleRole
LAYERED_PANE
```

A specialized pane that allows its children to be drawn in layers,
providing a form of stacking order. This is usually the pane that holds
the menu bar as well as the pane that contains most of the visual
components in a window.

**See Also:** GLASS_PANE

,

ROOT_PANE

- LIST

```java
public static final
AccessibleRole
LIST
```

An object that presents a list of objects to the user and allows the user
to select one or more of them. A list is usually contained within a
scroll pane.

**See Also:** SCROLL_PANE

,

LIST_ITEM

- LIST_ITEM

```java
public static final
AccessibleRole
LIST_ITEM
```

An object that presents an element in a list. A list is usually contained
within a scroll pane.

**See Also:** SCROLL_PANE

,

LIST

- MENU_BAR

```java
public static final
AccessibleRole
MENU_BAR
```

An object usually drawn at the top of the primary dialog box of an
application that contains a list of menus the user can choose from. For
example, a menu bar might contain menus for "File," "Edit," and "Help."

**See Also:** MENU

,

POPUP_MENU

,

LAYERED_PANE

- POPUP_MENU

```java
public static final
AccessibleRole
POPUP_MENU
```

A temporary window that is usually used to offer the user a list of
choices, and then hides when the user selects one of those choices.

**See Also:** MENU

,

MENU_ITEM

- MENU

```java
public static final
AccessibleRole
MENU
```

An object usually found inside a menu bar that contains a list of actions
the user can choose from. A menu can have any object as its children, but
most often they are menu items, other menus, or rudimentary objects such
as radio buttons, check boxes, or separators. For example, an application
may have an "Edit" menu that contains menu items for "Cut" and "Paste."

**See Also:** MENU_BAR

,

MENU_ITEM

,

SEPARATOR

,

RADIO_BUTTON

,

CHECK_BOX

,

POPUP_MENU

- MENU_ITEM

```java
public static final
AccessibleRole
MENU_ITEM
```

An object usually contained in a menu that presents an action the user
can choose. For example, the "Cut" menu item in an "Edit" menu would be
an action the user can select to cut the selected area of text in a
document.

**See Also:** MENU_BAR

,

SEPARATOR

,

POPUP_MENU

- SEPARATOR

```java
public static final
AccessibleRole
SEPARATOR
```

An object usually contained in a menu to provide a visual and logical
separation of the contents in a menu. For example, the "File" menu of an
application might contain menu items for "Open," "Close," and "Exit," and
will place a separator between "Close" and "Exit" menu items.

**See Also:** MENU

,

MENU_ITEM

- PAGE_TAB_LIST

```java
public static final
AccessibleRole
PAGE_TAB_LIST
```

An object that presents a series of panels (or page tabs), one at a time,
through some mechanism provided by the object. The most common mechanism
is a list of tabs at the top of the panel. The children of a page tab
list are all page tabs.

**See Also:** PAGE_TAB

- PAGE_TAB

```java
public static final
AccessibleRole
PAGE_TAB
```

An object that is a child of a page tab list. Its sole child is the panel
that is to be presented to the user when the user selects the page tab
from the list of tabs in the page tab list.

**See Also:** PAGE_TAB_LIST

- PANEL

```java
public static final
AccessibleRole
PANEL
```

A generic container that is often used to group objects.

- PROGRESS_BAR

```java
public static final
AccessibleRole
PROGRESS_BAR
```

An object used to indicate how much of a task has been completed.

- PASSWORD_TEXT

```java
public static final
AccessibleRole
PASSWORD_TEXT
```

A text object used for passwords, or other places where the text contents
is not shown visibly to the user.

- PUSH_BUTTON

```java
public static final
AccessibleRole
PUSH_BUTTON
```

An object the user can manipulate to tell the application to do
something.

**See Also:** CHECK_BOX

,

TOGGLE_BUTTON

,

RADIO_BUTTON

- TOGGLE_BUTTON

```java
public static final
AccessibleRole
TOGGLE_BUTTON
```

A specialized push button that can be checked or unchecked, but does not
provide a separate indicator for the current state.

**See Also:** PUSH_BUTTON

,

CHECK_BOX

,

RADIO_BUTTON

- CHECK_BOX

```java
public static final
AccessibleRole
CHECK_BOX
```

A choice that can be checked or unchecked and provides a separate
indicator for the current state.

**See Also:** PUSH_BUTTON

,

TOGGLE_BUTTON

,

RADIO_BUTTON

- RADIO_BUTTON

```java
public static final
AccessibleRole
RADIO_BUTTON
```

A specialized check box that will cause other radio buttons in the same
group to become unchecked when this one is checked.

**See Also:** PUSH_BUTTON

,

TOGGLE_BUTTON

,

CHECK_BOX

- ROW_HEADER

```java
public static final
AccessibleRole
ROW_HEADER
```

The header for a row of data.

- SCROLL_PANE

```java
public static final
AccessibleRole
SCROLL_PANE
```

An object that allows a user to incrementally view a large amount of
information. Its children can include scroll bars and a viewport.

**See Also:** SCROLL_BAR

,

VIEWPORT

- SCROLL_BAR

```java
public static final
AccessibleRole
SCROLL_BAR
```

An object usually used to allow a user to incrementally view a large
amount of data. Usually used only by a scroll pane.

**See Also:** SCROLL_PANE

- VIEWPORT

```java
public static final
AccessibleRole
VIEWPORT
```

An object usually used in a scroll pane. It represents the portion of the
entire data that the user can see. As the user manipulates the scroll
bars, the contents of the viewport can change.

**See Also:** SCROLL_PANE

- SLIDER

```java
public static final
AccessibleRole
SLIDER
```

An object that allows the user to select from a bounded range. For
example, a slider might be used to select a number between 0 and 100.

- SPLIT_PANE

```java
public static final
AccessibleRole
SPLIT_PANE
```

A specialized panel that presents two other panels at the same time.
Between the two panels is a divider the user can manipulate to make one
panel larger and the other panel smaller.

- TABLE

```java
public static final
AccessibleRole
TABLE
```

An object used to present information in terms of rows and columns. An
example might include a spreadsheet application.

- TEXT

```java
public static final
AccessibleRole
TEXT
```

An object that presents text to the user. The text is usually editable by
the user as opposed to a label.

**See Also:** LABEL

- TREE

```java
public static final
AccessibleRole
TREE
```

An object used to present hierarchical information to the user. The
individual nodes in the tree can be collapsed and expanded to provide
selective disclosure of the tree's contents.

- TOOL_BAR

```java
public static final
AccessibleRole
TOOL_BAR
```

A bar or palette usually composed of push buttons or toggle buttons. It
is often used to provide the most frequently used functions for an
application.

- TOOL_TIP

```java
public static final
AccessibleRole
TOOL_TIP
```

An object that provides information about another object. The

accessibleDescription

property of the tool tip is often displayed
to the user in a small "help bubble" when the user causes the mouse to
hover over the object associated with the tool tip.

- AWT_COMPONENT

```java
public static final
AccessibleRole
AWT_COMPONENT
```

An AWT component, but nothing else is known about it.

**See Also:** SWING_COMPONENT

,

UNKNOWN

- SWING_COMPONENT

```java
public static final
AccessibleRole
SWING_COMPONENT
```

A Swing component, but nothing else is known about it.

**See Also:** AWT_COMPONENT

,

UNKNOWN

- UNKNOWN

```java
public static final
AccessibleRole
UNKNOWN
```

The object contains some

Accessible

information, but its role is
not known.

**See Also:** AWT_COMPONENT

,

SWING_COMPONENT

- STATUS_BAR

```java
public static final
AccessibleRole
STATUS_BAR
```

A

STATUS_BAR

is an simple component that can contain multiple
labels of status information to the user.

- DATE_EDITOR

```java
public static final
AccessibleRole
DATE_EDITOR
```

A

DATE_EDITOR

is a component that allows users to edit

java.util.Date

and

java.util.Time

objects.

- SPIN_BOX

```java
public static final
AccessibleRole
SPIN_BOX
```

A

SPIN_BOX

is a simple spinner component and its main use is for
simple numbers.

- FONT_CHOOSER

```java
public static final
AccessibleRole
FONT_CHOOSER
```

A

FONT_CHOOSER

is a component that lets the user pick various
attributes for fonts.

- GROUP_BOX

```java
public static final
AccessibleRole
GROUP_BOX
```

A

GROUP_BOX

is a simple container that contains a border around
it and contains components inside it.

- HEADER

```java
public static final
AccessibleRole
HEADER
```

A text header.

**Since:** 1.5

- FOOTER

```java
public static final
AccessibleRole
FOOTER
```

A text footer.

**Since:** 1.5

- PARAGRAPH

```java
public static final
AccessibleRole
PARAGRAPH
```

A text paragraph.

**Since:** 1.5

- RULER

```java
public static final
AccessibleRole
RULER
```

A ruler is an object used to measure distance.

**Since:** 1.5

- EDITBAR

```java
public static final
AccessibleRole
EDITBAR
```

A role indicating the object acts as a formula for calculating a value.
An example is a formula in a spreadsheet cell.

**Since:** 1.5

- PROGRESS_MONITOR

```java
public static final
AccessibleRole
PROGRESS_MONITOR
```

A role indicating the object monitors the progress of some operation.

**Since:** 1.5

---

#### Field Detail

ALERT

```java
public static final
AccessibleRole
ALERT
```

Object is used to alert the user about something.

---

#### ALERT

public static final

AccessibleRole

ALERT

Object is used to alert the user about something.

COLUMN_HEADER

```java
public static final
AccessibleRole
COLUMN_HEADER
```

The header for a column of data.

---

#### COLUMN_HEADER

public static final

AccessibleRole

COLUMN_HEADER

The header for a column of data.

CANVAS

```java
public static final
AccessibleRole
CANVAS
```

Object that can be drawn into and is used to trap events.

**See Also:** FRAME

,

GLASS_PANE

,

LAYERED_PANE

---

#### CANVAS

public static final

AccessibleRole

CANVAS

Object that can be drawn into and is used to trap events.

COMBO_BOX

```java
public static final
AccessibleRole
COMBO_BOX
```

A list of choices the user can select from. Also optionally allows the
user to enter a choice of their own.

---

#### COMBO_BOX

public static final

AccessibleRole

COMBO_BOX

A list of choices the user can select from. Also optionally allows the
user to enter a choice of their own.

DESKTOP_ICON

```java
public static final
AccessibleRole
DESKTOP_ICON
```

An iconified internal frame in a

DESKTOP_PANE

.

**See Also:** DESKTOP_PANE

,

INTERNAL_FRAME

---

#### DESKTOP_ICON

public static final

AccessibleRole

DESKTOP_ICON

An iconified internal frame in a

DESKTOP_PANE

.

HTML_CONTAINER

```java
public static final
AccessibleRole
HTML_CONTAINER
```

An object containing a collection of

Accessibles

that together
represents

HTML

content. The child

Accessibles

would
include objects implementing

AccessibleText

,

AccessibleHypertext

,

AccessibleIcon

, and other
interfaces.

**Since:** 1.6
**See Also:** HYPERLINK

,

AccessibleText

,

AccessibleHypertext

,

AccessibleHyperlink

,

AccessibleIcon

---

#### HTML_CONTAINER

public static final

AccessibleRole

HTML_CONTAINER

An object containing a collection of

Accessibles

that together
represents

HTML

content. The child

Accessibles

would
include objects implementing

AccessibleText

,

AccessibleHypertext

,

AccessibleIcon

, and other
interfaces.

INTERNAL_FRAME

```java
public static final
AccessibleRole
INTERNAL_FRAME
```

A frame-like object that is clipped by a desktop pane. The desktop pane,
internal frame, and desktop icon objects are often used to create
multiple document interfaces within an application.

**See Also:** DESKTOP_ICON

,

DESKTOP_PANE

,

FRAME

---

#### INTERNAL_FRAME

public static final

AccessibleRole

INTERNAL_FRAME

A frame-like object that is clipped by a desktop pane. The desktop pane,
internal frame, and desktop icon objects are often used to create
multiple document interfaces within an application.

DESKTOP_PANE

```java
public static final
AccessibleRole
DESKTOP_PANE
```

A pane that supports internal frames and iconified versions of those
internal frames.

**See Also:** DESKTOP_ICON

,

INTERNAL_FRAME

---

#### DESKTOP_PANE

public static final

AccessibleRole

DESKTOP_PANE

A pane that supports internal frames and iconified versions of those
internal frames.

OPTION_PANE

```java
public static final
AccessibleRole
OPTION_PANE
```

A specialized pane whose primary use is inside a

DIALOG

.

**See Also:** DIALOG

---

#### OPTION_PANE

public static final

AccessibleRole

OPTION_PANE

A specialized pane whose primary use is inside a

DIALOG

.

WINDOW

```java
public static final
AccessibleRole
WINDOW
```

A top level window with no title or border.

**See Also:** FRAME

,

DIALOG

---

#### WINDOW

public static final

AccessibleRole

WINDOW

A top level window with no title or border.

FRAME

```java
public static final
AccessibleRole
FRAME
```

A top level window with a title bar, border, menu bar, etc. It is often
used as the primary window for an application.

**See Also:** DIALOG

,

CANVAS

,

WINDOW

---

#### FRAME

public static final

AccessibleRole

FRAME

A top level window with a title bar, border, menu bar, etc. It is often
used as the primary window for an application.

DIALOG

```java
public static final
AccessibleRole
DIALOG
```

A top level window with title bar and a border. A dialog is similar to a
frame, but it has fewer properties and is often used as a secondary
window for an application.

**See Also:** FRAME

,

WINDOW

---

#### DIALOG

public static final

AccessibleRole

DIALOG

A top level window with title bar and a border. A dialog is similar to a
frame, but it has fewer properties and is often used as a secondary
window for an application.

COLOR_CHOOSER

```java
public static final
AccessibleRole
COLOR_CHOOSER
```

A specialized pane that lets the user choose a color.

---

#### COLOR_CHOOSER

public static final

AccessibleRole

COLOR_CHOOSER

A specialized pane that lets the user choose a color.

DIRECTORY_PANE

```java
public static final
AccessibleRole
DIRECTORY_PANE
```

A pane that allows the user to navigate through and select the contents
of a directory. May be used by a file chooser.

**See Also:** FILE_CHOOSER

---

#### DIRECTORY_PANE

public static final

AccessibleRole

DIRECTORY_PANE

A pane that allows the user to navigate through and select the contents
of a directory. May be used by a file chooser.

FILE_CHOOSER

```java
public static final
AccessibleRole
FILE_CHOOSER
```

A specialized dialog that displays the files in the directory and lets
the user select a file, browse a different directory, or specify a
filename. May use the directory pane to show the contents of a directory.

**See Also:** DIRECTORY_PANE

---

#### FILE_CHOOSER

public static final

AccessibleRole

FILE_CHOOSER

A specialized dialog that displays the files in the directory and lets
the user select a file, browse a different directory, or specify a
filename. May use the directory pane to show the contents of a directory.

FILLER

```java
public static final
AccessibleRole
FILLER
```

An object that fills up space in a user interface. It is often used in
interfaces to tweak the spacing between components, but serves no other
purpose.

---

#### FILLER

public static final

AccessibleRole

FILLER

An object that fills up space in a user interface. It is often used in
interfaces to tweak the spacing between components, but serves no other
purpose.

HYPERLINK

```java
public static final
AccessibleRole
HYPERLINK
```

A hypertext anchor.

---

#### HYPERLINK

public static final

AccessibleRole

HYPERLINK

A hypertext anchor.

ICON

```java
public static final
AccessibleRole
ICON
```

A small fixed size picture, typically used to decorate components.

---

#### ICON

public static final

AccessibleRole

ICON

A small fixed size picture, typically used to decorate components.

LABEL

```java
public static final
AccessibleRole
LABEL
```

An object used to present an icon or short string in an interface.

---

#### LABEL

public static final

AccessibleRole

LABEL

An object used to present an icon or short string in an interface.

ROOT_PANE

```java
public static final
AccessibleRole
ROOT_PANE
```

A specialized pane that has a glass pane and a layered pane as its
children.

**See Also:** GLASS_PANE

,

LAYERED_PANE

---

#### ROOT_PANE

public static final

AccessibleRole

ROOT_PANE

A specialized pane that has a glass pane and a layered pane as its
children.

GLASS_PANE

```java
public static final
AccessibleRole
GLASS_PANE
```

A pane that is guaranteed to be painted on top of all panes beneath it.

**See Also:** ROOT_PANE

,

CANVAS

---

#### GLASS_PANE

public static final

AccessibleRole

GLASS_PANE

A pane that is guaranteed to be painted on top of all panes beneath it.

LAYERED_PANE

```java
public static final
AccessibleRole
LAYERED_PANE
```

A specialized pane that allows its children to be drawn in layers,
providing a form of stacking order. This is usually the pane that holds
the menu bar as well as the pane that contains most of the visual
components in a window.

**See Also:** GLASS_PANE

,

ROOT_PANE

---

#### LAYERED_PANE

public static final

AccessibleRole

LAYERED_PANE

A specialized pane that allows its children to be drawn in layers,
providing a form of stacking order. This is usually the pane that holds
the menu bar as well as the pane that contains most of the visual
components in a window.

LIST

```java
public static final
AccessibleRole
LIST
```

An object that presents a list of objects to the user and allows the user
to select one or more of them. A list is usually contained within a
scroll pane.

**See Also:** SCROLL_PANE

,

LIST_ITEM

---

#### LIST

public static final

AccessibleRole

LIST

An object that presents a list of objects to the user and allows the user
to select one or more of them. A list is usually contained within a
scroll pane.

LIST_ITEM

```java
public static final
AccessibleRole
LIST_ITEM
```

An object that presents an element in a list. A list is usually contained
within a scroll pane.

**See Also:** SCROLL_PANE

,

LIST

---

#### LIST_ITEM

public static final

AccessibleRole

LIST_ITEM

An object that presents an element in a list. A list is usually contained
within a scroll pane.

MENU_BAR

```java
public static final
AccessibleRole
MENU_BAR
```

An object usually drawn at the top of the primary dialog box of an
application that contains a list of menus the user can choose from. For
example, a menu bar might contain menus for "File," "Edit," and "Help."

**See Also:** MENU

,

POPUP_MENU

,

LAYERED_PANE

---

#### MENU_BAR

public static final

AccessibleRole

MENU_BAR

An object usually drawn at the top of the primary dialog box of an
application that contains a list of menus the user can choose from. For
example, a menu bar might contain menus for "File," "Edit," and "Help."

POPUP_MENU

```java
public static final
AccessibleRole
POPUP_MENU
```

A temporary window that is usually used to offer the user a list of
choices, and then hides when the user selects one of those choices.

**See Also:** MENU

,

MENU_ITEM

---

#### POPUP_MENU

public static final

AccessibleRole

POPUP_MENU

A temporary window that is usually used to offer the user a list of
choices, and then hides when the user selects one of those choices.

MENU

```java
public static final
AccessibleRole
MENU
```

An object usually found inside a menu bar that contains a list of actions
the user can choose from. A menu can have any object as its children, but
most often they are menu items, other menus, or rudimentary objects such
as radio buttons, check boxes, or separators. For example, an application
may have an "Edit" menu that contains menu items for "Cut" and "Paste."

**See Also:** MENU_BAR

,

MENU_ITEM

,

SEPARATOR

,

RADIO_BUTTON

,

CHECK_BOX

,

POPUP_MENU

---

#### MENU

public static final

AccessibleRole

MENU

An object usually found inside a menu bar that contains a list of actions
the user can choose from. A menu can have any object as its children, but
most often they are menu items, other menus, or rudimentary objects such
as radio buttons, check boxes, or separators. For example, an application
may have an "Edit" menu that contains menu items for "Cut" and "Paste."

MENU_ITEM

```java
public static final
AccessibleRole
MENU_ITEM
```

An object usually contained in a menu that presents an action the user
can choose. For example, the "Cut" menu item in an "Edit" menu would be
an action the user can select to cut the selected area of text in a
document.

**See Also:** MENU_BAR

,

SEPARATOR

,

POPUP_MENU

---

#### MENU_ITEM

public static final

AccessibleRole

MENU_ITEM

An object usually contained in a menu that presents an action the user
can choose. For example, the "Cut" menu item in an "Edit" menu would be
an action the user can select to cut the selected area of text in a
document.

SEPARATOR

```java
public static final
AccessibleRole
SEPARATOR
```

An object usually contained in a menu to provide a visual and logical
separation of the contents in a menu. For example, the "File" menu of an
application might contain menu items for "Open," "Close," and "Exit," and
will place a separator between "Close" and "Exit" menu items.

**See Also:** MENU

,

MENU_ITEM

---

#### SEPARATOR

public static final

AccessibleRole

SEPARATOR

An object usually contained in a menu to provide a visual and logical
separation of the contents in a menu. For example, the "File" menu of an
application might contain menu items for "Open," "Close," and "Exit," and
will place a separator between "Close" and "Exit" menu items.

PAGE_TAB_LIST

```java
public static final
AccessibleRole
PAGE_TAB_LIST
```

An object that presents a series of panels (or page tabs), one at a time,
through some mechanism provided by the object. The most common mechanism
is a list of tabs at the top of the panel. The children of a page tab
list are all page tabs.

**See Also:** PAGE_TAB

---

#### PAGE_TAB_LIST

public static final

AccessibleRole

PAGE_TAB_LIST

An object that presents a series of panels (or page tabs), one at a time,
through some mechanism provided by the object. The most common mechanism
is a list of tabs at the top of the panel. The children of a page tab
list are all page tabs.

PAGE_TAB

```java
public static final
AccessibleRole
PAGE_TAB
```

An object that is a child of a page tab list. Its sole child is the panel
that is to be presented to the user when the user selects the page tab
from the list of tabs in the page tab list.

**See Also:** PAGE_TAB_LIST

---

#### PAGE_TAB

public static final

AccessibleRole

PAGE_TAB

An object that is a child of a page tab list. Its sole child is the panel
that is to be presented to the user when the user selects the page tab
from the list of tabs in the page tab list.

PANEL

```java
public static final
AccessibleRole
PANEL
```

A generic container that is often used to group objects.

---

#### PANEL

public static final

AccessibleRole

PANEL

A generic container that is often used to group objects.

PROGRESS_BAR

```java
public static final
AccessibleRole
PROGRESS_BAR
```

An object used to indicate how much of a task has been completed.

---

#### PROGRESS_BAR

public static final

AccessibleRole

PROGRESS_BAR

An object used to indicate how much of a task has been completed.

PASSWORD_TEXT

```java
public static final
AccessibleRole
PASSWORD_TEXT
```

A text object used for passwords, or other places where the text contents
is not shown visibly to the user.

---

#### PASSWORD_TEXT

public static final

AccessibleRole

PASSWORD_TEXT

A text object used for passwords, or other places where the text contents
is not shown visibly to the user.

PUSH_BUTTON

```java
public static final
AccessibleRole
PUSH_BUTTON
```

An object the user can manipulate to tell the application to do
something.

**See Also:** CHECK_BOX

,

TOGGLE_BUTTON

,

RADIO_BUTTON

---

#### PUSH_BUTTON

public static final

AccessibleRole

PUSH_BUTTON

An object the user can manipulate to tell the application to do
something.

TOGGLE_BUTTON

```java
public static final
AccessibleRole
TOGGLE_BUTTON
```

A specialized push button that can be checked or unchecked, but does not
provide a separate indicator for the current state.

**See Also:** PUSH_BUTTON

,

CHECK_BOX

,

RADIO_BUTTON

---

#### TOGGLE_BUTTON

public static final

AccessibleRole

TOGGLE_BUTTON

A specialized push button that can be checked or unchecked, but does not
provide a separate indicator for the current state.

CHECK_BOX

```java
public static final
AccessibleRole
CHECK_BOX
```

A choice that can be checked or unchecked and provides a separate
indicator for the current state.

**See Also:** PUSH_BUTTON

,

TOGGLE_BUTTON

,

RADIO_BUTTON

---

#### CHECK_BOX

public static final

AccessibleRole

CHECK_BOX

A choice that can be checked or unchecked and provides a separate
indicator for the current state.

RADIO_BUTTON

```java
public static final
AccessibleRole
RADIO_BUTTON
```

A specialized check box that will cause other radio buttons in the same
group to become unchecked when this one is checked.

**See Also:** PUSH_BUTTON

,

TOGGLE_BUTTON

,

CHECK_BOX

---

#### RADIO_BUTTON

public static final

AccessibleRole

RADIO_BUTTON

A specialized check box that will cause other radio buttons in the same
group to become unchecked when this one is checked.

ROW_HEADER

```java
public static final
AccessibleRole
ROW_HEADER
```

The header for a row of data.

---

#### ROW_HEADER

public static final

AccessibleRole

ROW_HEADER

The header for a row of data.

SCROLL_PANE

```java
public static final
AccessibleRole
SCROLL_PANE
```

An object that allows a user to incrementally view a large amount of
information. Its children can include scroll bars and a viewport.

**See Also:** SCROLL_BAR

,

VIEWPORT

---

#### SCROLL_PANE

public static final

AccessibleRole

SCROLL_PANE

An object that allows a user to incrementally view a large amount of
information. Its children can include scroll bars and a viewport.

SCROLL_BAR

```java
public static final
AccessibleRole
SCROLL_BAR
```

An object usually used to allow a user to incrementally view a large
amount of data. Usually used only by a scroll pane.

**See Also:** SCROLL_PANE

---

#### SCROLL_BAR

public static final

AccessibleRole

SCROLL_BAR

An object usually used to allow a user to incrementally view a large
amount of data. Usually used only by a scroll pane.

VIEWPORT

```java
public static final
AccessibleRole
VIEWPORT
```

An object usually used in a scroll pane. It represents the portion of the
entire data that the user can see. As the user manipulates the scroll
bars, the contents of the viewport can change.

**See Also:** SCROLL_PANE

---

#### VIEWPORT

public static final

AccessibleRole

VIEWPORT

An object usually used in a scroll pane. It represents the portion of the
entire data that the user can see. As the user manipulates the scroll
bars, the contents of the viewport can change.

SLIDER

```java
public static final
AccessibleRole
SLIDER
```

An object that allows the user to select from a bounded range. For
example, a slider might be used to select a number between 0 and 100.

---

#### SLIDER

public static final

AccessibleRole

SLIDER

An object that allows the user to select from a bounded range. For
example, a slider might be used to select a number between 0 and 100.

SPLIT_PANE

```java
public static final
AccessibleRole
SPLIT_PANE
```

A specialized panel that presents two other panels at the same time.
Between the two panels is a divider the user can manipulate to make one
panel larger and the other panel smaller.

---

#### SPLIT_PANE

public static final

AccessibleRole

SPLIT_PANE

A specialized panel that presents two other panels at the same time.
Between the two panels is a divider the user can manipulate to make one
panel larger and the other panel smaller.

TABLE

```java
public static final
AccessibleRole
TABLE
```

An object used to present information in terms of rows and columns. An
example might include a spreadsheet application.

---

#### TABLE

public static final

AccessibleRole

TABLE

An object used to present information in terms of rows and columns. An
example might include a spreadsheet application.

TEXT

```java
public static final
AccessibleRole
TEXT
```

An object that presents text to the user. The text is usually editable by
the user as opposed to a label.

**See Also:** LABEL

---

#### TEXT

public static final

AccessibleRole

TEXT

An object that presents text to the user. The text is usually editable by
the user as opposed to a label.

TREE

```java
public static final
AccessibleRole
TREE
```

An object used to present hierarchical information to the user. The
individual nodes in the tree can be collapsed and expanded to provide
selective disclosure of the tree's contents.

---

#### TREE

public static final

AccessibleRole

TREE

An object used to present hierarchical information to the user. The
individual nodes in the tree can be collapsed and expanded to provide
selective disclosure of the tree's contents.

TOOL_BAR

```java
public static final
AccessibleRole
TOOL_BAR
```

A bar or palette usually composed of push buttons or toggle buttons. It
is often used to provide the most frequently used functions for an
application.

---

#### TOOL_BAR

public static final

AccessibleRole

TOOL_BAR

A bar or palette usually composed of push buttons or toggle buttons. It
is often used to provide the most frequently used functions for an
application.

TOOL_TIP

```java
public static final
AccessibleRole
TOOL_TIP
```

An object that provides information about another object. The

accessibleDescription

property of the tool tip is often displayed
to the user in a small "help bubble" when the user causes the mouse to
hover over the object associated with the tool tip.

---

#### TOOL_TIP

public static final

AccessibleRole

TOOL_TIP

An object that provides information about another object. The

accessibleDescription

property of the tool tip is often displayed
to the user in a small "help bubble" when the user causes the mouse to
hover over the object associated with the tool tip.

AWT_COMPONENT

```java
public static final
AccessibleRole
AWT_COMPONENT
```

An AWT component, but nothing else is known about it.

**See Also:** SWING_COMPONENT

,

UNKNOWN

---

#### AWT_COMPONENT

public static final

AccessibleRole

AWT_COMPONENT

An AWT component, but nothing else is known about it.

SWING_COMPONENT

```java
public static final
AccessibleRole
SWING_COMPONENT
```

A Swing component, but nothing else is known about it.

**See Also:** AWT_COMPONENT

,

UNKNOWN

---

#### SWING_COMPONENT

public static final

AccessibleRole

SWING_COMPONENT

A Swing component, but nothing else is known about it.

UNKNOWN

```java
public static final
AccessibleRole
UNKNOWN
```

The object contains some

Accessible

information, but its role is
not known.

**See Also:** AWT_COMPONENT

,

SWING_COMPONENT

---

#### UNKNOWN

public static final

AccessibleRole

UNKNOWN

The object contains some

Accessible

information, but its role is
not known.

STATUS_BAR

```java
public static final
AccessibleRole
STATUS_BAR
```

A

STATUS_BAR

is an simple component that can contain multiple
labels of status information to the user.

---

#### STATUS_BAR

public static final

AccessibleRole

STATUS_BAR

A

STATUS_BAR

is an simple component that can contain multiple
labels of status information to the user.

DATE_EDITOR

```java
public static final
AccessibleRole
DATE_EDITOR
```

A

DATE_EDITOR

is a component that allows users to edit

java.util.Date

and

java.util.Time

objects.

---

#### DATE_EDITOR

public static final

AccessibleRole

DATE_EDITOR

A

DATE_EDITOR

is a component that allows users to edit

java.util.Date

and

java.util.Time

objects.

SPIN_BOX

```java
public static final
AccessibleRole
SPIN_BOX
```

A

SPIN_BOX

is a simple spinner component and its main use is for
simple numbers.

---

#### SPIN_BOX

public static final

AccessibleRole

SPIN_BOX

A

SPIN_BOX

is a simple spinner component and its main use is for
simple numbers.

FONT_CHOOSER

```java
public static final
AccessibleRole
FONT_CHOOSER
```

A

FONT_CHOOSER

is a component that lets the user pick various
attributes for fonts.

---

#### FONT_CHOOSER

public static final

AccessibleRole

FONT_CHOOSER

A

FONT_CHOOSER

is a component that lets the user pick various
attributes for fonts.

GROUP_BOX

```java
public static final
AccessibleRole
GROUP_BOX
```

A

GROUP_BOX

is a simple container that contains a border around
it and contains components inside it.

---

#### GROUP_BOX

public static final

AccessibleRole

GROUP_BOX

A

GROUP_BOX

is a simple container that contains a border around
it and contains components inside it.

HEADER

```java
public static final
AccessibleRole
HEADER
```

A text header.

**Since:** 1.5

---

#### HEADER

public static final

AccessibleRole

HEADER

A text header.

FOOTER

```java
public static final
AccessibleRole
FOOTER
```

A text footer.

**Since:** 1.5

---

#### FOOTER

public static final

AccessibleRole

FOOTER

A text footer.

PARAGRAPH

```java
public static final
AccessibleRole
PARAGRAPH
```

A text paragraph.

**Since:** 1.5

---

#### PARAGRAPH

public static final

AccessibleRole

PARAGRAPH

A text paragraph.

RULER

```java
public static final
AccessibleRole
RULER
```

A ruler is an object used to measure distance.

**Since:** 1.5

---

#### RULER

public static final

AccessibleRole

RULER

A ruler is an object used to measure distance.

EDITBAR

```java
public static final
AccessibleRole
EDITBAR
```

A role indicating the object acts as a formula for calculating a value.
An example is a formula in a spreadsheet cell.

**Since:** 1.5

---

#### EDITBAR

public static final

AccessibleRole

EDITBAR

A role indicating the object acts as a formula for calculating a value.
An example is a formula in a spreadsheet cell.

PROGRESS_MONITOR

```java
public static final
AccessibleRole
PROGRESS_MONITOR
```

A role indicating the object monitors the progress of some operation.

**Since:** 1.5

---

#### PROGRESS_MONITOR

public static final

AccessibleRole

PROGRESS_MONITOR

A role indicating the object monitors the progress of some operation.

Constructor Detail

- AccessibleRole

```java
protected AccessibleRole​(
String
key)
```

Creates a new

AccessibleRole

using the given locale independent
key. This should not be a public method. Instead, it is used to create
the constants in this file to make it a strongly typed enumeration.
Subclasses of this class should enforce similar policy.

The key

String

should be a locale independent key for the role.
It is not intended to be used as the actual

String

to display to
the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

**Parameters:** key

- the locale independent name of the role
**See Also:** AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

---

#### Constructor Detail

AccessibleRole

```java
protected AccessibleRole​(
String
key)
```

Creates a new

AccessibleRole

using the given locale independent
key. This should not be a public method. Instead, it is used to create
the constants in this file to make it a strongly typed enumeration.
Subclasses of this class should enforce similar policy.

The key

String

should be a locale independent key for the role.
It is not intended to be used as the actual

String

to display to
the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

**Parameters:** key

- the locale independent name of the role
**See Also:** AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

---

#### AccessibleRole

protected AccessibleRole​(

String

key)

Creates a new

AccessibleRole

using the given locale independent
key. This should not be a public method. Instead, it is used to create
the constants in this file to make it a strongly typed enumeration.
Subclasses of this class should enforce similar policy.

The key

String

should be a locale independent key for the role.
It is not intended to be used as the actual

String

to display to
the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

The key

String

should be a locale independent key for the role.
It is not intended to be used as the actual

String

to display to
the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

---

