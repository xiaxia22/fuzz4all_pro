# Class JTabbedPane

**Source:** `java.desktop\javax\swing\JTabbedPane.html`

### Class Description

```java
@JavaBean
(
defaultProperty
="UI",

description
="A component which provides a tab folder metaphor for displaying one component from a set of components.")
public class
JTabbedPane

extends
JComponent

implements
Serializable
,
Accessible
,
SwingConstants
```

A component that lets the user switch between a group of components by
clicking on a tab with a given title and/or icon.
For examples and information on using tabbed panes see

How to Use Tabbed Panes

,
a section in

The Java Tutorial

.

Tabs/components are added to a

TabbedPane

object by using the

addTab

and

insertTab

methods.
A tab is represented by an index corresponding
to the position it was added in, where the first tab has an index equal to 0
and the last tab has an index equal to the tab count minus 1.

The

TabbedPane

uses a

SingleSelectionModel

to represent the set
of tab indices and the currently selected index. If the tab count
is greater than 0, then there will always be a selected index, which
by default will be initialized to the first tab. If the tab count is
0, then the selected index will be -1.

The tab title can be rendered by a

Component

.
For example, the following produce similar results:

```java
// In this case the look and feel renders the title for the tab.
tabbedPane.addTab("Tab", myComponent);
// In this case the custom component is responsible for rendering the
// title of the tab.
tabbedPane.addTab(null, myComponent);
tabbedPane.setTabComponentAt(0, new JLabel("Tab"));
```

The latter is typically used when you want a more complex user interaction
that requires custom components on the tab. For example, you could
provide a custom component that animates or one that has widgets for
closing the tab.

If you specify a component for a tab, the

JTabbedPane

will not render any text or icon you have specified for the tab.

Note:

Do not use

setVisible

directly on a tab component to make it visible,
use

setSelectedComponent

or

setSelectedIndex

methods instead.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

SwingConstants

---

### Field Details

#### public static final int WRAP_TAB_LAYOUT

The tab layout policy for wrapping tabs in multiple runs when all
tabs will not fit within a single run.

**See Also:**
- Constant Field Values

---

#### public static final int SCROLL_TAB_LAYOUT

Tab layout policy for providing a subset of available tabs when all
the tabs will not fit within a single run. If all the tabs do
not fit within a single run the look and feel will provide a way
to navigate to hidden tabs.

**See Also:**
- Constant Field Values

---

#### protected int tabPlacement

Where the tabs are placed.

**See Also:**
- setTabPlacement(int)

---

#### protected
SingleSelectionModel
model

The default selection model

---

#### protected
ChangeListener
changeListener

The

changeListener

is the listener we add to the
model.

---

#### protected transient
ChangeEvent
changeEvent

Only one

ChangeEvent

is needed per

TabPane

instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this".

---

### Constructor Details

#### public JTabbedPane()

Creates an empty

TabbedPane

with a default
tab placement of

JTabbedPane.TOP

.

**See Also:**
- addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

---

#### public JTabbedPane​(int tabPlacement)

Creates an empty

TabbedPane

with the specified tab placement
of either:

JTabbedPane.TOP

,

JTabbedPane.BOTTOM

,

JTabbedPane.LEFT

, or

JTabbedPane.RIGHT

.

**Parameters:**
- tabPlacement

- the placement for the tabs relative to the content

**See Also:**
- addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

---

#### public JTabbedPane​(int tabPlacement,
int tabLayoutPolicy)

Creates an empty

TabbedPane

with the specified tab placement
and tab layout policy. Tab placement may be either:

JTabbedPane.TOP

,

JTabbedPane.BOTTOM

,

JTabbedPane.LEFT

, or

JTabbedPane.RIGHT

.
Tab layout policy may be either:

JTabbedPane.WRAP_TAB_LAYOUT

or

JTabbedPane.SCROLL_TAB_LAYOUT

.

**Parameters:**
- tabPlacement

- the placement for the tabs relative to the content
- tabLayoutPolicy

- the policy for laying out tabs when all tabs will not fit on one run

**Throws:**
- IllegalArgumentException

- if tab placement or tab layout policy are not
one of the above supported values

**See Also:**
- addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

**Since:**
- 1.4

---

### Method Details

#### public
TabbedPaneUI
getUI()

Returns the UI object which implements the L&F for this component.

**Overrides:**
- getUI

in class

JComponent

**Returns:**
- a

TabbedPaneUI

object

**See Also:**
- setUI(javax.swing.plaf.TabbedPaneUI)

---

#### @BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the tabbedpane\'s LookAndFeel")
public void setUI​(
TabbedPaneUI
ui)

Sets the UI object which implements the L&F for this component.

**Parameters:**
- ui

- the new UI object

**See Also:**
- UIDefaults.getUI(javax.swing.JComponent)

---

#### public void updateUI()

Resets the UI property to a value from the current look and feel.

**Overrides:**
- updateUI

in class

JComponent

**See Also:**
- JComponent.updateUI()

---

#### @BeanProperty
(
bound
=false)
public
String
getUIClassID()

Returns the name of the UI class that implements the
L&F for this component.

**Overrides:**
- getUIClassID

in class

JComponent

**Returns:**
- the string "TabbedPaneUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### protected
ChangeListener
createChangeListener()

Subclasses that want to handle

ChangeEvents

differently
can override this to return a subclass of

ModelListener

or
another

ChangeListener

implementation.

**Returns:**
- a

ChangeListener

**See Also:**
- fireStateChanged()

---

#### public void addChangeListener​(
ChangeListener
l)

Adds a

ChangeListener

to this tabbedpane.

**Parameters:**
- l

- the

ChangeListener

to add

**See Also:**
- fireStateChanged()

,

removeChangeListener(javax.swing.event.ChangeListener)

---

#### public void removeChangeListener​(
ChangeListener
l)

Removes a

ChangeListener

from this tabbedpane.

**Parameters:**
- l

- the

ChangeListener

to remove

**See Also:**
- fireStateChanged()

,

addChangeListener(javax.swing.event.ChangeListener)

---

#### @BeanProperty
(
bound
=false)
public
ChangeListener
[] getChangeListeners()

Returns an array of all the

ChangeListener

s added
to this

JTabbedPane

with

addChangeListener

.

**Returns:**
- all of the

ChangeListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### protected void fireStateChanged()

Sends a

ChangeEvent

, with this

JTabbedPane

as the source,
to each registered listener. This method is called each time there is
a change to either the selected index or the selected tab in the

JTabbedPane

. Usually, the selected index and selected tab change
together. However, there are some cases, such as tab addition, where the
selected index changes and the same tab remains selected. There are other
cases, such as deleting the selected tab, where the index remains the
same, but a new tab moves to that index. Events are fired for all of
these cases.

**See Also:**
- addChangeListener(javax.swing.event.ChangeListener)

,

EventListenerList

---

#### public
SingleSelectionModel
getModel()

Returns the model associated with this tabbedpane.

**Returns:**
- the

SingleSelectionModel

associated with this tabbedpane

**See Also:**
- setModel(javax.swing.SingleSelectionModel)

---

#### @BeanProperty
(
description
="The tabbedpane\'s SingleSelectionModel.")
public void setModel​(
SingleSelectionModel
model)

Sets the model to be used with this tabbedpane.

**Parameters:**
- model

- the model to be used

**See Also:**
- getModel()

---

#### public int getTabPlacement()

Returns the placement of the tabs for this tabbedpane.

**Returns:**
- an

int

specifying the placement for the tabs

**See Also:**
- setTabPlacement(int)

---

#### @BeanProperty
(
preferred
=true,

visualUpdate
=true,

enumerationValues
={"JTabbedPane.TOP","JTabbedPane.LEFT","JTabbedPane.BOTTOM","JTabbedPane.RIGHT"},

description
="The tabbedpane\'s tab placement.")
public void setTabPlacement​(int tabPlacement)

Sets the tab placement for this tabbedpane.
Possible values are:

- JTabbedPane.TOP

JTabbedPane.BOTTOM

JTabbedPane.LEFT

JTabbedPane.RIGHT

The default value, if not set, is

SwingConstants.TOP

.

**Parameters:**
- tabPlacement

- the placement for the tabs relative to the content

**Throws:**
- IllegalArgumentException

- if tab placement value isn't one
of the above valid values

---

#### public int getTabLayoutPolicy()

Returns the policy used by the tabbedpane to layout the tabs when all the
tabs will not fit within a single run.

**Returns:**
- an

int

specifying the policy used to layout the tabs

**See Also:**
- setTabLayoutPolicy(int)

**Since:**
- 1.4

---

#### @BeanProperty
(
preferred
=true,

visualUpdate
=true,

enumerationValues
={"JTabbedPane.WRAP_TAB_LAYOUT","JTabbedPane.SCROLL_TAB_LAYOUT"},

description
="The tabbedpane\'s policy for laying out the tabs")
public void setTabLayoutPolicy​(int tabLayoutPolicy)

Sets the policy which the tabbedpane will use in laying out the tabs
when all the tabs will not fit within a single run.
Possible values are:

- JTabbedPane.WRAP_TAB_LAYOUT

JTabbedPane.SCROLL_TAB_LAYOUT

The default value, if not set by the UI, is

JTabbedPane.WRAP_TAB_LAYOUT

.

Some look and feels might only support a subset of the possible
layout policies, in which case the value of this property may be
ignored.

**Parameters:**
- tabLayoutPolicy

- the policy used to layout the tabs

**Throws:**
- IllegalArgumentException

- if layoutPolicy value isn't one
of the above valid values

**See Also:**
- getTabLayoutPolicy()

**Since:**
- 1.4

---

#### public int getSelectedIndex()

Returns the currently selected index for this tabbedpane.
Returns -1 if there is no currently selected tab.

**Returns:**
- the index of the selected tab

**See Also:**
- setSelectedIndex(int)

---

#### @BeanProperty
(
bound
=false,

preferred
=true,

description
="The tabbedpane\'s selected tab index.")
public void setSelectedIndex​(int index)

Sets the selected index for this tabbedpane. The index must be
a valid tab index or -1, which indicates that no tab should be selected
(can also be used when there are no tabs in the tabbedpane). If a -1
value is specified when the tabbedpane contains one or more tabs, then
the results will be implementation defined.

**Parameters:**
- index

- the index to be selected

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < -1 || index >= tab count)

**See Also:**
- getSelectedIndex()

,

SingleSelectionModel.setSelectedIndex(int)

---

#### public
Component
getSelectedComponent()

Returns the currently selected component for this tabbedpane.
Returns

null

if there is no currently selected tab.

**Returns:**
- the component corresponding to the selected tab

**See Also:**
- setSelectedComponent(java.awt.Component)

---

#### @BeanProperty
(
bound
=false,

preferred
=true,

description
="The tabbedpane\'s selected component.")
public void setSelectedComponent​(
Component
c)

Sets the selected component for this tabbedpane. This
will automatically set the

selectedIndex

to the index
corresponding to the specified component.

**Parameters:**
- c

- the selected

Component

for this

TabbedPane

**Throws:**
- IllegalArgumentException

- if component not found in tabbed
pane

**See Also:**
- getSelectedComponent()

---

#### public void insertTab​(
String
title,

Icon
icon,

Component
component,

String
tip,
int index)

Inserts a new tab for the given component, at the given index,
represented by the given title and/or icon, either of which may
be

null

.

**Parameters:**
- title

- the title to be displayed on the tab
- icon

- the icon to be displayed on the tab
- component

- the component to be displayed when this tab is clicked.
- tip

- the tooltip to be displayed for this tab
- index

- the position to insert this new tab
(

> 0 and <= getTabCount()

)

**Throws:**
- IndexOutOfBoundsException

- if the index is out of range
(

< 0 or > getTabCount()

)

**See Also:**
- addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

,

removeTabAt(int)

---

#### public void addTab​(
String
title,

Icon
icon,

Component
component,

String
tip)

Adds a

component

and

tip

represented by a

title

and/or

icon

,
either of which can be

null

.
Cover method for

insertTab

.

**Parameters:**
- title

- the title to be displayed in this tab
- icon

- the icon to be displayed in this tab
- component

- the component to be displayed when this tab is clicked
- tip

- the tooltip to be displayed for this tab

**See Also:**
- insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

---

#### public void addTab​(
String
title,

Icon
icon,

Component
component)

Adds a

component

represented by a

title

and/or

icon

, either of which can be

null

.
Cover method for

insertTab

.

**Parameters:**
- title

- the title to be displayed in this tab
- icon

- the icon to be displayed in this tab
- component

- the component to be displayed when this tab is clicked

**See Also:**
- insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

---

#### public void addTab​(
String
title,

Component
component)

Adds a

component

represented by a

title

and no icon.
Cover method for

insertTab

.

**Parameters:**
- title

- the title to be displayed in this tab
- component

- the component to be displayed when this tab is clicked

**See Also:**
- insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

---

#### public
Component
add​(
Component
component)

Adds a

component

with a tab title defaulting to
the name of the component which is the result of calling

component.getName

.
Cover method for

insertTab

.

**Overrides:**
- add

in class

Container

**Parameters:**
- component

- the component to be displayed when this tab is clicked

**Returns:**
- the component

**See Also:**
- insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

---

#### public
Component
add​(
String
title,

Component
component)

Adds a

component

with the specified tab title.
Cover method for

insertTab

.

**Overrides:**
- add

in class

Container

**Parameters:**
- title

- the title to be displayed in this tab
- component

- the component to be displayed when this tab is clicked

**Returns:**
- the component

**See Also:**
- insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

---

#### public
Component
add​(
Component
component,
int index)

Adds a

component

at the specified tab index with a tab
title defaulting to the name of the component.
Cover method for

insertTab

.

**Overrides:**
- add

in class

Container

**Parameters:**
- component

- the component to be displayed when this tab is clicked
- index

- the position to insert this new tab

**Returns:**
- the component

**See Also:**
- insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

---

#### public void add​(
Component
component,

Object
constraints)

Adds a

component

to the tabbed pane.
If

constraints

is a

String

or an

Icon

, it will be used for the tab title,
otherwise the component's name will be used as the tab title.
Cover method for

insertTab

.

**Overrides:**
- add

in class

Container

**Parameters:**
- component

- the component to be displayed when this tab is clicked
- constraints

- the object to be displayed in the tab

**See Also:**
- insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

---

#### public void add​(
Component
component,

Object
constraints,
int index)

Adds a

component

at the specified tab index.
If

constraints

is a

String

or an

Icon

, it will be used for the tab title,
otherwise the component's name will be used as the tab title.
Cover method for

insertTab

.

**Overrides:**
- add

in class

Container

**Parameters:**
- component

- the component to be displayed when this tab is clicked
- constraints

- the object to be displayed in the tab
- index

- the position to insert this new tab

**See Also:**
- insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

---

#### public void removeTabAt​(int index)

Removes the tab at

index

.
After the component associated with

index

is removed,
its visibility is reset to true to ensure it will be visible
if added to other containers.

**Parameters:**
- index

- the index of the tab to be removed

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

**See Also:**
- addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

,

insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

---

#### public void remove​(
Component
component)

Removes the specified

Component

from the

JTabbedPane

. The method does nothing
if the

component

is null.

**Overrides:**
- remove

in class

Container

**Parameters:**
- component

- the component to remove from the tabbedpane

**See Also:**
- addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

,

removeTabAt(int)

---

#### public void remove​(int index)

Removes the tab and component which corresponds to the specified index.

**Overrides:**
- remove

in class

Container

**Parameters:**
- index

- the index of the component to remove from the

tabbedpane

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

**See Also:**
- addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

,

removeTabAt(int)

---

#### public void removeAll()

Removes all the tabs and their corresponding components
from the

tabbedpane

.

**Overrides:**
- removeAll

in class

Container

**See Also:**
- addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

,

removeTabAt(int)

---

#### @BeanProperty
(
bound
=false)
public int getTabCount()

Returns the number of tabs in this

tabbedpane

.

**Returns:**
- an integer specifying the number of tabbed pages

---

#### @BeanProperty
(
bound
=false)
public int getTabRunCount()

Returns the number of tab runs currently used to display
the tabs.

**Returns:**
- an integer giving the number of rows if the

tabPlacement

is

TOP

or

BOTTOM

and the number of columns if

tabPlacement

is

LEFT

or

RIGHT

,
or 0 if there is no UI set on this

tabbedpane

---

#### public
String
getTitleAt​(int index)

Returns the tab title at

index

.

**Parameters:**
- index

- the index of the item being queried

**Returns:**
- the title at

index

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

**See Also:**
- setTitleAt(int, java.lang.String)

---

#### public
Icon
getIconAt​(int index)

Returns the tab icon at

index

.

**Parameters:**
- index

- the index of the item being queried

**Returns:**
- the icon at

index

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

**See Also:**
- setIconAt(int, javax.swing.Icon)

---

#### public
Icon
getDisabledIconAt​(int index)

Returns the tab disabled icon at

index

.
If the tab disabled icon doesn't exist at

index

this will forward the call to the look and feel to construct
an appropriate disabled Icon from the corresponding enabled
Icon. Some look and feels might not render the disabled Icon,
in which case it won't be created.

**Parameters:**
- index

- the index of the item being queried

**Returns:**
- the icon at

index

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

**See Also:**
- setDisabledIconAt(int, javax.swing.Icon)

---

#### public
String
getToolTipTextAt​(int index)

Returns the tab tooltip text at

index

.

**Parameters:**
- index

- the index of the item being queried

**Returns:**
- a string containing the tool tip text at

index

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

**See Also:**
- setToolTipTextAt(int, java.lang.String)

**Since:**
- 1.3

---

#### public
Color
getBackgroundAt​(int index)

Returns the tab background color at

index

.

**Parameters:**
- index

- the index of the item being queried

**Returns:**
- the

Color

of the tab background at

index

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

**See Also:**
- setBackgroundAt(int, java.awt.Color)

---

#### public
Color
getForegroundAt​(int index)

Returns the tab foreground color at

index

.

**Parameters:**
- index

- the index of the item being queried

**Returns:**
- the

Color

of the tab foreground at

index

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

**See Also:**
- setForegroundAt(int, java.awt.Color)

---

#### public boolean isEnabledAt​(int index)

Returns whether or not the tab at

index

is
currently enabled.

**Parameters:**
- index

- the index of the item being queried

**Returns:**
- true if the tab at

index

is enabled;
false otherwise

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

**See Also:**
- setEnabledAt(int, boolean)

---

#### public
Component
getComponentAt​(int index)

Returns the component at

index

.

**Parameters:**
- index

- the index of the item being queried

**Returns:**
- the

Component

at

index

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

**See Also:**
- setComponentAt(int, java.awt.Component)

---

#### public int getMnemonicAt​(int tabIndex)

Returns the keyboard mnemonic for accessing the specified tab.
The mnemonic is the key which when combined with the look and feel's
mouseless modifier (usually Alt) will activate the specified
tab.

**Parameters:**
- tabIndex

- the index of the tab that the mnemonic refers to

**Returns:**
- the key code which represents the mnemonic;
-1 if a mnemonic is not specified for the tab

**Throws:**
- IndexOutOfBoundsException

- if index is out of range
(

tabIndex

< 0 ||

tabIndex

>= tab count)

**See Also:**
- setDisplayedMnemonicIndexAt(int,int)

,

setMnemonicAt(int,int)

**Since:**
- 1.4

---

#### public int getDisplayedMnemonicIndexAt​(int tabIndex)

Returns the character, as an index, that the look and feel should
provide decoration for as representing the mnemonic character.

**Parameters:**
- tabIndex

- the index of the tab that the mnemonic refers to

**Returns:**
- index representing mnemonic character if one exists;
otherwise returns -1

**Throws:**
- IndexOutOfBoundsException

- if index is out of range
(

tabIndex

< 0 ||

tabIndex

>= tab count)

**See Also:**
- setDisplayedMnemonicIndexAt(int,int)

,

setMnemonicAt(int,int)

**Since:**
- 1.4

---

#### public
Rectangle
getBoundsAt​(int index)

Returns the tab bounds at

index

. If the tab at
this index is not currently visible in the UI, then returns

null

.
If there is no UI set on this

tabbedpane

,
then returns

null

.

**Parameters:**
- index

- the index to be queried

**Returns:**
- a

Rectangle

containing the tab bounds at

index

, or

null

if tab at

index

is not currently visible in the UI,
or if there is no UI set on this

tabbedpane

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

---

#### @BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The title at the specified tab index.")
public void setTitleAt​(int index,

String
title)

Sets the title at

index

to

title

which
can be

null

.
The title is not shown if a tab component for this tab was specified.
An internal exception is raised if there is no tab at that index.

**Parameters:**
- index

- the tab index where the title should be set
- title

- the title to be displayed in the tab

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

**See Also:**
- getTitleAt(int)

,

setTabComponentAt(int, java.awt.Component)

---

#### @BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The icon at the specified tab index.")
public void setIconAt​(int index,

Icon
icon)

Sets the icon at

index

to

icon

which can be

null

. This does not set disabled icon at

icon

.
If the new Icon is different than the current Icon and disabled icon
is not explicitly set, the LookAndFeel will be asked to generate a disabled
Icon. To explicitly set disabled icon, use

setDisableIconAt()

.
The icon is not shown if a tab component for this tab was specified.
An internal exception is raised if there is no tab at that index.

**Parameters:**
- index

- the tab index where the icon should be set
- icon

- the icon to be displayed in the tab

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

**See Also:**
- setDisabledIconAt(int, javax.swing.Icon)

,

getIconAt(int)

,

getDisabledIconAt(int)

,

setTabComponentAt(int, java.awt.Component)

---

#### @BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The disabled icon at the specified tab index.")
public void setDisabledIconAt​(int index,

Icon
disabledIcon)

Sets the disabled icon at

index

to

icon

which can be

null

.
An internal exception is raised if there is no tab at that index.

**Parameters:**
- index

- the tab index where the disabled icon should be set
- disabledIcon

- the icon to be displayed in the tab when disabled

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

**See Also:**
- getDisabledIconAt(int)

---

#### @BeanProperty
(
preferred
=true,

description
="The tooltip text at the specified tab index.")
public void setToolTipTextAt​(int index,

String
toolTipText)

Sets the tooltip text at

index

to

toolTipText

which can be

null

.
An internal exception is raised if there is no tab at that index.

**Parameters:**
- index

- the tab index where the tooltip text should be set
- toolTipText

- the tooltip text to be displayed for the tab

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

**See Also:**
- getToolTipTextAt(int)

**Since:**
- 1.3

---

#### @BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The background color at the specified tab index.")
public void setBackgroundAt​(int index,

Color
background)

Sets the background color at

index

to

background

which can be

null

, in which case the tab's background color
will default to the background color of the

tabbedpane

.
An internal exception is raised if there is no tab at that index.

It is up to the look and feel to honor this property, some may
choose to ignore it.

**Parameters:**
- index

- the tab index where the background should be set
- background

- the color to be displayed in the tab's background

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

**See Also:**
- getBackgroundAt(int)

---

#### @BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The foreground color at the specified tab index.")
public void setForegroundAt​(int index,

Color
foreground)

Sets the foreground color at

index

to

foreground

which can be

null

, in which case the tab's foreground color
will default to the foreground color of this

tabbedpane

.
An internal exception is raised if there is no tab at that index.

It is up to the look and feel to honor this property, some may
choose to ignore it.

**Parameters:**
- index

- the tab index where the foreground should be set
- foreground

- the color to be displayed as the tab's foreground

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

**See Also:**
- getForegroundAt(int)

---

#### public void setEnabledAt​(int index,
boolean enabled)

Sets whether or not the tab at

index

is enabled.
An internal exception is raised if there is no tab at that index.

**Parameters:**
- index

- the tab index which should be enabled/disabled
- enabled

- whether or not the tab should be enabled

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

**See Also:**
- isEnabledAt(int)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="The component at the specified tab index.")
public void setComponentAt​(int index,

Component
component)

Sets the component at

index

to

component

.
An internal exception is raised if there is no tab at that index.

**Parameters:**
- index

- the tab index where this component is being placed
- component

- the component for the tab

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

**See Also:**
- getComponentAt(int)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="the index into the String to draw the keyboard character mnemonic at")
public void setDisplayedMnemonicIndexAt​(int tabIndex,
int mnemonicIndex)

Provides a hint to the look and feel as to which character in the
text should be decorated to represent the mnemonic. Not all look and
feels may support this. A value of -1 indicates either there is
no mnemonic for this tab, or you do not wish the mnemonic to be
displayed for this tab.

The value of this is updated as the properties relating to the
mnemonic change (such as the mnemonic itself, the text...).
You should only ever have to call this if
you do not wish the default character to be underlined. For example, if
the text at tab index 3 was 'Apple Price', with a mnemonic of 'p',
and you wanted the 'P'
to be decorated, as 'Apple

P

rice', you would have to invoke

setDisplayedMnemonicIndex(3, 6)

after invoking

setMnemonicAt(3, KeyEvent.VK_P)

.

Note that it is the programmer's responsibility to ensure
that each tab has a unique mnemonic or unpredictable results may
occur.

**Parameters:**
- tabIndex

- the index of the tab that the mnemonic refers to
- mnemonicIndex

- index into the

String

to underline

**Throws:**
- IndexOutOfBoundsException

- if

tabIndex

is
out of range (

tabIndex < 0 || tabIndex >= tab
count

)
- IllegalArgumentException

- will be thrown if

mnemonicIndex

is >= length of the tab
title , or < -1

**See Also:**
- setMnemonicAt(int,int)

,

getDisplayedMnemonicIndexAt(int)

**Since:**
- 1.4

---

#### @BeanProperty
(
visualUpdate
=true,

description
="The keyboard mnenmonic, as a KeyEvent VK constant, for the specified tab")
public void setMnemonicAt​(int tabIndex,
int mnemonic)

Sets the keyboard mnemonic for accessing the specified tab.
The mnemonic is the key which when combined with the look and feel's
mouseless modifier (usually Alt) will activate the specified
tab.

A mnemonic must correspond to a single key on the keyboard
and should be specified using one of the

VK_XXX

keycodes defined in

java.awt.event.KeyEvent

or one of the extended keycodes obtained through

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.
Mnemonics are case-insensitive, therefore a key event
with the corresponding keycode would cause the button to be
activated whether or not the Shift modifier was pressed.

This will update the displayed mnemonic property for the specified
tab.

**Parameters:**
- tabIndex

- the index of the tab that the mnemonic refers to
- mnemonic

- the key code which represents the mnemonic

**Throws:**
- IndexOutOfBoundsException

- if

tabIndex

is out
of range (

tabIndex < 0 || tabIndex >= tab count

)

**See Also:**
- getMnemonicAt(int)

,

setDisplayedMnemonicIndexAt(int,int)

**Since:**
- 1.4

---

#### public int indexOfTab​(
String
title)

Returns the first tab index with a given

title

, or
-1 if no tab has this title.

**Parameters:**
- title

- the title for the tab

**Returns:**
- the first tab index which matches

title

, or
-1 if no tab has this title

---

#### public int indexOfTab​(
Icon
icon)

Returns the first tab index with a given

icon

,
or -1 if no tab has this icon.

**Parameters:**
- icon

- the icon for the tab

**Returns:**
- the first tab index which matches

icon

,
or -1 if no tab has this icon

---

#### public int indexOfComponent​(
Component
component)

Returns the index of the tab for the specified component.
Returns -1 if there is no tab for this component.

**Parameters:**
- component

- the component for the tab

**Returns:**
- the first tab which matches this component, or -1
if there is no tab for this component

---

#### public int indexAtLocation​(int x,
int y)

Returns the tab index corresponding to the tab whose bounds
intersect the specified location. Returns -1 if no tab
intersects the location.

**Parameters:**
- x

- the x location relative to this tabbedpane
- y

- the y location relative to this tabbedpane

**Returns:**
- the tab index which intersects the location, or
-1 if no tab intersects the location

**Since:**
- 1.4

---

#### public
String
getToolTipText​(
MouseEvent
event)

Returns the tooltip text for the component determined by the
mouse event location.

**Overrides:**
- getToolTipText

in class

JComponent

**Parameters:**
- event

- the

MouseEvent

that tells where the
cursor is lingering

**Returns:**
- the

String

containing the tooltip text

---

#### protected
String
paramString()

Returns a string representation of this

JTabbedPane

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:**
- paramString

in class

JComponent

**Returns:**
- a string representation of this JTabbedPane.

---

#### @BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this JTabbedPane.
For tabbed panes, the AccessibleContext takes the form of an
AccessibleJTabbedPane.
A new AccessibleJTabbedPane instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- an AccessibleJTabbedPane that serves as the
AccessibleContext of this JTabbedPane

---

#### @BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The tab component at the specified tab index.")
public void setTabComponentAt​(int index,

Component
component)

Sets the component that is responsible for rendering the
title for the specified tab. A null value means

JTabbedPane

will render the title and/or icon for
the specified tab. A non-null value means the component will
render the title and

JTabbedPane

will not render
the title and/or icon.

Note: The component must not be one that the developer has
already added to the tabbed pane.

**Parameters:**
- index

- the tab index where the component should be set
- component

- the component to render the title for the
specified tab

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
- IllegalArgumentException

- if component has already been
added to this

JTabbedPane

**See Also:**
- getTabComponentAt(int)

**Since:**
- 1.6

---

#### public
Component
getTabComponentAt​(int index)

Returns the tab component at

index

.

**Parameters:**
- index

- the index of the item being queried

**Returns:**
- the tab component at

index

**Throws:**
- IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

**See Also:**
- setTabComponentAt(int, java.awt.Component)

**Since:**
- 1.6

---

#### public int indexOfTabComponent​(
Component
tabComponent)

Returns the index of the tab for the specified tab component.
Returns -1 if there is no tab for this tab component.

**Parameters:**
- tabComponent

- the tab component for the tab

**Returns:**
- the first tab which matches this tab component, or -1
if there is no tab for this tab component

**See Also:**
- setTabComponentAt(int, java.awt.Component)

,

getTabComponentAt(int)

**Since:**
- 1.6

---

### Additional Sections

#### Class JTabbedPane

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JTabbedPane

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JTabbedPane

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JTabbedPane

javax.swing.JComponent

- javax.swing.JTabbedPane

javax.swing.JTabbedPane

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

SwingConstants

```java
@JavaBean
(
defaultProperty
="UI",

description
="A component which provides a tab folder metaphor for displaying one component from a set of components.")
public class
JTabbedPane

extends
JComponent

implements
Serializable
,
Accessible
,
SwingConstants
```

A component that lets the user switch between a group of components by
clicking on a tab with a given title and/or icon.
For examples and information on using tabbed panes see

How to Use Tabbed Panes

,
a section in

The Java Tutorial

.

Tabs/components are added to a

TabbedPane

object by using the

addTab

and

insertTab

methods.
A tab is represented by an index corresponding
to the position it was added in, where the first tab has an index equal to 0
and the last tab has an index equal to the tab count minus 1.

The

TabbedPane

uses a

SingleSelectionModel

to represent the set
of tab indices and the currently selected index. If the tab count
is greater than 0, then there will always be a selected index, which
by default will be initialized to the first tab. If the tab count is
0, then the selected index will be -1.

The tab title can be rendered by a

Component

.
For example, the following produce similar results:

```java
// In this case the look and feel renders the title for the tab.
tabbedPane.addTab("Tab", myComponent);
// In this case the custom component is responsible for rendering the
// title of the tab.
tabbedPane.addTab(null, myComponent);
tabbedPane.setTabComponentAt(0, new JLabel("Tab"));
```

The latter is typically used when you want a more complex user interaction
that requires custom components on the tab. For example, you could
provide a custom component that animates or one that has widgets for
closing the tab.

If you specify a component for a tab, the

JTabbedPane

will not render any text or icon you have specified for the tab.

Note:

Do not use

setVisible

directly on a tab component to make it visible,
use

setSelectedComponent

or

setSelectedIndex

methods instead.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**Since:** 1.2
**See Also:** SingleSelectionModel

,

Serialized Form

@JavaBean

(

defaultProperty

="UI",

description

="A component which provides a tab folder metaphor for displaying one component from a set of components.")
public class

JTabbedPane

extends

JComponent

implements

Serializable

,

Accessible

,

SwingConstants

A component that lets the user switch between a group of components by
clicking on a tab with a given title and/or icon.
For examples and information on using tabbed panes see

How to Use Tabbed Panes

,
a section in

The Java Tutorial

.

Tabs/components are added to a

TabbedPane

object by using the

addTab

and

insertTab

methods.
A tab is represented by an index corresponding
to the position it was added in, where the first tab has an index equal to 0
and the last tab has an index equal to the tab count minus 1.

The

TabbedPane

uses a

SingleSelectionModel

to represent the set
of tab indices and the currently selected index. If the tab count
is greater than 0, then there will always be a selected index, which
by default will be initialized to the first tab. If the tab count is
0, then the selected index will be -1.

The tab title can be rendered by a

Component

.
For example, the following produce similar results:

```java
// In this case the look and feel renders the title for the tab.
tabbedPane.addTab("Tab", myComponent);
// In this case the custom component is responsible for rendering the
// title of the tab.
tabbedPane.addTab(null, myComponent);
tabbedPane.setTabComponentAt(0, new JLabel("Tab"));
```

The latter is typically used when you want a more complex user interaction
that requires custom components on the tab. For example, you could
provide a custom component that animates or one that has widgets for
closing the tab.

If you specify a component for a tab, the

JTabbedPane

will not render any text or icon you have specified for the tab.

Note:

Do not use

setVisible

directly on a tab component to make it visible,
use

setSelectedComponent

or

setSelectedIndex

methods instead.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Tabs/components are added to a

TabbedPane

object by using the

addTab

and

insertTab

methods.
A tab is represented by an index corresponding
to the position it was added in, where the first tab has an index equal to 0
and the last tab has an index equal to the tab count minus 1.

The

TabbedPane

uses a

SingleSelectionModel

to represent the set
of tab indices and the currently selected index. If the tab count
is greater than 0, then there will always be a selected index, which
by default will be initialized to the first tab. If the tab count is
0, then the selected index will be -1.

The tab title can be rendered by a

Component

.
For example, the following produce similar results:

```java
// In this case the look and feel renders the title for the tab.
tabbedPane.addTab("Tab", myComponent);
// In this case the custom component is responsible for rendering the
// title of the tab.
tabbedPane.addTab(null, myComponent);
tabbedPane.setTabComponentAt(0, new JLabel("Tab"));
```

The latter is typically used when you want a more complex user interaction
that requires custom components on the tab. For example, you could
provide a custom component that animates or one that has widgets for
closing the tab.

If you specify a component for a tab, the

JTabbedPane

will not render any text or icon you have specified for the tab.

Note:

Do not use

setVisible

directly on a tab component to make it visible,
use

setSelectedComponent

or

setSelectedIndex

methods instead.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

The

TabbedPane

uses a

SingleSelectionModel

to represent the set
of tab indices and the currently selected index. If the tab count
is greater than 0, then there will always be a selected index, which
by default will be initialized to the first tab. If the tab count is
0, then the selected index will be -1.

The tab title can be rendered by a

Component

.
For example, the following produce similar results:

```java
// In this case the look and feel renders the title for the tab.
tabbedPane.addTab("Tab", myComponent);
// In this case the custom component is responsible for rendering the
// title of the tab.
tabbedPane.addTab(null, myComponent);
tabbedPane.setTabComponentAt(0, new JLabel("Tab"));
```

The latter is typically used when you want a more complex user interaction
that requires custom components on the tab. For example, you could
provide a custom component that animates or one that has widgets for
closing the tab.

If you specify a component for a tab, the

JTabbedPane

will not render any text or icon you have specified for the tab.

Note:

Do not use

setVisible

directly on a tab component to make it visible,
use

setSelectedComponent

or

setSelectedIndex

methods instead.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

The tab title can be rendered by a

Component

.
For example, the following produce similar results:

```java
// In this case the look and feel renders the title for the tab.
tabbedPane.addTab("Tab", myComponent);
// In this case the custom component is responsible for rendering the
// title of the tab.
tabbedPane.addTab(null, myComponent);
tabbedPane.setTabComponentAt(0, new JLabel("Tab"));
```

The latter is typically used when you want a more complex user interaction
that requires custom components on the tab. For example, you could
provide a custom component that animates or one that has widgets for
closing the tab.

If you specify a component for a tab, the

JTabbedPane

will not render any text or icon you have specified for the tab.

Note:

Do not use

setVisible

directly on a tab component to make it visible,
use

setSelectedComponent

or

setSelectedIndex

methods instead.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

// In this case the look and feel renders the title for the tab.
tabbedPane.addTab("Tab", myComponent);
// In this case the custom component is responsible for rendering the
// title of the tab.
tabbedPane.addTab(null, myComponent);
tabbedPane.setTabComponentAt(0, new JLabel("Tab"));

If you specify a component for a tab, the

JTabbedPane

will not render any text or icon you have specified for the tab.

Note:

Do not use

setVisible

directly on a tab component to make it visible,
use

setSelectedComponent

or

setSelectedIndex

methods instead.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Note:

Do not use

setVisible

directly on a tab component to make it visible,
use

setSelectedComponent

or

setSelectedIndex

methods instead.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

JTabbedPane.AccessibleJTabbedPane

This class implements accessibility support for the

JTabbedPane

class.

protected class

JTabbedPane.ModelListener

We pass

ModelChanged

events along to the listeners with
the tabbedpane (instead of the model itself) as the event source.

- Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

ChangeEvent

changeEvent

Only one

ChangeEvent

is needed per

TabPane

instance since the
event's only (read-only) state is the source property.

protected

ChangeListener

changeListener

The

changeListener

is the listener we add to the
model.

protected

SingleSelectionModel

model

The default selection model

static int

SCROLL_TAB_LAYOUT

Tab layout policy for providing a subset of available tabs when all
the tabs will not fit within a single run.

protected int

tabPlacement

Where the tabs are placed.

static int

WRAP_TAB_LAYOUT

The tab layout policy for wrapping tabs in multiple runs when all
tabs will not fit within a single run.

- Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

- Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JTabbedPane

()

Creates an empty

TabbedPane

with a default
tab placement of

JTabbedPane.TOP

.

JTabbedPane

​(int tabPlacement)

Creates an empty

TabbedPane

with the specified tab placement
of either:

JTabbedPane.TOP

,

JTabbedPane.BOTTOM

,

JTabbedPane.LEFT

, or

JTabbedPane.RIGHT

.

JTabbedPane

​(int tabPlacement,
int tabLayoutPolicy)

Creates an empty

TabbedPane

with the specified tab placement
and tab layout policy.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Component

add

​(

Component

component)

Adds a

component

with a tab title defaulting to
the name of the component which is the result of calling

component.getName

.

Component

add

​(

Component

component,
int index)

Adds a

component

at the specified tab index with a tab
title defaulting to the name of the component.

void

add

​(

Component

component,

Object

constraints)

Adds a

component

to the tabbed pane.

void

add

​(

Component

component,

Object

constraints,
int index)

Adds a

component

at the specified tab index.

Component

add

​(

String

title,

Component

component)

Adds a

component

with the specified tab title.

void

addChangeListener

​(

ChangeListener

l)

Adds a

ChangeListener

to this tabbedpane.

void

addTab

​(

String

title,

Component

component)

Adds a

component

represented by a

title

and no icon.

void

addTab

​(

String

title,

Icon

icon,

Component

component)

Adds a

component

represented by a

title

and/or

icon

, either of which can be

null

.

void

addTab

​(

String

title,

Icon

icon,

Component

component,

String

tip)

Adds a

component

and

tip

represented by a

title

and/or

icon

,
either of which can be

null

.

protected

ChangeListener

createChangeListener

()

Subclasses that want to handle

ChangeEvents

differently
can override this to return a subclass of

ModelListener

or
another

ChangeListener

implementation.

protected void

fireStateChanged

()

Sends a

ChangeEvent

, with this

JTabbedPane

as the source,
to each registered listener.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JTabbedPane.

Color

getBackgroundAt

​(int index)

Returns the tab background color at

index

.

Rectangle

getBoundsAt

​(int index)

Returns the tab bounds at

index

.

ChangeListener

[]

getChangeListeners

()

Returns an array of all the

ChangeListener

s added
to this

JTabbedPane

with

addChangeListener

.

Component

getComponentAt

​(int index)

Returns the component at

index

.

Icon

getDisabledIconAt

​(int index)

Returns the tab disabled icon at

index

.

int

getDisplayedMnemonicIndexAt

​(int tabIndex)

Returns the character, as an index, that the look and feel should
provide decoration for as representing the mnemonic character.

Color

getForegroundAt

​(int index)

Returns the tab foreground color at

index

.

Icon

getIconAt

​(int index)

Returns the tab icon at

index

.

int

getMnemonicAt

​(int tabIndex)

Returns the keyboard mnemonic for accessing the specified tab.

SingleSelectionModel

getModel

()

Returns the model associated with this tabbedpane.

Component

getSelectedComponent

()

Returns the currently selected component for this tabbedpane.

int

getSelectedIndex

()

Returns the currently selected index for this tabbedpane.

Component

getTabComponentAt

​(int index)

Returns the tab component at

index

.

int

getTabCount

()

Returns the number of tabs in this

tabbedpane

.

int

getTabLayoutPolicy

()

Returns the policy used by the tabbedpane to layout the tabs when all the
tabs will not fit within a single run.

int

getTabPlacement

()

Returns the placement of the tabs for this tabbedpane.

int

getTabRunCount

()

Returns the number of tab runs currently used to display
the tabs.

String

getTitleAt

​(int index)

Returns the tab title at

index

.

String

getToolTipText

​(

MouseEvent

event)

Returns the tooltip text for the component determined by the
mouse event location.

String

getToolTipTextAt

​(int index)

Returns the tab tooltip text at

index

.

TabbedPaneUI

getUI

()

Returns the UI object which implements the L&F for this component.

String

getUIClassID

()

Returns the name of the UI class that implements the
L&F for this component.

int

indexAtLocation

​(int x,
int y)

Returns the tab index corresponding to the tab whose bounds
intersect the specified location.

int

indexOfComponent

​(

Component

component)

Returns the index of the tab for the specified component.

int

indexOfTab

​(

String

title)

Returns the first tab index with a given

title

, or
-1 if no tab has this title.

int

indexOfTab

​(

Icon

icon)

Returns the first tab index with a given

icon

,
or -1 if no tab has this icon.

int

indexOfTabComponent

​(

Component

tabComponent)

Returns the index of the tab for the specified tab component.

void

insertTab

​(

String

title,

Icon

icon,

Component

component,

String

tip,
int index)

Inserts a new tab for the given component, at the given index,
represented by the given title and/or icon, either of which may
be

null

.

boolean

isEnabledAt

​(int index)

Returns whether or not the tab at

index

is
currently enabled.

protected

String

paramString

()

Returns a string representation of this

JTabbedPane

.

void

remove

​(int index)

Removes the tab and component which corresponds to the specified index.

void

remove

​(

Component

component)

Removes the specified

Component

from the

JTabbedPane

.

void

removeAll

()

Removes all the tabs and their corresponding components
from the

tabbedpane

.

void

removeChangeListener

​(

ChangeListener

l)

Removes a

ChangeListener

from this tabbedpane.

void

removeTabAt

​(int index)

Removes the tab at

index

.

void

setBackgroundAt

​(int index,

Color

background)

Sets the background color at

index

to

background

which can be

null

, in which case the tab's background color
will default to the background color of the

tabbedpane

.

void

setComponentAt

​(int index,

Component

component)

Sets the component at

index

to

component

.

void

setDisabledIconAt

​(int index,

Icon

disabledIcon)

Sets the disabled icon at

index

to

icon

which can be

null

.

void

setDisplayedMnemonicIndexAt

​(int tabIndex,
int mnemonicIndex)

Provides a hint to the look and feel as to which character in the
text should be decorated to represent the mnemonic.

void

setEnabledAt

​(int index,
boolean enabled)

Sets whether or not the tab at

index

is enabled.

void

setForegroundAt

​(int index,

Color

foreground)

Sets the foreground color at

index

to

foreground

which can be

null

, in which case the tab's foreground color
will default to the foreground color of this

tabbedpane

.

void

setIconAt

​(int index,

Icon

icon)

Sets the icon at

index

to

icon

which can be

null

.

void

setMnemonicAt

​(int tabIndex,
int mnemonic)

Sets the keyboard mnemonic for accessing the specified tab.

void

setModel

​(

SingleSelectionModel

model)

Sets the model to be used with this tabbedpane.

void

setSelectedComponent

​(

Component

c)

Sets the selected component for this tabbedpane.

void

setSelectedIndex

​(int index)

Sets the selected index for this tabbedpane.

void

setTabComponentAt

​(int index,

Component

component)

Sets the component that is responsible for rendering the
title for the specified tab.

void

setTabLayoutPolicy

​(int tabLayoutPolicy)

Sets the policy which the tabbedpane will use in laying out the tabs
when all the tabs will not fit within a single run.

void

setTabPlacement

​(int tabPlacement)

Sets the tab placement for this tabbedpane.

void

setTitleAt

​(int index,

String

title)

Sets the title at

index

to

title

which
can be

null

.

void

setToolTipTextAt

​(int index,

String

toolTipText)

Sets the tooltip text at

index

to

toolTipText

which can be

null

.

void

setUI

​(

TabbedPaneUI

ui)

Sets the UI object which implements the L&F for this component.

void

updateUI

()

Resets the UI property to a value from the current look and feel.

- Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paint

,

paintBorder

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

- Methods declared in class java.awt.

Container

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

JTabbedPane.AccessibleJTabbedPane

This class implements accessibility support for the

JTabbedPane

class.

protected class

JTabbedPane.ModelListener

We pass

ModelChanged

events along to the listeners with
the tabbedpane (instead of the model itself) as the event source.

- Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested Class Summary

This class implements accessibility support for the

JTabbedPane

class.

We pass

ModelChanged

events along to the listeners with
the tabbedpane (instead of the model itself) as the event source.

Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

---

#### Nested classes/interfaces declared in class javax.swing. JComponent

Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

---

#### Nested classes/interfaces declared in class java.awt. Container

Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested classes/interfaces declared in class java.awt. Component

Field Summary

Fields

Modifier and Type

Field

Description

protected

ChangeEvent

changeEvent

Only one

ChangeEvent

is needed per

TabPane

instance since the
event's only (read-only) state is the source property.

protected

ChangeListener

changeListener

The

changeListener

is the listener we add to the
model.

protected

SingleSelectionModel

model

The default selection model

static int

SCROLL_TAB_LAYOUT

Tab layout policy for providing a subset of available tabs when all
the tabs will not fit within a single run.

protected int

tabPlacement

Where the tabs are placed.

static int

WRAP_TAB_LAYOUT

The tab layout policy for wrapping tabs in multiple runs when all
tabs will not fit within a single run.

- Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

- Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

---

#### Field Summary

Only one

ChangeEvent

is needed per

TabPane

instance since the
event's only (read-only) state is the source property.

The

changeListener

is the listener we add to the
model.

The default selection model

Tab layout policy for providing a subset of available tabs when all
the tabs will not fit within a single run.

Where the tabs are placed.

The tab layout policy for wrapping tabs in multiple runs when all
tabs will not fit within a single run.

Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

---

#### Fields declared in class javax.swing. JComponent

Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

---

#### Fields declared in class java.awt. Component

Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

---

#### Fields declared in interface java.awt.image. ImageObserver

Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

---

#### Fields declared in interface javax.swing. SwingConstants

Constructor Summary

Constructors

Constructor

Description

JTabbedPane

()

Creates an empty

TabbedPane

with a default
tab placement of

JTabbedPane.TOP

.

JTabbedPane

​(int tabPlacement)

Creates an empty

TabbedPane

with the specified tab placement
of either:

JTabbedPane.TOP

,

JTabbedPane.BOTTOM

,

JTabbedPane.LEFT

, or

JTabbedPane.RIGHT

.

JTabbedPane

​(int tabPlacement,
int tabLayoutPolicy)

Creates an empty

TabbedPane

with the specified tab placement
and tab layout policy.

---

#### Constructor Summary

Creates an empty

TabbedPane

with a default
tab placement of

JTabbedPane.TOP

.

Creates an empty

TabbedPane

with the specified tab placement
of either:

JTabbedPane.TOP

,

JTabbedPane.BOTTOM

,

JTabbedPane.LEFT

, or

JTabbedPane.RIGHT

.

Creates an empty

TabbedPane

with the specified tab placement
and tab layout policy.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Component

add

​(

Component

component)

Adds a

component

with a tab title defaulting to
the name of the component which is the result of calling

component.getName

.

Component

add

​(

Component

component,
int index)

Adds a

component

at the specified tab index with a tab
title defaulting to the name of the component.

void

add

​(

Component

component,

Object

constraints)

Adds a

component

to the tabbed pane.

void

add

​(

Component

component,

Object

constraints,
int index)

Adds a

component

at the specified tab index.

Component

add

​(

String

title,

Component

component)

Adds a

component

with the specified tab title.

void

addChangeListener

​(

ChangeListener

l)

Adds a

ChangeListener

to this tabbedpane.

void

addTab

​(

String

title,

Component

component)

Adds a

component

represented by a

title

and no icon.

void

addTab

​(

String

title,

Icon

icon,

Component

component)

Adds a

component

represented by a

title

and/or

icon

, either of which can be

null

.

void

addTab

​(

String

title,

Icon

icon,

Component

component,

String

tip)

Adds a

component

and

tip

represented by a

title

and/or

icon

,
either of which can be

null

.

protected

ChangeListener

createChangeListener

()

Subclasses that want to handle

ChangeEvents

differently
can override this to return a subclass of

ModelListener

or
another

ChangeListener

implementation.

protected void

fireStateChanged

()

Sends a

ChangeEvent

, with this

JTabbedPane

as the source,
to each registered listener.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JTabbedPane.

Color

getBackgroundAt

​(int index)

Returns the tab background color at

index

.

Rectangle

getBoundsAt

​(int index)

Returns the tab bounds at

index

.

ChangeListener

[]

getChangeListeners

()

Returns an array of all the

ChangeListener

s added
to this

JTabbedPane

with

addChangeListener

.

Component

getComponentAt

​(int index)

Returns the component at

index

.

Icon

getDisabledIconAt

​(int index)

Returns the tab disabled icon at

index

.

int

getDisplayedMnemonicIndexAt

​(int tabIndex)

Returns the character, as an index, that the look and feel should
provide decoration for as representing the mnemonic character.

Color

getForegroundAt

​(int index)

Returns the tab foreground color at

index

.

Icon

getIconAt

​(int index)

Returns the tab icon at

index

.

int

getMnemonicAt

​(int tabIndex)

Returns the keyboard mnemonic for accessing the specified tab.

SingleSelectionModel

getModel

()

Returns the model associated with this tabbedpane.

Component

getSelectedComponent

()

Returns the currently selected component for this tabbedpane.

int

getSelectedIndex

()

Returns the currently selected index for this tabbedpane.

Component

getTabComponentAt

​(int index)

Returns the tab component at

index

.

int

getTabCount

()

Returns the number of tabs in this

tabbedpane

.

int

getTabLayoutPolicy

()

Returns the policy used by the tabbedpane to layout the tabs when all the
tabs will not fit within a single run.

int

getTabPlacement

()

Returns the placement of the tabs for this tabbedpane.

int

getTabRunCount

()

Returns the number of tab runs currently used to display
the tabs.

String

getTitleAt

​(int index)

Returns the tab title at

index

.

String

getToolTipText

​(

MouseEvent

event)

Returns the tooltip text for the component determined by the
mouse event location.

String

getToolTipTextAt

​(int index)

Returns the tab tooltip text at

index

.

TabbedPaneUI

getUI

()

Returns the UI object which implements the L&F for this component.

String

getUIClassID

()

Returns the name of the UI class that implements the
L&F for this component.

int

indexAtLocation

​(int x,
int y)

Returns the tab index corresponding to the tab whose bounds
intersect the specified location.

int

indexOfComponent

​(

Component

component)

Returns the index of the tab for the specified component.

int

indexOfTab

​(

String

title)

Returns the first tab index with a given

title

, or
-1 if no tab has this title.

int

indexOfTab

​(

Icon

icon)

Returns the first tab index with a given

icon

,
or -1 if no tab has this icon.

int

indexOfTabComponent

​(

Component

tabComponent)

Returns the index of the tab for the specified tab component.

void

insertTab

​(

String

title,

Icon

icon,

Component

component,

String

tip,
int index)

Inserts a new tab for the given component, at the given index,
represented by the given title and/or icon, either of which may
be

null

.

boolean

isEnabledAt

​(int index)

Returns whether or not the tab at

index

is
currently enabled.

protected

String

paramString

()

Returns a string representation of this

JTabbedPane

.

void

remove

​(int index)

Removes the tab and component which corresponds to the specified index.

void

remove

​(

Component

component)

Removes the specified

Component

from the

JTabbedPane

.

void

removeAll

()

Removes all the tabs and their corresponding components
from the

tabbedpane

.

void

removeChangeListener

​(

ChangeListener

l)

Removes a

ChangeListener

from this tabbedpane.

void

removeTabAt

​(int index)

Removes the tab at

index

.

void

setBackgroundAt

​(int index,

Color

background)

Sets the background color at

index

to

background

which can be

null

, in which case the tab's background color
will default to the background color of the

tabbedpane

.

void

setComponentAt

​(int index,

Component

component)

Sets the component at

index

to

component

.

void

setDisabledIconAt

​(int index,

Icon

disabledIcon)

Sets the disabled icon at

index

to

icon

which can be

null

.

void

setDisplayedMnemonicIndexAt

​(int tabIndex,
int mnemonicIndex)

Provides a hint to the look and feel as to which character in the
text should be decorated to represent the mnemonic.

void

setEnabledAt

​(int index,
boolean enabled)

Sets whether or not the tab at

index

is enabled.

void

setForegroundAt

​(int index,

Color

foreground)

Sets the foreground color at

index

to

foreground

which can be

null

, in which case the tab's foreground color
will default to the foreground color of this

tabbedpane

.

void

setIconAt

​(int index,

Icon

icon)

Sets the icon at

index

to

icon

which can be

null

.

void

setMnemonicAt

​(int tabIndex,
int mnemonic)

Sets the keyboard mnemonic for accessing the specified tab.

void

setModel

​(

SingleSelectionModel

model)

Sets the model to be used with this tabbedpane.

void

setSelectedComponent

​(

Component

c)

Sets the selected component for this tabbedpane.

void

setSelectedIndex

​(int index)

Sets the selected index for this tabbedpane.

void

setTabComponentAt

​(int index,

Component

component)

Sets the component that is responsible for rendering the
title for the specified tab.

void

setTabLayoutPolicy

​(int tabLayoutPolicy)

Sets the policy which the tabbedpane will use in laying out the tabs
when all the tabs will not fit within a single run.

void

setTabPlacement

​(int tabPlacement)

Sets the tab placement for this tabbedpane.

void

setTitleAt

​(int index,

String

title)

Sets the title at

index

to

title

which
can be

null

.

void

setToolTipTextAt

​(int index,

String

toolTipText)

Sets the tooltip text at

index

to

toolTipText

which can be

null

.

void

setUI

​(

TabbedPaneUI

ui)

Sets the UI object which implements the L&F for this component.

void

updateUI

()

Resets the UI property to a value from the current look and feel.

- Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paint

,

paintBorder

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

- Methods declared in class java.awt.

Container

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

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

Adds a

component

with a tab title defaulting to
the name of the component which is the result of calling

component.getName

.

Adds a

component

at the specified tab index with a tab
title defaulting to the name of the component.

Adds a

component

to the tabbed pane.

Adds a

component

at the specified tab index.

Adds a

component

with the specified tab title.

Adds a

ChangeListener

to this tabbedpane.

Adds a

component

represented by a

title

and no icon.

Adds a

component

represented by a

title

and/or

icon

, either of which can be

null

.

Adds a

component

and

tip

represented by a

title

and/or

icon

,
either of which can be

null

.

Subclasses that want to handle

ChangeEvents

differently
can override this to return a subclass of

ModelListener

or
another

ChangeListener

implementation.

Sends a

ChangeEvent

, with this

JTabbedPane

as the source,
to each registered listener.

Gets the AccessibleContext associated with this JTabbedPane.

Returns the tab background color at

index

.

Returns the tab bounds at

index

.

Returns an array of all the

ChangeListener

s added
to this

JTabbedPane

with

addChangeListener

.

Returns the component at

index

.

Returns the tab disabled icon at

index

.

Returns the character, as an index, that the look and feel should
provide decoration for as representing the mnemonic character.

Returns the tab foreground color at

index

.

Returns the tab icon at

index

.

Returns the keyboard mnemonic for accessing the specified tab.

Returns the model associated with this tabbedpane.

Returns the currently selected component for this tabbedpane.

Returns the currently selected index for this tabbedpane.

Returns the tab component at

index

.

Returns the number of tabs in this

tabbedpane

.

Returns the policy used by the tabbedpane to layout the tabs when all the
tabs will not fit within a single run.

Returns the placement of the tabs for this tabbedpane.

Returns the number of tab runs currently used to display
the tabs.

Returns the tab title at

index

.

Returns the tooltip text for the component determined by the
mouse event location.

Returns the tab tooltip text at

index

.

Returns the UI object which implements the L&F for this component.

Returns the name of the UI class that implements the
L&F for this component.

Returns the tab index corresponding to the tab whose bounds
intersect the specified location.

Returns the index of the tab for the specified component.

Returns the first tab index with a given

title

, or
-1 if no tab has this title.

Returns the first tab index with a given

icon

,
or -1 if no tab has this icon.

Returns the index of the tab for the specified tab component.

Inserts a new tab for the given component, at the given index,
represented by the given title and/or icon, either of which may
be

null

.

Returns whether or not the tab at

index

is
currently enabled.

Returns a string representation of this

JTabbedPane

.

Removes the tab and component which corresponds to the specified index.

Removes the specified

Component

from the

JTabbedPane

.

Removes all the tabs and their corresponding components
from the

tabbedpane

.

Removes a

ChangeListener

from this tabbedpane.

Removes the tab at

index

.

Sets the background color at

index

to

background

which can be

null

, in which case the tab's background color
will default to the background color of the

tabbedpane

.

Sets the component at

index

to

component

.

Sets the disabled icon at

index

to

icon

which can be

null

.

Provides a hint to the look and feel as to which character in the
text should be decorated to represent the mnemonic.

Sets whether or not the tab at

index

is enabled.

Sets the foreground color at

index

to

foreground

which can be

null

, in which case the tab's foreground color
will default to the foreground color of this

tabbedpane

.

Sets the icon at

index

to

icon

which can be

null

.

Sets the keyboard mnemonic for accessing the specified tab.

Sets the model to be used with this tabbedpane.

Sets the selected component for this tabbedpane.

Sets the selected index for this tabbedpane.

Sets the component that is responsible for rendering the
title for the specified tab.

Sets the policy which the tabbedpane will use in laying out the tabs
when all the tabs will not fit within a single run.

Sets the tab placement for this tabbedpane.

Sets the title at

index

to

title

which
can be

null

.

Sets the tooltip text at

index

to

toolTipText

which can be

null

.

Sets the UI object which implements the L&F for this component.

Resets the UI property to a value from the current look and feel.

Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paint

,

paintBorder

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

---

#### Methods declared in class javax.swing. JComponent

Methods declared in class java.awt.

Container

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

---

#### Methods declared in class java.awt. Container

Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

---

#### Methods declared in class java.awt. Component

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

- WRAP_TAB_LAYOUT

```java
public static final int WRAP_TAB_LAYOUT
```

The tab layout policy for wrapping tabs in multiple runs when all
tabs will not fit within a single run.

**See Also:** Constant Field Values

- SCROLL_TAB_LAYOUT

```java
public static final int SCROLL_TAB_LAYOUT
```

Tab layout policy for providing a subset of available tabs when all
the tabs will not fit within a single run. If all the tabs do
not fit within a single run the look and feel will provide a way
to navigate to hidden tabs.

**See Also:** Constant Field Values

- tabPlacement

```java
protected int tabPlacement
```

Where the tabs are placed.

**See Also:** setTabPlacement(int)

- model

```java
protected
SingleSelectionModel
model
```

The default selection model

- changeListener

```java
protected
ChangeListener
changeListener
```

The

changeListener

is the listener we add to the
model.

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one

ChangeEvent

is needed per

TabPane

instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this".

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JTabbedPane

```java
public JTabbedPane()
```

Creates an empty

TabbedPane

with a default
tab placement of

JTabbedPane.TOP

.

**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

- JTabbedPane

```java
public JTabbedPane​(int tabPlacement)
```

Creates an empty

TabbedPane

with the specified tab placement
of either:

JTabbedPane.TOP

,

JTabbedPane.BOTTOM

,

JTabbedPane.LEFT

, or

JTabbedPane.RIGHT

.

**Parameters:** tabPlacement

- the placement for the tabs relative to the content
**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

- JTabbedPane

```java
public JTabbedPane​(int tabPlacement,
int tabLayoutPolicy)
```

Creates an empty

TabbedPane

with the specified tab placement
and tab layout policy. Tab placement may be either:

JTabbedPane.TOP

,

JTabbedPane.BOTTOM

,

JTabbedPane.LEFT

, or

JTabbedPane.RIGHT

.
Tab layout policy may be either:

JTabbedPane.WRAP_TAB_LAYOUT

or

JTabbedPane.SCROLL_TAB_LAYOUT

.

**Parameters:** tabPlacement

- the placement for the tabs relative to the content
**Parameters:** tabLayoutPolicy

- the policy for laying out tabs when all tabs will not fit on one run
**Throws:** IllegalArgumentException

- if tab placement or tab layout policy are not
one of the above supported values
**Since:** 1.4
**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

============ METHOD DETAIL ==========

- Method Detail

- getUI

```java
public
TabbedPaneUI
getUI()
```

Returns the UI object which implements the L&F for this component.

**Overrides:** getUI

in class

JComponent
**Returns:** a

TabbedPaneUI

object
**See Also:** setUI(javax.swing.plaf.TabbedPaneUI)

- setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the tabbedpane\'s LookAndFeel")
public void setUI​(
TabbedPaneUI
ui)
```

Sets the UI object which implements the L&F for this component.

**Parameters:** ui

- the new UI object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

- updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look and feel.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

- getUIClassID

```java
@BeanProperty
(
bound
=false)
public
String
getUIClassID()
```

Returns the name of the UI class that implements the
L&F for this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "TabbedPaneUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- createChangeListener

```java
protected
ChangeListener
createChangeListener()
```

Subclasses that want to handle

ChangeEvents

differently
can override this to return a subclass of

ModelListener

or
another

ChangeListener

implementation.

**Returns:** a

ChangeListener
**See Also:** fireStateChanged()

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a

ChangeListener

to this tabbedpane.

**Parameters:** l

- the

ChangeListener

to add
**See Also:** fireStateChanged()

,

removeChangeListener(javax.swing.event.ChangeListener)

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a

ChangeListener

from this tabbedpane.

**Parameters:** l

- the

ChangeListener

to remove
**See Also:** fireStateChanged()

,

addChangeListener(javax.swing.event.ChangeListener)

- getChangeListeners

```java
@BeanProperty
(
bound
=false)
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the

ChangeListener

s added
to this

JTabbedPane

with

addChangeListener

.

**Returns:** all of the

ChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- fireStateChanged

```java
protected void fireStateChanged()
```

Sends a

ChangeEvent

, with this

JTabbedPane

as the source,
to each registered listener. This method is called each time there is
a change to either the selected index or the selected tab in the

JTabbedPane

. Usually, the selected index and selected tab change
together. However, there are some cases, such as tab addition, where the
selected index changes and the same tab remains selected. There are other
cases, such as deleting the selected tab, where the index remains the
same, but a new tab moves to that index. Events are fired for all of
these cases.

**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

EventListenerList

- getModel

```java
public
SingleSelectionModel
getModel()
```

Returns the model associated with this tabbedpane.

**Returns:** the

SingleSelectionModel

associated with this tabbedpane
**See Also:** setModel(javax.swing.SingleSelectionModel)

- setModel

```java
@BeanProperty
(
description
="The tabbedpane\'s SingleSelectionModel.")
public void setModel​(
SingleSelectionModel
model)
```

Sets the model to be used with this tabbedpane.

**Parameters:** model

- the model to be used
**See Also:** getModel()

- getTabPlacement

```java
public int getTabPlacement()
```

Returns the placement of the tabs for this tabbedpane.

**Returns:** an

int

specifying the placement for the tabs
**See Also:** setTabPlacement(int)

- setTabPlacement

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

enumerationValues
={"JTabbedPane.TOP","JTabbedPane.LEFT","JTabbedPane.BOTTOM","JTabbedPane.RIGHT"},

description
="The tabbedpane\'s tab placement.")
public void setTabPlacement​(int tabPlacement)
```

Sets the tab placement for this tabbedpane.
Possible values are:

- JTabbedPane.TOP

JTabbedPane.BOTTOM

JTabbedPane.LEFT

JTabbedPane.RIGHT

The default value, if not set, is

SwingConstants.TOP

.

**Parameters:** tabPlacement

- the placement for the tabs relative to the content
**Throws:** IllegalArgumentException

- if tab placement value isn't one
of the above valid values

- getTabLayoutPolicy

```java
public int getTabLayoutPolicy()
```

Returns the policy used by the tabbedpane to layout the tabs when all the
tabs will not fit within a single run.

**Returns:** an

int

specifying the policy used to layout the tabs
**Since:** 1.4
**See Also:** setTabLayoutPolicy(int)

- setTabLayoutPolicy

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

enumerationValues
={"JTabbedPane.WRAP_TAB_LAYOUT","JTabbedPane.SCROLL_TAB_LAYOUT"},

description
="The tabbedpane\'s policy for laying out the tabs")
public void setTabLayoutPolicy​(int tabLayoutPolicy)
```

Sets the policy which the tabbedpane will use in laying out the tabs
when all the tabs will not fit within a single run.
Possible values are:

- JTabbedPane.WRAP_TAB_LAYOUT

JTabbedPane.SCROLL_TAB_LAYOUT

The default value, if not set by the UI, is

JTabbedPane.WRAP_TAB_LAYOUT

.

Some look and feels might only support a subset of the possible
layout policies, in which case the value of this property may be
ignored.

**Parameters:** tabLayoutPolicy

- the policy used to layout the tabs
**Throws:** IllegalArgumentException

- if layoutPolicy value isn't one
of the above valid values
**Since:** 1.4
**See Also:** getTabLayoutPolicy()

- getSelectedIndex

```java
public int getSelectedIndex()
```

Returns the currently selected index for this tabbedpane.
Returns -1 if there is no currently selected tab.

**Returns:** the index of the selected tab
**See Also:** setSelectedIndex(int)

- setSelectedIndex

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The tabbedpane\'s selected tab index.")
public void setSelectedIndex​(int index)
```

Sets the selected index for this tabbedpane. The index must be
a valid tab index or -1, which indicates that no tab should be selected
(can also be used when there are no tabs in the tabbedpane). If a -1
value is specified when the tabbedpane contains one or more tabs, then
the results will be implementation defined.

**Parameters:** index

- the index to be selected
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < -1 || index >= tab count)
**See Also:** getSelectedIndex()

,

SingleSelectionModel.setSelectedIndex(int)

- getSelectedComponent

```java
public
Component
getSelectedComponent()
```

Returns the currently selected component for this tabbedpane.
Returns

null

if there is no currently selected tab.

**Returns:** the component corresponding to the selected tab
**See Also:** setSelectedComponent(java.awt.Component)

- setSelectedComponent

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The tabbedpane\'s selected component.")
public void setSelectedComponent​(
Component
c)
```

Sets the selected component for this tabbedpane. This
will automatically set the

selectedIndex

to the index
corresponding to the specified component.

**Parameters:** c

- the selected

Component

for this

TabbedPane
**Throws:** IllegalArgumentException

- if component not found in tabbed
pane
**See Also:** getSelectedComponent()

- insertTab

```java
public void insertTab​(
String
title,

Icon
icon,

Component
component,

String
tip,
int index)
```

Inserts a new tab for the given component, at the given index,
represented by the given title and/or icon, either of which may
be

null

.

**Parameters:** title

- the title to be displayed on the tab
**Parameters:** icon

- the icon to be displayed on the tab
**Parameters:** component

- the component to be displayed when this tab is clicked.
**Parameters:** tip

- the tooltip to be displayed for this tab
**Parameters:** index

- the position to insert this new tab
(

> 0 and <= getTabCount()

)
**Throws:** IndexOutOfBoundsException

- if the index is out of range
(

< 0 or > getTabCount()

)
**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

,

removeTabAt(int)

- addTab

```java
public void addTab​(
String
title,

Icon
icon,

Component
component,

String
tip)
```

Adds a

component

and

tip

represented by a

title

and/or

icon

,
either of which can be

null

.
Cover method for

insertTab

.

**Parameters:** title

- the title to be displayed in this tab
**Parameters:** icon

- the icon to be displayed in this tab
**Parameters:** component

- the component to be displayed when this tab is clicked
**Parameters:** tip

- the tooltip to be displayed for this tab
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

- addTab

```java
public void addTab​(
String
title,

Icon
icon,

Component
component)
```

Adds a

component

represented by a

title

and/or

icon

, either of which can be

null

.
Cover method for

insertTab

.

**Parameters:** title

- the title to be displayed in this tab
**Parameters:** icon

- the icon to be displayed in this tab
**Parameters:** component

- the component to be displayed when this tab is clicked
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

- addTab

```java
public void addTab​(
String
title,

Component
component)
```

Adds a

component

represented by a

title

and no icon.
Cover method for

insertTab

.

**Parameters:** title

- the title to be displayed in this tab
**Parameters:** component

- the component to be displayed when this tab is clicked
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

- add

```java
public
Component
add​(
Component
component)
```

Adds a

component

with a tab title defaulting to
the name of the component which is the result of calling

component.getName

.
Cover method for

insertTab

.

**Overrides:** add

in class

Container
**Parameters:** component

- the component to be displayed when this tab is clicked
**Returns:** the component
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

- add

```java
public
Component
add​(
String
title,

Component
component)
```

Adds a

component

with the specified tab title.
Cover method for

insertTab

.

**Overrides:** add

in class

Container
**Parameters:** title

- the title to be displayed in this tab
**Parameters:** component

- the component to be displayed when this tab is clicked
**Returns:** the component
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

- add

```java
public
Component
add​(
Component
component,
int index)
```

Adds a

component

at the specified tab index with a tab
title defaulting to the name of the component.
Cover method for

insertTab

.

**Overrides:** add

in class

Container
**Parameters:** component

- the component to be displayed when this tab is clicked
**Parameters:** index

- the position to insert this new tab
**Returns:** the component
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

- add

```java
public void add​(
Component
component,

Object
constraints)
```

Adds a

component

to the tabbed pane.
If

constraints

is a

String

or an

Icon

, it will be used for the tab title,
otherwise the component's name will be used as the tab title.
Cover method for

insertTab

.

**Overrides:** add

in class

Container
**Parameters:** component

- the component to be displayed when this tab is clicked
**Parameters:** constraints

- the object to be displayed in the tab
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

- add

```java
public void add​(
Component
component,

Object
constraints,
int index)
```

Adds a

component

at the specified tab index.
If

constraints

is a

String

or an

Icon

, it will be used for the tab title,
otherwise the component's name will be used as the tab title.
Cover method for

insertTab

.

**Overrides:** add

in class

Container
**Parameters:** component

- the component to be displayed when this tab is clicked
**Parameters:** constraints

- the object to be displayed in the tab
**Parameters:** index

- the position to insert this new tab
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

- removeTabAt

```java
public void removeTabAt​(int index)
```

Removes the tab at

index

.
After the component associated with

index

is removed,
its visibility is reset to true to ensure it will be visible
if added to other containers.

**Parameters:** index

- the index of the tab to be removed
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

,

insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

- remove

```java
public void remove​(
Component
component)
```

Removes the specified

Component

from the

JTabbedPane

. The method does nothing
if the

component

is null.

**Overrides:** remove

in class

Container
**Parameters:** component

- the component to remove from the tabbedpane
**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

,

removeTabAt(int)

- remove

```java
public void remove​(int index)
```

Removes the tab and component which corresponds to the specified index.

**Overrides:** remove

in class

Container
**Parameters:** index

- the index of the component to remove from the

tabbedpane
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

,

removeTabAt(int)

- removeAll

```java
public void removeAll()
```

Removes all the tabs and their corresponding components
from the

tabbedpane

.

**Overrides:** removeAll

in class

Container
**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

,

removeTabAt(int)

- getTabCount

```java
@BeanProperty
(
bound
=false)
public int getTabCount()
```

Returns the number of tabs in this

tabbedpane

.

**Returns:** an integer specifying the number of tabbed pages

- getTabRunCount

```java
@BeanProperty
(
bound
=false)
public int getTabRunCount()
```

Returns the number of tab runs currently used to display
the tabs.

**Returns:** an integer giving the number of rows if the

tabPlacement

is

TOP

or

BOTTOM

and the number of columns if

tabPlacement

is

LEFT

or

RIGHT

,
or 0 if there is no UI set on this

tabbedpane

- getTitleAt

```java
public
String
getTitleAt​(int index)
```

Returns the tab title at

index

.

**Parameters:** index

- the index of the item being queried
**Returns:** the title at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setTitleAt(int, java.lang.String)

- getIconAt

```java
public
Icon
getIconAt​(int index)
```

Returns the tab icon at

index

.

**Parameters:** index

- the index of the item being queried
**Returns:** the icon at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setIconAt(int, javax.swing.Icon)

- getDisabledIconAt

```java
public
Icon
getDisabledIconAt​(int index)
```

Returns the tab disabled icon at

index

.
If the tab disabled icon doesn't exist at

index

this will forward the call to the look and feel to construct
an appropriate disabled Icon from the corresponding enabled
Icon. Some look and feels might not render the disabled Icon,
in which case it won't be created.

**Parameters:** index

- the index of the item being queried
**Returns:** the icon at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setDisabledIconAt(int, javax.swing.Icon)

- getToolTipTextAt

```java
public
String
getToolTipTextAt​(int index)
```

Returns the tab tooltip text at

index

.

**Parameters:** index

- the index of the item being queried
**Returns:** a string containing the tool tip text at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**Since:** 1.3
**See Also:** setToolTipTextAt(int, java.lang.String)

- getBackgroundAt

```java
public
Color
getBackgroundAt​(int index)
```

Returns the tab background color at

index

.

**Parameters:** index

- the index of the item being queried
**Returns:** the

Color

of the tab background at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setBackgroundAt(int, java.awt.Color)

- getForegroundAt

```java
public
Color
getForegroundAt​(int index)
```

Returns the tab foreground color at

index

.

**Parameters:** index

- the index of the item being queried
**Returns:** the

Color

of the tab foreground at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setForegroundAt(int, java.awt.Color)

- isEnabledAt

```java
public boolean isEnabledAt​(int index)
```

Returns whether or not the tab at

index

is
currently enabled.

**Parameters:** index

- the index of the item being queried
**Returns:** true if the tab at

index

is enabled;
false otherwise
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setEnabledAt(int, boolean)

- getComponentAt

```java
public
Component
getComponentAt​(int index)
```

Returns the component at

index

.

**Parameters:** index

- the index of the item being queried
**Returns:** the

Component

at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setComponentAt(int, java.awt.Component)

- getMnemonicAt

```java
public int getMnemonicAt​(int tabIndex)
```

Returns the keyboard mnemonic for accessing the specified tab.
The mnemonic is the key which when combined with the look and feel's
mouseless modifier (usually Alt) will activate the specified
tab.

**Parameters:** tabIndex

- the index of the tab that the mnemonic refers to
**Returns:** the key code which represents the mnemonic;
-1 if a mnemonic is not specified for the tab
**Throws:** IndexOutOfBoundsException

- if index is out of range
(

tabIndex

< 0 ||

tabIndex

>= tab count)
**Since:** 1.4
**See Also:** setDisplayedMnemonicIndexAt(int,int)

,

setMnemonicAt(int,int)

- getDisplayedMnemonicIndexAt

```java
public int getDisplayedMnemonicIndexAt​(int tabIndex)
```

Returns the character, as an index, that the look and feel should
provide decoration for as representing the mnemonic character.

**Parameters:** tabIndex

- the index of the tab that the mnemonic refers to
**Returns:** index representing mnemonic character if one exists;
otherwise returns -1
**Throws:** IndexOutOfBoundsException

- if index is out of range
(

tabIndex

< 0 ||

tabIndex

>= tab count)
**Since:** 1.4
**See Also:** setDisplayedMnemonicIndexAt(int,int)

,

setMnemonicAt(int,int)

- getBoundsAt

```java
public
Rectangle
getBoundsAt​(int index)
```

Returns the tab bounds at

index

. If the tab at
this index is not currently visible in the UI, then returns

null

.
If there is no UI set on this

tabbedpane

,
then returns

null

.

**Parameters:** index

- the index to be queried
**Returns:** a

Rectangle

containing the tab bounds at

index

, or

null

if tab at

index

is not currently visible in the UI,
or if there is no UI set on this

tabbedpane
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

- setTitleAt

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The title at the specified tab index.")
public void setTitleAt​(int index,

String
title)
```

Sets the title at

index

to

title

which
can be

null

.
The title is not shown if a tab component for this tab was specified.
An internal exception is raised if there is no tab at that index.

**Parameters:** index

- the tab index where the title should be set
**Parameters:** title

- the title to be displayed in the tab
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** getTitleAt(int)

,

setTabComponentAt(int, java.awt.Component)

- setIconAt

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The icon at the specified tab index.")
public void setIconAt​(int index,

Icon
icon)
```

Sets the icon at

index

to

icon

which can be

null

. This does not set disabled icon at

icon

.
If the new Icon is different than the current Icon and disabled icon
is not explicitly set, the LookAndFeel will be asked to generate a disabled
Icon. To explicitly set disabled icon, use

setDisableIconAt()

.
The icon is not shown if a tab component for this tab was specified.
An internal exception is raised if there is no tab at that index.

**Parameters:** index

- the tab index where the icon should be set
**Parameters:** icon

- the icon to be displayed in the tab
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setDisabledIconAt(int, javax.swing.Icon)

,

getIconAt(int)

,

getDisabledIconAt(int)

,

setTabComponentAt(int, java.awt.Component)

- setDisabledIconAt

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The disabled icon at the specified tab index.")
public void setDisabledIconAt​(int index,

Icon
disabledIcon)
```

Sets the disabled icon at

index

to

icon

which can be

null

.
An internal exception is raised if there is no tab at that index.

**Parameters:** index

- the tab index where the disabled icon should be set
**Parameters:** disabledIcon

- the icon to be displayed in the tab when disabled
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** getDisabledIconAt(int)

- setToolTipTextAt

```java
@BeanProperty
(
preferred
=true,

description
="The tooltip text at the specified tab index.")
public void setToolTipTextAt​(int index,

String
toolTipText)
```

Sets the tooltip text at

index

to

toolTipText

which can be

null

.
An internal exception is raised if there is no tab at that index.

**Parameters:** index

- the tab index where the tooltip text should be set
**Parameters:** toolTipText

- the tooltip text to be displayed for the tab
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**Since:** 1.3
**See Also:** getToolTipTextAt(int)

- setBackgroundAt

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The background color at the specified tab index.")
public void setBackgroundAt​(int index,

Color
background)
```

Sets the background color at

index

to

background

which can be

null

, in which case the tab's background color
will default to the background color of the

tabbedpane

.
An internal exception is raised if there is no tab at that index.

It is up to the look and feel to honor this property, some may
choose to ignore it.

**Parameters:** index

- the tab index where the background should be set
**Parameters:** background

- the color to be displayed in the tab's background
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** getBackgroundAt(int)

- setForegroundAt

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The foreground color at the specified tab index.")
public void setForegroundAt​(int index,

Color
foreground)
```

Sets the foreground color at

index

to

foreground

which can be

null

, in which case the tab's foreground color
will default to the foreground color of this

tabbedpane

.
An internal exception is raised if there is no tab at that index.

It is up to the look and feel to honor this property, some may
choose to ignore it.

**Parameters:** index

- the tab index where the foreground should be set
**Parameters:** foreground

- the color to be displayed as the tab's foreground
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** getForegroundAt(int)

- setEnabledAt

```java
public void setEnabledAt​(int index,
boolean enabled)
```

Sets whether or not the tab at

index

is enabled.
An internal exception is raised if there is no tab at that index.

**Parameters:** index

- the tab index which should be enabled/disabled
**Parameters:** enabled

- whether or not the tab should be enabled
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** isEnabledAt(int)

- setComponentAt

```java
@BeanProperty
(
visualUpdate
=true,

description
="The component at the specified tab index.")
public void setComponentAt​(int index,

Component
component)
```

Sets the component at

index

to

component

.
An internal exception is raised if there is no tab at that index.

**Parameters:** index

- the tab index where this component is being placed
**Parameters:** component

- the component for the tab
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** getComponentAt(int)

- setDisplayedMnemonicIndexAt

```java
@BeanProperty
(
visualUpdate
=true,

description
="the index into the String to draw the keyboard character mnemonic at")
public void setDisplayedMnemonicIndexAt​(int tabIndex,
int mnemonicIndex)
```

Provides a hint to the look and feel as to which character in the
text should be decorated to represent the mnemonic. Not all look and
feels may support this. A value of -1 indicates either there is
no mnemonic for this tab, or you do not wish the mnemonic to be
displayed for this tab.

The value of this is updated as the properties relating to the
mnemonic change (such as the mnemonic itself, the text...).
You should only ever have to call this if
you do not wish the default character to be underlined. For example, if
the text at tab index 3 was 'Apple Price', with a mnemonic of 'p',
and you wanted the 'P'
to be decorated, as 'Apple

P

rice', you would have to invoke

setDisplayedMnemonicIndex(3, 6)

after invoking

setMnemonicAt(3, KeyEvent.VK_P)

.

Note that it is the programmer's responsibility to ensure
that each tab has a unique mnemonic or unpredictable results may
occur.

**Parameters:** tabIndex

- the index of the tab that the mnemonic refers to
**Parameters:** mnemonicIndex

- index into the

String

to underline
**Throws:** IndexOutOfBoundsException

- if

tabIndex

is
out of range (

tabIndex < 0 || tabIndex >= tab
count

)
**Throws:** IllegalArgumentException

- will be thrown if

mnemonicIndex

is >= length of the tab
title , or < -1
**Since:** 1.4
**See Also:** setMnemonicAt(int,int)

,

getDisplayedMnemonicIndexAt(int)

- setMnemonicAt

```java
@BeanProperty
(
visualUpdate
=true,

description
="The keyboard mnenmonic, as a KeyEvent VK constant, for the specified tab")
public void setMnemonicAt​(int tabIndex,
int mnemonic)
```

Sets the keyboard mnemonic for accessing the specified tab.
The mnemonic is the key which when combined with the look and feel's
mouseless modifier (usually Alt) will activate the specified
tab.

A mnemonic must correspond to a single key on the keyboard
and should be specified using one of the

VK_XXX

keycodes defined in

java.awt.event.KeyEvent

or one of the extended keycodes obtained through

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.
Mnemonics are case-insensitive, therefore a key event
with the corresponding keycode would cause the button to be
activated whether or not the Shift modifier was pressed.

This will update the displayed mnemonic property for the specified
tab.

**Parameters:** tabIndex

- the index of the tab that the mnemonic refers to
**Parameters:** mnemonic

- the key code which represents the mnemonic
**Throws:** IndexOutOfBoundsException

- if

tabIndex

is out
of range (

tabIndex < 0 || tabIndex >= tab count

)
**Since:** 1.4
**See Also:** getMnemonicAt(int)

,

setDisplayedMnemonicIndexAt(int,int)

- indexOfTab

```java
public int indexOfTab​(
String
title)
```

Returns the first tab index with a given

title

, or
-1 if no tab has this title.

**Parameters:** title

- the title for the tab
**Returns:** the first tab index which matches

title

, or
-1 if no tab has this title

- indexOfTab

```java
public int indexOfTab​(
Icon
icon)
```

Returns the first tab index with a given

icon

,
or -1 if no tab has this icon.

**Parameters:** icon

- the icon for the tab
**Returns:** the first tab index which matches

icon

,
or -1 if no tab has this icon

- indexOfComponent

```java
public int indexOfComponent​(
Component
component)
```

Returns the index of the tab for the specified component.
Returns -1 if there is no tab for this component.

**Parameters:** component

- the component for the tab
**Returns:** the first tab which matches this component, or -1
if there is no tab for this component

- indexAtLocation

```java
public int indexAtLocation​(int x,
int y)
```

Returns the tab index corresponding to the tab whose bounds
intersect the specified location. Returns -1 if no tab
intersects the location.

**Parameters:** x

- the x location relative to this tabbedpane
**Parameters:** y

- the y location relative to this tabbedpane
**Returns:** the tab index which intersects the location, or
-1 if no tab intersects the location
**Since:** 1.4

- getToolTipText

```java
public
String
getToolTipText​(
MouseEvent
event)
```

Returns the tooltip text for the component determined by the
mouse event location.

**Overrides:** getToolTipText

in class

JComponent
**Parameters:** event

- the

MouseEvent

that tells where the
cursor is lingering
**Returns:** the

String

containing the tooltip text

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JTabbedPane

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this JTabbedPane.

- getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JTabbedPane.
For tabbed panes, the AccessibleContext takes the form of an
AccessibleJTabbedPane.
A new AccessibleJTabbedPane instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJTabbedPane that serves as the
AccessibleContext of this JTabbedPane

- setTabComponentAt

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The tab component at the specified tab index.")
public void setTabComponentAt​(int index,

Component
component)
```

Sets the component that is responsible for rendering the
title for the specified tab. A null value means

JTabbedPane

will render the title and/or icon for
the specified tab. A non-null value means the component will
render the title and

JTabbedPane

will not render
the title and/or icon.

Note: The component must not be one that the developer has
already added to the tabbed pane.

**Parameters:** index

- the tab index where the component should be set
**Parameters:** component

- the component to render the title for the
specified tab
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**Throws:** IllegalArgumentException

- if component has already been
added to this

JTabbedPane
**Since:** 1.6
**See Also:** getTabComponentAt(int)

- getTabComponentAt

```java
public
Component
getTabComponentAt​(int index)
```

Returns the tab component at

index

.

**Parameters:** index

- the index of the item being queried
**Returns:** the tab component at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**Since:** 1.6
**See Also:** setTabComponentAt(int, java.awt.Component)

- indexOfTabComponent

```java
public int indexOfTabComponent​(
Component
tabComponent)
```

Returns the index of the tab for the specified tab component.
Returns -1 if there is no tab for this tab component.

**Parameters:** tabComponent

- the tab component for the tab
**Returns:** the first tab which matches this tab component, or -1
if there is no tab for this tab component
**Since:** 1.6
**See Also:** setTabComponentAt(int, java.awt.Component)

,

getTabComponentAt(int)

Field Detail

- WRAP_TAB_LAYOUT

```java
public static final int WRAP_TAB_LAYOUT
```

The tab layout policy for wrapping tabs in multiple runs when all
tabs will not fit within a single run.

**See Also:** Constant Field Values

- SCROLL_TAB_LAYOUT

```java
public static final int SCROLL_TAB_LAYOUT
```

Tab layout policy for providing a subset of available tabs when all
the tabs will not fit within a single run. If all the tabs do
not fit within a single run the look and feel will provide a way
to navigate to hidden tabs.

**See Also:** Constant Field Values

- tabPlacement

```java
protected int tabPlacement
```

Where the tabs are placed.

**See Also:** setTabPlacement(int)

- model

```java
protected
SingleSelectionModel
model
```

The default selection model

- changeListener

```java
protected
ChangeListener
changeListener
```

The

changeListener

is the listener we add to the
model.

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one

ChangeEvent

is needed per

TabPane

instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this".

---

#### Field Detail

WRAP_TAB_LAYOUT

```java
public static final int WRAP_TAB_LAYOUT
```

The tab layout policy for wrapping tabs in multiple runs when all
tabs will not fit within a single run.

**See Also:** Constant Field Values

---

#### WRAP_TAB_LAYOUT

public static final int WRAP_TAB_LAYOUT

The tab layout policy for wrapping tabs in multiple runs when all
tabs will not fit within a single run.

SCROLL_TAB_LAYOUT

```java
public static final int SCROLL_TAB_LAYOUT
```

Tab layout policy for providing a subset of available tabs when all
the tabs will not fit within a single run. If all the tabs do
not fit within a single run the look and feel will provide a way
to navigate to hidden tabs.

**See Also:** Constant Field Values

---

#### SCROLL_TAB_LAYOUT

public static final int SCROLL_TAB_LAYOUT

Tab layout policy for providing a subset of available tabs when all
the tabs will not fit within a single run. If all the tabs do
not fit within a single run the look and feel will provide a way
to navigate to hidden tabs.

tabPlacement

```java
protected int tabPlacement
```

Where the tabs are placed.

**See Also:** setTabPlacement(int)

---

#### tabPlacement

protected int tabPlacement

Where the tabs are placed.

model

```java
protected
SingleSelectionModel
model
```

The default selection model

---

#### model

protected

SingleSelectionModel

model

The default selection model

changeListener

```java
protected
ChangeListener
changeListener
```

The

changeListener

is the listener we add to the
model.

---

#### changeListener

protected

ChangeListener

changeListener

The

changeListener

is the listener we add to the
model.

changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one

ChangeEvent

is needed per

TabPane

instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this".

---

#### changeEvent

protected transient

ChangeEvent

changeEvent

Only one

ChangeEvent

is needed per

TabPane

instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this".

Constructor Detail

- JTabbedPane

```java
public JTabbedPane()
```

Creates an empty

TabbedPane

with a default
tab placement of

JTabbedPane.TOP

.

**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

- JTabbedPane

```java
public JTabbedPane​(int tabPlacement)
```

Creates an empty

TabbedPane

with the specified tab placement
of either:

JTabbedPane.TOP

,

JTabbedPane.BOTTOM

,

JTabbedPane.LEFT

, or

JTabbedPane.RIGHT

.

**Parameters:** tabPlacement

- the placement for the tabs relative to the content
**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

- JTabbedPane

```java
public JTabbedPane​(int tabPlacement,
int tabLayoutPolicy)
```

Creates an empty

TabbedPane

with the specified tab placement
and tab layout policy. Tab placement may be either:

JTabbedPane.TOP

,

JTabbedPane.BOTTOM

,

JTabbedPane.LEFT

, or

JTabbedPane.RIGHT

.
Tab layout policy may be either:

JTabbedPane.WRAP_TAB_LAYOUT

or

JTabbedPane.SCROLL_TAB_LAYOUT

.

**Parameters:** tabPlacement

- the placement for the tabs relative to the content
**Parameters:** tabLayoutPolicy

- the policy for laying out tabs when all tabs will not fit on one run
**Throws:** IllegalArgumentException

- if tab placement or tab layout policy are not
one of the above supported values
**Since:** 1.4
**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

---

#### Constructor Detail

JTabbedPane

```java
public JTabbedPane()
```

Creates an empty

TabbedPane

with a default
tab placement of

JTabbedPane.TOP

.

**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

---

#### JTabbedPane

public JTabbedPane()

Creates an empty

TabbedPane

with a default
tab placement of

JTabbedPane.TOP

.

JTabbedPane

```java
public JTabbedPane​(int tabPlacement)
```

Creates an empty

TabbedPane

with the specified tab placement
of either:

JTabbedPane.TOP

,

JTabbedPane.BOTTOM

,

JTabbedPane.LEFT

, or

JTabbedPane.RIGHT

.

**Parameters:** tabPlacement

- the placement for the tabs relative to the content
**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

---

#### JTabbedPane

public JTabbedPane​(int tabPlacement)

Creates an empty

TabbedPane

with the specified tab placement
of either:

JTabbedPane.TOP

,

JTabbedPane.BOTTOM

,

JTabbedPane.LEFT

, or

JTabbedPane.RIGHT

.

JTabbedPane

```java
public JTabbedPane​(int tabPlacement,
int tabLayoutPolicy)
```

Creates an empty

TabbedPane

with the specified tab placement
and tab layout policy. Tab placement may be either:

JTabbedPane.TOP

,

JTabbedPane.BOTTOM

,

JTabbedPane.LEFT

, or

JTabbedPane.RIGHT

.
Tab layout policy may be either:

JTabbedPane.WRAP_TAB_LAYOUT

or

JTabbedPane.SCROLL_TAB_LAYOUT

.

**Parameters:** tabPlacement

- the placement for the tabs relative to the content
**Parameters:** tabLayoutPolicy

- the policy for laying out tabs when all tabs will not fit on one run
**Throws:** IllegalArgumentException

- if tab placement or tab layout policy are not
one of the above supported values
**Since:** 1.4
**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

---

#### JTabbedPane

public JTabbedPane​(int tabPlacement,
int tabLayoutPolicy)

Creates an empty

TabbedPane

with the specified tab placement
and tab layout policy. Tab placement may be either:

JTabbedPane.TOP

,

JTabbedPane.BOTTOM

,

JTabbedPane.LEFT

, or

JTabbedPane.RIGHT

.
Tab layout policy may be either:

JTabbedPane.WRAP_TAB_LAYOUT

or

JTabbedPane.SCROLL_TAB_LAYOUT

.

Method Detail

- getUI

```java
public
TabbedPaneUI
getUI()
```

Returns the UI object which implements the L&F for this component.

**Overrides:** getUI

in class

JComponent
**Returns:** a

TabbedPaneUI

object
**See Also:** setUI(javax.swing.plaf.TabbedPaneUI)

- setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the tabbedpane\'s LookAndFeel")
public void setUI​(
TabbedPaneUI
ui)
```

Sets the UI object which implements the L&F for this component.

**Parameters:** ui

- the new UI object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

- updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look and feel.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

- getUIClassID

```java
@BeanProperty
(
bound
=false)
public
String
getUIClassID()
```

Returns the name of the UI class that implements the
L&F for this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "TabbedPaneUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- createChangeListener

```java
protected
ChangeListener
createChangeListener()
```

Subclasses that want to handle

ChangeEvents

differently
can override this to return a subclass of

ModelListener

or
another

ChangeListener

implementation.

**Returns:** a

ChangeListener
**See Also:** fireStateChanged()

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a

ChangeListener

to this tabbedpane.

**Parameters:** l

- the

ChangeListener

to add
**See Also:** fireStateChanged()

,

removeChangeListener(javax.swing.event.ChangeListener)

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a

ChangeListener

from this tabbedpane.

**Parameters:** l

- the

ChangeListener

to remove
**See Also:** fireStateChanged()

,

addChangeListener(javax.swing.event.ChangeListener)

- getChangeListeners

```java
@BeanProperty
(
bound
=false)
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the

ChangeListener

s added
to this

JTabbedPane

with

addChangeListener

.

**Returns:** all of the

ChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- fireStateChanged

```java
protected void fireStateChanged()
```

Sends a

ChangeEvent

, with this

JTabbedPane

as the source,
to each registered listener. This method is called each time there is
a change to either the selected index or the selected tab in the

JTabbedPane

. Usually, the selected index and selected tab change
together. However, there are some cases, such as tab addition, where the
selected index changes and the same tab remains selected. There are other
cases, such as deleting the selected tab, where the index remains the
same, but a new tab moves to that index. Events are fired for all of
these cases.

**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

EventListenerList

- getModel

```java
public
SingleSelectionModel
getModel()
```

Returns the model associated with this tabbedpane.

**Returns:** the

SingleSelectionModel

associated with this tabbedpane
**See Also:** setModel(javax.swing.SingleSelectionModel)

- setModel

```java
@BeanProperty
(
description
="The tabbedpane\'s SingleSelectionModel.")
public void setModel​(
SingleSelectionModel
model)
```

Sets the model to be used with this tabbedpane.

**Parameters:** model

- the model to be used
**See Also:** getModel()

- getTabPlacement

```java
public int getTabPlacement()
```

Returns the placement of the tabs for this tabbedpane.

**Returns:** an

int

specifying the placement for the tabs
**See Also:** setTabPlacement(int)

- setTabPlacement

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

enumerationValues
={"JTabbedPane.TOP","JTabbedPane.LEFT","JTabbedPane.BOTTOM","JTabbedPane.RIGHT"},

description
="The tabbedpane\'s tab placement.")
public void setTabPlacement​(int tabPlacement)
```

Sets the tab placement for this tabbedpane.
Possible values are:

- JTabbedPane.TOP

JTabbedPane.BOTTOM

JTabbedPane.LEFT

JTabbedPane.RIGHT

The default value, if not set, is

SwingConstants.TOP

.

**Parameters:** tabPlacement

- the placement for the tabs relative to the content
**Throws:** IllegalArgumentException

- if tab placement value isn't one
of the above valid values

- getTabLayoutPolicy

```java
public int getTabLayoutPolicy()
```

Returns the policy used by the tabbedpane to layout the tabs when all the
tabs will not fit within a single run.

**Returns:** an

int

specifying the policy used to layout the tabs
**Since:** 1.4
**See Also:** setTabLayoutPolicy(int)

- setTabLayoutPolicy

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

enumerationValues
={"JTabbedPane.WRAP_TAB_LAYOUT","JTabbedPane.SCROLL_TAB_LAYOUT"},

description
="The tabbedpane\'s policy for laying out the tabs")
public void setTabLayoutPolicy​(int tabLayoutPolicy)
```

Sets the policy which the tabbedpane will use in laying out the tabs
when all the tabs will not fit within a single run.
Possible values are:

- JTabbedPane.WRAP_TAB_LAYOUT

JTabbedPane.SCROLL_TAB_LAYOUT

The default value, if not set by the UI, is

JTabbedPane.WRAP_TAB_LAYOUT

.

Some look and feels might only support a subset of the possible
layout policies, in which case the value of this property may be
ignored.

**Parameters:** tabLayoutPolicy

- the policy used to layout the tabs
**Throws:** IllegalArgumentException

- if layoutPolicy value isn't one
of the above valid values
**Since:** 1.4
**See Also:** getTabLayoutPolicy()

- getSelectedIndex

```java
public int getSelectedIndex()
```

Returns the currently selected index for this tabbedpane.
Returns -1 if there is no currently selected tab.

**Returns:** the index of the selected tab
**See Also:** setSelectedIndex(int)

- setSelectedIndex

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The tabbedpane\'s selected tab index.")
public void setSelectedIndex​(int index)
```

Sets the selected index for this tabbedpane. The index must be
a valid tab index or -1, which indicates that no tab should be selected
(can also be used when there are no tabs in the tabbedpane). If a -1
value is specified when the tabbedpane contains one or more tabs, then
the results will be implementation defined.

**Parameters:** index

- the index to be selected
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < -1 || index >= tab count)
**See Also:** getSelectedIndex()

,

SingleSelectionModel.setSelectedIndex(int)

- getSelectedComponent

```java
public
Component
getSelectedComponent()
```

Returns the currently selected component for this tabbedpane.
Returns

null

if there is no currently selected tab.

**Returns:** the component corresponding to the selected tab
**See Also:** setSelectedComponent(java.awt.Component)

- setSelectedComponent

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The tabbedpane\'s selected component.")
public void setSelectedComponent​(
Component
c)
```

Sets the selected component for this tabbedpane. This
will automatically set the

selectedIndex

to the index
corresponding to the specified component.

**Parameters:** c

- the selected

Component

for this

TabbedPane
**Throws:** IllegalArgumentException

- if component not found in tabbed
pane
**See Also:** getSelectedComponent()

- insertTab

```java
public void insertTab​(
String
title,

Icon
icon,

Component
component,

String
tip,
int index)
```

Inserts a new tab for the given component, at the given index,
represented by the given title and/or icon, either of which may
be

null

.

**Parameters:** title

- the title to be displayed on the tab
**Parameters:** icon

- the icon to be displayed on the tab
**Parameters:** component

- the component to be displayed when this tab is clicked.
**Parameters:** tip

- the tooltip to be displayed for this tab
**Parameters:** index

- the position to insert this new tab
(

> 0 and <= getTabCount()

)
**Throws:** IndexOutOfBoundsException

- if the index is out of range
(

< 0 or > getTabCount()

)
**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

,

removeTabAt(int)

- addTab

```java
public void addTab​(
String
title,

Icon
icon,

Component
component,

String
tip)
```

Adds a

component

and

tip

represented by a

title

and/or

icon

,
either of which can be

null

.
Cover method for

insertTab

.

**Parameters:** title

- the title to be displayed in this tab
**Parameters:** icon

- the icon to be displayed in this tab
**Parameters:** component

- the component to be displayed when this tab is clicked
**Parameters:** tip

- the tooltip to be displayed for this tab
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

- addTab

```java
public void addTab​(
String
title,

Icon
icon,

Component
component)
```

Adds a

component

represented by a

title

and/or

icon

, either of which can be

null

.
Cover method for

insertTab

.

**Parameters:** title

- the title to be displayed in this tab
**Parameters:** icon

- the icon to be displayed in this tab
**Parameters:** component

- the component to be displayed when this tab is clicked
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

- addTab

```java
public void addTab​(
String
title,

Component
component)
```

Adds a

component

represented by a

title

and no icon.
Cover method for

insertTab

.

**Parameters:** title

- the title to be displayed in this tab
**Parameters:** component

- the component to be displayed when this tab is clicked
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

- add

```java
public
Component
add​(
Component
component)
```

Adds a

component

with a tab title defaulting to
the name of the component which is the result of calling

component.getName

.
Cover method for

insertTab

.

**Overrides:** add

in class

Container
**Parameters:** component

- the component to be displayed when this tab is clicked
**Returns:** the component
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

- add

```java
public
Component
add​(
String
title,

Component
component)
```

Adds a

component

with the specified tab title.
Cover method for

insertTab

.

**Overrides:** add

in class

Container
**Parameters:** title

- the title to be displayed in this tab
**Parameters:** component

- the component to be displayed when this tab is clicked
**Returns:** the component
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

- add

```java
public
Component
add​(
Component
component,
int index)
```

Adds a

component

at the specified tab index with a tab
title defaulting to the name of the component.
Cover method for

insertTab

.

**Overrides:** add

in class

Container
**Parameters:** component

- the component to be displayed when this tab is clicked
**Parameters:** index

- the position to insert this new tab
**Returns:** the component
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

- add

```java
public void add​(
Component
component,

Object
constraints)
```

Adds a

component

to the tabbed pane.
If

constraints

is a

String

or an

Icon

, it will be used for the tab title,
otherwise the component's name will be used as the tab title.
Cover method for

insertTab

.

**Overrides:** add

in class

Container
**Parameters:** component

- the component to be displayed when this tab is clicked
**Parameters:** constraints

- the object to be displayed in the tab
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

- add

```java
public void add​(
Component
component,

Object
constraints,
int index)
```

Adds a

component

at the specified tab index.
If

constraints

is a

String

or an

Icon

, it will be used for the tab title,
otherwise the component's name will be used as the tab title.
Cover method for

insertTab

.

**Overrides:** add

in class

Container
**Parameters:** component

- the component to be displayed when this tab is clicked
**Parameters:** constraints

- the object to be displayed in the tab
**Parameters:** index

- the position to insert this new tab
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

- removeTabAt

```java
public void removeTabAt​(int index)
```

Removes the tab at

index

.
After the component associated with

index

is removed,
its visibility is reset to true to ensure it will be visible
if added to other containers.

**Parameters:** index

- the index of the tab to be removed
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

,

insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

- remove

```java
public void remove​(
Component
component)
```

Removes the specified

Component

from the

JTabbedPane

. The method does nothing
if the

component

is null.

**Overrides:** remove

in class

Container
**Parameters:** component

- the component to remove from the tabbedpane
**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

,

removeTabAt(int)

- remove

```java
public void remove​(int index)
```

Removes the tab and component which corresponds to the specified index.

**Overrides:** remove

in class

Container
**Parameters:** index

- the index of the component to remove from the

tabbedpane
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

,

removeTabAt(int)

- removeAll

```java
public void removeAll()
```

Removes all the tabs and their corresponding components
from the

tabbedpane

.

**Overrides:** removeAll

in class

Container
**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

,

removeTabAt(int)

- getTabCount

```java
@BeanProperty
(
bound
=false)
public int getTabCount()
```

Returns the number of tabs in this

tabbedpane

.

**Returns:** an integer specifying the number of tabbed pages

- getTabRunCount

```java
@BeanProperty
(
bound
=false)
public int getTabRunCount()
```

Returns the number of tab runs currently used to display
the tabs.

**Returns:** an integer giving the number of rows if the

tabPlacement

is

TOP

or

BOTTOM

and the number of columns if

tabPlacement

is

LEFT

or

RIGHT

,
or 0 if there is no UI set on this

tabbedpane

- getTitleAt

```java
public
String
getTitleAt​(int index)
```

Returns the tab title at

index

.

**Parameters:** index

- the index of the item being queried
**Returns:** the title at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setTitleAt(int, java.lang.String)

- getIconAt

```java
public
Icon
getIconAt​(int index)
```

Returns the tab icon at

index

.

**Parameters:** index

- the index of the item being queried
**Returns:** the icon at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setIconAt(int, javax.swing.Icon)

- getDisabledIconAt

```java
public
Icon
getDisabledIconAt​(int index)
```

Returns the tab disabled icon at

index

.
If the tab disabled icon doesn't exist at

index

this will forward the call to the look and feel to construct
an appropriate disabled Icon from the corresponding enabled
Icon. Some look and feels might not render the disabled Icon,
in which case it won't be created.

**Parameters:** index

- the index of the item being queried
**Returns:** the icon at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setDisabledIconAt(int, javax.swing.Icon)

- getToolTipTextAt

```java
public
String
getToolTipTextAt​(int index)
```

Returns the tab tooltip text at

index

.

**Parameters:** index

- the index of the item being queried
**Returns:** a string containing the tool tip text at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**Since:** 1.3
**See Also:** setToolTipTextAt(int, java.lang.String)

- getBackgroundAt

```java
public
Color
getBackgroundAt​(int index)
```

Returns the tab background color at

index

.

**Parameters:** index

- the index of the item being queried
**Returns:** the

Color

of the tab background at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setBackgroundAt(int, java.awt.Color)

- getForegroundAt

```java
public
Color
getForegroundAt​(int index)
```

Returns the tab foreground color at

index

.

**Parameters:** index

- the index of the item being queried
**Returns:** the

Color

of the tab foreground at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setForegroundAt(int, java.awt.Color)

- isEnabledAt

```java
public boolean isEnabledAt​(int index)
```

Returns whether or not the tab at

index

is
currently enabled.

**Parameters:** index

- the index of the item being queried
**Returns:** true if the tab at

index

is enabled;
false otherwise
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setEnabledAt(int, boolean)

- getComponentAt

```java
public
Component
getComponentAt​(int index)
```

Returns the component at

index

.

**Parameters:** index

- the index of the item being queried
**Returns:** the

Component

at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setComponentAt(int, java.awt.Component)

- getMnemonicAt

```java
public int getMnemonicAt​(int tabIndex)
```

Returns the keyboard mnemonic for accessing the specified tab.
The mnemonic is the key which when combined with the look and feel's
mouseless modifier (usually Alt) will activate the specified
tab.

**Parameters:** tabIndex

- the index of the tab that the mnemonic refers to
**Returns:** the key code which represents the mnemonic;
-1 if a mnemonic is not specified for the tab
**Throws:** IndexOutOfBoundsException

- if index is out of range
(

tabIndex

< 0 ||

tabIndex

>= tab count)
**Since:** 1.4
**See Also:** setDisplayedMnemonicIndexAt(int,int)

,

setMnemonicAt(int,int)

- getDisplayedMnemonicIndexAt

```java
public int getDisplayedMnemonicIndexAt​(int tabIndex)
```

Returns the character, as an index, that the look and feel should
provide decoration for as representing the mnemonic character.

**Parameters:** tabIndex

- the index of the tab that the mnemonic refers to
**Returns:** index representing mnemonic character if one exists;
otherwise returns -1
**Throws:** IndexOutOfBoundsException

- if index is out of range
(

tabIndex

< 0 ||

tabIndex

>= tab count)
**Since:** 1.4
**See Also:** setDisplayedMnemonicIndexAt(int,int)

,

setMnemonicAt(int,int)

- getBoundsAt

```java
public
Rectangle
getBoundsAt​(int index)
```

Returns the tab bounds at

index

. If the tab at
this index is not currently visible in the UI, then returns

null

.
If there is no UI set on this

tabbedpane

,
then returns

null

.

**Parameters:** index

- the index to be queried
**Returns:** a

Rectangle

containing the tab bounds at

index

, or

null

if tab at

index

is not currently visible in the UI,
or if there is no UI set on this

tabbedpane
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

- setTitleAt

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The title at the specified tab index.")
public void setTitleAt​(int index,

String
title)
```

Sets the title at

index

to

title

which
can be

null

.
The title is not shown if a tab component for this tab was specified.
An internal exception is raised if there is no tab at that index.

**Parameters:** index

- the tab index where the title should be set
**Parameters:** title

- the title to be displayed in the tab
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** getTitleAt(int)

,

setTabComponentAt(int, java.awt.Component)

- setIconAt

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The icon at the specified tab index.")
public void setIconAt​(int index,

Icon
icon)
```

Sets the icon at

index

to

icon

which can be

null

. This does not set disabled icon at

icon

.
If the new Icon is different than the current Icon and disabled icon
is not explicitly set, the LookAndFeel will be asked to generate a disabled
Icon. To explicitly set disabled icon, use

setDisableIconAt()

.
The icon is not shown if a tab component for this tab was specified.
An internal exception is raised if there is no tab at that index.

**Parameters:** index

- the tab index where the icon should be set
**Parameters:** icon

- the icon to be displayed in the tab
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setDisabledIconAt(int, javax.swing.Icon)

,

getIconAt(int)

,

getDisabledIconAt(int)

,

setTabComponentAt(int, java.awt.Component)

- setDisabledIconAt

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The disabled icon at the specified tab index.")
public void setDisabledIconAt​(int index,

Icon
disabledIcon)
```

Sets the disabled icon at

index

to

icon

which can be

null

.
An internal exception is raised if there is no tab at that index.

**Parameters:** index

- the tab index where the disabled icon should be set
**Parameters:** disabledIcon

- the icon to be displayed in the tab when disabled
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** getDisabledIconAt(int)

- setToolTipTextAt

```java
@BeanProperty
(
preferred
=true,

description
="The tooltip text at the specified tab index.")
public void setToolTipTextAt​(int index,

String
toolTipText)
```

Sets the tooltip text at

index

to

toolTipText

which can be

null

.
An internal exception is raised if there is no tab at that index.

**Parameters:** index

- the tab index where the tooltip text should be set
**Parameters:** toolTipText

- the tooltip text to be displayed for the tab
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**Since:** 1.3
**See Also:** getToolTipTextAt(int)

- setBackgroundAt

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The background color at the specified tab index.")
public void setBackgroundAt​(int index,

Color
background)
```

Sets the background color at

index

to

background

which can be

null

, in which case the tab's background color
will default to the background color of the

tabbedpane

.
An internal exception is raised if there is no tab at that index.

It is up to the look and feel to honor this property, some may
choose to ignore it.

**Parameters:** index

- the tab index where the background should be set
**Parameters:** background

- the color to be displayed in the tab's background
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** getBackgroundAt(int)

- setForegroundAt

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The foreground color at the specified tab index.")
public void setForegroundAt​(int index,

Color
foreground)
```

Sets the foreground color at

index

to

foreground

which can be

null

, in which case the tab's foreground color
will default to the foreground color of this

tabbedpane

.
An internal exception is raised if there is no tab at that index.

It is up to the look and feel to honor this property, some may
choose to ignore it.

**Parameters:** index

- the tab index where the foreground should be set
**Parameters:** foreground

- the color to be displayed as the tab's foreground
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** getForegroundAt(int)

- setEnabledAt

```java
public void setEnabledAt​(int index,
boolean enabled)
```

Sets whether or not the tab at

index

is enabled.
An internal exception is raised if there is no tab at that index.

**Parameters:** index

- the tab index which should be enabled/disabled
**Parameters:** enabled

- whether or not the tab should be enabled
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** isEnabledAt(int)

- setComponentAt

```java
@BeanProperty
(
visualUpdate
=true,

description
="The component at the specified tab index.")
public void setComponentAt​(int index,

Component
component)
```

Sets the component at

index

to

component

.
An internal exception is raised if there is no tab at that index.

**Parameters:** index

- the tab index where this component is being placed
**Parameters:** component

- the component for the tab
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** getComponentAt(int)

- setDisplayedMnemonicIndexAt

```java
@BeanProperty
(
visualUpdate
=true,

description
="the index into the String to draw the keyboard character mnemonic at")
public void setDisplayedMnemonicIndexAt​(int tabIndex,
int mnemonicIndex)
```

Provides a hint to the look and feel as to which character in the
text should be decorated to represent the mnemonic. Not all look and
feels may support this. A value of -1 indicates either there is
no mnemonic for this tab, or you do not wish the mnemonic to be
displayed for this tab.

The value of this is updated as the properties relating to the
mnemonic change (such as the mnemonic itself, the text...).
You should only ever have to call this if
you do not wish the default character to be underlined. For example, if
the text at tab index 3 was 'Apple Price', with a mnemonic of 'p',
and you wanted the 'P'
to be decorated, as 'Apple

P

rice', you would have to invoke

setDisplayedMnemonicIndex(3, 6)

after invoking

setMnemonicAt(3, KeyEvent.VK_P)

.

Note that it is the programmer's responsibility to ensure
that each tab has a unique mnemonic or unpredictable results may
occur.

**Parameters:** tabIndex

- the index of the tab that the mnemonic refers to
**Parameters:** mnemonicIndex

- index into the

String

to underline
**Throws:** IndexOutOfBoundsException

- if

tabIndex

is
out of range (

tabIndex < 0 || tabIndex >= tab
count

)
**Throws:** IllegalArgumentException

- will be thrown if

mnemonicIndex

is >= length of the tab
title , or < -1
**Since:** 1.4
**See Also:** setMnemonicAt(int,int)

,

getDisplayedMnemonicIndexAt(int)

- setMnemonicAt

```java
@BeanProperty
(
visualUpdate
=true,

description
="The keyboard mnenmonic, as a KeyEvent VK constant, for the specified tab")
public void setMnemonicAt​(int tabIndex,
int mnemonic)
```

Sets the keyboard mnemonic for accessing the specified tab.
The mnemonic is the key which when combined with the look and feel's
mouseless modifier (usually Alt) will activate the specified
tab.

A mnemonic must correspond to a single key on the keyboard
and should be specified using one of the

VK_XXX

keycodes defined in

java.awt.event.KeyEvent

or one of the extended keycodes obtained through

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.
Mnemonics are case-insensitive, therefore a key event
with the corresponding keycode would cause the button to be
activated whether or not the Shift modifier was pressed.

This will update the displayed mnemonic property for the specified
tab.

**Parameters:** tabIndex

- the index of the tab that the mnemonic refers to
**Parameters:** mnemonic

- the key code which represents the mnemonic
**Throws:** IndexOutOfBoundsException

- if

tabIndex

is out
of range (

tabIndex < 0 || tabIndex >= tab count

)
**Since:** 1.4
**See Also:** getMnemonicAt(int)

,

setDisplayedMnemonicIndexAt(int,int)

- indexOfTab

```java
public int indexOfTab​(
String
title)
```

Returns the first tab index with a given

title

, or
-1 if no tab has this title.

**Parameters:** title

- the title for the tab
**Returns:** the first tab index which matches

title

, or
-1 if no tab has this title

- indexOfTab

```java
public int indexOfTab​(
Icon
icon)
```

Returns the first tab index with a given

icon

,
or -1 if no tab has this icon.

**Parameters:** icon

- the icon for the tab
**Returns:** the first tab index which matches

icon

,
or -1 if no tab has this icon

- indexOfComponent

```java
public int indexOfComponent​(
Component
component)
```

Returns the index of the tab for the specified component.
Returns -1 if there is no tab for this component.

**Parameters:** component

- the component for the tab
**Returns:** the first tab which matches this component, or -1
if there is no tab for this component

- indexAtLocation

```java
public int indexAtLocation​(int x,
int y)
```

Returns the tab index corresponding to the tab whose bounds
intersect the specified location. Returns -1 if no tab
intersects the location.

**Parameters:** x

- the x location relative to this tabbedpane
**Parameters:** y

- the y location relative to this tabbedpane
**Returns:** the tab index which intersects the location, or
-1 if no tab intersects the location
**Since:** 1.4

- getToolTipText

```java
public
String
getToolTipText​(
MouseEvent
event)
```

Returns the tooltip text for the component determined by the
mouse event location.

**Overrides:** getToolTipText

in class

JComponent
**Parameters:** event

- the

MouseEvent

that tells where the
cursor is lingering
**Returns:** the

String

containing the tooltip text

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JTabbedPane

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this JTabbedPane.

- getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JTabbedPane.
For tabbed panes, the AccessibleContext takes the form of an
AccessibleJTabbedPane.
A new AccessibleJTabbedPane instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJTabbedPane that serves as the
AccessibleContext of this JTabbedPane

- setTabComponentAt

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The tab component at the specified tab index.")
public void setTabComponentAt​(int index,

Component
component)
```

Sets the component that is responsible for rendering the
title for the specified tab. A null value means

JTabbedPane

will render the title and/or icon for
the specified tab. A non-null value means the component will
render the title and

JTabbedPane

will not render
the title and/or icon.

Note: The component must not be one that the developer has
already added to the tabbed pane.

**Parameters:** index

- the tab index where the component should be set
**Parameters:** component

- the component to render the title for the
specified tab
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**Throws:** IllegalArgumentException

- if component has already been
added to this

JTabbedPane
**Since:** 1.6
**See Also:** getTabComponentAt(int)

- getTabComponentAt

```java
public
Component
getTabComponentAt​(int index)
```

Returns the tab component at

index

.

**Parameters:** index

- the index of the item being queried
**Returns:** the tab component at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**Since:** 1.6
**See Also:** setTabComponentAt(int, java.awt.Component)

- indexOfTabComponent

```java
public int indexOfTabComponent​(
Component
tabComponent)
```

Returns the index of the tab for the specified tab component.
Returns -1 if there is no tab for this tab component.

**Parameters:** tabComponent

- the tab component for the tab
**Returns:** the first tab which matches this tab component, or -1
if there is no tab for this tab component
**Since:** 1.6
**See Also:** setTabComponentAt(int, java.awt.Component)

,

getTabComponentAt(int)

---

#### Method Detail

getUI

```java
public
TabbedPaneUI
getUI()
```

Returns the UI object which implements the L&F for this component.

**Overrides:** getUI

in class

JComponent
**Returns:** a

TabbedPaneUI

object
**See Also:** setUI(javax.swing.plaf.TabbedPaneUI)

---

#### getUI

public

TabbedPaneUI

getUI()

Returns the UI object which implements the L&F for this component.

setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the tabbedpane\'s LookAndFeel")
public void setUI​(
TabbedPaneUI
ui)
```

Sets the UI object which implements the L&F for this component.

**Parameters:** ui

- the new UI object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

---

#### setUI

@BeanProperty

(

hidden

=true,

visualUpdate

=true,

description

="The UI object that implements the tabbedpane\'s LookAndFeel")
public void setUI​(

TabbedPaneUI

ui)

Sets the UI object which implements the L&F for this component.

updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look and feel.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

---

#### updateUI

public void updateUI()

Resets the UI property to a value from the current look and feel.

getUIClassID

```java
@BeanProperty
(
bound
=false)
public
String
getUIClassID()
```

Returns the name of the UI class that implements the
L&F for this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "TabbedPaneUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### getUIClassID

@BeanProperty

(

bound

=false)
public

String

getUIClassID()

Returns the name of the UI class that implements the
L&F for this component.

createChangeListener

```java
protected
ChangeListener
createChangeListener()
```

Subclasses that want to handle

ChangeEvents

differently
can override this to return a subclass of

ModelListener

or
another

ChangeListener

implementation.

**Returns:** a

ChangeListener
**See Also:** fireStateChanged()

---

#### createChangeListener

protected

ChangeListener

createChangeListener()

Subclasses that want to handle

ChangeEvents

differently
can override this to return a subclass of

ModelListener

or
another

ChangeListener

implementation.

addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a

ChangeListener

to this tabbedpane.

**Parameters:** l

- the

ChangeListener

to add
**See Also:** fireStateChanged()

,

removeChangeListener(javax.swing.event.ChangeListener)

---

#### addChangeListener

public void addChangeListener​(

ChangeListener

l)

Adds a

ChangeListener

to this tabbedpane.

removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a

ChangeListener

from this tabbedpane.

**Parameters:** l

- the

ChangeListener

to remove
**See Also:** fireStateChanged()

,

addChangeListener(javax.swing.event.ChangeListener)

---

#### removeChangeListener

public void removeChangeListener​(

ChangeListener

l)

Removes a

ChangeListener

from this tabbedpane.

getChangeListeners

```java
@BeanProperty
(
bound
=false)
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the

ChangeListener

s added
to this

JTabbedPane

with

addChangeListener

.

**Returns:** all of the

ChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

---

#### getChangeListeners

@BeanProperty

(

bound

=false)
public

ChangeListener

[] getChangeListeners()

Returns an array of all the

ChangeListener

s added
to this

JTabbedPane

with

addChangeListener

.

fireStateChanged

```java
protected void fireStateChanged()
```

Sends a

ChangeEvent

, with this

JTabbedPane

as the source,
to each registered listener. This method is called each time there is
a change to either the selected index or the selected tab in the

JTabbedPane

. Usually, the selected index and selected tab change
together. However, there are some cases, such as tab addition, where the
selected index changes and the same tab remains selected. There are other
cases, such as deleting the selected tab, where the index remains the
same, but a new tab moves to that index. Events are fired for all of
these cases.

**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

EventListenerList

---

#### fireStateChanged

protected void fireStateChanged()

Sends a

ChangeEvent

, with this

JTabbedPane

as the source,
to each registered listener. This method is called each time there is
a change to either the selected index or the selected tab in the

JTabbedPane

. Usually, the selected index and selected tab change
together. However, there are some cases, such as tab addition, where the
selected index changes and the same tab remains selected. There are other
cases, such as deleting the selected tab, where the index remains the
same, but a new tab moves to that index. Events are fired for all of
these cases.

getModel

```java
public
SingleSelectionModel
getModel()
```

Returns the model associated with this tabbedpane.

**Returns:** the

SingleSelectionModel

associated with this tabbedpane
**See Also:** setModel(javax.swing.SingleSelectionModel)

---

#### getModel

public

SingleSelectionModel

getModel()

Returns the model associated with this tabbedpane.

setModel

```java
@BeanProperty
(
description
="The tabbedpane\'s SingleSelectionModel.")
public void setModel​(
SingleSelectionModel
model)
```

Sets the model to be used with this tabbedpane.

**Parameters:** model

- the model to be used
**See Also:** getModel()

---

#### setModel

@BeanProperty

(

description

="The tabbedpane\'s SingleSelectionModel.")
public void setModel​(

SingleSelectionModel

model)

Sets the model to be used with this tabbedpane.

getTabPlacement

```java
public int getTabPlacement()
```

Returns the placement of the tabs for this tabbedpane.

**Returns:** an

int

specifying the placement for the tabs
**See Also:** setTabPlacement(int)

---

#### getTabPlacement

public int getTabPlacement()

Returns the placement of the tabs for this tabbedpane.

setTabPlacement

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

enumerationValues
={"JTabbedPane.TOP","JTabbedPane.LEFT","JTabbedPane.BOTTOM","JTabbedPane.RIGHT"},

description
="The tabbedpane\'s tab placement.")
public void setTabPlacement​(int tabPlacement)
```

Sets the tab placement for this tabbedpane.
Possible values are:

- JTabbedPane.TOP

JTabbedPane.BOTTOM

JTabbedPane.LEFT

JTabbedPane.RIGHT

The default value, if not set, is

SwingConstants.TOP

.

**Parameters:** tabPlacement

- the placement for the tabs relative to the content
**Throws:** IllegalArgumentException

- if tab placement value isn't one
of the above valid values

---

#### setTabPlacement

@BeanProperty

(

preferred

=true,

visualUpdate

=true,

enumerationValues

={"JTabbedPane.TOP","JTabbedPane.LEFT","JTabbedPane.BOTTOM","JTabbedPane.RIGHT"},

description

="The tabbedpane\'s tab placement.")
public void setTabPlacement​(int tabPlacement)

Sets the tab placement for this tabbedpane.
Possible values are:

- JTabbedPane.TOP

JTabbedPane.BOTTOM

JTabbedPane.LEFT

JTabbedPane.RIGHT

The default value, if not set, is

SwingConstants.TOP

.

JTabbedPane.TOP

JTabbedPane.BOTTOM

JTabbedPane.LEFT

JTabbedPane.RIGHT

getTabLayoutPolicy

```java
public int getTabLayoutPolicy()
```

Returns the policy used by the tabbedpane to layout the tabs when all the
tabs will not fit within a single run.

**Returns:** an

int

specifying the policy used to layout the tabs
**Since:** 1.4
**See Also:** setTabLayoutPolicy(int)

---

#### getTabLayoutPolicy

public int getTabLayoutPolicy()

Returns the policy used by the tabbedpane to layout the tabs when all the
tabs will not fit within a single run.

setTabLayoutPolicy

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

enumerationValues
={"JTabbedPane.WRAP_TAB_LAYOUT","JTabbedPane.SCROLL_TAB_LAYOUT"},

description
="The tabbedpane\'s policy for laying out the tabs")
public void setTabLayoutPolicy​(int tabLayoutPolicy)
```

Sets the policy which the tabbedpane will use in laying out the tabs
when all the tabs will not fit within a single run.
Possible values are:

- JTabbedPane.WRAP_TAB_LAYOUT

JTabbedPane.SCROLL_TAB_LAYOUT

The default value, if not set by the UI, is

JTabbedPane.WRAP_TAB_LAYOUT

.

Some look and feels might only support a subset of the possible
layout policies, in which case the value of this property may be
ignored.

**Parameters:** tabLayoutPolicy

- the policy used to layout the tabs
**Throws:** IllegalArgumentException

- if layoutPolicy value isn't one
of the above valid values
**Since:** 1.4
**See Also:** getTabLayoutPolicy()

---

#### setTabLayoutPolicy

@BeanProperty

(

preferred

=true,

visualUpdate

=true,

enumerationValues

={"JTabbedPane.WRAP_TAB_LAYOUT","JTabbedPane.SCROLL_TAB_LAYOUT"},

description

="The tabbedpane\'s policy for laying out the tabs")
public void setTabLayoutPolicy​(int tabLayoutPolicy)

Sets the policy which the tabbedpane will use in laying out the tabs
when all the tabs will not fit within a single run.
Possible values are:

- JTabbedPane.WRAP_TAB_LAYOUT

JTabbedPane.SCROLL_TAB_LAYOUT

The default value, if not set by the UI, is

JTabbedPane.WRAP_TAB_LAYOUT

.

Some look and feels might only support a subset of the possible
layout policies, in which case the value of this property may be
ignored.

JTabbedPane.WRAP_TAB_LAYOUT

JTabbedPane.SCROLL_TAB_LAYOUT

Some look and feels might only support a subset of the possible
layout policies, in which case the value of this property may be
ignored.

getSelectedIndex

```java
public int getSelectedIndex()
```

Returns the currently selected index for this tabbedpane.
Returns -1 if there is no currently selected tab.

**Returns:** the index of the selected tab
**See Also:** setSelectedIndex(int)

---

#### getSelectedIndex

public int getSelectedIndex()

Returns the currently selected index for this tabbedpane.
Returns -1 if there is no currently selected tab.

setSelectedIndex

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The tabbedpane\'s selected tab index.")
public void setSelectedIndex​(int index)
```

Sets the selected index for this tabbedpane. The index must be
a valid tab index or -1, which indicates that no tab should be selected
(can also be used when there are no tabs in the tabbedpane). If a -1
value is specified when the tabbedpane contains one or more tabs, then
the results will be implementation defined.

**Parameters:** index

- the index to be selected
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < -1 || index >= tab count)
**See Also:** getSelectedIndex()

,

SingleSelectionModel.setSelectedIndex(int)

---

#### setSelectedIndex

@BeanProperty

(

bound

=false,

preferred

=true,

description

="The tabbedpane\'s selected tab index.")
public void setSelectedIndex​(int index)

Sets the selected index for this tabbedpane. The index must be
a valid tab index or -1, which indicates that no tab should be selected
(can also be used when there are no tabs in the tabbedpane). If a -1
value is specified when the tabbedpane contains one or more tabs, then
the results will be implementation defined.

getSelectedComponent

```java
public
Component
getSelectedComponent()
```

Returns the currently selected component for this tabbedpane.
Returns

null

if there is no currently selected tab.

**Returns:** the component corresponding to the selected tab
**See Also:** setSelectedComponent(java.awt.Component)

---

#### getSelectedComponent

public

Component

getSelectedComponent()

Returns the currently selected component for this tabbedpane.
Returns

null

if there is no currently selected tab.

setSelectedComponent

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The tabbedpane\'s selected component.")
public void setSelectedComponent​(
Component
c)
```

Sets the selected component for this tabbedpane. This
will automatically set the

selectedIndex

to the index
corresponding to the specified component.

**Parameters:** c

- the selected

Component

for this

TabbedPane
**Throws:** IllegalArgumentException

- if component not found in tabbed
pane
**See Also:** getSelectedComponent()

---

#### setSelectedComponent

@BeanProperty

(

bound

=false,

preferred

=true,

description

="The tabbedpane\'s selected component.")
public void setSelectedComponent​(

Component

c)

Sets the selected component for this tabbedpane. This
will automatically set the

selectedIndex

to the index
corresponding to the specified component.

insertTab

```java
public void insertTab​(
String
title,

Icon
icon,

Component
component,

String
tip,
int index)
```

Inserts a new tab for the given component, at the given index,
represented by the given title and/or icon, either of which may
be

null

.

**Parameters:** title

- the title to be displayed on the tab
**Parameters:** icon

- the icon to be displayed on the tab
**Parameters:** component

- the component to be displayed when this tab is clicked.
**Parameters:** tip

- the tooltip to be displayed for this tab
**Parameters:** index

- the position to insert this new tab
(

> 0 and <= getTabCount()

)
**Throws:** IndexOutOfBoundsException

- if the index is out of range
(

< 0 or > getTabCount()

)
**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

,

removeTabAt(int)

---

#### insertTab

public void insertTab​(

String

title,

Icon

icon,

Component

component,

String

tip,
int index)

Inserts a new tab for the given component, at the given index,
represented by the given title and/or icon, either of which may
be

null

.

addTab

```java
public void addTab​(
String
title,

Icon
icon,

Component
component,

String
tip)
```

Adds a

component

and

tip

represented by a

title

and/or

icon

,
either of which can be

null

.
Cover method for

insertTab

.

**Parameters:** title

- the title to be displayed in this tab
**Parameters:** icon

- the icon to be displayed in this tab
**Parameters:** component

- the component to be displayed when this tab is clicked
**Parameters:** tip

- the tooltip to be displayed for this tab
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

---

#### addTab

public void addTab​(

String

title,

Icon

icon,

Component

component,

String

tip)

Adds a

component

and

tip

represented by a

title

and/or

icon

,
either of which can be

null

.
Cover method for

insertTab

.

addTab

```java
public void addTab​(
String
title,

Icon
icon,

Component
component)
```

Adds a

component

represented by a

title

and/or

icon

, either of which can be

null

.
Cover method for

insertTab

.

**Parameters:** title

- the title to be displayed in this tab
**Parameters:** icon

- the icon to be displayed in this tab
**Parameters:** component

- the component to be displayed when this tab is clicked
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

---

#### addTab

public void addTab​(

String

title,

Icon

icon,

Component

component)

Adds a

component

represented by a

title

and/or

icon

, either of which can be

null

.
Cover method for

insertTab

.

addTab

```java
public void addTab​(
String
title,

Component
component)
```

Adds a

component

represented by a

title

and no icon.
Cover method for

insertTab

.

**Parameters:** title

- the title to be displayed in this tab
**Parameters:** component

- the component to be displayed when this tab is clicked
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

---

#### addTab

public void addTab​(

String

title,

Component

component)

Adds a

component

represented by a

title

and no icon.
Cover method for

insertTab

.

add

```java
public
Component
add​(
Component
component)
```

Adds a

component

with a tab title defaulting to
the name of the component which is the result of calling

component.getName

.
Cover method for

insertTab

.

**Overrides:** add

in class

Container
**Parameters:** component

- the component to be displayed when this tab is clicked
**Returns:** the component
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

---

#### add

public

Component

add​(

Component

component)

Adds a

component

with a tab title defaulting to
the name of the component which is the result of calling

component.getName

.
Cover method for

insertTab

.

add

```java
public
Component
add​(
String
title,

Component
component)
```

Adds a

component

with the specified tab title.
Cover method for

insertTab

.

**Overrides:** add

in class

Container
**Parameters:** title

- the title to be displayed in this tab
**Parameters:** component

- the component to be displayed when this tab is clicked
**Returns:** the component
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

---

#### add

public

Component

add​(

String

title,

Component

component)

Adds a

component

with the specified tab title.
Cover method for

insertTab

.

add

```java
public
Component
add​(
Component
component,
int index)
```

Adds a

component

at the specified tab index with a tab
title defaulting to the name of the component.
Cover method for

insertTab

.

**Overrides:** add

in class

Container
**Parameters:** component

- the component to be displayed when this tab is clicked
**Parameters:** index

- the position to insert this new tab
**Returns:** the component
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

---

#### add

public

Component

add​(

Component

component,
int index)

Adds a

component

at the specified tab index with a tab
title defaulting to the name of the component.
Cover method for

insertTab

.

add

```java
public void add​(
Component
component,

Object
constraints)
```

Adds a

component

to the tabbed pane.
If

constraints

is a

String

or an

Icon

, it will be used for the tab title,
otherwise the component's name will be used as the tab title.
Cover method for

insertTab

.

**Overrides:** add

in class

Container
**Parameters:** component

- the component to be displayed when this tab is clicked
**Parameters:** constraints

- the object to be displayed in the tab
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

---

#### add

public void add​(

Component

component,

Object

constraints)

Adds a

component

to the tabbed pane.
If

constraints

is a

String

or an

Icon

, it will be used for the tab title,
otherwise the component's name will be used as the tab title.
Cover method for

insertTab

.

add

```java
public void add​(
Component
component,

Object
constraints,
int index)
```

Adds a

component

at the specified tab index.
If

constraints

is a

String

or an

Icon

, it will be used for the tab title,
otherwise the component's name will be used as the tab title.
Cover method for

insertTab

.

**Overrides:** add

in class

Container
**Parameters:** component

- the component to be displayed when this tab is clicked
**Parameters:** constraints

- the object to be displayed in the tab
**Parameters:** index

- the position to insert this new tab
**See Also:** insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

,

removeTabAt(int)

---

#### add

public void add​(

Component

component,

Object

constraints,
int index)

Adds a

component

at the specified tab index.
If

constraints

is a

String

or an

Icon

, it will be used for the tab title,
otherwise the component's name will be used as the tab title.
Cover method for

insertTab

.

removeTabAt

```java
public void removeTabAt​(int index)
```

Removes the tab at

index

.
After the component associated with

index

is removed,
its visibility is reset to true to ensure it will be visible
if added to other containers.

**Parameters:** index

- the index of the tab to be removed
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

,

insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)

---

#### removeTabAt

public void removeTabAt​(int index)

Removes the tab at

index

.
After the component associated with

index

is removed,
its visibility is reset to true to ensure it will be visible
if added to other containers.

remove

```java
public void remove​(
Component
component)
```

Removes the specified

Component

from the

JTabbedPane

. The method does nothing
if the

component

is null.

**Overrides:** remove

in class

Container
**Parameters:** component

- the component to remove from the tabbedpane
**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

,

removeTabAt(int)

---

#### remove

public void remove​(

Component

component)

Removes the specified

Component

from the

JTabbedPane

. The method does nothing
if the

component

is null.

remove

```java
public void remove​(int index)
```

Removes the tab and component which corresponds to the specified index.

**Overrides:** remove

in class

Container
**Parameters:** index

- the index of the component to remove from the

tabbedpane
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

,

removeTabAt(int)

---

#### remove

public void remove​(int index)

Removes the tab and component which corresponds to the specified index.

removeAll

```java
public void removeAll()
```

Removes all the tabs and their corresponding components
from the

tabbedpane

.

**Overrides:** removeAll

in class

Container
**See Also:** addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String)

,

removeTabAt(int)

---

#### removeAll

public void removeAll()

Removes all the tabs and their corresponding components
from the

tabbedpane

.

getTabCount

```java
@BeanProperty
(
bound
=false)
public int getTabCount()
```

Returns the number of tabs in this

tabbedpane

.

**Returns:** an integer specifying the number of tabbed pages

---

#### getTabCount

@BeanProperty

(

bound

=false)
public int getTabCount()

Returns the number of tabs in this

tabbedpane

.

getTabRunCount

```java
@BeanProperty
(
bound
=false)
public int getTabRunCount()
```

Returns the number of tab runs currently used to display
the tabs.

**Returns:** an integer giving the number of rows if the

tabPlacement

is

TOP

or

BOTTOM

and the number of columns if

tabPlacement

is

LEFT

or

RIGHT

,
or 0 if there is no UI set on this

tabbedpane

---

#### getTabRunCount

@BeanProperty

(

bound

=false)
public int getTabRunCount()

Returns the number of tab runs currently used to display
the tabs.

getTitleAt

```java
public
String
getTitleAt​(int index)
```

Returns the tab title at

index

.

**Parameters:** index

- the index of the item being queried
**Returns:** the title at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setTitleAt(int, java.lang.String)

---

#### getTitleAt

public

String

getTitleAt​(int index)

Returns the tab title at

index

.

getIconAt

```java
public
Icon
getIconAt​(int index)
```

Returns the tab icon at

index

.

**Parameters:** index

- the index of the item being queried
**Returns:** the icon at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setIconAt(int, javax.swing.Icon)

---

#### getIconAt

public

Icon

getIconAt​(int index)

Returns the tab icon at

index

.

getDisabledIconAt

```java
public
Icon
getDisabledIconAt​(int index)
```

Returns the tab disabled icon at

index

.
If the tab disabled icon doesn't exist at

index

this will forward the call to the look and feel to construct
an appropriate disabled Icon from the corresponding enabled
Icon. Some look and feels might not render the disabled Icon,
in which case it won't be created.

**Parameters:** index

- the index of the item being queried
**Returns:** the icon at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setDisabledIconAt(int, javax.swing.Icon)

---

#### getDisabledIconAt

public

Icon

getDisabledIconAt​(int index)

Returns the tab disabled icon at

index

.
If the tab disabled icon doesn't exist at

index

this will forward the call to the look and feel to construct
an appropriate disabled Icon from the corresponding enabled
Icon. Some look and feels might not render the disabled Icon,
in which case it won't be created.

getToolTipTextAt

```java
public
String
getToolTipTextAt​(int index)
```

Returns the tab tooltip text at

index

.

**Parameters:** index

- the index of the item being queried
**Returns:** a string containing the tool tip text at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**Since:** 1.3
**See Also:** setToolTipTextAt(int, java.lang.String)

---

#### getToolTipTextAt

public

String

getToolTipTextAt​(int index)

Returns the tab tooltip text at

index

.

getBackgroundAt

```java
public
Color
getBackgroundAt​(int index)
```

Returns the tab background color at

index

.

**Parameters:** index

- the index of the item being queried
**Returns:** the

Color

of the tab background at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setBackgroundAt(int, java.awt.Color)

---

#### getBackgroundAt

public

Color

getBackgroundAt​(int index)

Returns the tab background color at

index

.

getForegroundAt

```java
public
Color
getForegroundAt​(int index)
```

Returns the tab foreground color at

index

.

**Parameters:** index

- the index of the item being queried
**Returns:** the

Color

of the tab foreground at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setForegroundAt(int, java.awt.Color)

---

#### getForegroundAt

public

Color

getForegroundAt​(int index)

Returns the tab foreground color at

index

.

isEnabledAt

```java
public boolean isEnabledAt​(int index)
```

Returns whether or not the tab at

index

is
currently enabled.

**Parameters:** index

- the index of the item being queried
**Returns:** true if the tab at

index

is enabled;
false otherwise
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setEnabledAt(int, boolean)

---

#### isEnabledAt

public boolean isEnabledAt​(int index)

Returns whether or not the tab at

index

is
currently enabled.

getComponentAt

```java
public
Component
getComponentAt​(int index)
```

Returns the component at

index

.

**Parameters:** index

- the index of the item being queried
**Returns:** the

Component

at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setComponentAt(int, java.awt.Component)

---

#### getComponentAt

public

Component

getComponentAt​(int index)

Returns the component at

index

.

getMnemonicAt

```java
public int getMnemonicAt​(int tabIndex)
```

Returns the keyboard mnemonic for accessing the specified tab.
The mnemonic is the key which when combined with the look and feel's
mouseless modifier (usually Alt) will activate the specified
tab.

**Parameters:** tabIndex

- the index of the tab that the mnemonic refers to
**Returns:** the key code which represents the mnemonic;
-1 if a mnemonic is not specified for the tab
**Throws:** IndexOutOfBoundsException

- if index is out of range
(

tabIndex

< 0 ||

tabIndex

>= tab count)
**Since:** 1.4
**See Also:** setDisplayedMnemonicIndexAt(int,int)

,

setMnemonicAt(int,int)

---

#### getMnemonicAt

public int getMnemonicAt​(int tabIndex)

Returns the keyboard mnemonic for accessing the specified tab.
The mnemonic is the key which when combined with the look and feel's
mouseless modifier (usually Alt) will activate the specified
tab.

getDisplayedMnemonicIndexAt

```java
public int getDisplayedMnemonicIndexAt​(int tabIndex)
```

Returns the character, as an index, that the look and feel should
provide decoration for as representing the mnemonic character.

**Parameters:** tabIndex

- the index of the tab that the mnemonic refers to
**Returns:** index representing mnemonic character if one exists;
otherwise returns -1
**Throws:** IndexOutOfBoundsException

- if index is out of range
(

tabIndex

< 0 ||

tabIndex

>= tab count)
**Since:** 1.4
**See Also:** setDisplayedMnemonicIndexAt(int,int)

,

setMnemonicAt(int,int)

---

#### getDisplayedMnemonicIndexAt

public int getDisplayedMnemonicIndexAt​(int tabIndex)

Returns the character, as an index, that the look and feel should
provide decoration for as representing the mnemonic character.

getBoundsAt

```java
public
Rectangle
getBoundsAt​(int index)
```

Returns the tab bounds at

index

. If the tab at
this index is not currently visible in the UI, then returns

null

.
If there is no UI set on this

tabbedpane

,
then returns

null

.

**Parameters:** index

- the index to be queried
**Returns:** a

Rectangle

containing the tab bounds at

index

, or

null

if tab at

index

is not currently visible in the UI,
or if there is no UI set on this

tabbedpane
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)

---

#### getBoundsAt

public

Rectangle

getBoundsAt​(int index)

Returns the tab bounds at

index

. If the tab at
this index is not currently visible in the UI, then returns

null

.
If there is no UI set on this

tabbedpane

,
then returns

null

.

setTitleAt

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The title at the specified tab index.")
public void setTitleAt​(int index,

String
title)
```

Sets the title at

index

to

title

which
can be

null

.
The title is not shown if a tab component for this tab was specified.
An internal exception is raised if there is no tab at that index.

**Parameters:** index

- the tab index where the title should be set
**Parameters:** title

- the title to be displayed in the tab
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** getTitleAt(int)

,

setTabComponentAt(int, java.awt.Component)

---

#### setTitleAt

@BeanProperty

(

preferred

=true,

visualUpdate

=true,

description

="The title at the specified tab index.")
public void setTitleAt​(int index,

String

title)

Sets the title at

index

to

title

which
can be

null

.
The title is not shown if a tab component for this tab was specified.
An internal exception is raised if there is no tab at that index.

setIconAt

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The icon at the specified tab index.")
public void setIconAt​(int index,

Icon
icon)
```

Sets the icon at

index

to

icon

which can be

null

. This does not set disabled icon at

icon

.
If the new Icon is different than the current Icon and disabled icon
is not explicitly set, the LookAndFeel will be asked to generate a disabled
Icon. To explicitly set disabled icon, use

setDisableIconAt()

.
The icon is not shown if a tab component for this tab was specified.
An internal exception is raised if there is no tab at that index.

**Parameters:** index

- the tab index where the icon should be set
**Parameters:** icon

- the icon to be displayed in the tab
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** setDisabledIconAt(int, javax.swing.Icon)

,

getIconAt(int)

,

getDisabledIconAt(int)

,

setTabComponentAt(int, java.awt.Component)

---

#### setIconAt

@BeanProperty

(

preferred

=true,

visualUpdate

=true,

description

="The icon at the specified tab index.")
public void setIconAt​(int index,

Icon

icon)

Sets the icon at

index

to

icon

which can be

null

. This does not set disabled icon at

icon

.
If the new Icon is different than the current Icon and disabled icon
is not explicitly set, the LookAndFeel will be asked to generate a disabled
Icon. To explicitly set disabled icon, use

setDisableIconAt()

.
The icon is not shown if a tab component for this tab was specified.
An internal exception is raised if there is no tab at that index.

setDisabledIconAt

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The disabled icon at the specified tab index.")
public void setDisabledIconAt​(int index,

Icon
disabledIcon)
```

Sets the disabled icon at

index

to

icon

which can be

null

.
An internal exception is raised if there is no tab at that index.

**Parameters:** index

- the tab index where the disabled icon should be set
**Parameters:** disabledIcon

- the icon to be displayed in the tab when disabled
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** getDisabledIconAt(int)

---

#### setDisabledIconAt

@BeanProperty

(

preferred

=true,

visualUpdate

=true,

description

="The disabled icon at the specified tab index.")
public void setDisabledIconAt​(int index,

Icon

disabledIcon)

Sets the disabled icon at

index

to

icon

which can be

null

.
An internal exception is raised if there is no tab at that index.

setToolTipTextAt

```java
@BeanProperty
(
preferred
=true,

description
="The tooltip text at the specified tab index.")
public void setToolTipTextAt​(int index,

String
toolTipText)
```

Sets the tooltip text at

index

to

toolTipText

which can be

null

.
An internal exception is raised if there is no tab at that index.

**Parameters:** index

- the tab index where the tooltip text should be set
**Parameters:** toolTipText

- the tooltip text to be displayed for the tab
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**Since:** 1.3
**See Also:** getToolTipTextAt(int)

---

#### setToolTipTextAt

@BeanProperty

(

preferred

=true,

description

="The tooltip text at the specified tab index.")
public void setToolTipTextAt​(int index,

String

toolTipText)

Sets the tooltip text at

index

to

toolTipText

which can be

null

.
An internal exception is raised if there is no tab at that index.

setBackgroundAt

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The background color at the specified tab index.")
public void setBackgroundAt​(int index,

Color
background)
```

Sets the background color at

index

to

background

which can be

null

, in which case the tab's background color
will default to the background color of the

tabbedpane

.
An internal exception is raised if there is no tab at that index.

It is up to the look and feel to honor this property, some may
choose to ignore it.

**Parameters:** index

- the tab index where the background should be set
**Parameters:** background

- the color to be displayed in the tab's background
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** getBackgroundAt(int)

---

#### setBackgroundAt

@BeanProperty

(

preferred

=true,

visualUpdate

=true,

description

="The background color at the specified tab index.")
public void setBackgroundAt​(int index,

Color

background)

Sets the background color at

index

to

background

which can be

null

, in which case the tab's background color
will default to the background color of the

tabbedpane

.
An internal exception is raised if there is no tab at that index.

It is up to the look and feel to honor this property, some may
choose to ignore it.

It is up to the look and feel to honor this property, some may
choose to ignore it.

setForegroundAt

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The foreground color at the specified tab index.")
public void setForegroundAt​(int index,

Color
foreground)
```

Sets the foreground color at

index

to

foreground

which can be

null

, in which case the tab's foreground color
will default to the foreground color of this

tabbedpane

.
An internal exception is raised if there is no tab at that index.

It is up to the look and feel to honor this property, some may
choose to ignore it.

**Parameters:** index

- the tab index where the foreground should be set
**Parameters:** foreground

- the color to be displayed as the tab's foreground
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** getForegroundAt(int)

---

#### setForegroundAt

@BeanProperty

(

preferred

=true,

visualUpdate

=true,

description

="The foreground color at the specified tab index.")
public void setForegroundAt​(int index,

Color

foreground)

Sets the foreground color at

index

to

foreground

which can be

null

, in which case the tab's foreground color
will default to the foreground color of this

tabbedpane

.
An internal exception is raised if there is no tab at that index.

It is up to the look and feel to honor this property, some may
choose to ignore it.

It is up to the look and feel to honor this property, some may
choose to ignore it.

setEnabledAt

```java
public void setEnabledAt​(int index,
boolean enabled)
```

Sets whether or not the tab at

index

is enabled.
An internal exception is raised if there is no tab at that index.

**Parameters:** index

- the tab index which should be enabled/disabled
**Parameters:** enabled

- whether or not the tab should be enabled
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** isEnabledAt(int)

---

#### setEnabledAt

public void setEnabledAt​(int index,
boolean enabled)

Sets whether or not the tab at

index

is enabled.
An internal exception is raised if there is no tab at that index.

setComponentAt

```java
@BeanProperty
(
visualUpdate
=true,

description
="The component at the specified tab index.")
public void setComponentAt​(int index,

Component
component)
```

Sets the component at

index

to

component

.
An internal exception is raised if there is no tab at that index.

**Parameters:** index

- the tab index where this component is being placed
**Parameters:** component

- the component for the tab
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**See Also:** getComponentAt(int)

---

#### setComponentAt

@BeanProperty

(

visualUpdate

=true,

description

="The component at the specified tab index.")
public void setComponentAt​(int index,

Component

component)

Sets the component at

index

to

component

.
An internal exception is raised if there is no tab at that index.

setDisplayedMnemonicIndexAt

```java
@BeanProperty
(
visualUpdate
=true,

description
="the index into the String to draw the keyboard character mnemonic at")
public void setDisplayedMnemonicIndexAt​(int tabIndex,
int mnemonicIndex)
```

Provides a hint to the look and feel as to which character in the
text should be decorated to represent the mnemonic. Not all look and
feels may support this. A value of -1 indicates either there is
no mnemonic for this tab, or you do not wish the mnemonic to be
displayed for this tab.

The value of this is updated as the properties relating to the
mnemonic change (such as the mnemonic itself, the text...).
You should only ever have to call this if
you do not wish the default character to be underlined. For example, if
the text at tab index 3 was 'Apple Price', with a mnemonic of 'p',
and you wanted the 'P'
to be decorated, as 'Apple

P

rice', you would have to invoke

setDisplayedMnemonicIndex(3, 6)

after invoking

setMnemonicAt(3, KeyEvent.VK_P)

.

Note that it is the programmer's responsibility to ensure
that each tab has a unique mnemonic or unpredictable results may
occur.

**Parameters:** tabIndex

- the index of the tab that the mnemonic refers to
**Parameters:** mnemonicIndex

- index into the

String

to underline
**Throws:** IndexOutOfBoundsException

- if

tabIndex

is
out of range (

tabIndex < 0 || tabIndex >= tab
count

)
**Throws:** IllegalArgumentException

- will be thrown if

mnemonicIndex

is >= length of the tab
title , or < -1
**Since:** 1.4
**See Also:** setMnemonicAt(int,int)

,

getDisplayedMnemonicIndexAt(int)

---

#### setDisplayedMnemonicIndexAt

@BeanProperty

(

visualUpdate

=true,

description

="the index into the String to draw the keyboard character mnemonic at")
public void setDisplayedMnemonicIndexAt​(int tabIndex,
int mnemonicIndex)

Provides a hint to the look and feel as to which character in the
text should be decorated to represent the mnemonic. Not all look and
feels may support this. A value of -1 indicates either there is
no mnemonic for this tab, or you do not wish the mnemonic to be
displayed for this tab.

The value of this is updated as the properties relating to the
mnemonic change (such as the mnemonic itself, the text...).
You should only ever have to call this if
you do not wish the default character to be underlined. For example, if
the text at tab index 3 was 'Apple Price', with a mnemonic of 'p',
and you wanted the 'P'
to be decorated, as 'Apple

P

rice', you would have to invoke

setDisplayedMnemonicIndex(3, 6)

after invoking

setMnemonicAt(3, KeyEvent.VK_P)

.

Note that it is the programmer's responsibility to ensure
that each tab has a unique mnemonic or unpredictable results may
occur.

The value of this is updated as the properties relating to the
mnemonic change (such as the mnemonic itself, the text...).
You should only ever have to call this if
you do not wish the default character to be underlined. For example, if
the text at tab index 3 was 'Apple Price', with a mnemonic of 'p',
and you wanted the 'P'
to be decorated, as 'Apple

P

rice', you would have to invoke

setDisplayedMnemonicIndex(3, 6)

after invoking

setMnemonicAt(3, KeyEvent.VK_P)

.

Note that it is the programmer's responsibility to ensure
that each tab has a unique mnemonic or unpredictable results may
occur.

Note that it is the programmer's responsibility to ensure
that each tab has a unique mnemonic or unpredictable results may
occur.

setMnemonicAt

```java
@BeanProperty
(
visualUpdate
=true,

description
="The keyboard mnenmonic, as a KeyEvent VK constant, for the specified tab")
public void setMnemonicAt​(int tabIndex,
int mnemonic)
```

Sets the keyboard mnemonic for accessing the specified tab.
The mnemonic is the key which when combined with the look and feel's
mouseless modifier (usually Alt) will activate the specified
tab.

A mnemonic must correspond to a single key on the keyboard
and should be specified using one of the

VK_XXX

keycodes defined in

java.awt.event.KeyEvent

or one of the extended keycodes obtained through

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.
Mnemonics are case-insensitive, therefore a key event
with the corresponding keycode would cause the button to be
activated whether or not the Shift modifier was pressed.

This will update the displayed mnemonic property for the specified
tab.

**Parameters:** tabIndex

- the index of the tab that the mnemonic refers to
**Parameters:** mnemonic

- the key code which represents the mnemonic
**Throws:** IndexOutOfBoundsException

- if

tabIndex

is out
of range (

tabIndex < 0 || tabIndex >= tab count

)
**Since:** 1.4
**See Also:** getMnemonicAt(int)

,

setDisplayedMnemonicIndexAt(int,int)

---

#### setMnemonicAt

@BeanProperty

(

visualUpdate

=true,

description

="The keyboard mnenmonic, as a KeyEvent VK constant, for the specified tab")
public void setMnemonicAt​(int tabIndex,
int mnemonic)

Sets the keyboard mnemonic for accessing the specified tab.
The mnemonic is the key which when combined with the look and feel's
mouseless modifier (usually Alt) will activate the specified
tab.

A mnemonic must correspond to a single key on the keyboard
and should be specified using one of the

VK_XXX

keycodes defined in

java.awt.event.KeyEvent

or one of the extended keycodes obtained through

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.
Mnemonics are case-insensitive, therefore a key event
with the corresponding keycode would cause the button to be
activated whether or not the Shift modifier was pressed.

This will update the displayed mnemonic property for the specified
tab.

A mnemonic must correspond to a single key on the keyboard
and should be specified using one of the

VK_XXX

keycodes defined in

java.awt.event.KeyEvent

or one of the extended keycodes obtained through

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.
Mnemonics are case-insensitive, therefore a key event
with the corresponding keycode would cause the button to be
activated whether or not the Shift modifier was pressed.

This will update the displayed mnemonic property for the specified
tab.

This will update the displayed mnemonic property for the specified
tab.

indexOfTab

```java
public int indexOfTab​(
String
title)
```

Returns the first tab index with a given

title

, or
-1 if no tab has this title.

**Parameters:** title

- the title for the tab
**Returns:** the first tab index which matches

title

, or
-1 if no tab has this title

---

#### indexOfTab

public int indexOfTab​(

String

title)

Returns the first tab index with a given

title

, or
-1 if no tab has this title.

indexOfTab

```java
public int indexOfTab​(
Icon
icon)
```

Returns the first tab index with a given

icon

,
or -1 if no tab has this icon.

**Parameters:** icon

- the icon for the tab
**Returns:** the first tab index which matches

icon

,
or -1 if no tab has this icon

---

#### indexOfTab

public int indexOfTab​(

Icon

icon)

Returns the first tab index with a given

icon

,
or -1 if no tab has this icon.

indexOfComponent

```java
public int indexOfComponent​(
Component
component)
```

Returns the index of the tab for the specified component.
Returns -1 if there is no tab for this component.

**Parameters:** component

- the component for the tab
**Returns:** the first tab which matches this component, or -1
if there is no tab for this component

---

#### indexOfComponent

public int indexOfComponent​(

Component

component)

Returns the index of the tab for the specified component.
Returns -1 if there is no tab for this component.

indexAtLocation

```java
public int indexAtLocation​(int x,
int y)
```

Returns the tab index corresponding to the tab whose bounds
intersect the specified location. Returns -1 if no tab
intersects the location.

**Parameters:** x

- the x location relative to this tabbedpane
**Parameters:** y

- the y location relative to this tabbedpane
**Returns:** the tab index which intersects the location, or
-1 if no tab intersects the location
**Since:** 1.4

---

#### indexAtLocation

public int indexAtLocation​(int x,
int y)

Returns the tab index corresponding to the tab whose bounds
intersect the specified location. Returns -1 if no tab
intersects the location.

getToolTipText

```java
public
String
getToolTipText​(
MouseEvent
event)
```

Returns the tooltip text for the component determined by the
mouse event location.

**Overrides:** getToolTipText

in class

JComponent
**Parameters:** event

- the

MouseEvent

that tells where the
cursor is lingering
**Returns:** the

String

containing the tooltip text

---

#### getToolTipText

public

String

getToolTipText​(

MouseEvent

event)

Returns the tooltip text for the component determined by the
mouse event location.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JTabbedPane

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this JTabbedPane.

---

#### paramString

protected

String

paramString()

Returns a string representation of this

JTabbedPane

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JTabbedPane.
For tabbed panes, the AccessibleContext takes the form of an
AccessibleJTabbedPane.
A new AccessibleJTabbedPane instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJTabbedPane that serves as the
AccessibleContext of this JTabbedPane

---

#### getAccessibleContext

@BeanProperty

(

bound

=false)
public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this JTabbedPane.
For tabbed panes, the AccessibleContext takes the form of an
AccessibleJTabbedPane.
A new AccessibleJTabbedPane instance is created if necessary.

setTabComponentAt

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The tab component at the specified tab index.")
public void setTabComponentAt​(int index,

Component
component)
```

Sets the component that is responsible for rendering the
title for the specified tab. A null value means

JTabbedPane

will render the title and/or icon for
the specified tab. A non-null value means the component will
render the title and

JTabbedPane

will not render
the title and/or icon.

Note: The component must not be one that the developer has
already added to the tabbed pane.

**Parameters:** index

- the tab index where the component should be set
**Parameters:** component

- the component to render the title for the
specified tab
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**Throws:** IllegalArgumentException

- if component has already been
added to this

JTabbedPane
**Since:** 1.6
**See Also:** getTabComponentAt(int)

---

#### setTabComponentAt

@BeanProperty

(

preferred

=true,

visualUpdate

=true,

description

="The tab component at the specified tab index.")
public void setTabComponentAt​(int index,

Component

component)

Sets the component that is responsible for rendering the
title for the specified tab. A null value means

JTabbedPane

will render the title and/or icon for
the specified tab. A non-null value means the component will
render the title and

JTabbedPane

will not render
the title and/or icon.

Note: The component must not be one that the developer has
already added to the tabbed pane.

Note: The component must not be one that the developer has
already added to the tabbed pane.

getTabComponentAt

```java
public
Component
getTabComponentAt​(int index)
```

Returns the tab component at

index

.

**Parameters:** index

- the index of the item being queried
**Returns:** the tab component at

index
**Throws:** IndexOutOfBoundsException

- if index is out of range

(index < 0 || index >= tab count)
**Since:** 1.6
**See Also:** setTabComponentAt(int, java.awt.Component)

---

#### getTabComponentAt

public

Component

getTabComponentAt​(int index)

Returns the tab component at

index

.

indexOfTabComponent

```java
public int indexOfTabComponent​(
Component
tabComponent)
```

Returns the index of the tab for the specified tab component.
Returns -1 if there is no tab for this tab component.

**Parameters:** tabComponent

- the tab component for the tab
**Returns:** the first tab which matches this tab component, or -1
if there is no tab for this tab component
**Since:** 1.6
**See Also:** setTabComponentAt(int, java.awt.Component)

,

getTabComponentAt(int)

---

#### indexOfTabComponent

public int indexOfTabComponent​(

Component

tabComponent)

Returns the index of the tab for the specified tab component.
Returns -1 if there is no tab for this tab component.

---

