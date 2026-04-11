# Class JProgressBar

**Source:** `java.desktop\javax\swing\JProgressBar.html`

### Class Description

```java
@JavaBean
(
defaultProperty
="UI",

description
="A component that displays an integer value.")
public class
JProgressBar

extends
JComponent

implements
SwingConstants
,
Accessible
```

A component that visually displays the progress of some task. As the task
progresses towards completion, the progress bar displays the
task's percentage of completion.
This percentage is typically represented visually by a rectangle which
starts out empty and gradually becomes filled in as the task progresses.
In addition, the progress bar can display a textual representation of this
percentage.

JProgressBar

uses a

BoundedRangeModel

as its data model,
with the

value

property representing the "current" state of the task,
and the

minimum

and

maximum

properties representing the
beginning and end points, respectively.

To indicate that a task of unknown length is executing,
you can put a progress bar into indeterminate mode.
While the bar is in indeterminate mode,
it animates constantly to show that work is occurring.
As soon as you can determine the task's length and amount of progress,
you should update the progress bar's value
and switch it back to determinate mode.

Here is an example of creating a progress bar,
where

task

is an object (representing some piece of work)
which returns information about the progress of the task:

```java
progressBar = new JProgressBar(0, task.getLengthOfTask());
progressBar.setValue(0);
progressBar.setStringPainted(true);
```

Here is an example of querying the current state of the task, and using
the returned value to update the progress bar:

```java
progressBar.setValue(task.getCurrent());
```

Here is an example of putting a progress bar into
indeterminate mode,
and then switching back to determinate mode
once the length of the task is known:

```java
progressBar = new JProgressBar();

...//when the task of (initially) unknown length begins:

progressBar.setIndeterminate(true);

...//do some work; get length of task...

progressBar.setMaximum(newLength);
progressBar.setValue(newValue);
progressBar.setIndeterminate(false);
```

For complete examples and further documentation see

How to Monitor Progress

,
a section in

The Java Tutorial.

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

#### protected int orientation

Whether the progress bar is horizontal or vertical.
The default is

HORIZONTAL

.

**See Also:**
- setOrientation(int)

---

#### protected boolean paintBorder

Whether to display a border around the progress bar.
The default is

true

.

**See Also:**
- setBorderPainted(boolean)

---

#### protected
BoundedRangeModel
model

The object that holds the data for the progress bar.

**See Also:**
- setModel(javax.swing.BoundedRangeModel)

---

#### protected
String
progressString

An optional string that can be displayed on the progress bar.
The default is

null

. Setting this to a non-

null

value does not imply that the string will be displayed.
To display the string,

paintString

must be

true

.

**See Also:**
- setString(java.lang.String)

,

setStringPainted(boolean)

---

#### protected boolean paintString

Whether to display a string of text on the progress bar.
The default is

false

.
Setting this to

true

causes a textual
display of the progress to be rendered on the progress bar. If
the

progressString

is

null

,
the percentage of completion is displayed on the progress bar.
Otherwise, the

progressString

is
rendered on the progress bar.

**See Also:**
- setStringPainted(boolean)

,

setString(java.lang.String)

---

#### protected transient
ChangeEvent
changeEvent

Only one

ChangeEvent

is needed per instance since the
event's only interesting property is the immutable source, which
is the progress bar.
The event is lazily created the first time that an
event notification is fired.

**See Also:**
- fireStateChanged()

---

#### protected
ChangeListener
changeListener

Listens for change events sent by the progress bar's model,
redispatching them
to change-event listeners registered upon
this progress bar.

**See Also:**
- createChangeListener()

---

### Constructor Details

#### public JProgressBar()

Creates a horizontal progress bar
that displays a border but no progress string.
The initial and minimum values are 0,
and the maximum is 100.

**See Also:**
- setOrientation(int)

,

setBorderPainted(boolean)

,

setStringPainted(boolean)

,

setString(java.lang.String)

,

setIndeterminate(boolean)

---

#### public JProgressBar​(int orient)

Creates a progress bar with the specified orientation,
which can be
either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.
By default, a border is painted but a progress string is not.
The initial and minimum values are 0,
and the maximum is 100.

**Parameters:**
- orient

- the desired orientation of the progress bar

**Throws:**
- IllegalArgumentException

- if

orient

is an illegal value

**See Also:**
- setOrientation(int)

,

setBorderPainted(boolean)

,

setStringPainted(boolean)

,

setString(java.lang.String)

,

setIndeterminate(boolean)

---

#### public JProgressBar​(int min,
int max)

Creates a horizontal progress bar
with the specified minimum and maximum.
Sets the initial value of the progress bar to the specified minimum.
By default, a border is painted but a progress string is not.

The

BoundedRangeModel

that holds the progress bar's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the progress bar.
See the

BoundedRangeModel

documentation for details.

**Parameters:**
- min

- the minimum value of the progress bar
- max

- the maximum value of the progress bar

**See Also:**
- BoundedRangeModel

,

setOrientation(int)

,

setBorderPainted(boolean)

,

setStringPainted(boolean)

,

setString(java.lang.String)

,

setIndeterminate(boolean)

---

#### public JProgressBar​(int orient,
int min,
int max)

Creates a progress bar using the specified orientation,
minimum, and maximum.
By default, a border is painted but a progress string is not.
Sets the initial value of the progress bar to the specified minimum.

The

BoundedRangeModel

that holds the progress bar's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the progress bar.
See the

BoundedRangeModel

documentation for details.

**Parameters:**
- orient

- the desired orientation of the progress bar
- min

- the minimum value of the progress bar
- max

- the maximum value of the progress bar

**Throws:**
- IllegalArgumentException

- if

orient

is an illegal value

**See Also:**
- BoundedRangeModel

,

setOrientation(int)

,

setBorderPainted(boolean)

,

setStringPainted(boolean)

,

setString(java.lang.String)

,

setIndeterminate(boolean)

---

#### public JProgressBar​(
BoundedRangeModel
newModel)

Creates a horizontal progress bar
that uses the specified model
to hold the progress bar's data.
By default, a border is painted but a progress string is not.

**Parameters:**
- newModel

- the data model for the progress bar

**See Also:**
- setOrientation(int)

,

setBorderPainted(boolean)

,

setStringPainted(boolean)

,

setString(java.lang.String)

,

setIndeterminate(boolean)

---

### Method Details

#### public int getOrientation()

Returns

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

, depending on the orientation
of the progress bar. The default orientation is

SwingConstants.HORIZONTAL

.

**Returns:**
- HORIZONTAL

or

VERTICAL

**See Also:**
- setOrientation(int)

---

#### @BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="Set the progress bar\'s orientation.")
public void setOrientation​(int newOrientation)

Sets the progress bar's orientation to

newOrientation

,
which must be

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

. The default orientation
is

SwingConstants.HORIZONTAL

.

**Parameters:**
- newOrientation

-

HORIZONTAL

or

VERTICAL

**Throws:**
- IllegalArgumentException

- if

newOrientation

is an illegal value

**See Also:**
- getOrientation()

---

#### public boolean isStringPainted()

Returns the value of the

stringPainted

property.

**Returns:**
- the value of the

stringPainted

property

**See Also:**
- setStringPainted(boolean)

,

setString(java.lang.String)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="Whether the progress bar should render a string.")
public void setStringPainted​(boolean b)

Sets the value of the

stringPainted

property,
which determines whether the progress bar
should render a progress string.
The default is

false

, meaning
no string is painted.
Some look and feels might not support progress strings
or might support them only when the progress bar is in determinate mode.

**Parameters:**
- b

-

true

if the progress bar should render a string

**See Also:**
- isStringPainted()

,

setString(java.lang.String)

---

#### public
String
getString()

Returns a

String

representation of the current progress.
By default, this returns a simple percentage

String

based on
the value returned from

getPercentComplete

. An example
would be the "42%". You can change this by calling

setString

.

**Returns:**
- the value of the progress string, or a simple percentage string
if the progress string is

null

**See Also:**
- setString(java.lang.String)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="Specifies the progress string to paint")
public void setString​(
String
s)

Sets the value of the progress string. By default,
this string is

null

, implying the built-in behavior of
using a simple percent string.
If you have provided a custom progress string and want to revert to
the built-in behavior, set the string back to

null

.

The progress string is painted only if
the

isStringPainted

method returns

true

.

**Parameters:**
- s

- the value of the progress string

**See Also:**
- getString()

,

setStringPainted(boolean)

,

isStringPainted()

---

#### @BeanProperty
(
bound
=false)
public double getPercentComplete()

Returns the percent complete for the progress bar.
Note that this number is between 0.0 and 1.0.

**Returns:**
- the percent complete for this progress bar

---

#### public boolean isBorderPainted()

Returns the

borderPainted

property.

**Returns:**
- the value of the

borderPainted

property

**See Also:**
- setBorderPainted(boolean)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="Whether the progress bar should paint its border.")
public void setBorderPainted​(boolean b)

Sets the

borderPainted

property, which is

true

if the progress bar should paint its border.
The default value for this property is

true

.
Some look and feels might not implement painted borders;
they will ignore this property.

**Parameters:**
- b

-

true

if the progress bar
should paint its border;
otherwise,

false

**See Also:**
- isBorderPainted()

---

#### protected void paintBorder​(
Graphics
g)

Paints the progress bar's border if the

borderPainted

property is

true

.

**Overrides:**
- paintBorder

in class

JComponent

**Parameters:**
- g

- the

Graphics

context within which to paint the border

**See Also:**
- JComponent.paint(java.awt.Graphics)

,

JComponent.setBorder(javax.swing.border.Border)

,

isBorderPainted()

,

setBorderPainted(boolean)

---

#### public
ProgressBarUI
getUI()

Returns the look-and-feel object that renders this component.

**Overrides:**
- getUI

in class

JComponent

**Returns:**
- the

ProgressBarUI

object that renders this component

---

#### @BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
ProgressBarUI
ui)

Sets the look-and-feel object that renders this component.

**Parameters:**
- ui

- a

ProgressBarUI

object

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
=false,

expert
=true,

description
="A string that specifies the name of the look-and-feel class.")
public
String
getUIClassID()

Returns the name of the look-and-feel class that renders this component.

**Overrides:**
- getUIClassID

in class

JComponent

**Returns:**
- the string "ProgressBarUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### protected
ChangeListener
createChangeListener()

Subclasses that want to handle change events
from the model differently
can override this to return
an instance of a custom

ChangeListener

implementation.
The default

ChangeListener

simply calls the

fireStateChanged

method to forward

ChangeEvent

s
to the

ChangeListener

s that have been added directly to the
progress bar.

**Returns:**
- the instance of a custom

ChangeListener

implementation.

**See Also:**
- changeListener

,

fireStateChanged()

,

ChangeListener

,

BoundedRangeModel

---

#### public void addChangeListener​(
ChangeListener
l)

Adds the specified

ChangeListener

to the progress bar.

**Parameters:**
- l

- the

ChangeListener

to add

---

#### public void removeChangeListener​(
ChangeListener
l)

Removes a

ChangeListener

from the progress bar.

**Parameters:**
- l

- the

ChangeListener

to remove

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
to this progress bar with

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

Send a

ChangeEvent

, whose source is this

JProgressBar

, to
all

ChangeListener

s that have registered interest in

ChangeEvent

s.
This method is called each time a

ChangeEvent

is received from
the model.

The event instance is created if necessary, and stored in

changeEvent

.

**See Also:**
- addChangeListener(javax.swing.event.ChangeListener)

,

EventListenerList

---

#### public
BoundedRangeModel
getModel()

Returns the data model used by this progress bar.

**Returns:**
- the

BoundedRangeModel

currently in use

**See Also:**
- setModel(javax.swing.BoundedRangeModel)

,

BoundedRangeModel

---

#### @BeanProperty
(
bound
=false,

expert
=true,

description
="The data model used by the JProgressBar.")
public void setModel​(
BoundedRangeModel
newModel)

Sets the data model used by the

JProgressBar

.
Note that the

BoundedRangeModel

's

extent

is not used,
and is set to

0

.

**Parameters:**
- newModel

- the

BoundedRangeModel

to use

---

#### public int getValue()

Returns the progress bar's current

value

from the

BoundedRangeModel

.
The value is always between the
minimum and maximum values, inclusive.

**Returns:**
- the current value of the progress bar

**See Also:**
- setValue(int)

,

BoundedRangeModel.getValue()

---

#### public int getMinimum()

Returns the progress bar's

minimum

value
from the

BoundedRangeModel

.

**Returns:**
- the progress bar's minimum value

**See Also:**
- setMinimum(int)

,

BoundedRangeModel.getMinimum()

---

#### public int getMaximum()

Returns the progress bar's

maximum

value
from the

BoundedRangeModel

.

**Returns:**
- the progress bar's maximum value

**See Also:**
- setMaximum(int)

,

BoundedRangeModel.getMaximum()

---

#### @BeanProperty
(
bound
=false,

preferred
=true,

description
="The progress bar\'s current value.")
public void setValue​(int n)

Sets the progress bar's current value to

n

. This method
forwards the new value to the model.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new value is different from the previous value,
all change listeners are notified.

**Parameters:**
- n

- the new value

**See Also:**
- getValue()

,

addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.setValue(int)

---

#### @BeanProperty
(
bound
=false,

preferred
=true,

description
="The progress bar\'s minimum value.")
public void setMinimum​(int n)

Sets the progress bar's minimum value
(stored in the progress bar's data model) to

n

.

The data model (a

BoundedRangeModel

instance)
handles any mathematical
issues arising from assigning faulty values.
See the

BoundedRangeModel

documentation for details.

If the minimum value is different from the previous minimum,
all change listeners are notified.

**Parameters:**
- n

- the new minimum

**See Also:**
- getMinimum()

,

addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.setMinimum(int)

---

#### @BeanProperty
(
bound
=false,

preferred
=true,

description
="The progress bar\'s maximum value.")
public void setMaximum​(int n)

Sets the progress bar's maximum value
(stored in the progress bar's data model) to

n

.

The underlying

BoundedRangeModel

handles any mathematical
issues arising from assigning faulty values.
See the

BoundedRangeModel

documentation for details.

If the maximum value is different from the previous maximum,
all change listeners are notified.

**Parameters:**
- n

- the new maximum

**See Also:**
- getMaximum()

,

addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.setMaximum(int)

---

#### public void setIndeterminate​(boolean newValue)

Sets the

indeterminate

property of the progress bar,
which determines whether the progress bar is in determinate
or indeterminate mode.
An indeterminate progress bar continuously displays animation
indicating that an operation of unknown length is occurring.
By default, this property is

false

.
Some look and feels might not support indeterminate progress bars;
they will ignore this property.

See

How to Monitor Progress

for examples of using indeterminate progress bars.

**Parameters:**
- newValue

-

true

if the progress bar
should change to indeterminate mode;

false

if it should revert to normal.

**See Also:**
- isIndeterminate()

,

BasicProgressBarUI

**Since:**
- 1.4

---

#### @BeanProperty
(
bound
=false,

description
="Is the progress bar indeterminate (true) or normal (false)?")
public boolean isIndeterminate()

Returns the value of the

indeterminate

property.

**Returns:**
- the value of the

indeterminate

property

**See Also:**
- setIndeterminate(boolean)

**Since:**
- 1.4

---

#### protected
String
paramString()

Returns a string representation of this

JProgressBar

.
This method is intended to be used only for debugging purposes. The
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
- a string representation of this

JProgressBar

---

#### @BeanProperty
(
bound
=false,

expert
=true,

description
="The AccessibleContext associated with this ProgressBar.")
public
AccessibleContext
getAccessibleContext()

Gets the

AccessibleContext

associated with this

JProgressBar

. For progress bars, the

AccessibleContext

takes the form of an

AccessibleJProgressBar

.
A new

AccessibleJProgressBar

instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- an

AccessibleJProgressBar

that serves as the

AccessibleContext

of this

JProgressBar

---

### Additional Sections

#### Class JProgressBar

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JProgressBar

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JProgressBar

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JProgressBar

javax.swing.JComponent

- javax.swing.JProgressBar

javax.swing.JProgressBar

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
="A component that displays an integer value.")
public class
JProgressBar

extends
JComponent

implements
SwingConstants
,
Accessible
```

A component that visually displays the progress of some task. As the task
progresses towards completion, the progress bar displays the
task's percentage of completion.
This percentage is typically represented visually by a rectangle which
starts out empty and gradually becomes filled in as the task progresses.
In addition, the progress bar can display a textual representation of this
percentage.

JProgressBar

uses a

BoundedRangeModel

as its data model,
with the

value

property representing the "current" state of the task,
and the

minimum

and

maximum

properties representing the
beginning and end points, respectively.

To indicate that a task of unknown length is executing,
you can put a progress bar into indeterminate mode.
While the bar is in indeterminate mode,
it animates constantly to show that work is occurring.
As soon as you can determine the task's length and amount of progress,
you should update the progress bar's value
and switch it back to determinate mode.

Here is an example of creating a progress bar,
where

task

is an object (representing some piece of work)
which returns information about the progress of the task:

```java
progressBar = new JProgressBar(0, task.getLengthOfTask());
progressBar.setValue(0);
progressBar.setStringPainted(true);
```

Here is an example of querying the current state of the task, and using
the returned value to update the progress bar:

```java
progressBar.setValue(task.getCurrent());
```

Here is an example of putting a progress bar into
indeterminate mode,
and then switching back to determinate mode
once the length of the task is known:

```java
progressBar = new JProgressBar();

...//when the task of (initially) unknown length begins:

progressBar.setIndeterminate(true);

...//do some work; get length of task...

progressBar.setMaximum(newLength);
progressBar.setValue(newValue);
progressBar.setIndeterminate(false);
```

For complete examples and further documentation see

How to Monitor Progress

,
a section in

The Java Tutorial.

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
**See Also:** BasicProgressBarUI

,

BoundedRangeModel

,

SwingWorker

,

Serialized Form

@JavaBean

(

defaultProperty

="UI",

description

="A component that displays an integer value.")
public class

JProgressBar

extends

JComponent

implements

SwingConstants

,

Accessible

A component that visually displays the progress of some task. As the task
progresses towards completion, the progress bar displays the
task's percentage of completion.
This percentage is typically represented visually by a rectangle which
starts out empty and gradually becomes filled in as the task progresses.
In addition, the progress bar can display a textual representation of this
percentage.

JProgressBar

uses a

BoundedRangeModel

as its data model,
with the

value

property representing the "current" state of the task,
and the

minimum

and

maximum

properties representing the
beginning and end points, respectively.

To indicate that a task of unknown length is executing,
you can put a progress bar into indeterminate mode.
While the bar is in indeterminate mode,
it animates constantly to show that work is occurring.
As soon as you can determine the task's length and amount of progress,
you should update the progress bar's value
and switch it back to determinate mode.

Here is an example of creating a progress bar,
where

task

is an object (representing some piece of work)
which returns information about the progress of the task:

```java
progressBar = new JProgressBar(0, task.getLengthOfTask());
progressBar.setValue(0);
progressBar.setStringPainted(true);
```

Here is an example of querying the current state of the task, and using
the returned value to update the progress bar:

```java
progressBar.setValue(task.getCurrent());
```

Here is an example of putting a progress bar into
indeterminate mode,
and then switching back to determinate mode
once the length of the task is known:

```java
progressBar = new JProgressBar();

...//when the task of (initially) unknown length begins:

progressBar.setIndeterminate(true);

...//do some work; get length of task...

progressBar.setMaximum(newLength);
progressBar.setValue(newValue);
progressBar.setIndeterminate(false);
```

For complete examples and further documentation see

How to Monitor Progress

,
a section in

The Java Tutorial.

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

JProgressBar

uses a

BoundedRangeModel

as its data model,
with the

value

property representing the "current" state of the task,
and the

minimum

and

maximum

properties representing the
beginning and end points, respectively.

To indicate that a task of unknown length is executing,
you can put a progress bar into indeterminate mode.
While the bar is in indeterminate mode,
it animates constantly to show that work is occurring.
As soon as you can determine the task's length and amount of progress,
you should update the progress bar's value
and switch it back to determinate mode.

Here is an example of creating a progress bar,
where

task

is an object (representing some piece of work)
which returns information about the progress of the task:

```java
progressBar = new JProgressBar(0, task.getLengthOfTask());
progressBar.setValue(0);
progressBar.setStringPainted(true);
```

Here is an example of querying the current state of the task, and using
the returned value to update the progress bar:

```java
progressBar.setValue(task.getCurrent());
```

Here is an example of putting a progress bar into
indeterminate mode,
and then switching back to determinate mode
once the length of the task is known:

```java
progressBar = new JProgressBar();

...//when the task of (initially) unknown length begins:

progressBar.setIndeterminate(true);

...//do some work; get length of task...

progressBar.setMaximum(newLength);
progressBar.setValue(newValue);
progressBar.setIndeterminate(false);
```

For complete examples and further documentation see

How to Monitor Progress

,
a section in

The Java Tutorial.

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

To indicate that a task of unknown length is executing,
you can put a progress bar into indeterminate mode.
While the bar is in indeterminate mode,
it animates constantly to show that work is occurring.
As soon as you can determine the task's length and amount of progress,
you should update the progress bar's value
and switch it back to determinate mode.

Here is an example of creating a progress bar,
where

task

is an object (representing some piece of work)
which returns information about the progress of the task:

```java
progressBar = new JProgressBar(0, task.getLengthOfTask());
progressBar.setValue(0);
progressBar.setStringPainted(true);
```

Here is an example of querying the current state of the task, and using
the returned value to update the progress bar:

```java
progressBar.setValue(task.getCurrent());
```

Here is an example of putting a progress bar into
indeterminate mode,
and then switching back to determinate mode
once the length of the task is known:

```java
progressBar = new JProgressBar();

...//when the task of (initially) unknown length begins:

progressBar.setIndeterminate(true);

...//do some work; get length of task...

progressBar.setMaximum(newLength);
progressBar.setValue(newValue);
progressBar.setIndeterminate(false);
```

For complete examples and further documentation see

How to Monitor Progress

,
a section in

The Java Tutorial.

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

Here is an example of creating a progress bar,
where

task

is an object (representing some piece of work)
which returns information about the progress of the task:

```java
progressBar = new JProgressBar(0, task.getLengthOfTask());
progressBar.setValue(0);
progressBar.setStringPainted(true);
```

Here is an example of querying the current state of the task, and using
the returned value to update the progress bar:

```java
progressBar.setValue(task.getCurrent());
```

Here is an example of putting a progress bar into
indeterminate mode,
and then switching back to determinate mode
once the length of the task is known:

```java
progressBar = new JProgressBar();

...//when the task of (initially) unknown length begins:

progressBar.setIndeterminate(true);

...//do some work; get length of task...

progressBar.setMaximum(newLength);
progressBar.setValue(newValue);
progressBar.setIndeterminate(false);
```

For complete examples and further documentation see

How to Monitor Progress

,
a section in

The Java Tutorial.

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

progressBar = new JProgressBar(0, task.getLengthOfTask());
progressBar.setValue(0);
progressBar.setStringPainted(true);

progressBar.setValue(task.getCurrent());

progressBar = new JProgressBar();

...//when the task of (initially) unknown length begins:

progressBar.setIndeterminate(true);

...//do some work; get length of task...

progressBar.setMaximum(newLength);
progressBar.setValue(newValue);
progressBar.setIndeterminate(false);

For complete examples and further documentation see

How to Monitor Progress

,
a section in

The Java Tutorial.

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

JProgressBar.AccessibleJProgressBar

This class implements accessibility support for the

JProgressBar

class.

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

is needed per instance since the
event's only interesting property is the immutable source, which
is the progress bar.

protected

ChangeListener

changeListener

Listens for change events sent by the progress bar's model,
redispatching them
to change-event listeners registered upon
this progress bar.

protected

BoundedRangeModel

model

The object that holds the data for the progress bar.

protected int

orientation

Whether the progress bar is horizontal or vertical.

protected boolean

paintBorder

Whether to display a border around the progress bar.

protected boolean

paintString

Whether to display a string of text on the progress bar.

protected

String

progressString

An optional string that can be displayed on the progress bar.

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

JProgressBar

()

Creates a horizontal progress bar
that displays a border but no progress string.

JProgressBar

​(int orient)

Creates a progress bar with the specified orientation,
which can be
either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

JProgressBar

​(int min,
int max)

Creates a horizontal progress bar
with the specified minimum and maximum.

JProgressBar

​(int orient,
int min,
int max)

Creates a progress bar using the specified orientation,
minimum, and maximum.

JProgressBar

​(

BoundedRangeModel

newModel)

Creates a horizontal progress bar
that uses the specified model
to hold the progress bar's data.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addChangeListener

​(

ChangeListener

l)

Adds the specified

ChangeListener

to the progress bar.

protected

ChangeListener

createChangeListener

()

Subclasses that want to handle change events
from the model differently
can override this to return
an instance of a custom

ChangeListener

implementation.

protected void

fireStateChanged

()

Send a

ChangeEvent

, whose source is this

JProgressBar

, to
all

ChangeListener

s that have registered interest in

ChangeEvent

s.

AccessibleContext

getAccessibleContext

()

Gets the

AccessibleContext

associated with this

JProgressBar

.

ChangeListener

[]

getChangeListeners

()

Returns an array of all the

ChangeListener

s added
to this progress bar with

addChangeListener

.

int

getMaximum

()

Returns the progress bar's

maximum

value
from the

BoundedRangeModel

.

int

getMinimum

()

Returns the progress bar's

minimum

value
from the

BoundedRangeModel

.

BoundedRangeModel

getModel

()

Returns the data model used by this progress bar.

int

getOrientation

()

Returns

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

, depending on the orientation
of the progress bar.

double

getPercentComplete

()

Returns the percent complete for the progress bar.

String

getString

()

Returns a

String

representation of the current progress.

ProgressBarUI

getUI

()

Returns the look-and-feel object that renders this component.

String

getUIClassID

()

Returns the name of the look-and-feel class that renders this component.

int

getValue

()

Returns the progress bar's current

value

from the

BoundedRangeModel

.

boolean

isBorderPainted

()

Returns the

borderPainted

property.

boolean

isIndeterminate

()

Returns the value of the

indeterminate

property.

boolean

isStringPainted

()

Returns the value of the

stringPainted

property.

protected void

paintBorder

​(

Graphics

g)

Paints the progress bar's border if the

borderPainted

property is

true

.

protected

String

paramString

()

Returns a string representation of this

JProgressBar

.

void

removeChangeListener

​(

ChangeListener

l)

Removes a

ChangeListener

from the progress bar.

void

setBorderPainted

​(boolean b)

Sets the

borderPainted

property, which is

true

if the progress bar should paint its border.

void

setIndeterminate

​(boolean newValue)

Sets the

indeterminate

property of the progress bar,
which determines whether the progress bar is in determinate
or indeterminate mode.

void

setMaximum

​(int n)

Sets the progress bar's maximum value
(stored in the progress bar's data model) to

n

.

void

setMinimum

​(int n)

Sets the progress bar's minimum value
(stored in the progress bar's data model) to

n

.

void

setModel

​(

BoundedRangeModel

newModel)

Sets the data model used by the

JProgressBar

.

void

setOrientation

​(int newOrientation)

Sets the progress bar's orientation to

newOrientation

,
which must be

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

void

setString

​(

String

s)

Sets the value of the progress string.

void

setStringPainted

​(boolean b)

Sets the value of the

stringPainted

property,
which determines whether the progress bar
should render a progress string.

void

setUI

​(

ProgressBarUI

ui)

Sets the look-and-feel object that renders this component.

void

setValue

​(int n)

Sets the progress bar's current value to

n

.

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

add

,

add

,

add

,

add

,

add

,

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

remove

,

remove

,

removeAll

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

JProgressBar.AccessibleJProgressBar

This class implements accessibility support for the

JProgressBar

class.

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

JProgressBar

class.

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

is needed per instance since the
event's only interesting property is the immutable source, which
is the progress bar.

protected

ChangeListener

changeListener

Listens for change events sent by the progress bar's model,
redispatching them
to change-event listeners registered upon
this progress bar.

protected

BoundedRangeModel

model

The object that holds the data for the progress bar.

protected int

orientation

Whether the progress bar is horizontal or vertical.

protected boolean

paintBorder

Whether to display a border around the progress bar.

protected boolean

paintString

Whether to display a string of text on the progress bar.

protected

String

progressString

An optional string that can be displayed on the progress bar.

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

is needed per instance since the
event's only interesting property is the immutable source, which
is the progress bar.

Listens for change events sent by the progress bar's model,
redispatching them
to change-event listeners registered upon
this progress bar.

The object that holds the data for the progress bar.

Whether the progress bar is horizontal or vertical.

Whether to display a border around the progress bar.

Whether to display a string of text on the progress bar.

An optional string that can be displayed on the progress bar.

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

JProgressBar

()

Creates a horizontal progress bar
that displays a border but no progress string.

JProgressBar

​(int orient)

Creates a progress bar with the specified orientation,
which can be
either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

JProgressBar

​(int min,
int max)

Creates a horizontal progress bar
with the specified minimum and maximum.

JProgressBar

​(int orient,
int min,
int max)

Creates a progress bar using the specified orientation,
minimum, and maximum.

JProgressBar

​(

BoundedRangeModel

newModel)

Creates a horizontal progress bar
that uses the specified model
to hold the progress bar's data.

---

#### Constructor Summary

Creates a horizontal progress bar
that displays a border but no progress string.

Creates a progress bar with the specified orientation,
which can be
either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

Creates a horizontal progress bar
with the specified minimum and maximum.

Creates a progress bar using the specified orientation,
minimum, and maximum.

Creates a horizontal progress bar
that uses the specified model
to hold the progress bar's data.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addChangeListener

​(

ChangeListener

l)

Adds the specified

ChangeListener

to the progress bar.

protected

ChangeListener

createChangeListener

()

Subclasses that want to handle change events
from the model differently
can override this to return
an instance of a custom

ChangeListener

implementation.

protected void

fireStateChanged

()

Send a

ChangeEvent

, whose source is this

JProgressBar

, to
all

ChangeListener

s that have registered interest in

ChangeEvent

s.

AccessibleContext

getAccessibleContext

()

Gets the

AccessibleContext

associated with this

JProgressBar

.

ChangeListener

[]

getChangeListeners

()

Returns an array of all the

ChangeListener

s added
to this progress bar with

addChangeListener

.

int

getMaximum

()

Returns the progress bar's

maximum

value
from the

BoundedRangeModel

.

int

getMinimum

()

Returns the progress bar's

minimum

value
from the

BoundedRangeModel

.

BoundedRangeModel

getModel

()

Returns the data model used by this progress bar.

int

getOrientation

()

Returns

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

, depending on the orientation
of the progress bar.

double

getPercentComplete

()

Returns the percent complete for the progress bar.

String

getString

()

Returns a

String

representation of the current progress.

ProgressBarUI

getUI

()

Returns the look-and-feel object that renders this component.

String

getUIClassID

()

Returns the name of the look-and-feel class that renders this component.

int

getValue

()

Returns the progress bar's current

value

from the

BoundedRangeModel

.

boolean

isBorderPainted

()

Returns the

borderPainted

property.

boolean

isIndeterminate

()

Returns the value of the

indeterminate

property.

boolean

isStringPainted

()

Returns the value of the

stringPainted

property.

protected void

paintBorder

​(

Graphics

g)

Paints the progress bar's border if the

borderPainted

property is

true

.

protected

String

paramString

()

Returns a string representation of this

JProgressBar

.

void

removeChangeListener

​(

ChangeListener

l)

Removes a

ChangeListener

from the progress bar.

void

setBorderPainted

​(boolean b)

Sets the

borderPainted

property, which is

true

if the progress bar should paint its border.

void

setIndeterminate

​(boolean newValue)

Sets the

indeterminate

property of the progress bar,
which determines whether the progress bar is in determinate
or indeterminate mode.

void

setMaximum

​(int n)

Sets the progress bar's maximum value
(stored in the progress bar's data model) to

n

.

void

setMinimum

​(int n)

Sets the progress bar's minimum value
(stored in the progress bar's data model) to

n

.

void

setModel

​(

BoundedRangeModel

newModel)

Sets the data model used by the

JProgressBar

.

void

setOrientation

​(int newOrientation)

Sets the progress bar's orientation to

newOrientation

,
which must be

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

void

setString

​(

String

s)

Sets the value of the progress string.

void

setStringPainted

​(boolean b)

Sets the value of the

stringPainted

property,
which determines whether the progress bar
should render a progress string.

void

setUI

​(

ProgressBarUI

ui)

Sets the look-and-feel object that renders this component.

void

setValue

​(int n)

Sets the progress bar's current value to

n

.

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

add

,

add

,

add

,

add

,

add

,

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

remove

,

remove

,

removeAll

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

Adds the specified

ChangeListener

to the progress bar.

Subclasses that want to handle change events
from the model differently
can override this to return
an instance of a custom

ChangeListener

implementation.

Send a

ChangeEvent

, whose source is this

JProgressBar

, to
all

ChangeListener

s that have registered interest in

ChangeEvent

s.

Gets the

AccessibleContext

associated with this

JProgressBar

.

Returns an array of all the

ChangeListener

s added
to this progress bar with

addChangeListener

.

Returns the progress bar's

maximum

value
from the

BoundedRangeModel

.

Returns the progress bar's

minimum

value
from the

BoundedRangeModel

.

Returns the data model used by this progress bar.

Returns

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

, depending on the orientation
of the progress bar.

Returns the percent complete for the progress bar.

Returns a

String

representation of the current progress.

Returns the look-and-feel object that renders this component.

Returns the name of the look-and-feel class that renders this component.

Returns the progress bar's current

value

from the

BoundedRangeModel

.

Returns the

borderPainted

property.

Returns the value of the

indeterminate

property.

Returns the value of the

stringPainted

property.

Paints the progress bar's border if the

borderPainted

property is

true

.

Returns a string representation of this

JProgressBar

.

Removes a

ChangeListener

from the progress bar.

Sets the

borderPainted

property, which is

true

if the progress bar should paint its border.

Sets the

indeterminate

property of the progress bar,
which determines whether the progress bar is in determinate
or indeterminate mode.

Sets the progress bar's maximum value
(stored in the progress bar's data model) to

n

.

Sets the progress bar's minimum value
(stored in the progress bar's data model) to

n

.

Sets the data model used by the

JProgressBar

.

Sets the progress bar's orientation to

newOrientation

,
which must be

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

Sets the value of the progress string.

Sets the value of the

stringPainted

property,
which determines whether the progress bar
should render a progress string.

Sets the look-and-feel object that renders this component.

Sets the progress bar's current value to

n

.

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

add

,

add

,

add

,

add

,

add

,

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

remove

,

remove

,

removeAll

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

- orientation

```java
protected int orientation
```

Whether the progress bar is horizontal or vertical.
The default is

HORIZONTAL

.

**See Also:** setOrientation(int)

- paintBorder

```java
protected boolean paintBorder
```

Whether to display a border around the progress bar.
The default is

true

.

**See Also:** setBorderPainted(boolean)

- model

```java
protected
BoundedRangeModel
model
```

The object that holds the data for the progress bar.

**See Also:** setModel(javax.swing.BoundedRangeModel)

- progressString

```java
protected
String
progressString
```

An optional string that can be displayed on the progress bar.
The default is

null

. Setting this to a non-

null

value does not imply that the string will be displayed.
To display the string,

paintString

must be

true

.

**See Also:** setString(java.lang.String)

,

setStringPainted(boolean)

- paintString

```java
protected boolean paintString
```

Whether to display a string of text on the progress bar.
The default is

false

.
Setting this to

true

causes a textual
display of the progress to be rendered on the progress bar. If
the

progressString

is

null

,
the percentage of completion is displayed on the progress bar.
Otherwise, the

progressString

is
rendered on the progress bar.

**See Also:** setStringPainted(boolean)

,

setString(java.lang.String)

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one

ChangeEvent

is needed per instance since the
event's only interesting property is the immutable source, which
is the progress bar.
The event is lazily created the first time that an
event notification is fired.

**See Also:** fireStateChanged()

- changeListener

```java
protected
ChangeListener
changeListener
```

Listens for change events sent by the progress bar's model,
redispatching them
to change-event listeners registered upon
this progress bar.

**See Also:** createChangeListener()

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JProgressBar

```java
public JProgressBar()
```

Creates a horizontal progress bar
that displays a border but no progress string.
The initial and minimum values are 0,
and the maximum is 100.

**See Also:** setOrientation(int)

,

setBorderPainted(boolean)

,

setStringPainted(boolean)

,

setString(java.lang.String)

,

setIndeterminate(boolean)

- JProgressBar

```java
public JProgressBar​(int orient)
```

Creates a progress bar with the specified orientation,
which can be
either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.
By default, a border is painted but a progress string is not.
The initial and minimum values are 0,
and the maximum is 100.

**Parameters:** orient

- the desired orientation of the progress bar
**Throws:** IllegalArgumentException

- if

orient

is an illegal value
**See Also:** setOrientation(int)

,

setBorderPainted(boolean)

,

setStringPainted(boolean)

,

setString(java.lang.String)

,

setIndeterminate(boolean)

- JProgressBar

```java
public JProgressBar​(int min,
int max)
```

Creates a horizontal progress bar
with the specified minimum and maximum.
Sets the initial value of the progress bar to the specified minimum.
By default, a border is painted but a progress string is not.

The

BoundedRangeModel

that holds the progress bar's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the progress bar.
See the

BoundedRangeModel

documentation for details.

**Parameters:** min

- the minimum value of the progress bar
**Parameters:** max

- the maximum value of the progress bar
**See Also:** BoundedRangeModel

,

setOrientation(int)

,

setBorderPainted(boolean)

,

setStringPainted(boolean)

,

setString(java.lang.String)

,

setIndeterminate(boolean)

- JProgressBar

```java
public JProgressBar​(int orient,
int min,
int max)
```

Creates a progress bar using the specified orientation,
minimum, and maximum.
By default, a border is painted but a progress string is not.
Sets the initial value of the progress bar to the specified minimum.

The

BoundedRangeModel

that holds the progress bar's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the progress bar.
See the

BoundedRangeModel

documentation for details.

**Parameters:** orient

- the desired orientation of the progress bar
**Parameters:** min

- the minimum value of the progress bar
**Parameters:** max

- the maximum value of the progress bar
**Throws:** IllegalArgumentException

- if

orient

is an illegal value
**See Also:** BoundedRangeModel

,

setOrientation(int)

,

setBorderPainted(boolean)

,

setStringPainted(boolean)

,

setString(java.lang.String)

,

setIndeterminate(boolean)

- JProgressBar

```java
public JProgressBar​(
BoundedRangeModel
newModel)
```

Creates a horizontal progress bar
that uses the specified model
to hold the progress bar's data.
By default, a border is painted but a progress string is not.

**Parameters:** newModel

- the data model for the progress bar
**See Also:** setOrientation(int)

,

setBorderPainted(boolean)

,

setStringPainted(boolean)

,

setString(java.lang.String)

,

setIndeterminate(boolean)

============ METHOD DETAIL ==========

- Method Detail

- getOrientation

```java
public int getOrientation()
```

Returns

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

, depending on the orientation
of the progress bar. The default orientation is

SwingConstants.HORIZONTAL

.

**Returns:** HORIZONTAL

or

VERTICAL
**See Also:** setOrientation(int)

- setOrientation

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="Set the progress bar\'s orientation.")
public void setOrientation​(int newOrientation)
```

Sets the progress bar's orientation to

newOrientation

,
which must be

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

. The default orientation
is

SwingConstants.HORIZONTAL

.

**Parameters:** newOrientation

-

HORIZONTAL

or

VERTICAL
**Throws:** IllegalArgumentException

- if

newOrientation

is an illegal value
**See Also:** getOrientation()

- isStringPainted

```java
public boolean isStringPainted()
```

Returns the value of the

stringPainted

property.

**Returns:** the value of the

stringPainted

property
**See Also:** setStringPainted(boolean)

,

setString(java.lang.String)

- setStringPainted

```java
@BeanProperty
(
visualUpdate
=true,

description
="Whether the progress bar should render a string.")
public void setStringPainted​(boolean b)
```

Sets the value of the

stringPainted

property,
which determines whether the progress bar
should render a progress string.
The default is

false

, meaning
no string is painted.
Some look and feels might not support progress strings
or might support them only when the progress bar is in determinate mode.

**Parameters:** b

-

true

if the progress bar should render a string
**See Also:** isStringPainted()

,

setString(java.lang.String)

- getString

```java
public
String
getString()
```

Returns a

String

representation of the current progress.
By default, this returns a simple percentage

String

based on
the value returned from

getPercentComplete

. An example
would be the "42%". You can change this by calling

setString

.

**Returns:** the value of the progress string, or a simple percentage string
if the progress string is

null
**See Also:** setString(java.lang.String)

- setString

```java
@BeanProperty
(
visualUpdate
=true,

description
="Specifies the progress string to paint")
public void setString​(
String
s)
```

Sets the value of the progress string. By default,
this string is

null

, implying the built-in behavior of
using a simple percent string.
If you have provided a custom progress string and want to revert to
the built-in behavior, set the string back to

null

.

The progress string is painted only if
the

isStringPainted

method returns

true

.

**Parameters:** s

- the value of the progress string
**See Also:** getString()

,

setStringPainted(boolean)

,

isStringPainted()

- getPercentComplete

```java
@BeanProperty
(
bound
=false)
public double getPercentComplete()
```

Returns the percent complete for the progress bar.
Note that this number is between 0.0 and 1.0.

**Returns:** the percent complete for this progress bar

- isBorderPainted

```java
public boolean isBorderPainted()
```

Returns the

borderPainted

property.

**Returns:** the value of the

borderPainted

property
**See Also:** setBorderPainted(boolean)

- setBorderPainted

```java
@BeanProperty
(
visualUpdate
=true,

description
="Whether the progress bar should paint its border.")
public void setBorderPainted​(boolean b)
```

Sets the

borderPainted

property, which is

true

if the progress bar should paint its border.
The default value for this property is

true

.
Some look and feels might not implement painted borders;
they will ignore this property.

**Parameters:** b

-

true

if the progress bar
should paint its border;
otherwise,

false
**See Also:** isBorderPainted()

- paintBorder

```java
protected void paintBorder​(
Graphics
g)
```

Paints the progress bar's border if the

borderPainted

property is

true

.

**Overrides:** paintBorder

in class

JComponent
**Parameters:** g

- the

Graphics

context within which to paint the border
**See Also:** JComponent.paint(java.awt.Graphics)

,

JComponent.setBorder(javax.swing.border.Border)

,

isBorderPainted()

,

setBorderPainted(boolean)

- getUI

```java
public
ProgressBarUI
getUI()
```

Returns the look-and-feel object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

ProgressBarUI

object that renders this component

- setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
ProgressBarUI
ui)
```

Sets the look-and-feel object that renders this component.

**Parameters:** ui

- a

ProgressBarUI

object
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
=false,

expert
=true,

description
="A string that specifies the name of the look-and-feel class.")
public
String
getUIClassID()
```

Returns the name of the look-and-feel class that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "ProgressBarUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- createChangeListener

```java
protected
ChangeListener
createChangeListener()
```

Subclasses that want to handle change events
from the model differently
can override this to return
an instance of a custom

ChangeListener

implementation.
The default

ChangeListener

simply calls the

fireStateChanged

method to forward

ChangeEvent

s
to the

ChangeListener

s that have been added directly to the
progress bar.

**Returns:** the instance of a custom

ChangeListener

implementation.
**See Also:** changeListener

,

fireStateChanged()

,

ChangeListener

,

BoundedRangeModel

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds the specified

ChangeListener

to the progress bar.

**Parameters:** l

- the

ChangeListener

to add

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a

ChangeListener

from the progress bar.

**Parameters:** l

- the

ChangeListener

to remove

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
to this progress bar with

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

Send a

ChangeEvent

, whose source is this

JProgressBar

, to
all

ChangeListener

s that have registered interest in

ChangeEvent

s.
This method is called each time a

ChangeEvent

is received from
the model.

The event instance is created if necessary, and stored in

changeEvent

.

**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

EventListenerList

- getModel

```java
public
BoundedRangeModel
getModel()
```

Returns the data model used by this progress bar.

**Returns:** the

BoundedRangeModel

currently in use
**See Also:** setModel(javax.swing.BoundedRangeModel)

,

BoundedRangeModel

- setModel

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The data model used by the JProgressBar.")
public void setModel​(
BoundedRangeModel
newModel)
```

Sets the data model used by the

JProgressBar

.
Note that the

BoundedRangeModel

's

extent

is not used,
and is set to

0

.

**Parameters:** newModel

- the

BoundedRangeModel

to use

- getValue

```java
public int getValue()
```

Returns the progress bar's current

value

from the

BoundedRangeModel

.
The value is always between the
minimum and maximum values, inclusive.

**Returns:** the current value of the progress bar
**See Also:** setValue(int)

,

BoundedRangeModel.getValue()

- getMinimum

```java
public int getMinimum()
```

Returns the progress bar's

minimum

value
from the

BoundedRangeModel

.

**Returns:** the progress bar's minimum value
**See Also:** setMinimum(int)

,

BoundedRangeModel.getMinimum()

- getMaximum

```java
public int getMaximum()
```

Returns the progress bar's

maximum

value
from the

BoundedRangeModel

.

**Returns:** the progress bar's maximum value
**See Also:** setMaximum(int)

,

BoundedRangeModel.getMaximum()

- setValue

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The progress bar\'s current value.")
public void setValue​(int n)
```

Sets the progress bar's current value to

n

. This method
forwards the new value to the model.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new value is different from the previous value,
all change listeners are notified.

**Parameters:** n

- the new value
**See Also:** getValue()

,

addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.setValue(int)

- setMinimum

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The progress bar\'s minimum value.")
public void setMinimum​(int n)
```

Sets the progress bar's minimum value
(stored in the progress bar's data model) to

n

.

The data model (a

BoundedRangeModel

instance)
handles any mathematical
issues arising from assigning faulty values.
See the

BoundedRangeModel

documentation for details.

If the minimum value is different from the previous minimum,
all change listeners are notified.

**Parameters:** n

- the new minimum
**See Also:** getMinimum()

,

addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.setMinimum(int)

- setMaximum

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The progress bar\'s maximum value.")
public void setMaximum​(int n)
```

Sets the progress bar's maximum value
(stored in the progress bar's data model) to

n

.

The underlying

BoundedRangeModel

handles any mathematical
issues arising from assigning faulty values.
See the

BoundedRangeModel

documentation for details.

If the maximum value is different from the previous maximum,
all change listeners are notified.

**Parameters:** n

- the new maximum
**See Also:** getMaximum()

,

addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.setMaximum(int)

- setIndeterminate

```java
public void setIndeterminate​(boolean newValue)
```

Sets the

indeterminate

property of the progress bar,
which determines whether the progress bar is in determinate
or indeterminate mode.
An indeterminate progress bar continuously displays animation
indicating that an operation of unknown length is occurring.
By default, this property is

false

.
Some look and feels might not support indeterminate progress bars;
they will ignore this property.

See

How to Monitor Progress

for examples of using indeterminate progress bars.

**Parameters:** newValue

-

true

if the progress bar
should change to indeterminate mode;

false

if it should revert to normal.
**Since:** 1.4
**See Also:** isIndeterminate()

,

BasicProgressBarUI

- isIndeterminate

```java
@BeanProperty
(
bound
=false,

description
="Is the progress bar indeterminate (true) or normal (false)?")
public boolean isIndeterminate()
```

Returns the value of the

indeterminate

property.

**Returns:** the value of the

indeterminate

property
**Since:** 1.4
**See Also:** setIndeterminate(boolean)

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JProgressBar

.
This method is intended to be used only for debugging purposes. The
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

JProgressBar

- getAccessibleContext

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The AccessibleContext associated with this ProgressBar.")
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated with this

JProgressBar

. For progress bars, the

AccessibleContext

takes the form of an

AccessibleJProgressBar

.
A new

AccessibleJProgressBar

instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an

AccessibleJProgressBar

that serves as the

AccessibleContext

of this

JProgressBar

Field Detail

- orientation

```java
protected int orientation
```

Whether the progress bar is horizontal or vertical.
The default is

HORIZONTAL

.

**See Also:** setOrientation(int)

- paintBorder

```java
protected boolean paintBorder
```

Whether to display a border around the progress bar.
The default is

true

.

**See Also:** setBorderPainted(boolean)

- model

```java
protected
BoundedRangeModel
model
```

The object that holds the data for the progress bar.

**See Also:** setModel(javax.swing.BoundedRangeModel)

- progressString

```java
protected
String
progressString
```

An optional string that can be displayed on the progress bar.
The default is

null

. Setting this to a non-

null

value does not imply that the string will be displayed.
To display the string,

paintString

must be

true

.

**See Also:** setString(java.lang.String)

,

setStringPainted(boolean)

- paintString

```java
protected boolean paintString
```

Whether to display a string of text on the progress bar.
The default is

false

.
Setting this to

true

causes a textual
display of the progress to be rendered on the progress bar. If
the

progressString

is

null

,
the percentage of completion is displayed on the progress bar.
Otherwise, the

progressString

is
rendered on the progress bar.

**See Also:** setStringPainted(boolean)

,

setString(java.lang.String)

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one

ChangeEvent

is needed per instance since the
event's only interesting property is the immutable source, which
is the progress bar.
The event is lazily created the first time that an
event notification is fired.

**See Also:** fireStateChanged()

- changeListener

```java
protected
ChangeListener
changeListener
```

Listens for change events sent by the progress bar's model,
redispatching them
to change-event listeners registered upon
this progress bar.

**See Also:** createChangeListener()

---

#### Field Detail

orientation

```java
protected int orientation
```

Whether the progress bar is horizontal or vertical.
The default is

HORIZONTAL

.

**See Also:** setOrientation(int)

---

#### orientation

protected int orientation

Whether the progress bar is horizontal or vertical.
The default is

HORIZONTAL

.

paintBorder

```java
protected boolean paintBorder
```

Whether to display a border around the progress bar.
The default is

true

.

**See Also:** setBorderPainted(boolean)

---

#### paintBorder

protected boolean paintBorder

Whether to display a border around the progress bar.
The default is

true

.

model

```java
protected
BoundedRangeModel
model
```

The object that holds the data for the progress bar.

**See Also:** setModel(javax.swing.BoundedRangeModel)

---

#### model

protected

BoundedRangeModel

model

The object that holds the data for the progress bar.

progressString

```java
protected
String
progressString
```

An optional string that can be displayed on the progress bar.
The default is

null

. Setting this to a non-

null

value does not imply that the string will be displayed.
To display the string,

paintString

must be

true

.

**See Also:** setString(java.lang.String)

,

setStringPainted(boolean)

---

#### progressString

protected

String

progressString

An optional string that can be displayed on the progress bar.
The default is

null

. Setting this to a non-

null

value does not imply that the string will be displayed.
To display the string,

paintString

must be

true

.

paintString

```java
protected boolean paintString
```

Whether to display a string of text on the progress bar.
The default is

false

.
Setting this to

true

causes a textual
display of the progress to be rendered on the progress bar. If
the

progressString

is

null

,
the percentage of completion is displayed on the progress bar.
Otherwise, the

progressString

is
rendered on the progress bar.

**See Also:** setStringPainted(boolean)

,

setString(java.lang.String)

---

#### paintString

protected boolean paintString

Whether to display a string of text on the progress bar.
The default is

false

.
Setting this to

true

causes a textual
display of the progress to be rendered on the progress bar. If
the

progressString

is

null

,
the percentage of completion is displayed on the progress bar.
Otherwise, the

progressString

is
rendered on the progress bar.

changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one

ChangeEvent

is needed per instance since the
event's only interesting property is the immutable source, which
is the progress bar.
The event is lazily created the first time that an
event notification is fired.

**See Also:** fireStateChanged()

---

#### changeEvent

protected transient

ChangeEvent

changeEvent

Only one

ChangeEvent

is needed per instance since the
event's only interesting property is the immutable source, which
is the progress bar.
The event is lazily created the first time that an
event notification is fired.

changeListener

```java
protected
ChangeListener
changeListener
```

Listens for change events sent by the progress bar's model,
redispatching them
to change-event listeners registered upon
this progress bar.

**See Also:** createChangeListener()

---

#### changeListener

protected

ChangeListener

changeListener

Listens for change events sent by the progress bar's model,
redispatching them
to change-event listeners registered upon
this progress bar.

Constructor Detail

- JProgressBar

```java
public JProgressBar()
```

Creates a horizontal progress bar
that displays a border but no progress string.
The initial and minimum values are 0,
and the maximum is 100.

**See Also:** setOrientation(int)

,

setBorderPainted(boolean)

,

setStringPainted(boolean)

,

setString(java.lang.String)

,

setIndeterminate(boolean)

- JProgressBar

```java
public JProgressBar​(int orient)
```

Creates a progress bar with the specified orientation,
which can be
either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.
By default, a border is painted but a progress string is not.
The initial and minimum values are 0,
and the maximum is 100.

**Parameters:** orient

- the desired orientation of the progress bar
**Throws:** IllegalArgumentException

- if

orient

is an illegal value
**See Also:** setOrientation(int)

,

setBorderPainted(boolean)

,

setStringPainted(boolean)

,

setString(java.lang.String)

,

setIndeterminate(boolean)

- JProgressBar

```java
public JProgressBar​(int min,
int max)
```

Creates a horizontal progress bar
with the specified minimum and maximum.
Sets the initial value of the progress bar to the specified minimum.
By default, a border is painted but a progress string is not.

The

BoundedRangeModel

that holds the progress bar's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the progress bar.
See the

BoundedRangeModel

documentation for details.

**Parameters:** min

- the minimum value of the progress bar
**Parameters:** max

- the maximum value of the progress bar
**See Also:** BoundedRangeModel

,

setOrientation(int)

,

setBorderPainted(boolean)

,

setStringPainted(boolean)

,

setString(java.lang.String)

,

setIndeterminate(boolean)

- JProgressBar

```java
public JProgressBar​(int orient,
int min,
int max)
```

Creates a progress bar using the specified orientation,
minimum, and maximum.
By default, a border is painted but a progress string is not.
Sets the initial value of the progress bar to the specified minimum.

The

BoundedRangeModel

that holds the progress bar's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the progress bar.
See the

BoundedRangeModel

documentation for details.

**Parameters:** orient

- the desired orientation of the progress bar
**Parameters:** min

- the minimum value of the progress bar
**Parameters:** max

- the maximum value of the progress bar
**Throws:** IllegalArgumentException

- if

orient

is an illegal value
**See Also:** BoundedRangeModel

,

setOrientation(int)

,

setBorderPainted(boolean)

,

setStringPainted(boolean)

,

setString(java.lang.String)

,

setIndeterminate(boolean)

- JProgressBar

```java
public JProgressBar​(
BoundedRangeModel
newModel)
```

Creates a horizontal progress bar
that uses the specified model
to hold the progress bar's data.
By default, a border is painted but a progress string is not.

**Parameters:** newModel

- the data model for the progress bar
**See Also:** setOrientation(int)

,

setBorderPainted(boolean)

,

setStringPainted(boolean)

,

setString(java.lang.String)

,

setIndeterminate(boolean)

---

#### Constructor Detail

JProgressBar

```java
public JProgressBar()
```

Creates a horizontal progress bar
that displays a border but no progress string.
The initial and minimum values are 0,
and the maximum is 100.

**See Also:** setOrientation(int)

,

setBorderPainted(boolean)

,

setStringPainted(boolean)

,

setString(java.lang.String)

,

setIndeterminate(boolean)

---

#### JProgressBar

public JProgressBar()

Creates a horizontal progress bar
that displays a border but no progress string.
The initial and minimum values are 0,
and the maximum is 100.

JProgressBar

```java
public JProgressBar​(int orient)
```

Creates a progress bar with the specified orientation,
which can be
either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.
By default, a border is painted but a progress string is not.
The initial and minimum values are 0,
and the maximum is 100.

**Parameters:** orient

- the desired orientation of the progress bar
**Throws:** IllegalArgumentException

- if

orient

is an illegal value
**See Also:** setOrientation(int)

,

setBorderPainted(boolean)

,

setStringPainted(boolean)

,

setString(java.lang.String)

,

setIndeterminate(boolean)

---

#### JProgressBar

public JProgressBar​(int orient)

Creates a progress bar with the specified orientation,
which can be
either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.
By default, a border is painted but a progress string is not.
The initial and minimum values are 0,
and the maximum is 100.

JProgressBar

```java
public JProgressBar​(int min,
int max)
```

Creates a horizontal progress bar
with the specified minimum and maximum.
Sets the initial value of the progress bar to the specified minimum.
By default, a border is painted but a progress string is not.

The

BoundedRangeModel

that holds the progress bar's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the progress bar.
See the

BoundedRangeModel

documentation for details.

**Parameters:** min

- the minimum value of the progress bar
**Parameters:** max

- the maximum value of the progress bar
**See Also:** BoundedRangeModel

,

setOrientation(int)

,

setBorderPainted(boolean)

,

setStringPainted(boolean)

,

setString(java.lang.String)

,

setIndeterminate(boolean)

---

#### JProgressBar

public JProgressBar​(int min,
int max)

Creates a horizontal progress bar
with the specified minimum and maximum.
Sets the initial value of the progress bar to the specified minimum.
By default, a border is painted but a progress string is not.

The

BoundedRangeModel

that holds the progress bar's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the progress bar.
See the

BoundedRangeModel

documentation for details.

The

BoundedRangeModel

that holds the progress bar's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the progress bar.
See the

BoundedRangeModel

documentation for details.

JProgressBar

```java
public JProgressBar​(int orient,
int min,
int max)
```

Creates a progress bar using the specified orientation,
minimum, and maximum.
By default, a border is painted but a progress string is not.
Sets the initial value of the progress bar to the specified minimum.

The

BoundedRangeModel

that holds the progress bar's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the progress bar.
See the

BoundedRangeModel

documentation for details.

**Parameters:** orient

- the desired orientation of the progress bar
**Parameters:** min

- the minimum value of the progress bar
**Parameters:** max

- the maximum value of the progress bar
**Throws:** IllegalArgumentException

- if

orient

is an illegal value
**See Also:** BoundedRangeModel

,

setOrientation(int)

,

setBorderPainted(boolean)

,

setStringPainted(boolean)

,

setString(java.lang.String)

,

setIndeterminate(boolean)

---

#### JProgressBar

public JProgressBar​(int orient,
int min,
int max)

Creates a progress bar using the specified orientation,
minimum, and maximum.
By default, a border is painted but a progress string is not.
Sets the initial value of the progress bar to the specified minimum.

The

BoundedRangeModel

that holds the progress bar's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the progress bar.
See the

BoundedRangeModel

documentation for details.

The

BoundedRangeModel

that holds the progress bar's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the progress bar.
See the

BoundedRangeModel

documentation for details.

JProgressBar

```java
public JProgressBar​(
BoundedRangeModel
newModel)
```

Creates a horizontal progress bar
that uses the specified model
to hold the progress bar's data.
By default, a border is painted but a progress string is not.

**Parameters:** newModel

- the data model for the progress bar
**See Also:** setOrientation(int)

,

setBorderPainted(boolean)

,

setStringPainted(boolean)

,

setString(java.lang.String)

,

setIndeterminate(boolean)

---

#### JProgressBar

public JProgressBar​(

BoundedRangeModel

newModel)

Creates a horizontal progress bar
that uses the specified model
to hold the progress bar's data.
By default, a border is painted but a progress string is not.

Method Detail

- getOrientation

```java
public int getOrientation()
```

Returns

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

, depending on the orientation
of the progress bar. The default orientation is

SwingConstants.HORIZONTAL

.

**Returns:** HORIZONTAL

or

VERTICAL
**See Also:** setOrientation(int)

- setOrientation

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="Set the progress bar\'s orientation.")
public void setOrientation​(int newOrientation)
```

Sets the progress bar's orientation to

newOrientation

,
which must be

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

. The default orientation
is

SwingConstants.HORIZONTAL

.

**Parameters:** newOrientation

-

HORIZONTAL

or

VERTICAL
**Throws:** IllegalArgumentException

- if

newOrientation

is an illegal value
**See Also:** getOrientation()

- isStringPainted

```java
public boolean isStringPainted()
```

Returns the value of the

stringPainted

property.

**Returns:** the value of the

stringPainted

property
**See Also:** setStringPainted(boolean)

,

setString(java.lang.String)

- setStringPainted

```java
@BeanProperty
(
visualUpdate
=true,

description
="Whether the progress bar should render a string.")
public void setStringPainted​(boolean b)
```

Sets the value of the

stringPainted

property,
which determines whether the progress bar
should render a progress string.
The default is

false

, meaning
no string is painted.
Some look and feels might not support progress strings
or might support them only when the progress bar is in determinate mode.

**Parameters:** b

-

true

if the progress bar should render a string
**See Also:** isStringPainted()

,

setString(java.lang.String)

- getString

```java
public
String
getString()
```

Returns a

String

representation of the current progress.
By default, this returns a simple percentage

String

based on
the value returned from

getPercentComplete

. An example
would be the "42%". You can change this by calling

setString

.

**Returns:** the value of the progress string, or a simple percentage string
if the progress string is

null
**See Also:** setString(java.lang.String)

- setString

```java
@BeanProperty
(
visualUpdate
=true,

description
="Specifies the progress string to paint")
public void setString​(
String
s)
```

Sets the value of the progress string. By default,
this string is

null

, implying the built-in behavior of
using a simple percent string.
If you have provided a custom progress string and want to revert to
the built-in behavior, set the string back to

null

.

The progress string is painted only if
the

isStringPainted

method returns

true

.

**Parameters:** s

- the value of the progress string
**See Also:** getString()

,

setStringPainted(boolean)

,

isStringPainted()

- getPercentComplete

```java
@BeanProperty
(
bound
=false)
public double getPercentComplete()
```

Returns the percent complete for the progress bar.
Note that this number is between 0.0 and 1.0.

**Returns:** the percent complete for this progress bar

- isBorderPainted

```java
public boolean isBorderPainted()
```

Returns the

borderPainted

property.

**Returns:** the value of the

borderPainted

property
**See Also:** setBorderPainted(boolean)

- setBorderPainted

```java
@BeanProperty
(
visualUpdate
=true,

description
="Whether the progress bar should paint its border.")
public void setBorderPainted​(boolean b)
```

Sets the

borderPainted

property, which is

true

if the progress bar should paint its border.
The default value for this property is

true

.
Some look and feels might not implement painted borders;
they will ignore this property.

**Parameters:** b

-

true

if the progress bar
should paint its border;
otherwise,

false
**See Also:** isBorderPainted()

- paintBorder

```java
protected void paintBorder​(
Graphics
g)
```

Paints the progress bar's border if the

borderPainted

property is

true

.

**Overrides:** paintBorder

in class

JComponent
**Parameters:** g

- the

Graphics

context within which to paint the border
**See Also:** JComponent.paint(java.awt.Graphics)

,

JComponent.setBorder(javax.swing.border.Border)

,

isBorderPainted()

,

setBorderPainted(boolean)

- getUI

```java
public
ProgressBarUI
getUI()
```

Returns the look-and-feel object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

ProgressBarUI

object that renders this component

- setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
ProgressBarUI
ui)
```

Sets the look-and-feel object that renders this component.

**Parameters:** ui

- a

ProgressBarUI

object
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
=false,

expert
=true,

description
="A string that specifies the name of the look-and-feel class.")
public
String
getUIClassID()
```

Returns the name of the look-and-feel class that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "ProgressBarUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- createChangeListener

```java
protected
ChangeListener
createChangeListener()
```

Subclasses that want to handle change events
from the model differently
can override this to return
an instance of a custom

ChangeListener

implementation.
The default

ChangeListener

simply calls the

fireStateChanged

method to forward

ChangeEvent

s
to the

ChangeListener

s that have been added directly to the
progress bar.

**Returns:** the instance of a custom

ChangeListener

implementation.
**See Also:** changeListener

,

fireStateChanged()

,

ChangeListener

,

BoundedRangeModel

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds the specified

ChangeListener

to the progress bar.

**Parameters:** l

- the

ChangeListener

to add

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a

ChangeListener

from the progress bar.

**Parameters:** l

- the

ChangeListener

to remove

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
to this progress bar with

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

Send a

ChangeEvent

, whose source is this

JProgressBar

, to
all

ChangeListener

s that have registered interest in

ChangeEvent

s.
This method is called each time a

ChangeEvent

is received from
the model.

The event instance is created if necessary, and stored in

changeEvent

.

**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

EventListenerList

- getModel

```java
public
BoundedRangeModel
getModel()
```

Returns the data model used by this progress bar.

**Returns:** the

BoundedRangeModel

currently in use
**See Also:** setModel(javax.swing.BoundedRangeModel)

,

BoundedRangeModel

- setModel

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The data model used by the JProgressBar.")
public void setModel​(
BoundedRangeModel
newModel)
```

Sets the data model used by the

JProgressBar

.
Note that the

BoundedRangeModel

's

extent

is not used,
and is set to

0

.

**Parameters:** newModel

- the

BoundedRangeModel

to use

- getValue

```java
public int getValue()
```

Returns the progress bar's current

value

from the

BoundedRangeModel

.
The value is always between the
minimum and maximum values, inclusive.

**Returns:** the current value of the progress bar
**See Also:** setValue(int)

,

BoundedRangeModel.getValue()

- getMinimum

```java
public int getMinimum()
```

Returns the progress bar's

minimum

value
from the

BoundedRangeModel

.

**Returns:** the progress bar's minimum value
**See Also:** setMinimum(int)

,

BoundedRangeModel.getMinimum()

- getMaximum

```java
public int getMaximum()
```

Returns the progress bar's

maximum

value
from the

BoundedRangeModel

.

**Returns:** the progress bar's maximum value
**See Also:** setMaximum(int)

,

BoundedRangeModel.getMaximum()

- setValue

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The progress bar\'s current value.")
public void setValue​(int n)
```

Sets the progress bar's current value to

n

. This method
forwards the new value to the model.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new value is different from the previous value,
all change listeners are notified.

**Parameters:** n

- the new value
**See Also:** getValue()

,

addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.setValue(int)

- setMinimum

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The progress bar\'s minimum value.")
public void setMinimum​(int n)
```

Sets the progress bar's minimum value
(stored in the progress bar's data model) to

n

.

The data model (a

BoundedRangeModel

instance)
handles any mathematical
issues arising from assigning faulty values.
See the

BoundedRangeModel

documentation for details.

If the minimum value is different from the previous minimum,
all change listeners are notified.

**Parameters:** n

- the new minimum
**See Also:** getMinimum()

,

addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.setMinimum(int)

- setMaximum

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The progress bar\'s maximum value.")
public void setMaximum​(int n)
```

Sets the progress bar's maximum value
(stored in the progress bar's data model) to

n

.

The underlying

BoundedRangeModel

handles any mathematical
issues arising from assigning faulty values.
See the

BoundedRangeModel

documentation for details.

If the maximum value is different from the previous maximum,
all change listeners are notified.

**Parameters:** n

- the new maximum
**See Also:** getMaximum()

,

addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.setMaximum(int)

- setIndeterminate

```java
public void setIndeterminate​(boolean newValue)
```

Sets the

indeterminate

property of the progress bar,
which determines whether the progress bar is in determinate
or indeterminate mode.
An indeterminate progress bar continuously displays animation
indicating that an operation of unknown length is occurring.
By default, this property is

false

.
Some look and feels might not support indeterminate progress bars;
they will ignore this property.

See

How to Monitor Progress

for examples of using indeterminate progress bars.

**Parameters:** newValue

-

true

if the progress bar
should change to indeterminate mode;

false

if it should revert to normal.
**Since:** 1.4
**See Also:** isIndeterminate()

,

BasicProgressBarUI

- isIndeterminate

```java
@BeanProperty
(
bound
=false,

description
="Is the progress bar indeterminate (true) or normal (false)?")
public boolean isIndeterminate()
```

Returns the value of the

indeterminate

property.

**Returns:** the value of the

indeterminate

property
**Since:** 1.4
**See Also:** setIndeterminate(boolean)

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JProgressBar

.
This method is intended to be used only for debugging purposes. The
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

JProgressBar

- getAccessibleContext

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The AccessibleContext associated with this ProgressBar.")
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated with this

JProgressBar

. For progress bars, the

AccessibleContext

takes the form of an

AccessibleJProgressBar

.
A new

AccessibleJProgressBar

instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an

AccessibleJProgressBar

that serves as the

AccessibleContext

of this

JProgressBar

---

#### Method Detail

getOrientation

```java
public int getOrientation()
```

Returns

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

, depending on the orientation
of the progress bar. The default orientation is

SwingConstants.HORIZONTAL

.

**Returns:** HORIZONTAL

or

VERTICAL
**See Also:** setOrientation(int)

---

#### getOrientation

public int getOrientation()

Returns

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

, depending on the orientation
of the progress bar. The default orientation is

SwingConstants.HORIZONTAL

.

setOrientation

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="Set the progress bar\'s orientation.")
public void setOrientation​(int newOrientation)
```

Sets the progress bar's orientation to

newOrientation

,
which must be

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

. The default orientation
is

SwingConstants.HORIZONTAL

.

**Parameters:** newOrientation

-

HORIZONTAL

or

VERTICAL
**Throws:** IllegalArgumentException

- if

newOrientation

is an illegal value
**See Also:** getOrientation()

---

#### setOrientation

@BeanProperty

(

preferred

=true,

visualUpdate

=true,

description

="Set the progress bar\'s orientation.")
public void setOrientation​(int newOrientation)

Sets the progress bar's orientation to

newOrientation

,
which must be

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

. The default orientation
is

SwingConstants.HORIZONTAL

.

isStringPainted

```java
public boolean isStringPainted()
```

Returns the value of the

stringPainted

property.

**Returns:** the value of the

stringPainted

property
**See Also:** setStringPainted(boolean)

,

setString(java.lang.String)

---

#### isStringPainted

public boolean isStringPainted()

Returns the value of the

stringPainted

property.

setStringPainted

```java
@BeanProperty
(
visualUpdate
=true,

description
="Whether the progress bar should render a string.")
public void setStringPainted​(boolean b)
```

Sets the value of the

stringPainted

property,
which determines whether the progress bar
should render a progress string.
The default is

false

, meaning
no string is painted.
Some look and feels might not support progress strings
or might support them only when the progress bar is in determinate mode.

**Parameters:** b

-

true

if the progress bar should render a string
**See Also:** isStringPainted()

,

setString(java.lang.String)

---

#### setStringPainted

@BeanProperty

(

visualUpdate

=true,

description

="Whether the progress bar should render a string.")
public void setStringPainted​(boolean b)

Sets the value of the

stringPainted

property,
which determines whether the progress bar
should render a progress string.
The default is

false

, meaning
no string is painted.
Some look and feels might not support progress strings
or might support them only when the progress bar is in determinate mode.

getString

```java
public
String
getString()
```

Returns a

String

representation of the current progress.
By default, this returns a simple percentage

String

based on
the value returned from

getPercentComplete

. An example
would be the "42%". You can change this by calling

setString

.

**Returns:** the value of the progress string, or a simple percentage string
if the progress string is

null
**See Also:** setString(java.lang.String)

---

#### getString

public

String

getString()

Returns a

String

representation of the current progress.
By default, this returns a simple percentage

String

based on
the value returned from

getPercentComplete

. An example
would be the "42%". You can change this by calling

setString

.

setString

```java
@BeanProperty
(
visualUpdate
=true,

description
="Specifies the progress string to paint")
public void setString​(
String
s)
```

Sets the value of the progress string. By default,
this string is

null

, implying the built-in behavior of
using a simple percent string.
If you have provided a custom progress string and want to revert to
the built-in behavior, set the string back to

null

.

The progress string is painted only if
the

isStringPainted

method returns

true

.

**Parameters:** s

- the value of the progress string
**See Also:** getString()

,

setStringPainted(boolean)

,

isStringPainted()

---

#### setString

@BeanProperty

(

visualUpdate

=true,

description

="Specifies the progress string to paint")
public void setString​(

String

s)

Sets the value of the progress string. By default,
this string is

null

, implying the built-in behavior of
using a simple percent string.
If you have provided a custom progress string and want to revert to
the built-in behavior, set the string back to

null

.

The progress string is painted only if
the

isStringPainted

method returns

true

.

The progress string is painted only if
the

isStringPainted

method returns

true

.

getPercentComplete

```java
@BeanProperty
(
bound
=false)
public double getPercentComplete()
```

Returns the percent complete for the progress bar.
Note that this number is between 0.0 and 1.0.

**Returns:** the percent complete for this progress bar

---

#### getPercentComplete

@BeanProperty

(

bound

=false)
public double getPercentComplete()

Returns the percent complete for the progress bar.
Note that this number is between 0.0 and 1.0.

isBorderPainted

```java
public boolean isBorderPainted()
```

Returns the

borderPainted

property.

**Returns:** the value of the

borderPainted

property
**See Also:** setBorderPainted(boolean)

---

#### isBorderPainted

public boolean isBorderPainted()

Returns the

borderPainted

property.

setBorderPainted

```java
@BeanProperty
(
visualUpdate
=true,

description
="Whether the progress bar should paint its border.")
public void setBorderPainted​(boolean b)
```

Sets the

borderPainted

property, which is

true

if the progress bar should paint its border.
The default value for this property is

true

.
Some look and feels might not implement painted borders;
they will ignore this property.

**Parameters:** b

-

true

if the progress bar
should paint its border;
otherwise,

false
**See Also:** isBorderPainted()

---

#### setBorderPainted

@BeanProperty

(

visualUpdate

=true,

description

="Whether the progress bar should paint its border.")
public void setBorderPainted​(boolean b)

Sets the

borderPainted

property, which is

true

if the progress bar should paint its border.
The default value for this property is

true

.
Some look and feels might not implement painted borders;
they will ignore this property.

paintBorder

```java
protected void paintBorder​(
Graphics
g)
```

Paints the progress bar's border if the

borderPainted

property is

true

.

**Overrides:** paintBorder

in class

JComponent
**Parameters:** g

- the

Graphics

context within which to paint the border
**See Also:** JComponent.paint(java.awt.Graphics)

,

JComponent.setBorder(javax.swing.border.Border)

,

isBorderPainted()

,

setBorderPainted(boolean)

---

#### paintBorder

protected void paintBorder​(

Graphics

g)

Paints the progress bar's border if the

borderPainted

property is

true

.

getUI

```java
public
ProgressBarUI
getUI()
```

Returns the look-and-feel object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

ProgressBarUI

object that renders this component

---

#### getUI

public

ProgressBarUI

getUI()

Returns the look-and-feel object that renders this component.

setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
ProgressBarUI
ui)
```

Sets the look-and-feel object that renders this component.

**Parameters:** ui

- a

ProgressBarUI

object
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

="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(

ProgressBarUI

ui)

Sets the look-and-feel object that renders this component.

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
=false,

expert
=true,

description
="A string that specifies the name of the look-and-feel class.")
public
String
getUIClassID()
```

Returns the name of the look-and-feel class that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "ProgressBarUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### getUIClassID

@BeanProperty

(

bound

=false,

expert

=true,

description

="A string that specifies the name of the look-and-feel class.")
public

String

getUIClassID()

Returns the name of the look-and-feel class that renders this component.

createChangeListener

```java
protected
ChangeListener
createChangeListener()
```

Subclasses that want to handle change events
from the model differently
can override this to return
an instance of a custom

ChangeListener

implementation.
The default

ChangeListener

simply calls the

fireStateChanged

method to forward

ChangeEvent

s
to the

ChangeListener

s that have been added directly to the
progress bar.

**Returns:** the instance of a custom

ChangeListener

implementation.
**See Also:** changeListener

,

fireStateChanged()

,

ChangeListener

,

BoundedRangeModel

---

#### createChangeListener

protected

ChangeListener

createChangeListener()

Subclasses that want to handle change events
from the model differently
can override this to return
an instance of a custom

ChangeListener

implementation.
The default

ChangeListener

simply calls the

fireStateChanged

method to forward

ChangeEvent

s
to the

ChangeListener

s that have been added directly to the
progress bar.

addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds the specified

ChangeListener

to the progress bar.

**Parameters:** l

- the

ChangeListener

to add

---

#### addChangeListener

public void addChangeListener​(

ChangeListener

l)

Adds the specified

ChangeListener

to the progress bar.

removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a

ChangeListener

from the progress bar.

**Parameters:** l

- the

ChangeListener

to remove

---

#### removeChangeListener

public void removeChangeListener​(

ChangeListener

l)

Removes a

ChangeListener

from the progress bar.

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
to this progress bar with

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
to this progress bar with

addChangeListener

.

fireStateChanged

```java
protected void fireStateChanged()
```

Send a

ChangeEvent

, whose source is this

JProgressBar

, to
all

ChangeListener

s that have registered interest in

ChangeEvent

s.
This method is called each time a

ChangeEvent

is received from
the model.

The event instance is created if necessary, and stored in

changeEvent

.

**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

EventListenerList

---

#### fireStateChanged

protected void fireStateChanged()

Send a

ChangeEvent

, whose source is this

JProgressBar

, to
all

ChangeListener

s that have registered interest in

ChangeEvent

s.
This method is called each time a

ChangeEvent

is received from
the model.

The event instance is created if necessary, and stored in

changeEvent

.

The event instance is created if necessary, and stored in

changeEvent

.

getModel

```java
public
BoundedRangeModel
getModel()
```

Returns the data model used by this progress bar.

**Returns:** the

BoundedRangeModel

currently in use
**See Also:** setModel(javax.swing.BoundedRangeModel)

,

BoundedRangeModel

---

#### getModel

public

BoundedRangeModel

getModel()

Returns the data model used by this progress bar.

setModel

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The data model used by the JProgressBar.")
public void setModel​(
BoundedRangeModel
newModel)
```

Sets the data model used by the

JProgressBar

.
Note that the

BoundedRangeModel

's

extent

is not used,
and is set to

0

.

**Parameters:** newModel

- the

BoundedRangeModel

to use

---

#### setModel

@BeanProperty

(

bound

=false,

expert

=true,

description

="The data model used by the JProgressBar.")
public void setModel​(

BoundedRangeModel

newModel)

Sets the data model used by the

JProgressBar

.
Note that the

BoundedRangeModel

's

extent

is not used,
and is set to

0

.

getValue

```java
public int getValue()
```

Returns the progress bar's current

value

from the

BoundedRangeModel

.
The value is always between the
minimum and maximum values, inclusive.

**Returns:** the current value of the progress bar
**See Also:** setValue(int)

,

BoundedRangeModel.getValue()

---

#### getValue

public int getValue()

Returns the progress bar's current

value

from the

BoundedRangeModel

.
The value is always between the
minimum and maximum values, inclusive.

getMinimum

```java
public int getMinimum()
```

Returns the progress bar's

minimum

value
from the

BoundedRangeModel

.

**Returns:** the progress bar's minimum value
**See Also:** setMinimum(int)

,

BoundedRangeModel.getMinimum()

---

#### getMinimum

public int getMinimum()

Returns the progress bar's

minimum

value
from the

BoundedRangeModel

.

getMaximum

```java
public int getMaximum()
```

Returns the progress bar's

maximum

value
from the

BoundedRangeModel

.

**Returns:** the progress bar's maximum value
**See Also:** setMaximum(int)

,

BoundedRangeModel.getMaximum()

---

#### getMaximum

public int getMaximum()

Returns the progress bar's

maximum

value
from the

BoundedRangeModel

.

setValue

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The progress bar\'s current value.")
public void setValue​(int n)
```

Sets the progress bar's current value to

n

. This method
forwards the new value to the model.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new value is different from the previous value,
all change listeners are notified.

**Parameters:** n

- the new value
**See Also:** getValue()

,

addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.setValue(int)

---

#### setValue

@BeanProperty

(

bound

=false,

preferred

=true,

description

="The progress bar\'s current value.")
public void setValue​(int n)

Sets the progress bar's current value to

n

. This method
forwards the new value to the model.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new value is different from the previous value,
all change listeners are notified.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new value is different from the previous value,
all change listeners are notified.

If the new value is different from the previous value,
all change listeners are notified.

setMinimum

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The progress bar\'s minimum value.")
public void setMinimum​(int n)
```

Sets the progress bar's minimum value
(stored in the progress bar's data model) to

n

.

The data model (a

BoundedRangeModel

instance)
handles any mathematical
issues arising from assigning faulty values.
See the

BoundedRangeModel

documentation for details.

If the minimum value is different from the previous minimum,
all change listeners are notified.

**Parameters:** n

- the new minimum
**See Also:** getMinimum()

,

addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.setMinimum(int)

---

#### setMinimum

@BeanProperty

(

bound

=false,

preferred

=true,

description

="The progress bar\'s minimum value.")
public void setMinimum​(int n)

Sets the progress bar's minimum value
(stored in the progress bar's data model) to

n

.

The data model (a

BoundedRangeModel

instance)
handles any mathematical
issues arising from assigning faulty values.
See the

BoundedRangeModel

documentation for details.

If the minimum value is different from the previous minimum,
all change listeners are notified.

The data model (a

BoundedRangeModel

instance)
handles any mathematical
issues arising from assigning faulty values.
See the

BoundedRangeModel

documentation for details.

If the minimum value is different from the previous minimum,
all change listeners are notified.

If the minimum value is different from the previous minimum,
all change listeners are notified.

setMaximum

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The progress bar\'s maximum value.")
public void setMaximum​(int n)
```

Sets the progress bar's maximum value
(stored in the progress bar's data model) to

n

.

The underlying

BoundedRangeModel

handles any mathematical
issues arising from assigning faulty values.
See the

BoundedRangeModel

documentation for details.

If the maximum value is different from the previous maximum,
all change listeners are notified.

**Parameters:** n

- the new maximum
**See Also:** getMaximum()

,

addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.setMaximum(int)

---

#### setMaximum

@BeanProperty

(

bound

=false,

preferred

=true,

description

="The progress bar\'s maximum value.")
public void setMaximum​(int n)

Sets the progress bar's maximum value
(stored in the progress bar's data model) to

n

.

The underlying

BoundedRangeModel

handles any mathematical
issues arising from assigning faulty values.
See the

BoundedRangeModel

documentation for details.

If the maximum value is different from the previous maximum,
all change listeners are notified.

The underlying

BoundedRangeModel

handles any mathematical
issues arising from assigning faulty values.
See the

BoundedRangeModel

documentation for details.

If the maximum value is different from the previous maximum,
all change listeners are notified.

If the maximum value is different from the previous maximum,
all change listeners are notified.

setIndeterminate

```java
public void setIndeterminate​(boolean newValue)
```

Sets the

indeterminate

property of the progress bar,
which determines whether the progress bar is in determinate
or indeterminate mode.
An indeterminate progress bar continuously displays animation
indicating that an operation of unknown length is occurring.
By default, this property is

false

.
Some look and feels might not support indeterminate progress bars;
they will ignore this property.

See

How to Monitor Progress

for examples of using indeterminate progress bars.

**Parameters:** newValue

-

true

if the progress bar
should change to indeterminate mode;

false

if it should revert to normal.
**Since:** 1.4
**See Also:** isIndeterminate()

,

BasicProgressBarUI

---

#### setIndeterminate

public void setIndeterminate​(boolean newValue)

Sets the

indeterminate

property of the progress bar,
which determines whether the progress bar is in determinate
or indeterminate mode.
An indeterminate progress bar continuously displays animation
indicating that an operation of unknown length is occurring.
By default, this property is

false

.
Some look and feels might not support indeterminate progress bars;
they will ignore this property.

See

How to Monitor Progress

for examples of using indeterminate progress bars.

See

How to Monitor Progress

for examples of using indeterminate progress bars.

isIndeterminate

```java
@BeanProperty
(
bound
=false,

description
="Is the progress bar indeterminate (true) or normal (false)?")
public boolean isIndeterminate()
```

Returns the value of the

indeterminate

property.

**Returns:** the value of the

indeterminate

property
**Since:** 1.4
**See Also:** setIndeterminate(boolean)

---

#### isIndeterminate

@BeanProperty

(

bound

=false,

description

="Is the progress bar indeterminate (true) or normal (false)?")
public boolean isIndeterminate()

Returns the value of the

indeterminate

property.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JProgressBar

.
This method is intended to be used only for debugging purposes. The
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

JProgressBar

---

#### paramString

protected

String

paramString()

Returns a string representation of this

JProgressBar

.
This method is intended to be used only for debugging purposes. The
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
=false,

expert
=true,

description
="The AccessibleContext associated with this ProgressBar.")
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated with this

JProgressBar

. For progress bars, the

AccessibleContext

takes the form of an

AccessibleJProgressBar

.
A new

AccessibleJProgressBar

instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an

AccessibleJProgressBar

that serves as the

AccessibleContext

of this

JProgressBar

---

#### getAccessibleContext

@BeanProperty

(

bound

=false,

expert

=true,

description

="The AccessibleContext associated with this ProgressBar.")
public

AccessibleContext

getAccessibleContext()

Gets the

AccessibleContext

associated with this

JProgressBar

. For progress bars, the

AccessibleContext

takes the form of an

AccessibleJProgressBar

.
A new

AccessibleJProgressBar

instance is created if necessary.

---

