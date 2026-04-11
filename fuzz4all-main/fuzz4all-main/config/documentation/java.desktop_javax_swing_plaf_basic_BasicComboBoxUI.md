# Class BasicComboBoxUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicComboBoxUI.html`

### Class Description

```java
public class
BasicComboBoxUI

extends
ComboBoxUI
```

Basic UI implementation for JComboBox.

The combo box is a compound component which means that it is an aggregate of
many simpler components. This class creates and manages the listeners
on the combo box and the combo box model. These listeners update the user
interface in response to changes in the properties and state of the combo box.

All event handling is handled by listener classes created with the

createxxxListener()

methods and internal classes.
You can change the behavior of this class by overriding the

createxxxListener()

methods and supplying your own
event listeners or subclassing from the ones supplied in this class.

For adding specific actions,
overide

installKeyboardActions

to add actions in response to
KeyStroke bindings. See the article

How to Use Key Bindings

**Direct Known Subclasses:** MetalComboBoxUI

,

SynthComboBoxUI

---

### Field Details

#### protected
JComboBox
<
Object
> comboBox

The instance of

JComboBox

.

---

#### protected boolean hasFocus

This protected field is implementation specific. Do not access directly
or override.

---

#### protected
JList
<
Object
> listBox

This list is for drawing the current item in the combo box.

---

#### protected
CellRendererPane
currentValuePane

Used to render the currently selected item in the combo box.
It doesn't have anything to do with the popup's rendering.

---

#### protected
ComboPopup
popup

The implementation of

ComboPopup

that is used to show the popup.

---

#### protected
Component
editor

The Component that the @{code ComboBoxEditor} uses for editing.

---

#### protected
JButton
arrowButton

The arrow button that invokes the popup.

---

#### protected
KeyListener
keyListener

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

**See Also:**
- createKeyListener()

---

#### protected
FocusListener
focusListener

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

**See Also:**
- createFocusListener()

---

#### protected
PropertyChangeListener
propertyChangeListener

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

**See Also:**
- createPropertyChangeListener()

---

#### protected
ItemListener
itemListener

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

**See Also:**
- createItemListener()

---

#### protected
MouseListener
popupMouseListener

The

MouseListener

listens to events.

---

#### protected
MouseMotionListener
popupMouseMotionListener

The

MouseMotionListener

listens to events.

---

#### protected
KeyListener
popupKeyListener

The

KeyListener

listens to events.

---

#### protected
ListDataListener
listDataListener

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

**See Also:**
- createListDataListener()

---

#### protected boolean isMinimumSizeDirty

The flag for recalculating the minimum preferred size.

---

#### protected
Dimension
cachedMinimumSize

The cached minimum preferred size.

---

#### protected boolean squareButton

Indicates whether or not the combo box button should be square.
If square, then the width and height are equal, and are both set to
the height of the combo minus appropriate insets.

**Since:**
- 1.7

---

#### protected
Insets
padding

If specified, these insets act as padding around the cell renderer when
laying out and painting the "selected" item in the combo box. These
insets add to those specified by the cell renderer.

**Since:**
- 1.7

---

### Constructor Details

#### public BasicComboBoxUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Constructs a new instance of

BasicComboBoxUI

.

**Parameters:**
- c

- a component

**Returns:**
- a new instance of

BasicComboBoxUI

---

#### protected void installDefaults()

Installs the default colors, default font, default renderer, and default
editor into the JComboBox.

---

#### protected void installListeners()

Creates and installs listeners for the combo box and its model.
This method is called when the UI is installed.

---

#### protected void uninstallDefaults()

Uninstalls the default colors, default font, default renderer,
and default editor from the combo box.

---

#### protected void uninstallListeners()

Removes the installed listeners from the combo box and its model.
The number and types of listeners removed and in this method should be
the same that was added in

installListeners

---

#### protected
ComboPopup
createPopup()

Creates the popup portion of the combo box.

**Returns:**
- an instance of

ComboPopup

**See Also:**
- ComboPopup

---

#### protected
KeyListener
createKeyListener()

Creates a

KeyListener

which will be added to the
combo box. If this method returns null then it will not be added
to the combo box.

**Returns:**
- an instance

KeyListener

or null

---

#### protected
FocusListener
createFocusListener()

Creates a

FocusListener

which will be added to the combo box.
If this method returns null then it will not be added to the combo box.

**Returns:**
- an instance of a

FocusListener

or null

---

#### protected
ListDataListener
createListDataListener()

Creates a list data listener which will be added to the

ComboBoxModel

. If this method returns null then
it will not be added to the combo box model.

**Returns:**
- an instance of a

ListDataListener

or null

---

#### protected
ItemListener
createItemListener()

Creates an

ItemListener

which will be added to the
combo box. If this method returns null then it will not
be added to the combo box.

Subclasses may override this method to return instances of their own
ItemEvent handlers.

**Returns:**
- an instance of an

ItemListener

or null

---

#### protected
PropertyChangeListener
createPropertyChangeListener()

Creates a

PropertyChangeListener

which will be added to
the combo box. If this method returns null then it will not
be added to the combo box.

**Returns:**
- an instance of a

PropertyChangeListener

or null

---

#### protected
LayoutManager
createLayoutManager()

Creates a layout manager for managing the components which make up the
combo box.

**Returns:**
- an instance of a layout manager

---

#### protected
ListCellRenderer
<
Object
> createRenderer()

Creates the default renderer that will be used in a non-editiable combo
box. A default renderer will used only if a renderer has not been
explicitly set with

setRenderer

.

**Returns:**
- a

ListCellRender

used for the combo box

**See Also:**
- JComboBox.setRenderer(javax.swing.ListCellRenderer<? super E>)

---

#### protected
ComboBoxEditor
createEditor()

Creates the default editor that will be used in editable combo boxes.
A default editor will be used only if an editor has not been
explicitly set with

setEditor

.

**Returns:**
- a

ComboBoxEditor

used for the combo box

**See Also:**
- JComboBox.setEditor(javax.swing.ComboBoxEditor)

---

#### protected void installComponents()

Creates and initializes the components which make up the
aggregate combo box. This method is called as part of the UI
installation process.

---

#### protected void uninstallComponents()

The aggregate components which comprise the combo box are
unregistered and uninitialized. This method is called as part of the
UI uninstallation process.

---

#### public void addEditor()

This public method is implementation specific and should be private.
do not call or override. To implement a specific editor create a
custom

ComboBoxEditor

**See Also:**
- createEditor()

,

JComboBox.setEditor(javax.swing.ComboBoxEditor)

,

ComboBoxEditor

---

#### public void removeEditor()

This public method is implementation specific and should be private.
do not call or override.

**See Also:**
- addEditor()

---

#### protected void configureEditor()

This protected method is implementation specific and should be private.
do not call or override.

**See Also:**
- addEditor()

---

#### protected void unconfigureEditor()

This protected method is implementation specific and should be private.
Do not call or override.

**See Also:**
- addEditor()

---

#### public void configureArrowButton()

This public method is implementation specific and should be private. Do
not call or override.

**See Also:**
- createArrowButton()

---

#### public void unconfigureArrowButton()

This public method is implementation specific and should be private. Do
not call or override.

**See Also:**
- createArrowButton()

---

#### protected
JButton
createArrowButton()

Creates a button which will be used as the control to show or hide
the popup portion of the combo box.

**Returns:**
- a button which represents the popup control

---

#### public boolean isPopupVisible​(
JComboBox
<?> c)

Tells if the popup is visible or not.

**Specified by:**
- isPopupVisible

in class

ComboBoxUI

**Parameters:**
- c

- a

JComboBox

**Returns:**
- true if popup of the

JComboBox

is visible

---

#### public void setPopupVisible​(
JComboBox
<?> c,
boolean v)

Hides the popup.

**Specified by:**
- setPopupVisible

in class

ComboBoxUI

**Parameters:**
- c

- a

JComboBox
- v

- a

boolean

determining the visibilty of the popup

---

#### public boolean isFocusTraversable​(
JComboBox
<?> c)

Determines if the JComboBox is focus traversable. If the JComboBox is editable
this returns false, otherwise it returns true.

**Specified by:**
- isFocusTraversable

in class

ComboBoxUI

**Parameters:**
- c

- a

JComboBox

**Returns:**
- true if the given

JComboBox

is traversable

---

#### public
Dimension
getMinimumSize​(
JComponent
c)

The minimum size is the size of the display area plus insets plus the button.

**Overrides:**
- getMinimumSize

in class

ComponentUI

**Parameters:**
- c

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**Returns:**
- a

Dimension

object or

null

**See Also:**
- JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

---

#### public int getBaseline​(
JComponent
c,
int width,
int height)

Returns the baseline.

**Overrides:**
- getBaseline

in class

ComponentUI

**Parameters:**
- c

-

JComponent

baseline is being requested for
- width

- the width to get the baseline for
- height

- the height to get the baseline for

**Returns:**
- baseline or a value < 0 indicating there is no reasonable
baseline

**Throws:**
- NullPointerException

- if

c

is

null
- IllegalArgumentException

- if width or height is < 0

**See Also:**
- JComponent.getBaseline(int, int)

**Since:**
- 1.6

---

#### public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

**Overrides:**
- getBaselineResizeBehavior

in class

ComponentUI

**Parameters:**
- c

-

JComponent

to return baseline resize behavior for

**Returns:**
- an enum indicating how the baseline changes as the component
size changes

**Throws:**
- NullPointerException

- if

c

is

null

**See Also:**
- JComponent.getBaseline(int, int)

**Since:**
- 1.6

---

#### protected boolean isNavigationKey​(int keyCode)

Returns whether or not the supplied keyCode maps to a key that is used for
navigation. This is used for optimizing key input by only passing non-
navigation keys to the type-ahead mechanism. Subclasses should override this
if they change the navigation keys.

**Parameters:**
- keyCode

- a key code

**Returns:**
- true

if the supplied

keyCode

maps to a navigation key

---

#### protected void selectNextPossibleValue()

Selects the next item in the list. It won't change the selection if the
currently selected item is already the last item.

---

#### protected void selectPreviousPossibleValue()

Selects the previous item in the list. It won't change the selection if the
currently selected item is already the first item.

---

#### protected void toggleOpenClose()

Hides the popup if it is showing and shows the popup if it is hidden.

---

#### protected
Rectangle
rectangleForCurrentValue()

Returns the area that is reserved for drawing the currently selected item.

**Returns:**
- the area that is reserved for drawing the currently selected item

---

#### protected
Insets
getInsets()

Gets the insets from the JComboBox.

**Returns:**
- the insets

---

#### public void paintCurrentValue​(
Graphics
g,

Rectangle
bounds,
boolean hasFocus)

Paints the currently selected item.

**Parameters:**
- g

- an instance of

Graphics
- bounds

- a bounding rectangle to render to
- hasFocus

- is focused

---

#### public void paintCurrentValueBackground​(
Graphics
g,

Rectangle
bounds,
boolean hasFocus)

Paints the background of the currently selected item.

**Parameters:**
- g

- an instance of

Graphics
- bounds

- a bounding rectangle to render to
- hasFocus

- is focused

---

#### protected
Dimension
getDefaultSize()

Return the default size of an empty display area of the combo box using
the current renderer and font.

**Returns:**
- the size of an empty display area

**See Also:**
- getDisplaySize()

---

#### protected
Dimension
getDisplaySize()

Returns the calculated size of the display area. The display area is the
portion of the combo box in which the selected item is displayed. This
method will use the prototype display value if it has been set.

For combo boxes with a non trivial number of items, it is recommended to
use a prototype display value to significantly speed up the display
size calculation.

**Returns:**
- the size of the display area calculated from the combo box items

**See Also:**
- JComboBox.setPrototypeDisplayValue(E)

---

#### protected
Dimension
getSizeForComponent​(
Component
comp)

Returns the size a component would have if used as a cell renderer.

**Parameters:**
- comp

- a

Component

to check

**Returns:**
- size of the component

**Since:**
- 1.7

---

#### protected void installKeyboardActions()

Adds keyboard actions to the JComboBox. Actions on enter and esc are already
supplied. Add more actions as you need them.

---

#### protected void uninstallKeyboardActions()

Removes the focus InputMap and ActionMap.

---

### Additional Sections

#### Class BasicComboBoxUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ComboBoxUI
- - javax.swing.plaf.basic.BasicComboBoxUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ComboBoxUI
- - javax.swing.plaf.basic.BasicComboBoxUI

javax.swing.plaf.ComboBoxUI

- javax.swing.plaf.basic.BasicComboBoxUI

javax.swing.plaf.basic.BasicComboBoxUI

**Direct Known Subclasses:** MetalComboBoxUI

,

SynthComboBoxUI

```java
public class
BasicComboBoxUI

extends
ComboBoxUI
```

Basic UI implementation for JComboBox.

The combo box is a compound component which means that it is an aggregate of
many simpler components. This class creates and manages the listeners
on the combo box and the combo box model. These listeners update the user
interface in response to changes in the properties and state of the combo box.

All event handling is handled by listener classes created with the

createxxxListener()

methods and internal classes.
You can change the behavior of this class by overriding the

createxxxListener()

methods and supplying your own
event listeners or subclassing from the ones supplied in this class.

For adding specific actions,
overide

installKeyboardActions

to add actions in response to
KeyStroke bindings. See the article

How to Use Key Bindings

public class

BasicComboBoxUI

extends

ComboBoxUI

Basic UI implementation for JComboBox.

The combo box is a compound component which means that it is an aggregate of
many simpler components. This class creates and manages the listeners
on the combo box and the combo box model. These listeners update the user
interface in response to changes in the properties and state of the combo box.

All event handling is handled by listener classes created with the

createxxxListener()

methods and internal classes.
You can change the behavior of this class by overriding the

createxxxListener()

methods and supplying your own
event listeners or subclassing from the ones supplied in this class.

For adding specific actions,
overide

installKeyboardActions

to add actions in response to
KeyStroke bindings. See the article

How to Use Key Bindings

The combo box is a compound component which means that it is an aggregate of
many simpler components. This class creates and manages the listeners
on the combo box and the combo box model. These listeners update the user
interface in response to changes in the properties and state of the combo box.

All event handling is handled by listener classes created with the

createxxxListener()

methods and internal classes.
You can change the behavior of this class by overriding the

createxxxListener()

methods and supplying your own
event listeners or subclassing from the ones supplied in this class.

For adding specific actions,
overide

installKeyboardActions

to add actions in response to
KeyStroke bindings. See the article

How to Use Key Bindings

All event handling is handled by listener classes created with the

createxxxListener()

methods and internal classes.
You can change the behavior of this class by overriding the

createxxxListener()

methods and supplying your own
event listeners or subclassing from the ones supplied in this class.

For adding specific actions,
overide

installKeyboardActions

to add actions in response to
KeyStroke bindings. See the article

How to Use Key Bindings

For adding specific actions,
overide

installKeyboardActions

to add actions in response to
KeyStroke bindings. See the article

How to Use Key Bindings

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

BasicComboBoxUI.ComboBoxLayoutManager

This layout manager handles the 'standard' layout of combo boxes.

class

BasicComboBoxUI.FocusHandler

This listener hides the popup when the focus is lost.

class

BasicComboBoxUI.ItemHandler

This listener watches for changes to the selection in the
combo box.

class

BasicComboBoxUI.KeyHandler

This listener checks to see if the key event isn't a navigation key.

class

BasicComboBoxUI.ListDataHandler

This listener watches for changes in the

ComboBoxModel

.

class

BasicComboBoxUI.PropertyChangeHandler

This listener watches for bound properties that have changed in the
combo box.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

JButton

arrowButton

The arrow button that invokes the popup.

protected

Dimension

cachedMinimumSize

The cached minimum preferred size.

protected

JComboBox

<

Object

>

comboBox

The instance of

JComboBox

.

protected

CellRendererPane

currentValuePane

Used to render the currently selected item in the combo box.

protected

Component

editor

The Component that the @{code ComboBoxEditor} uses for editing.

protected

FocusListener

focusListener

This protected field is implementation specific.

protected boolean

hasFocus

This protected field is implementation specific.

protected boolean

isMinimumSizeDirty

The flag for recalculating the minimum preferred size.

protected

ItemListener

itemListener

This protected field is implementation specific.

protected

KeyListener

keyListener

This protected field is implementation specific.

protected

JList

<

Object

>

listBox

This list is for drawing the current item in the combo box.

protected

ListDataListener

listDataListener

This protected field is implementation specific.

protected

Insets

padding

If specified, these insets act as padding around the cell renderer when
laying out and painting the "selected" item in the combo box.

protected

ComboPopup

popup

The implementation of

ComboPopup

that is used to show the popup.

protected

KeyListener

popupKeyListener

The

KeyListener

listens to events.

protected

MouseListener

popupMouseListener

The

MouseListener

listens to events.

protected

MouseMotionListener

popupMouseMotionListener

The

MouseMotionListener

listens to events.

protected

PropertyChangeListener

propertyChangeListener

This protected field is implementation specific.

protected boolean

squareButton

Indicates whether or not the combo box button should be square.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicComboBoxUI

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addEditor

()

This public method is implementation specific and should be private.

void

configureArrowButton

()

This public method is implementation specific and should be private.

protected void

configureEditor

()

This protected method is implementation specific and should be private.

protected

JButton

createArrowButton

()

Creates a button which will be used as the control to show or hide
the popup portion of the combo box.

protected

ComboBoxEditor

createEditor

()

Creates the default editor that will be used in editable combo boxes.

protected

FocusListener

createFocusListener

()

Creates a

FocusListener

which will be added to the combo box.

protected

ItemListener

createItemListener

()

Creates an

ItemListener

which will be added to the
combo box.

protected

KeyListener

createKeyListener

()

Creates a

KeyListener

which will be added to the
combo box.

protected

LayoutManager

createLayoutManager

()

Creates a layout manager for managing the components which make up the
combo box.

protected

ListDataListener

createListDataListener

()

Creates a list data listener which will be added to the

ComboBoxModel

.

protected

ComboPopup

createPopup

()

Creates the popup portion of the combo box.

protected

PropertyChangeListener

createPropertyChangeListener

()

Creates a

PropertyChangeListener

which will be added to
the combo box.

protected

ListCellRenderer

<

Object

>

createRenderer

()

Creates the default renderer that will be used in a non-editiable combo
box.

static

ComponentUI

createUI

​(

JComponent

c)

Constructs a new instance of

BasicComboBoxUI

.

int

getBaseline

​(

JComponent

c,
int width,
int height)

Returns the baseline.

Component.BaselineResizeBehavior

getBaselineResizeBehavior

​(

JComponent

c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

protected

Dimension

getDefaultSize

()

Return the default size of an empty display area of the combo box using
the current renderer and font.

protected

Dimension

getDisplaySize

()

Returns the calculated size of the display area.

protected

Insets

getInsets

()

Gets the insets from the JComboBox.

Dimension

getMinimumSize

​(

JComponent

c)

The minimum size is the size of the display area plus insets plus the button.

protected

Dimension

getSizeForComponent

​(

Component

comp)

Returns the size a component would have if used as a cell renderer.

protected void

installComponents

()

Creates and initializes the components which make up the
aggregate combo box.

protected void

installDefaults

()

Installs the default colors, default font, default renderer, and default
editor into the JComboBox.

protected void

installKeyboardActions

()

Adds keyboard actions to the JComboBox.

protected void

installListeners

()

Creates and installs listeners for the combo box and its model.

boolean

isFocusTraversable

​(

JComboBox

<?> c)

Determines if the JComboBox is focus traversable.

protected boolean

isNavigationKey

​(int keyCode)

Returns whether or not the supplied keyCode maps to a key that is used for
navigation.

boolean

isPopupVisible

​(

JComboBox

<?> c)

Tells if the popup is visible or not.

void

paintCurrentValue

​(

Graphics

g,

Rectangle

bounds,
boolean hasFocus)

Paints the currently selected item.

void

paintCurrentValueBackground

​(

Graphics

g,

Rectangle

bounds,
boolean hasFocus)

Paints the background of the currently selected item.

protected

Rectangle

rectangleForCurrentValue

()

Returns the area that is reserved for drawing the currently selected item.

void

removeEditor

()

This public method is implementation specific and should be private.

protected void

selectNextPossibleValue

()

Selects the next item in the list.

protected void

selectPreviousPossibleValue

()

Selects the previous item in the list.

void

setPopupVisible

​(

JComboBox

<?> c,
boolean v)

Hides the popup.

protected void

toggleOpenClose

()

Hides the popup if it is showing and shows the popup if it is hidden.

void

unconfigureArrowButton

()

This public method is implementation specific and should be private.

protected void

unconfigureEditor

()

This protected method is implementation specific and should be private.

protected void

uninstallComponents

()

The aggregate components which comprise the combo box are
unregistered and uninitialized.

protected void

uninstallDefaults

()

Uninstalls the default colors, default font, default renderer,
and default editor from the combo box.

protected void

uninstallKeyboardActions

()

Removes the focus InputMap and ActionMap.

protected void

uninstallListeners

()

Removes the installed listeners from the combo box and its model.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getMaximumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

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

toString

,

wait

,

wait

,

wait

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

BasicComboBoxUI.ComboBoxLayoutManager

This layout manager handles the 'standard' layout of combo boxes.

class

BasicComboBoxUI.FocusHandler

This listener hides the popup when the focus is lost.

class

BasicComboBoxUI.ItemHandler

This listener watches for changes to the selection in the
combo box.

class

BasicComboBoxUI.KeyHandler

This listener checks to see if the key event isn't a navigation key.

class

BasicComboBoxUI.ListDataHandler

This listener watches for changes in the

ComboBoxModel

.

class

BasicComboBoxUI.PropertyChangeHandler

This listener watches for bound properties that have changed in the
combo box.

---

#### Nested Class Summary

This layout manager handles the 'standard' layout of combo boxes.

This listener hides the popup when the focus is lost.

This listener watches for changes to the selection in the
combo box.

This listener checks to see if the key event isn't a navigation key.

This listener watches for changes in the

ComboBoxModel

.

This listener watches for bound properties that have changed in the
combo box.

Field Summary

Fields

Modifier and Type

Field

Description

protected

JButton

arrowButton

The arrow button that invokes the popup.

protected

Dimension

cachedMinimumSize

The cached minimum preferred size.

protected

JComboBox

<

Object

>

comboBox

The instance of

JComboBox

.

protected

CellRendererPane

currentValuePane

Used to render the currently selected item in the combo box.

protected

Component

editor

The Component that the @{code ComboBoxEditor} uses for editing.

protected

FocusListener

focusListener

This protected field is implementation specific.

protected boolean

hasFocus

This protected field is implementation specific.

protected boolean

isMinimumSizeDirty

The flag for recalculating the minimum preferred size.

protected

ItemListener

itemListener

This protected field is implementation specific.

protected

KeyListener

keyListener

This protected field is implementation specific.

protected

JList

<

Object

>

listBox

This list is for drawing the current item in the combo box.

protected

ListDataListener

listDataListener

This protected field is implementation specific.

protected

Insets

padding

If specified, these insets act as padding around the cell renderer when
laying out and painting the "selected" item in the combo box.

protected

ComboPopup

popup

The implementation of

ComboPopup

that is used to show the popup.

protected

KeyListener

popupKeyListener

The

KeyListener

listens to events.

protected

MouseListener

popupMouseListener

The

MouseListener

listens to events.

protected

MouseMotionListener

popupMouseMotionListener

The

MouseMotionListener

listens to events.

protected

PropertyChangeListener

propertyChangeListener

This protected field is implementation specific.

protected boolean

squareButton

Indicates whether or not the combo box button should be square.

---

#### Field Summary

The arrow button that invokes the popup.

The cached minimum preferred size.

The instance of

JComboBox

.

Used to render the currently selected item in the combo box.

The Component that the @{code ComboBoxEditor} uses for editing.

This protected field is implementation specific.

The flag for recalculating the minimum preferred size.

This list is for drawing the current item in the combo box.

If specified, these insets act as padding around the cell renderer when
laying out and painting the "selected" item in the combo box.

The implementation of

ComboPopup

that is used to show the popup.

The

KeyListener

listens to events.

The

MouseListener

listens to events.

The

MouseMotionListener

listens to events.

Indicates whether or not the combo box button should be square.

Constructor Summary

Constructors

Constructor

Description

BasicComboBoxUI

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addEditor

()

This public method is implementation specific and should be private.

void

configureArrowButton

()

This public method is implementation specific and should be private.

protected void

configureEditor

()

This protected method is implementation specific and should be private.

protected

JButton

createArrowButton

()

Creates a button which will be used as the control to show or hide
the popup portion of the combo box.

protected

ComboBoxEditor

createEditor

()

Creates the default editor that will be used in editable combo boxes.

protected

FocusListener

createFocusListener

()

Creates a

FocusListener

which will be added to the combo box.

protected

ItemListener

createItemListener

()

Creates an

ItemListener

which will be added to the
combo box.

protected

KeyListener

createKeyListener

()

Creates a

KeyListener

which will be added to the
combo box.

protected

LayoutManager

createLayoutManager

()

Creates a layout manager for managing the components which make up the
combo box.

protected

ListDataListener

createListDataListener

()

Creates a list data listener which will be added to the

ComboBoxModel

.

protected

ComboPopup

createPopup

()

Creates the popup portion of the combo box.

protected

PropertyChangeListener

createPropertyChangeListener

()

Creates a

PropertyChangeListener

which will be added to
the combo box.

protected

ListCellRenderer

<

Object

>

createRenderer

()

Creates the default renderer that will be used in a non-editiable combo
box.

static

ComponentUI

createUI

​(

JComponent

c)

Constructs a new instance of

BasicComboBoxUI

.

int

getBaseline

​(

JComponent

c,
int width,
int height)

Returns the baseline.

Component.BaselineResizeBehavior

getBaselineResizeBehavior

​(

JComponent

c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

protected

Dimension

getDefaultSize

()

Return the default size of an empty display area of the combo box using
the current renderer and font.

protected

Dimension

getDisplaySize

()

Returns the calculated size of the display area.

protected

Insets

getInsets

()

Gets the insets from the JComboBox.

Dimension

getMinimumSize

​(

JComponent

c)

The minimum size is the size of the display area plus insets plus the button.

protected

Dimension

getSizeForComponent

​(

Component

comp)

Returns the size a component would have if used as a cell renderer.

protected void

installComponents

()

Creates and initializes the components which make up the
aggregate combo box.

protected void

installDefaults

()

Installs the default colors, default font, default renderer, and default
editor into the JComboBox.

protected void

installKeyboardActions

()

Adds keyboard actions to the JComboBox.

protected void

installListeners

()

Creates and installs listeners for the combo box and its model.

boolean

isFocusTraversable

​(

JComboBox

<?> c)

Determines if the JComboBox is focus traversable.

protected boolean

isNavigationKey

​(int keyCode)

Returns whether or not the supplied keyCode maps to a key that is used for
navigation.

boolean

isPopupVisible

​(

JComboBox

<?> c)

Tells if the popup is visible or not.

void

paintCurrentValue

​(

Graphics

g,

Rectangle

bounds,
boolean hasFocus)

Paints the currently selected item.

void

paintCurrentValueBackground

​(

Graphics

g,

Rectangle

bounds,
boolean hasFocus)

Paints the background of the currently selected item.

protected

Rectangle

rectangleForCurrentValue

()

Returns the area that is reserved for drawing the currently selected item.

void

removeEditor

()

This public method is implementation specific and should be private.

protected void

selectNextPossibleValue

()

Selects the next item in the list.

protected void

selectPreviousPossibleValue

()

Selects the previous item in the list.

void

setPopupVisible

​(

JComboBox

<?> c,
boolean v)

Hides the popup.

protected void

toggleOpenClose

()

Hides the popup if it is showing and shows the popup if it is hidden.

void

unconfigureArrowButton

()

This public method is implementation specific and should be private.

protected void

unconfigureEditor

()

This protected method is implementation specific and should be private.

protected void

uninstallComponents

()

The aggregate components which comprise the combo box are
unregistered and uninitialized.

protected void

uninstallDefaults

()

Uninstalls the default colors, default font, default renderer,
and default editor from the combo box.

protected void

uninstallKeyboardActions

()

Removes the focus InputMap and ActionMap.

protected void

uninstallListeners

()

Removes the installed listeners from the combo box and its model.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getMaximumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

This public method is implementation specific and should be private.

This protected method is implementation specific and should be private.

Creates a button which will be used as the control to show or hide
the popup portion of the combo box.

Creates the default editor that will be used in editable combo boxes.

Creates a

FocusListener

which will be added to the combo box.

Creates an

ItemListener

which will be added to the
combo box.

Creates a

KeyListener

which will be added to the
combo box.

Creates a layout manager for managing the components which make up the
combo box.

Creates a list data listener which will be added to the

ComboBoxModel

.

Creates the popup portion of the combo box.

Creates a

PropertyChangeListener

which will be added to
the combo box.

Creates the default renderer that will be used in a non-editiable combo
box.

Constructs a new instance of

BasicComboBoxUI

.

Returns the baseline.

Returns an enum indicating how the baseline of the component
changes as the size changes.

Return the default size of an empty display area of the combo box using
the current renderer and font.

Returns the calculated size of the display area.

Gets the insets from the JComboBox.

The minimum size is the size of the display area plus insets plus the button.

Returns the size a component would have if used as a cell renderer.

Creates and initializes the components which make up the
aggregate combo box.

Installs the default colors, default font, default renderer, and default
editor into the JComboBox.

Adds keyboard actions to the JComboBox.

Creates and installs listeners for the combo box and its model.

Determines if the JComboBox is focus traversable.

Returns whether or not the supplied keyCode maps to a key that is used for
navigation.

Tells if the popup is visible or not.

Paints the currently selected item.

Paints the background of the currently selected item.

Returns the area that is reserved for drawing the currently selected item.

Selects the next item in the list.

Selects the previous item in the list.

Hides the popup.

Hides the popup if it is showing and shows the popup if it is hidden.

The aggregate components which comprise the combo box are
unregistered and uninitialized.

Uninstalls the default colors, default font, default renderer,
and default editor from the combo box.

Removes the focus InputMap and ActionMap.

Removes the installed listeners from the combo box and its model.

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getMaximumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

---

#### Methods declared in class javax.swing.plaf. ComponentUI

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

toString

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

- comboBox

```java
protected
JComboBox
<
Object
> comboBox
```

The instance of

JComboBox

.

- hasFocus

```java
protected boolean hasFocus
```

This protected field is implementation specific. Do not access directly
or override.

- listBox

```java
protected
JList
<
Object
> listBox
```

This list is for drawing the current item in the combo box.

- currentValuePane

```java
protected
CellRendererPane
currentValuePane
```

Used to render the currently selected item in the combo box.
It doesn't have anything to do with the popup's rendering.

- popup

```java
protected
ComboPopup
popup
```

The implementation of

ComboPopup

that is used to show the popup.

- editor

```java
protected
Component
editor
```

The Component that the @{code ComboBoxEditor} uses for editing.

- arrowButton

```java
protected
JButton
arrowButton
```

The arrow button that invokes the popup.

- keyListener

```java
protected
KeyListener
keyListener
```

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

**See Also:** createKeyListener()

- focusListener

```java
protected
FocusListener
focusListener
```

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

**See Also:** createFocusListener()

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

**See Also:** createPropertyChangeListener()

- itemListener

```java
protected
ItemListener
itemListener
```

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

**See Also:** createItemListener()

- popupMouseListener

```java
protected
MouseListener
popupMouseListener
```

The

MouseListener

listens to events.

- popupMouseMotionListener

```java
protected
MouseMotionListener
popupMouseMotionListener
```

The

MouseMotionListener

listens to events.

- popupKeyListener

```java
protected
KeyListener
popupKeyListener
```

The

KeyListener

listens to events.

- listDataListener

```java
protected
ListDataListener
listDataListener
```

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

**See Also:** createListDataListener()

- isMinimumSizeDirty

```java
protected boolean isMinimumSizeDirty
```

The flag for recalculating the minimum preferred size.

- cachedMinimumSize

```java
protected
Dimension
cachedMinimumSize
```

The cached minimum preferred size.

- squareButton

```java
protected boolean squareButton
```

Indicates whether or not the combo box button should be square.
If square, then the width and height are equal, and are both set to
the height of the combo minus appropriate insets.

**Since:** 1.7

- padding

```java
protected
Insets
padding
```

If specified, these insets act as padding around the cell renderer when
laying out and painting the "selected" item in the combo box. These
insets add to those specified by the cell renderer.

**Since:** 1.7

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicComboBoxUI

```java
public BasicComboBoxUI()
```

============ METHOD DETAIL ==========

- Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Constructs a new instance of

BasicComboBoxUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicComboBoxUI

- installDefaults

```java
protected void installDefaults()
```

Installs the default colors, default font, default renderer, and default
editor into the JComboBox.

- installListeners

```java
protected void installListeners()
```

Creates and installs listeners for the combo box and its model.
This method is called when the UI is installed.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls the default colors, default font, default renderer,
and default editor from the combo box.

- uninstallListeners

```java
protected void uninstallListeners()
```

Removes the installed listeners from the combo box and its model.
The number and types of listeners removed and in this method should be
the same that was added in

installListeners

- createPopup

```java
protected
ComboPopup
createPopup()
```

Creates the popup portion of the combo box.

**Returns:** an instance of

ComboPopup
**See Also:** ComboPopup

- createKeyListener

```java
protected
KeyListener
createKeyListener()
```

Creates a

KeyListener

which will be added to the
combo box. If this method returns null then it will not be added
to the combo box.

**Returns:** an instance

KeyListener

or null

- createFocusListener

```java
protected
FocusListener
createFocusListener()
```

Creates a

FocusListener

which will be added to the combo box.
If this method returns null then it will not be added to the combo box.

**Returns:** an instance of a

FocusListener

or null

- createListDataListener

```java
protected
ListDataListener
createListDataListener()
```

Creates a list data listener which will be added to the

ComboBoxModel

. If this method returns null then
it will not be added to the combo box model.

**Returns:** an instance of a

ListDataListener

or null

- createItemListener

```java
protected
ItemListener
createItemListener()
```

Creates an

ItemListener

which will be added to the
combo box. If this method returns null then it will not
be added to the combo box.

Subclasses may override this method to return instances of their own
ItemEvent handlers.

**Returns:** an instance of an

ItemListener

or null

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates a

PropertyChangeListener

which will be added to
the combo box. If this method returns null then it will not
be added to the combo box.

**Returns:** an instance of a

PropertyChangeListener

or null

- createLayoutManager

```java
protected
LayoutManager
createLayoutManager()
```

Creates a layout manager for managing the components which make up the
combo box.

**Returns:** an instance of a layout manager

- createRenderer

```java
protected
ListCellRenderer
<
Object
> createRenderer()
```

Creates the default renderer that will be used in a non-editiable combo
box. A default renderer will used only if a renderer has not been
explicitly set with

setRenderer

.

**Returns:** a

ListCellRender

used for the combo box
**See Also:** JComboBox.setRenderer(javax.swing.ListCellRenderer<? super E>)

- createEditor

```java
protected
ComboBoxEditor
createEditor()
```

Creates the default editor that will be used in editable combo boxes.
A default editor will be used only if an editor has not been
explicitly set with

setEditor

.

**Returns:** a

ComboBoxEditor

used for the combo box
**See Also:** JComboBox.setEditor(javax.swing.ComboBoxEditor)

- installComponents

```java
protected void installComponents()
```

Creates and initializes the components which make up the
aggregate combo box. This method is called as part of the UI
installation process.

- uninstallComponents

```java
protected void uninstallComponents()
```

The aggregate components which comprise the combo box are
unregistered and uninitialized. This method is called as part of the
UI uninstallation process.

- addEditor

```java
public void addEditor()
```

This public method is implementation specific and should be private.
do not call or override. To implement a specific editor create a
custom

ComboBoxEditor

**See Also:** createEditor()

,

JComboBox.setEditor(javax.swing.ComboBoxEditor)

,

ComboBoxEditor

- removeEditor

```java
public void removeEditor()
```

This public method is implementation specific and should be private.
do not call or override.

**See Also:** addEditor()

- configureEditor

```java
protected void configureEditor()
```

This protected method is implementation specific and should be private.
do not call or override.

**See Also:** addEditor()

- unconfigureEditor

```java
protected void unconfigureEditor()
```

This protected method is implementation specific and should be private.
Do not call or override.

**See Also:** addEditor()

- configureArrowButton

```java
public void configureArrowButton()
```

This public method is implementation specific and should be private. Do
not call or override.

**See Also:** createArrowButton()

- unconfigureArrowButton

```java
public void unconfigureArrowButton()
```

This public method is implementation specific and should be private. Do
not call or override.

**See Also:** createArrowButton()

- createArrowButton

```java
protected
JButton
createArrowButton()
```

Creates a button which will be used as the control to show or hide
the popup portion of the combo box.

**Returns:** a button which represents the popup control

- isPopupVisible

```java
public boolean isPopupVisible​(
JComboBox
<?> c)
```

Tells if the popup is visible or not.

**Specified by:** isPopupVisible

in class

ComboBoxUI
**Parameters:** c

- a

JComboBox
**Returns:** true if popup of the

JComboBox

is visible

- setPopupVisible

```java
public void setPopupVisible​(
JComboBox
<?> c,
boolean v)
```

Hides the popup.

**Specified by:** setPopupVisible

in class

ComboBoxUI
**Parameters:** c

- a

JComboBox
**Parameters:** v

- a

boolean

determining the visibilty of the popup

- isFocusTraversable

```java
public boolean isFocusTraversable​(
JComboBox
<?> c)
```

Determines if the JComboBox is focus traversable. If the JComboBox is editable
this returns false, otherwise it returns true.

**Specified by:** isFocusTraversable

in class

ComboBoxUI
**Parameters:** c

- a

JComboBox
**Returns:** true if the given

JComboBox

is traversable

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

The minimum size is the size of the display area plus insets plus the button.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** c

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

- getBaseline

```java
public int getBaseline​(
JComponent
c,
int width,
int height)
```

Returns the baseline.

**Overrides:** getBaseline

in class

ComponentUI
**Parameters:** c

-

JComponent

baseline is being requested for
**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** baseline or a value < 0 indicating there is no reasonable
baseline
**Throws:** NullPointerException

- if

c

is

null
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

- getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)
```

Returns an enum indicating how the baseline of the component
changes as the size changes.

**Overrides:** getBaselineResizeBehavior

in class

ComponentUI
**Parameters:** c

-

JComponent

to return baseline resize behavior for
**Returns:** an enum indicating how the baseline changes as the component
size changes
**Throws:** NullPointerException

- if

c

is

null
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

- isNavigationKey

```java
protected boolean isNavigationKey​(int keyCode)
```

Returns whether or not the supplied keyCode maps to a key that is used for
navigation. This is used for optimizing key input by only passing non-
navigation keys to the type-ahead mechanism. Subclasses should override this
if they change the navigation keys.

**Parameters:** keyCode

- a key code
**Returns:** true

if the supplied

keyCode

maps to a navigation key

- selectNextPossibleValue

```java
protected void selectNextPossibleValue()
```

Selects the next item in the list. It won't change the selection if the
currently selected item is already the last item.

- selectPreviousPossibleValue

```java
protected void selectPreviousPossibleValue()
```

Selects the previous item in the list. It won't change the selection if the
currently selected item is already the first item.

- toggleOpenClose

```java
protected void toggleOpenClose()
```

Hides the popup if it is showing and shows the popup if it is hidden.

- rectangleForCurrentValue

```java
protected
Rectangle
rectangleForCurrentValue()
```

Returns the area that is reserved for drawing the currently selected item.

**Returns:** the area that is reserved for drawing the currently selected item

- getInsets

```java
protected
Insets
getInsets()
```

Gets the insets from the JComboBox.

**Returns:** the insets

- paintCurrentValue

```java
public void paintCurrentValue​(
Graphics
g,

Rectangle
bounds,
boolean hasFocus)
```

Paints the currently selected item.

**Parameters:** g

- an instance of

Graphics
**Parameters:** bounds

- a bounding rectangle to render to
**Parameters:** hasFocus

- is focused

- paintCurrentValueBackground

```java
public void paintCurrentValueBackground​(
Graphics
g,

Rectangle
bounds,
boolean hasFocus)
```

Paints the background of the currently selected item.

**Parameters:** g

- an instance of

Graphics
**Parameters:** bounds

- a bounding rectangle to render to
**Parameters:** hasFocus

- is focused

- getDefaultSize

```java
protected
Dimension
getDefaultSize()
```

Return the default size of an empty display area of the combo box using
the current renderer and font.

**Returns:** the size of an empty display area
**See Also:** getDisplaySize()

- getDisplaySize

```java
protected
Dimension
getDisplaySize()
```

Returns the calculated size of the display area. The display area is the
portion of the combo box in which the selected item is displayed. This
method will use the prototype display value if it has been set.

For combo boxes with a non trivial number of items, it is recommended to
use a prototype display value to significantly speed up the display
size calculation.

**Returns:** the size of the display area calculated from the combo box items
**See Also:** JComboBox.setPrototypeDisplayValue(E)

- getSizeForComponent

```java
protected
Dimension
getSizeForComponent​(
Component
comp)
```

Returns the size a component would have if used as a cell renderer.

**Parameters:** comp

- a

Component

to check
**Returns:** size of the component
**Since:** 1.7

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Adds keyboard actions to the JComboBox. Actions on enter and esc are already
supplied. Add more actions as you need them.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Removes the focus InputMap and ActionMap.

Field Detail

- comboBox

```java
protected
JComboBox
<
Object
> comboBox
```

The instance of

JComboBox

.

- hasFocus

```java
protected boolean hasFocus
```

This protected field is implementation specific. Do not access directly
or override.

- listBox

```java
protected
JList
<
Object
> listBox
```

This list is for drawing the current item in the combo box.

- currentValuePane

```java
protected
CellRendererPane
currentValuePane
```

Used to render the currently selected item in the combo box.
It doesn't have anything to do with the popup's rendering.

- popup

```java
protected
ComboPopup
popup
```

The implementation of

ComboPopup

that is used to show the popup.

- editor

```java
protected
Component
editor
```

The Component that the @{code ComboBoxEditor} uses for editing.

- arrowButton

```java
protected
JButton
arrowButton
```

The arrow button that invokes the popup.

- keyListener

```java
protected
KeyListener
keyListener
```

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

**See Also:** createKeyListener()

- focusListener

```java
protected
FocusListener
focusListener
```

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

**See Also:** createFocusListener()

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

**See Also:** createPropertyChangeListener()

- itemListener

```java
protected
ItemListener
itemListener
```

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

**See Also:** createItemListener()

- popupMouseListener

```java
protected
MouseListener
popupMouseListener
```

The

MouseListener

listens to events.

- popupMouseMotionListener

```java
protected
MouseMotionListener
popupMouseMotionListener
```

The

MouseMotionListener

listens to events.

- popupKeyListener

```java
protected
KeyListener
popupKeyListener
```

The

KeyListener

listens to events.

- listDataListener

```java
protected
ListDataListener
listDataListener
```

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

**See Also:** createListDataListener()

- isMinimumSizeDirty

```java
protected boolean isMinimumSizeDirty
```

The flag for recalculating the minimum preferred size.

- cachedMinimumSize

```java
protected
Dimension
cachedMinimumSize
```

The cached minimum preferred size.

- squareButton

```java
protected boolean squareButton
```

Indicates whether or not the combo box button should be square.
If square, then the width and height are equal, and are both set to
the height of the combo minus appropriate insets.

**Since:** 1.7

- padding

```java
protected
Insets
padding
```

If specified, these insets act as padding around the cell renderer when
laying out and painting the "selected" item in the combo box. These
insets add to those specified by the cell renderer.

**Since:** 1.7

---

#### Field Detail

comboBox

```java
protected
JComboBox
<
Object
> comboBox
```

The instance of

JComboBox

.

---

#### comboBox

protected

JComboBox

<

Object

> comboBox

The instance of

JComboBox

.

hasFocus

```java
protected boolean hasFocus
```

This protected field is implementation specific. Do not access directly
or override.

---

#### hasFocus

protected boolean hasFocus

This protected field is implementation specific. Do not access directly
or override.

listBox

```java
protected
JList
<
Object
> listBox
```

This list is for drawing the current item in the combo box.

---

#### listBox

protected

JList

<

Object

> listBox

This list is for drawing the current item in the combo box.

currentValuePane

```java
protected
CellRendererPane
currentValuePane
```

Used to render the currently selected item in the combo box.
It doesn't have anything to do with the popup's rendering.

---

#### currentValuePane

protected

CellRendererPane

currentValuePane

Used to render the currently selected item in the combo box.
It doesn't have anything to do with the popup's rendering.

popup

```java
protected
ComboPopup
popup
```

The implementation of

ComboPopup

that is used to show the popup.

---

#### popup

protected

ComboPopup

popup

The implementation of

ComboPopup

that is used to show the popup.

editor

```java
protected
Component
editor
```

The Component that the @{code ComboBoxEditor} uses for editing.

---

#### editor

protected

Component

editor

The Component that the @{code ComboBoxEditor} uses for editing.

arrowButton

```java
protected
JButton
arrowButton
```

The arrow button that invokes the popup.

---

#### arrowButton

protected

JButton

arrowButton

The arrow button that invokes the popup.

keyListener

```java
protected
KeyListener
keyListener
```

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

**See Also:** createKeyListener()

---

#### keyListener

protected

KeyListener

keyListener

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

focusListener

```java
protected
FocusListener
focusListener
```

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

**See Also:** createFocusListener()

---

#### focusListener

protected

FocusListener

focusListener

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

**See Also:** createPropertyChangeListener()

---

#### propertyChangeListener

protected

PropertyChangeListener

propertyChangeListener

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

itemListener

```java
protected
ItemListener
itemListener
```

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

**See Also:** createItemListener()

---

#### itemListener

protected

ItemListener

itemListener

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

popupMouseListener

```java
protected
MouseListener
popupMouseListener
```

The

MouseListener

listens to events.

---

#### popupMouseListener

protected

MouseListener

popupMouseListener

The

MouseListener

listens to events.

popupMouseMotionListener

```java
protected
MouseMotionListener
popupMouseMotionListener
```

The

MouseMotionListener

listens to events.

---

#### popupMouseMotionListener

protected

MouseMotionListener

popupMouseMotionListener

The

MouseMotionListener

listens to events.

popupKeyListener

```java
protected
KeyListener
popupKeyListener
```

The

KeyListener

listens to events.

---

#### popupKeyListener

protected

KeyListener

popupKeyListener

The

KeyListener

listens to events.

listDataListener

```java
protected
ListDataListener
listDataListener
```

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

**See Also:** createListDataListener()

---

#### listDataListener

protected

ListDataListener

listDataListener

This protected field is implementation specific. Do not access directly
or override. Override the listener construction method instead.

isMinimumSizeDirty

```java
protected boolean isMinimumSizeDirty
```

The flag for recalculating the minimum preferred size.

---

#### isMinimumSizeDirty

protected boolean isMinimumSizeDirty

The flag for recalculating the minimum preferred size.

cachedMinimumSize

```java
protected
Dimension
cachedMinimumSize
```

The cached minimum preferred size.

---

#### cachedMinimumSize

protected

Dimension

cachedMinimumSize

The cached minimum preferred size.

squareButton

```java
protected boolean squareButton
```

Indicates whether or not the combo box button should be square.
If square, then the width and height are equal, and are both set to
the height of the combo minus appropriate insets.

**Since:** 1.7

---

#### squareButton

protected boolean squareButton

Indicates whether or not the combo box button should be square.
If square, then the width and height are equal, and are both set to
the height of the combo minus appropriate insets.

padding

```java
protected
Insets
padding
```

If specified, these insets act as padding around the cell renderer when
laying out and painting the "selected" item in the combo box. These
insets add to those specified by the cell renderer.

**Since:** 1.7

---

#### padding

protected

Insets

padding

If specified, these insets act as padding around the cell renderer when
laying out and painting the "selected" item in the combo box. These
insets add to those specified by the cell renderer.

Constructor Detail

- BasicComboBoxUI

```java
public BasicComboBoxUI()
```

---

#### Constructor Detail

BasicComboBoxUI

```java
public BasicComboBoxUI()
```

---

#### BasicComboBoxUI

public BasicComboBoxUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Constructs a new instance of

BasicComboBoxUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicComboBoxUI

- installDefaults

```java
protected void installDefaults()
```

Installs the default colors, default font, default renderer, and default
editor into the JComboBox.

- installListeners

```java
protected void installListeners()
```

Creates and installs listeners for the combo box and its model.
This method is called when the UI is installed.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls the default colors, default font, default renderer,
and default editor from the combo box.

- uninstallListeners

```java
protected void uninstallListeners()
```

Removes the installed listeners from the combo box and its model.
The number and types of listeners removed and in this method should be
the same that was added in

installListeners

- createPopup

```java
protected
ComboPopup
createPopup()
```

Creates the popup portion of the combo box.

**Returns:** an instance of

ComboPopup
**See Also:** ComboPopup

- createKeyListener

```java
protected
KeyListener
createKeyListener()
```

Creates a

KeyListener

which will be added to the
combo box. If this method returns null then it will not be added
to the combo box.

**Returns:** an instance

KeyListener

or null

- createFocusListener

```java
protected
FocusListener
createFocusListener()
```

Creates a

FocusListener

which will be added to the combo box.
If this method returns null then it will not be added to the combo box.

**Returns:** an instance of a

FocusListener

or null

- createListDataListener

```java
protected
ListDataListener
createListDataListener()
```

Creates a list data listener which will be added to the

ComboBoxModel

. If this method returns null then
it will not be added to the combo box model.

**Returns:** an instance of a

ListDataListener

or null

- createItemListener

```java
protected
ItemListener
createItemListener()
```

Creates an

ItemListener

which will be added to the
combo box. If this method returns null then it will not
be added to the combo box.

Subclasses may override this method to return instances of their own
ItemEvent handlers.

**Returns:** an instance of an

ItemListener

or null

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates a

PropertyChangeListener

which will be added to
the combo box. If this method returns null then it will not
be added to the combo box.

**Returns:** an instance of a

PropertyChangeListener

or null

- createLayoutManager

```java
protected
LayoutManager
createLayoutManager()
```

Creates a layout manager for managing the components which make up the
combo box.

**Returns:** an instance of a layout manager

- createRenderer

```java
protected
ListCellRenderer
<
Object
> createRenderer()
```

Creates the default renderer that will be used in a non-editiable combo
box. A default renderer will used only if a renderer has not been
explicitly set with

setRenderer

.

**Returns:** a

ListCellRender

used for the combo box
**See Also:** JComboBox.setRenderer(javax.swing.ListCellRenderer<? super E>)

- createEditor

```java
protected
ComboBoxEditor
createEditor()
```

Creates the default editor that will be used in editable combo boxes.
A default editor will be used only if an editor has not been
explicitly set with

setEditor

.

**Returns:** a

ComboBoxEditor

used for the combo box
**See Also:** JComboBox.setEditor(javax.swing.ComboBoxEditor)

- installComponents

```java
protected void installComponents()
```

Creates and initializes the components which make up the
aggregate combo box. This method is called as part of the UI
installation process.

- uninstallComponents

```java
protected void uninstallComponents()
```

The aggregate components which comprise the combo box are
unregistered and uninitialized. This method is called as part of the
UI uninstallation process.

- addEditor

```java
public void addEditor()
```

This public method is implementation specific and should be private.
do not call or override. To implement a specific editor create a
custom

ComboBoxEditor

**See Also:** createEditor()

,

JComboBox.setEditor(javax.swing.ComboBoxEditor)

,

ComboBoxEditor

- removeEditor

```java
public void removeEditor()
```

This public method is implementation specific and should be private.
do not call or override.

**See Also:** addEditor()

- configureEditor

```java
protected void configureEditor()
```

This protected method is implementation specific and should be private.
do not call or override.

**See Also:** addEditor()

- unconfigureEditor

```java
protected void unconfigureEditor()
```

This protected method is implementation specific and should be private.
Do not call or override.

**See Also:** addEditor()

- configureArrowButton

```java
public void configureArrowButton()
```

This public method is implementation specific and should be private. Do
not call or override.

**See Also:** createArrowButton()

- unconfigureArrowButton

```java
public void unconfigureArrowButton()
```

This public method is implementation specific and should be private. Do
not call or override.

**See Also:** createArrowButton()

- createArrowButton

```java
protected
JButton
createArrowButton()
```

Creates a button which will be used as the control to show or hide
the popup portion of the combo box.

**Returns:** a button which represents the popup control

- isPopupVisible

```java
public boolean isPopupVisible​(
JComboBox
<?> c)
```

Tells if the popup is visible or not.

**Specified by:** isPopupVisible

in class

ComboBoxUI
**Parameters:** c

- a

JComboBox
**Returns:** true if popup of the

JComboBox

is visible

- setPopupVisible

```java
public void setPopupVisible​(
JComboBox
<?> c,
boolean v)
```

Hides the popup.

**Specified by:** setPopupVisible

in class

ComboBoxUI
**Parameters:** c

- a

JComboBox
**Parameters:** v

- a

boolean

determining the visibilty of the popup

- isFocusTraversable

```java
public boolean isFocusTraversable​(
JComboBox
<?> c)
```

Determines if the JComboBox is focus traversable. If the JComboBox is editable
this returns false, otherwise it returns true.

**Specified by:** isFocusTraversable

in class

ComboBoxUI
**Parameters:** c

- a

JComboBox
**Returns:** true if the given

JComboBox

is traversable

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

The minimum size is the size of the display area plus insets plus the button.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** c

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

- getBaseline

```java
public int getBaseline​(
JComponent
c,
int width,
int height)
```

Returns the baseline.

**Overrides:** getBaseline

in class

ComponentUI
**Parameters:** c

-

JComponent

baseline is being requested for
**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** baseline or a value < 0 indicating there is no reasonable
baseline
**Throws:** NullPointerException

- if

c

is

null
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

- getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)
```

Returns an enum indicating how the baseline of the component
changes as the size changes.

**Overrides:** getBaselineResizeBehavior

in class

ComponentUI
**Parameters:** c

-

JComponent

to return baseline resize behavior for
**Returns:** an enum indicating how the baseline changes as the component
size changes
**Throws:** NullPointerException

- if

c

is

null
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

- isNavigationKey

```java
protected boolean isNavigationKey​(int keyCode)
```

Returns whether or not the supplied keyCode maps to a key that is used for
navigation. This is used for optimizing key input by only passing non-
navigation keys to the type-ahead mechanism. Subclasses should override this
if they change the navigation keys.

**Parameters:** keyCode

- a key code
**Returns:** true

if the supplied

keyCode

maps to a navigation key

- selectNextPossibleValue

```java
protected void selectNextPossibleValue()
```

Selects the next item in the list. It won't change the selection if the
currently selected item is already the last item.

- selectPreviousPossibleValue

```java
protected void selectPreviousPossibleValue()
```

Selects the previous item in the list. It won't change the selection if the
currently selected item is already the first item.

- toggleOpenClose

```java
protected void toggleOpenClose()
```

Hides the popup if it is showing and shows the popup if it is hidden.

- rectangleForCurrentValue

```java
protected
Rectangle
rectangleForCurrentValue()
```

Returns the area that is reserved for drawing the currently selected item.

**Returns:** the area that is reserved for drawing the currently selected item

- getInsets

```java
protected
Insets
getInsets()
```

Gets the insets from the JComboBox.

**Returns:** the insets

- paintCurrentValue

```java
public void paintCurrentValue​(
Graphics
g,

Rectangle
bounds,
boolean hasFocus)
```

Paints the currently selected item.

**Parameters:** g

- an instance of

Graphics
**Parameters:** bounds

- a bounding rectangle to render to
**Parameters:** hasFocus

- is focused

- paintCurrentValueBackground

```java
public void paintCurrentValueBackground​(
Graphics
g,

Rectangle
bounds,
boolean hasFocus)
```

Paints the background of the currently selected item.

**Parameters:** g

- an instance of

Graphics
**Parameters:** bounds

- a bounding rectangle to render to
**Parameters:** hasFocus

- is focused

- getDefaultSize

```java
protected
Dimension
getDefaultSize()
```

Return the default size of an empty display area of the combo box using
the current renderer and font.

**Returns:** the size of an empty display area
**See Also:** getDisplaySize()

- getDisplaySize

```java
protected
Dimension
getDisplaySize()
```

Returns the calculated size of the display area. The display area is the
portion of the combo box in which the selected item is displayed. This
method will use the prototype display value if it has been set.

For combo boxes with a non trivial number of items, it is recommended to
use a prototype display value to significantly speed up the display
size calculation.

**Returns:** the size of the display area calculated from the combo box items
**See Also:** JComboBox.setPrototypeDisplayValue(E)

- getSizeForComponent

```java
protected
Dimension
getSizeForComponent​(
Component
comp)
```

Returns the size a component would have if used as a cell renderer.

**Parameters:** comp

- a

Component

to check
**Returns:** size of the component
**Since:** 1.7

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Adds keyboard actions to the JComboBox. Actions on enter and esc are already
supplied. Add more actions as you need them.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Removes the focus InputMap and ActionMap.

---

#### Method Detail

createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Constructs a new instance of

BasicComboBoxUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicComboBoxUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Constructs a new instance of

BasicComboBoxUI

.

installDefaults

```java
protected void installDefaults()
```

Installs the default colors, default font, default renderer, and default
editor into the JComboBox.

---

#### installDefaults

protected void installDefaults()

Installs the default colors, default font, default renderer, and default
editor into the JComboBox.

installListeners

```java
protected void installListeners()
```

Creates and installs listeners for the combo box and its model.
This method is called when the UI is installed.

---

#### installListeners

protected void installListeners()

Creates and installs listeners for the combo box and its model.
This method is called when the UI is installed.

uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls the default colors, default font, default renderer,
and default editor from the combo box.

---

#### uninstallDefaults

protected void uninstallDefaults()

Uninstalls the default colors, default font, default renderer,
and default editor from the combo box.

uninstallListeners

```java
protected void uninstallListeners()
```

Removes the installed listeners from the combo box and its model.
The number and types of listeners removed and in this method should be
the same that was added in

installListeners

---

#### uninstallListeners

protected void uninstallListeners()

Removes the installed listeners from the combo box and its model.
The number and types of listeners removed and in this method should be
the same that was added in

installListeners

createPopup

```java
protected
ComboPopup
createPopup()
```

Creates the popup portion of the combo box.

**Returns:** an instance of

ComboPopup
**See Also:** ComboPopup

---

#### createPopup

protected

ComboPopup

createPopup()

Creates the popup portion of the combo box.

createKeyListener

```java
protected
KeyListener
createKeyListener()
```

Creates a

KeyListener

which will be added to the
combo box. If this method returns null then it will not be added
to the combo box.

**Returns:** an instance

KeyListener

or null

---

#### createKeyListener

protected

KeyListener

createKeyListener()

Creates a

KeyListener

which will be added to the
combo box. If this method returns null then it will not be added
to the combo box.

createFocusListener

```java
protected
FocusListener
createFocusListener()
```

Creates a

FocusListener

which will be added to the combo box.
If this method returns null then it will not be added to the combo box.

**Returns:** an instance of a

FocusListener

or null

---

#### createFocusListener

protected

FocusListener

createFocusListener()

Creates a

FocusListener

which will be added to the combo box.
If this method returns null then it will not be added to the combo box.

createListDataListener

```java
protected
ListDataListener
createListDataListener()
```

Creates a list data listener which will be added to the

ComboBoxModel

. If this method returns null then
it will not be added to the combo box model.

**Returns:** an instance of a

ListDataListener

or null

---

#### createListDataListener

protected

ListDataListener

createListDataListener()

Creates a list data listener which will be added to the

ComboBoxModel

. If this method returns null then
it will not be added to the combo box model.

createItemListener

```java
protected
ItemListener
createItemListener()
```

Creates an

ItemListener

which will be added to the
combo box. If this method returns null then it will not
be added to the combo box.

Subclasses may override this method to return instances of their own
ItemEvent handlers.

**Returns:** an instance of an

ItemListener

or null

---

#### createItemListener

protected

ItemListener

createItemListener()

Creates an

ItemListener

which will be added to the
combo box. If this method returns null then it will not
be added to the combo box.

Subclasses may override this method to return instances of their own
ItemEvent handlers.

Subclasses may override this method to return instances of their own
ItemEvent handlers.

createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates a

PropertyChangeListener

which will be added to
the combo box. If this method returns null then it will not
be added to the combo box.

**Returns:** an instance of a

PropertyChangeListener

or null

---

#### createPropertyChangeListener

protected

PropertyChangeListener

createPropertyChangeListener()

Creates a

PropertyChangeListener

which will be added to
the combo box. If this method returns null then it will not
be added to the combo box.

createLayoutManager

```java
protected
LayoutManager
createLayoutManager()
```

Creates a layout manager for managing the components which make up the
combo box.

**Returns:** an instance of a layout manager

---

#### createLayoutManager

protected

LayoutManager

createLayoutManager()

Creates a layout manager for managing the components which make up the
combo box.

createRenderer

```java
protected
ListCellRenderer
<
Object
> createRenderer()
```

Creates the default renderer that will be used in a non-editiable combo
box. A default renderer will used only if a renderer has not been
explicitly set with

setRenderer

.

**Returns:** a

ListCellRender

used for the combo box
**See Also:** JComboBox.setRenderer(javax.swing.ListCellRenderer<? super E>)

---

#### createRenderer

protected

ListCellRenderer

<

Object

> createRenderer()

Creates the default renderer that will be used in a non-editiable combo
box. A default renderer will used only if a renderer has not been
explicitly set with

setRenderer

.

createEditor

```java
protected
ComboBoxEditor
createEditor()
```

Creates the default editor that will be used in editable combo boxes.
A default editor will be used only if an editor has not been
explicitly set with

setEditor

.

**Returns:** a

ComboBoxEditor

used for the combo box
**See Also:** JComboBox.setEditor(javax.swing.ComboBoxEditor)

---

#### createEditor

protected

ComboBoxEditor

createEditor()

Creates the default editor that will be used in editable combo boxes.
A default editor will be used only if an editor has not been
explicitly set with

setEditor

.

installComponents

```java
protected void installComponents()
```

Creates and initializes the components which make up the
aggregate combo box. This method is called as part of the UI
installation process.

---

#### installComponents

protected void installComponents()

Creates and initializes the components which make up the
aggregate combo box. This method is called as part of the UI
installation process.

uninstallComponents

```java
protected void uninstallComponents()
```

The aggregate components which comprise the combo box are
unregistered and uninitialized. This method is called as part of the
UI uninstallation process.

---

#### uninstallComponents

protected void uninstallComponents()

The aggregate components which comprise the combo box are
unregistered and uninitialized. This method is called as part of the
UI uninstallation process.

addEditor

```java
public void addEditor()
```

This public method is implementation specific and should be private.
do not call or override. To implement a specific editor create a
custom

ComboBoxEditor

**See Also:** createEditor()

,

JComboBox.setEditor(javax.swing.ComboBoxEditor)

,

ComboBoxEditor

---

#### addEditor

public void addEditor()

This public method is implementation specific and should be private.
do not call or override. To implement a specific editor create a
custom

ComboBoxEditor

removeEditor

```java
public void removeEditor()
```

This public method is implementation specific and should be private.
do not call or override.

**See Also:** addEditor()

---

#### removeEditor

public void removeEditor()

This public method is implementation specific and should be private.
do not call or override.

configureEditor

```java
protected void configureEditor()
```

This protected method is implementation specific and should be private.
do not call or override.

**See Also:** addEditor()

---

#### configureEditor

protected void configureEditor()

This protected method is implementation specific and should be private.
do not call or override.

unconfigureEditor

```java
protected void unconfigureEditor()
```

This protected method is implementation specific and should be private.
Do not call or override.

**See Also:** addEditor()

---

#### unconfigureEditor

protected void unconfigureEditor()

This protected method is implementation specific and should be private.
Do not call or override.

configureArrowButton

```java
public void configureArrowButton()
```

This public method is implementation specific and should be private. Do
not call or override.

**See Also:** createArrowButton()

---

#### configureArrowButton

public void configureArrowButton()

This public method is implementation specific and should be private. Do
not call or override.

unconfigureArrowButton

```java
public void unconfigureArrowButton()
```

This public method is implementation specific and should be private. Do
not call or override.

**See Also:** createArrowButton()

---

#### unconfigureArrowButton

public void unconfigureArrowButton()

This public method is implementation specific and should be private. Do
not call or override.

createArrowButton

```java
protected
JButton
createArrowButton()
```

Creates a button which will be used as the control to show or hide
the popup portion of the combo box.

**Returns:** a button which represents the popup control

---

#### createArrowButton

protected

JButton

createArrowButton()

Creates a button which will be used as the control to show or hide
the popup portion of the combo box.

isPopupVisible

```java
public boolean isPopupVisible​(
JComboBox
<?> c)
```

Tells if the popup is visible or not.

**Specified by:** isPopupVisible

in class

ComboBoxUI
**Parameters:** c

- a

JComboBox
**Returns:** true if popup of the

JComboBox

is visible

---

#### isPopupVisible

public boolean isPopupVisible​(

JComboBox

<?> c)

Tells if the popup is visible or not.

setPopupVisible

```java
public void setPopupVisible​(
JComboBox
<?> c,
boolean v)
```

Hides the popup.

**Specified by:** setPopupVisible

in class

ComboBoxUI
**Parameters:** c

- a

JComboBox
**Parameters:** v

- a

boolean

determining the visibilty of the popup

---

#### setPopupVisible

public void setPopupVisible​(

JComboBox

<?> c,
boolean v)

Hides the popup.

isFocusTraversable

```java
public boolean isFocusTraversable​(
JComboBox
<?> c)
```

Determines if the JComboBox is focus traversable. If the JComboBox is editable
this returns false, otherwise it returns true.

**Specified by:** isFocusTraversable

in class

ComboBoxUI
**Parameters:** c

- a

JComboBox
**Returns:** true if the given

JComboBox

is traversable

---

#### isFocusTraversable

public boolean isFocusTraversable​(

JComboBox

<?> c)

Determines if the JComboBox is focus traversable. If the JComboBox is editable
this returns false, otherwise it returns true.

getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

The minimum size is the size of the display area plus insets plus the button.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** c

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

---

#### getMinimumSize

public

Dimension

getMinimumSize​(

JComponent

c)

The minimum size is the size of the display area plus insets plus the button.

getBaseline

```java
public int getBaseline​(
JComponent
c,
int width,
int height)
```

Returns the baseline.

**Overrides:** getBaseline

in class

ComponentUI
**Parameters:** c

-

JComponent

baseline is being requested for
**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** baseline or a value < 0 indicating there is no reasonable
baseline
**Throws:** NullPointerException

- if

c

is

null
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

---

#### getBaseline

public int getBaseline​(

JComponent

c,
int width,
int height)

Returns the baseline.

getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)
```

Returns an enum indicating how the baseline of the component
changes as the size changes.

**Overrides:** getBaselineResizeBehavior

in class

ComponentUI
**Parameters:** c

-

JComponent

to return baseline resize behavior for
**Returns:** an enum indicating how the baseline changes as the component
size changes
**Throws:** NullPointerException

- if

c

is

null
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

---

#### getBaselineResizeBehavior

public

Component.BaselineResizeBehavior

getBaselineResizeBehavior​(

JComponent

c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

isNavigationKey

```java
protected boolean isNavigationKey​(int keyCode)
```

Returns whether or not the supplied keyCode maps to a key that is used for
navigation. This is used for optimizing key input by only passing non-
navigation keys to the type-ahead mechanism. Subclasses should override this
if they change the navigation keys.

**Parameters:** keyCode

- a key code
**Returns:** true

if the supplied

keyCode

maps to a navigation key

---

#### isNavigationKey

protected boolean isNavigationKey​(int keyCode)

Returns whether or not the supplied keyCode maps to a key that is used for
navigation. This is used for optimizing key input by only passing non-
navigation keys to the type-ahead mechanism. Subclasses should override this
if they change the navigation keys.

selectNextPossibleValue

```java
protected void selectNextPossibleValue()
```

Selects the next item in the list. It won't change the selection if the
currently selected item is already the last item.

---

#### selectNextPossibleValue

protected void selectNextPossibleValue()

Selects the next item in the list. It won't change the selection if the
currently selected item is already the last item.

selectPreviousPossibleValue

```java
protected void selectPreviousPossibleValue()
```

Selects the previous item in the list. It won't change the selection if the
currently selected item is already the first item.

---

#### selectPreviousPossibleValue

protected void selectPreviousPossibleValue()

Selects the previous item in the list. It won't change the selection if the
currently selected item is already the first item.

toggleOpenClose

```java
protected void toggleOpenClose()
```

Hides the popup if it is showing and shows the popup if it is hidden.

---

#### toggleOpenClose

protected void toggleOpenClose()

Hides the popup if it is showing and shows the popup if it is hidden.

rectangleForCurrentValue

```java
protected
Rectangle
rectangleForCurrentValue()
```

Returns the area that is reserved for drawing the currently selected item.

**Returns:** the area that is reserved for drawing the currently selected item

---

#### rectangleForCurrentValue

protected

Rectangle

rectangleForCurrentValue()

Returns the area that is reserved for drawing the currently selected item.

getInsets

```java
protected
Insets
getInsets()
```

Gets the insets from the JComboBox.

**Returns:** the insets

---

#### getInsets

protected

Insets

getInsets()

Gets the insets from the JComboBox.

paintCurrentValue

```java
public void paintCurrentValue​(
Graphics
g,

Rectangle
bounds,
boolean hasFocus)
```

Paints the currently selected item.

**Parameters:** g

- an instance of

Graphics
**Parameters:** bounds

- a bounding rectangle to render to
**Parameters:** hasFocus

- is focused

---

#### paintCurrentValue

public void paintCurrentValue​(

Graphics

g,

Rectangle

bounds,
boolean hasFocus)

Paints the currently selected item.

paintCurrentValueBackground

```java
public void paintCurrentValueBackground​(
Graphics
g,

Rectangle
bounds,
boolean hasFocus)
```

Paints the background of the currently selected item.

**Parameters:** g

- an instance of

Graphics
**Parameters:** bounds

- a bounding rectangle to render to
**Parameters:** hasFocus

- is focused

---

#### paintCurrentValueBackground

public void paintCurrentValueBackground​(

Graphics

g,

Rectangle

bounds,
boolean hasFocus)

Paints the background of the currently selected item.

getDefaultSize

```java
protected
Dimension
getDefaultSize()
```

Return the default size of an empty display area of the combo box using
the current renderer and font.

**Returns:** the size of an empty display area
**See Also:** getDisplaySize()

---

#### getDefaultSize

protected

Dimension

getDefaultSize()

Return the default size of an empty display area of the combo box using
the current renderer and font.

getDisplaySize

```java
protected
Dimension
getDisplaySize()
```

Returns the calculated size of the display area. The display area is the
portion of the combo box in which the selected item is displayed. This
method will use the prototype display value if it has been set.

For combo boxes with a non trivial number of items, it is recommended to
use a prototype display value to significantly speed up the display
size calculation.

**Returns:** the size of the display area calculated from the combo box items
**See Also:** JComboBox.setPrototypeDisplayValue(E)

---

#### getDisplaySize

protected

Dimension

getDisplaySize()

Returns the calculated size of the display area. The display area is the
portion of the combo box in which the selected item is displayed. This
method will use the prototype display value if it has been set.

For combo boxes with a non trivial number of items, it is recommended to
use a prototype display value to significantly speed up the display
size calculation.

For combo boxes with a non trivial number of items, it is recommended to
use a prototype display value to significantly speed up the display
size calculation.

getSizeForComponent

```java
protected
Dimension
getSizeForComponent​(
Component
comp)
```

Returns the size a component would have if used as a cell renderer.

**Parameters:** comp

- a

Component

to check
**Returns:** size of the component
**Since:** 1.7

---

#### getSizeForComponent

protected

Dimension

getSizeForComponent​(

Component

comp)

Returns the size a component would have if used as a cell renderer.

installKeyboardActions

```java
protected void installKeyboardActions()
```

Adds keyboard actions to the JComboBox. Actions on enter and esc are already
supplied. Add more actions as you need them.

---

#### installKeyboardActions

protected void installKeyboardActions()

Adds keyboard actions to the JComboBox. Actions on enter and esc are already
supplied. Add more actions as you need them.

uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Removes the focus InputMap and ActionMap.

---

#### uninstallKeyboardActions

protected void uninstallKeyboardActions()

Removes the focus InputMap and ActionMap.

---

