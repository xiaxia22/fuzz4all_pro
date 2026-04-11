# Class JSlider

**Source:** `java.desktop\javax\swing\JSlider.html`

### Class Description

```java
@JavaBean
(
defaultProperty
="UI",

description
="A component that supports selecting a integer value from a range.")
public class
JSlider

extends
JComponent

implements
SwingConstants
,
Accessible
```

A component that lets the user graphically select a value by sliding
a knob within a bounded interval. The knob is always positioned
at the points that match integer values within the specified interval.

The slider can show both
major tick marks, and minor tick marks between the major ones. The number of
values between the tick marks is controlled with

setMajorTickSpacing

and

setMinorTickSpacing

.
Painting of tick marks is controlled by

setPaintTicks

.

Sliders can also print text labels at regular intervals (or at
arbitrary locations) along the slider track. Painting of labels is
controlled by

setLabelTable

and

setPaintLabels

.

For further information and examples see

How to Use Sliders

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

#### protected
BoundedRangeModel
sliderModel

The data model that handles the numeric maximum value,
minimum value, and current-position value for the slider.

---

#### protected int majorTickSpacing

The number of values between the major tick marks -- the
larger marks that break up the minor tick marks.

---

#### protected int minorTickSpacing

The number of values between the minor tick marks -- the
smaller marks that occur between the major tick marks.

**See Also:**
- setMinorTickSpacing(int)

---

#### protected boolean snapToTicks

If true, the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob. The default is false.

**See Also:**
- setSnapToTicks(boolean)

---

#### protected int orientation

Whether the slider is horizontal or vertical
The default is horizontal.

**See Also:**
- setOrientation(int)

---

#### protected
ChangeListener
changeListener

The changeListener (no suffix) is the listener we add to the
slider's model. This listener is initialized to the

ChangeListener

returned from

createChangeListener

,
which by default just forwards events
to

ChangeListener

s (if any) added directly to the slider.

**See Also:**
- addChangeListener(javax.swing.event.ChangeListener)

,

createChangeListener()

---

#### protected transient
ChangeEvent
changeEvent

Only one

ChangeEvent

is needed per slider instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this". The event is lazily
created the first time that an event notification is fired.

**See Also:**
- fireStateChanged()

---

### Constructor Details

#### public JSlider()

Creates a horizontal slider with the range 0 to 100 and
an initial value of 50.

---

#### public JSlider​(int orientation)

Creates a slider using the specified orientation with the
range

0

to

100

and an initial value of

50

.
The orientation can be
either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

**Parameters:**
- orientation

- the orientation of the slider

**Throws:**
- IllegalArgumentException

- if orientation is not one of

VERTICAL

,

HORIZONTAL

**See Also:**
- setOrientation(int)

---

#### public JSlider​(int min,
int max)

Creates a horizontal slider using the specified min and max
with an initial value equal to the average of the min plus max.

The

BoundedRangeModel

that holds the slider's data
handles any issues that may arise from improperly setting the
minimum and maximum values on the slider. See the

BoundedRangeModel

documentation for details.

**Parameters:**
- min

- the minimum value of the slider
- max

- the maximum value of the slider

**See Also:**
- BoundedRangeModel

,

setMinimum(int)

,

setMaximum(int)

---

#### public JSlider​(int min,
int max,
int value)

Creates a horizontal slider using the specified min, max and value.

The

BoundedRangeModel

that holds the slider's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the slider. See the

BoundedRangeModel

documentation for details.

**Parameters:**
- min

- the minimum value of the slider
- max

- the maximum value of the slider
- value

- the initial value of the slider

**See Also:**
- BoundedRangeModel

,

setMinimum(int)

,

setMaximum(int)

,

setValue(int)

---

#### public JSlider​(int orientation,
int min,
int max,
int value)

Creates a slider with the specified orientation and the
specified minimum, maximum, and initial values.
The orientation can be
either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

The

BoundedRangeModel

that holds the slider's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the slider. See the

BoundedRangeModel

documentation for details.

**Parameters:**
- orientation

- the orientation of the slider
- min

- the minimum value of the slider
- max

- the maximum value of the slider
- value

- the initial value of the slider

**Throws:**
- IllegalArgumentException

- if orientation is not one of

VERTICAL

,

HORIZONTAL

**See Also:**
- BoundedRangeModel

,

setOrientation(int)

,

setMinimum(int)

,

setMaximum(int)

,

setValue(int)

---

#### public JSlider​(
BoundedRangeModel
brm)

Creates a horizontal slider using the specified
BoundedRangeModel.

**Parameters:**
- brm

- a

BoundedRangeModel

for the slider

---

### Method Details

#### public
SliderUI
getUI()

Gets the UI object which implements the L&F for this component.

**Overrides:**
- getUI

in class

JComponent

**Returns:**
- the SliderUI object that implements the Slider L&F

---

#### @BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the slider\'s LookAndFeel.")
public void setUI​(
SliderUI
ui)

Sets the UI object which implements the L&F for this component.

**Parameters:**
- ui

- the SliderUI L&F object

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

Returns the name of the L&F class that renders this component.

**Overrides:**
- getUIClassID

in class

JComponent

**Returns:**
- "SliderUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### protected
ChangeListener
createChangeListener()

Subclasses that want to handle

ChangeEvent

s
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
slider.

**Returns:**
- a instance of new

ChangeListener

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

Adds a ChangeListener to the slider.

**Parameters:**
- l

- the ChangeListener to add

**See Also:**
- fireStateChanged()

,

removeChangeListener(javax.swing.event.ChangeListener)

---

#### public void removeChangeListener​(
ChangeListener
l)

Removes a ChangeListener from the slider.

**Parameters:**
- l

- the ChangeListener to remove

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
to this JSlider with addChangeListener().

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

JSlider

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

Returns the

BoundedRangeModel

that handles the slider's three
fundamental properties: minimum, maximum, value.

**Returns:**
- the data model for this component

**See Also:**
- setModel(javax.swing.BoundedRangeModel)

,

BoundedRangeModel

---

#### @BeanProperty
(
description
="The sliders BoundedRangeModel.")
public void setModel​(
BoundedRangeModel
newModel)

Sets the

BoundedRangeModel

that handles the slider's three
fundamental properties: minimum, maximum, value.

Attempts to pass a

null

model to this method result in
undefined behavior, and, most likely, exceptions.

**Parameters:**
- newModel

- the new,

non-null

BoundedRangeModel

to use

**See Also:**
- getModel()

,

BoundedRangeModel

---

#### public int getValue()

Returns the slider's current value
from the

BoundedRangeModel

.

**Returns:**
- the current value of the slider

**See Also:**
- setValue(int)

,

BoundedRangeModel.getValue()

---

#### @BeanProperty
(
bound
=false,

preferred
=true,

description
="The sliders current value.")
public void setValue​(int n)

Sets the slider's current value to

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

#### public int getMinimum()

Returns the minimum value supported by the slider
from the

BoundedRangeModel

.

**Returns:**
- the value of the model's minimum property

**See Also:**
- setMinimum(int)

,

BoundedRangeModel.getMinimum()

---

#### @BeanProperty
(
preferred
=true,

description
="The sliders minimum value.")
public void setMinimum​(int minimum)

Sets the slider's minimum value to

minimum

. This method
forwards the new minimum value to the model.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new minimum value is different from the previous minimum value,
all change listeners are notified.

**Parameters:**
- minimum

- the new minimum

**See Also:**
- getMinimum()

,

addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.setMinimum(int)

---

#### public int getMaximum()

Returns the maximum value supported by the slider
from the

BoundedRangeModel

.

**Returns:**
- the value of the model's maximum property

**See Also:**
- setMaximum(int)

,

BoundedRangeModel.getMaximum()

---

#### @BeanProperty
(
preferred
=true,

description
="The sliders maximum value.")
public void setMaximum​(int maximum)

Sets the slider's maximum value to

maximum

. This method
forwards the new maximum value to the model.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new maximum value is different from the previous maximum value,
all change listeners are notified.

**Parameters:**
- maximum

- the new maximum

**See Also:**
- getMaximum()

,

addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.setMaximum(int)

---

#### public boolean getValueIsAdjusting()

Returns the

valueIsAdjusting

property from the model. For
details on how this is used, see the

setValueIsAdjusting

documentation.

**Returns:**
- the value of the model's

valueIsAdjusting

property

**See Also:**
- setValueIsAdjusting(boolean)

---

#### @BeanProperty
(
bound
=false,

expert
=true,

description
="True if the slider knob is being dragged.")
public void setValueIsAdjusting​(boolean b)

Sets the model's

valueIsAdjusting

property. Slider look and
feel implementations should set this property to

true

when
a knob drag begins, and to

false

when the drag ends.

**Parameters:**
- b

- the new value for the

valueIsAdjusting

property

**See Also:**
- getValueIsAdjusting()

,

BoundedRangeModel.setValueIsAdjusting(boolean)

---

#### public int getExtent()

Returns the "extent" from the

BoundedRangeModel

.
This represents the range of values "covered" by the knob.

**Returns:**
- an int representing the extent

**See Also:**
- setExtent(int)

,

BoundedRangeModel.getExtent()

---

#### @BeanProperty
(
bound
=false,

expert
=true,

description
="Size of the range covered by the knob.")
public void setExtent​(int extent)

Sets the size of the range "covered" by the knob. Most look
and feel implementations will change the value by this amount
if the user clicks on either side of the knob. This method just
forwards the new extent value to the model.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new extent value is different from the previous extent value,
all change listeners are notified.

**Parameters:**
- extent

- the new extent

**See Also:**
- getExtent()

,

BoundedRangeModel.setExtent(int)

---

#### public int getOrientation()

Return this slider's vertical or horizontal orientation.

**Returns:**
- SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

**See Also:**
- setOrientation(int)

---

#### @BeanProperty
(
preferred
=true,

visualUpdate
=true,

enumerationValues
={"JSlider.VERTICAL","JSlider.HORIZONTAL"},

description
="Set the scrollbars orientation to either VERTICAL or HORIZONTAL.")
public void setOrientation​(int orientation)

Set the slider's orientation to either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

**Parameters:**
- orientation

-

HORIZONTAL

or

VERTICAL

**Throws:**
- IllegalArgumentException

- if orientation is not one of

VERTICAL

,

HORIZONTAL

**See Also:**
- getOrientation()

---

#### public void setFont​(
Font
font)

Sets the font for this component.

**Overrides:**
- setFont

in class

JComponent

**Parameters:**
- font

- the desired

Font

for this component

**See Also:**
- Component.getFont()

**Since:**
- 1.6

---

#### public boolean imageUpdate​(
Image
img,
int infoflags,
int x,
int y,
int w,
int h)

Repaints the component when the image has changed.
This

imageUpdate

method of an

ImageObserver

is called when more information about an
image which had been previously requested using an asynchronous
routine such as the

drawImage

method of

Graphics

becomes available.
See the definition of

imageUpdate

for
more information on this method and its arguments.

The

imageUpdate

method of

Component

incrementally draws an image on the component as more of the bits
of the image are available.

If the system property

awt.image.incrementaldraw

is missing or has the value

true

, the image is
incrementally drawn. If the system property has any other value,
then the image is not drawn until it has been completely loaded.

Also, if incremental drawing is in effect, the value of the
system property

awt.image.redrawrate

is interpreted
as an integer to give the maximum redraw rate, in milliseconds. If
the system property is missing or cannot be interpreted as an
integer, the redraw rate is once every 100ms.

The interpretation of the

x

,

y

,

width

, and

height

arguments depends on
the value of the

infoflags

argument.

**Specified by:**
- imageUpdate

in interface

ImageObserver

**Overrides:**
- imageUpdate

in class

Component

**Parameters:**
- img

- the image being observed
- infoflags

- see

imageUpdate

for more information
- x

- the

x

coordinate
- y

- the

y

coordinate
- w

- the width
- h

- the height

**Returns:**
- false

if the infoflags indicate that the
image is completely loaded;

true

otherwise.

**See Also:**
- ImageObserver

,

Graphics.drawImage(Image, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, java.awt.image.ImageObserver)

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

**Since:**
- 1.7

---

#### public
Dictionary
getLabelTable()

Returns the dictionary of what labels to draw at which values.

**Returns:**
- the

Dictionary

containing labels and
where to draw them

---

#### @BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="Specifies what labels will be drawn for any given value.")
public void setLabelTable​(
Dictionary
labels)

Used to specify what label will be drawn at any given value.
The key-value pairs are of this format:

{ Integer value, java.swing.JComponent label }

.

An easy way to generate a standard table of value labels is by using the

createStandardLabels

method.

Once the labels have been set, this method calls

updateLabelUIs()

.
Note that the labels are only painted if the

paintLabels

property is

true

.

**Parameters:**
- labels

- new

Dictionary

of labels, or

null

to
remove all labels

**See Also:**
- createStandardLabels(int)

,

getLabelTable()

,

setPaintLabels(boolean)

---

#### protected void updateLabelUIs()

Updates the UIs for the labels in the label table by calling

updateUI

on each label. The UIs are updated from
the current look and feel. The labels are also set to their
preferred size.

**See Also:**
- setLabelTable(java.util.Dictionary)

,

JComponent.updateUI()

---

#### public
Hashtable
<
Integer
,​
JComponent
> createStandardLabels​(int increment)

Creates a

Hashtable

of numerical text labels, starting at the
slider minimum, and using the increment specified.
For example, if you call

createStandardLabels( 10 )

and the slider minimum is zero,
then labels will be created for the values 0, 10, 20, 30, and so on.

For the labels to be drawn on the slider, the returned

Hashtable

must be passed into

setLabelTable

, and

setPaintLabels

must be set to

true

.

For further details on the makeup of the returned

Hashtable

, see
the

setLabelTable

documentation.

**Parameters:**
- increment

- distance between labels in the generated hashtable

**Returns:**
- a new

Hashtable

of labels

**Throws:**
- IllegalArgumentException

- if

increment

is less than or
equal to zero

**See Also:**
- setLabelTable(java.util.Dictionary)

,

setPaintLabels(boolean)

---

#### public
Hashtable
<
Integer
,​
JComponent
> createStandardLabels​(int increment,
int start)

Creates a

Hashtable

of numerical text labels, starting at the
starting point specified, and using the increment specified.
For example, if you call

createStandardLabels( 10, 2 )

,
then labels will be created for the values 2, 12, 22, 32, and so on.

For the labels to be drawn on the slider, the returned

Hashtable

must be passed into

setLabelTable

, and

setPaintLabels

must be set to

true

.

For further details on the makeup of the returned

Hashtable

, see
the

setLabelTable

documentation.

**Parameters:**
- increment

- distance between labels in the generated hashtable
- start

- value at which the labels will begin

**Returns:**
- a new

Hashtable

of labels

**Throws:**
- IllegalArgumentException

- if

start

is
out of range, or if

increment

is less than or equal
to zero

**See Also:**
- setLabelTable(java.util.Dictionary)

,

setPaintLabels(boolean)

---

#### public boolean getInverted()

Returns true if the value-range shown for the slider is reversed,

**Returns:**
- true if the slider values are reversed from their normal order

**See Also:**
- setInverted(boolean)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="If true reverses the slider values from their normal order")
public void setInverted​(boolean b)

Specify true to reverse the value-range shown for the slider and false to
put the value range in the normal order. The order depends on the
slider's

ComponentOrientation

property. Normal (non-inverted)
horizontal sliders with a

ComponentOrientation

value of

LEFT_TO_RIGHT

have their maximum on the right.
Normal horizontal sliders with a

ComponentOrientation

value of

RIGHT_TO_LEFT

have their maximum on the left. Normal vertical
sliders have their maximum on the top. These labels are reversed when the
slider is inverted.

By default, the value of this property is

false

.

**Parameters:**
- b

- true to reverse the slider values from their normal order

---

#### public int getMajorTickSpacing()

This method returns the major tick spacing. The number that is returned
represents the distance, measured in values, between each major tick mark.
If you have a slider with a range from 0 to 50 and the major tick spacing
is set to 10, you will get major ticks next to the following values:
0, 10, 20, 30, 40, 50.

**Returns:**
- the number of values between major ticks

**See Also:**
- setMajorTickSpacing(int)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="Sets the number of values between major tick marks.")
public void setMajorTickSpacing​(int n)

This method sets the major tick spacing. The number that is passed in
represents the distance, measured in values, between each major tick mark.
If you have a slider with a range from 0 to 50 and the major tick spacing
is set to 10, you will get major ticks next to the following values:
0, 10, 20, 30, 40, 50.

In order for major ticks to be painted,

setPaintTicks

must be
set to

true

.

This method will also set up a label table for you.
If there is not already a label table, and the major tick spacing is

> 0

, and

getPaintLabels

returns

true

, a standard label table will be generated (by calling

createStandardLabels

) with labels at the major tick marks.
For the example above, you would get text labels: "0",
"10", "20", "30", "40", "50".
The label table is then set on the slider by calling

setLabelTable

.

**Parameters:**
- n

- new value for the

majorTickSpacing

property

**See Also:**
- getMajorTickSpacing()

,

setPaintTicks(boolean)

,

setLabelTable(java.util.Dictionary)

,

createStandardLabels(int)

---

#### public int getMinorTickSpacing()

This method returns the minor tick spacing. The number that is returned
represents the distance, measured in values, between each minor tick mark.
If you have a slider with a range from 0 to 50 and the minor tick spacing
is set to 10, you will get minor ticks next to the following values:
0, 10, 20, 30, 40, 50.

**Returns:**
- the number of values between minor ticks

**See Also:**
- getMinorTickSpacing()

---

#### @BeanProperty
(
visualUpdate
=true,

description
="Sets the number of values between minor tick marks.")
public void setMinorTickSpacing​(int n)

This method sets the minor tick spacing. The number that is passed in
represents the distance, measured in values, between each minor tick mark.
If you have a slider with a range from 0 to 50 and the minor tick spacing
is set to 10, you will get minor ticks next to the following values:
0, 10, 20, 30, 40, 50.

In order for minor ticks to be painted,

setPaintTicks

must be
set to

true

.

**Parameters:**
- n

- new value for the

minorTickSpacing

property

**See Also:**
- getMinorTickSpacing()

,

setPaintTicks(boolean)

---

#### public boolean getSnapToTicks()

Returns true if the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob.

**Returns:**
- true if the value snaps to the nearest tick mark, else false

**See Also:**
- setSnapToTicks(boolean)

---

#### @BeanProperty
(
description
="If true snap the knob to the nearest tick mark.")
public void setSnapToTicks​(boolean b)

Specifying true makes the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob.
By default, this property is

false

.

**Parameters:**
- b

- true to snap the knob to the nearest tick mark

**See Also:**
- getSnapToTicks()

---

#### public boolean getPaintTicks()

Tells if tick marks are to be painted.

**Returns:**
- true if tick marks are painted, else false

**See Also:**
- setPaintTicks(boolean)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="If true tick marks are painted on the slider.")
public void setPaintTicks​(boolean b)

Determines whether tick marks are painted on the slider.
By default, this property is

false

.

**Parameters:**
- b

- whether or not tick marks should be painted

**See Also:**
- getPaintTicks()

---

#### public boolean getPaintTrack()

Tells if the track (area the slider slides in) is to be painted.

**Returns:**
- true if track is painted, else false

**See Also:**
- setPaintTrack(boolean)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="If true, the track is painted on the slider.")
public void setPaintTrack​(boolean b)

Determines whether the track is painted on the slider. By default, this
property is

true

. It is up to the look and feel to honor this
property, some may choose to ignore it.

**Parameters:**
- b

- whether or not to paint the slider track

**See Also:**
- getPaintTrack()

---

#### public boolean getPaintLabels()

Tells if labels are to be painted.

**Returns:**
- true if labels are painted, else false

**See Also:**
- setPaintLabels(boolean)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="If true labels are painted on the slider.")
public void setPaintLabels​(boolean b)

Determines whether labels are painted on the slider.

This method will also set up a label table for you.
If there is not already a label table, and the major tick spacing is

> 0

,
a standard label table will be generated (by calling

createStandardLabels

) with labels at the major tick marks.
The label table is then set on the slider by calling

setLabelTable

.

By default, this property is

false

.

**Parameters:**
- b

- whether or not to paint labels

**See Also:**
- getPaintLabels()

,

getLabelTable()

,

createStandardLabels(int)

---

#### protected
String
paramString()

Returns a string representation of this JSlider. This method
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
- a string representation of this JSlider.

---

#### @BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this JSlider.
For sliders, the AccessibleContext takes the form of an
AccessibleJSlider.
A new AccessibleJSlider instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- an AccessibleJSlider that serves as the
AccessibleContext of this JSlider

---

### Additional Sections

#### Class JSlider

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JSlider

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JSlider

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JSlider

javax.swing.JComponent

- javax.swing.JSlider

javax.swing.JSlider

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
="A component that supports selecting a integer value from a range.")
public class
JSlider

extends
JComponent

implements
SwingConstants
,
Accessible
```

A component that lets the user graphically select a value by sliding
a knob within a bounded interval. The knob is always positioned
at the points that match integer values within the specified interval.

The slider can show both
major tick marks, and minor tick marks between the major ones. The number of
values between the tick marks is controlled with

setMajorTickSpacing

and

setMinorTickSpacing

.
Painting of tick marks is controlled by

setPaintTicks

.

Sliders can also print text labels at regular intervals (or at
arbitrary locations) along the slider track. Painting of labels is
controlled by

setLabelTable

and

setPaintLabels

.

For further information and examples see

How to Use Sliders

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
**See Also:** Serialized Form

@JavaBean

(

defaultProperty

="UI",

description

="A component that supports selecting a integer value from a range.")
public class

JSlider

extends

JComponent

implements

SwingConstants

,

Accessible

A component that lets the user graphically select a value by sliding
a knob within a bounded interval. The knob is always positioned
at the points that match integer values within the specified interval.

The slider can show both
major tick marks, and minor tick marks between the major ones. The number of
values between the tick marks is controlled with

setMajorTickSpacing

and

setMinorTickSpacing

.
Painting of tick marks is controlled by

setPaintTicks

.

Sliders can also print text labels at regular intervals (or at
arbitrary locations) along the slider track. Painting of labels is
controlled by

setLabelTable

and

setPaintLabels

.

For further information and examples see

How to Use Sliders

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

The slider can show both
major tick marks, and minor tick marks between the major ones. The number of
values between the tick marks is controlled with

setMajorTickSpacing

and

setMinorTickSpacing

.
Painting of tick marks is controlled by

setPaintTicks

.

Sliders can also print text labels at regular intervals (or at
arbitrary locations) along the slider track. Painting of labels is
controlled by

setLabelTable

and

setPaintLabels

.

For further information and examples see

How to Use Sliders

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

Sliders can also print text labels at regular intervals (or at
arbitrary locations) along the slider track. Painting of labels is
controlled by

setLabelTable

and

setPaintLabels

.

For further information and examples see

How to Use Sliders

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

For further information and examples see

How to Use Sliders

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

JSlider.AccessibleJSlider

This class implements accessibility support for the

JSlider

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

is needed per slider instance since the
event's only (read-only) state is the source property.

protected

ChangeListener

changeListener

The changeListener (no suffix) is the listener we add to the
slider's model.

protected int

majorTickSpacing

The number of values between the major tick marks -- the
larger marks that break up the minor tick marks.

protected int

minorTickSpacing

The number of values between the minor tick marks -- the
smaller marks that occur between the major tick marks.

protected int

orientation

Whether the slider is horizontal or vertical
The default is horizontal.

protected

BoundedRangeModel

sliderModel

The data model that handles the numeric maximum value,
minimum value, and current-position value for the slider.

protected boolean

snapToTicks

If true, the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob.

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

JSlider

()

Creates a horizontal slider with the range 0 to 100 and
an initial value of 50.

JSlider

​(int orientation)

Creates a slider using the specified orientation with the
range

0

to

100

and an initial value of

50

.

JSlider

​(int min,
int max)

Creates a horizontal slider using the specified min and max
with an initial value equal to the average of the min plus max.

JSlider

​(int min,
int max,
int value)

Creates a horizontal slider using the specified min, max and value.

JSlider

​(int orientation,
int min,
int max,
int value)

Creates a slider with the specified orientation and the
specified minimum, maximum, and initial values.

JSlider

​(

BoundedRangeModel

brm)

Creates a horizontal slider using the specified
BoundedRangeModel.

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

Adds a ChangeListener to the slider.

protected

ChangeListener

createChangeListener

()

Subclasses that want to handle

ChangeEvent

s
from the model differently
can override this to return
an instance of a custom

ChangeListener

implementation.

Hashtable

<

Integer

,​

JComponent

>

createStandardLabels

​(int increment)

Creates a

Hashtable

of numerical text labels, starting at the
slider minimum, and using the increment specified.

Hashtable

<

Integer

,​

JComponent

>

createStandardLabels

​(int increment,
int start)

Creates a

Hashtable

of numerical text labels, starting at the
starting point specified, and using the increment specified.

protected void

fireStateChanged

()

Send a

ChangeEvent

, whose source is this

JSlider

, to
all

ChangeListener

s that have registered interest in

ChangeEvent

s.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JSlider.

ChangeListener

[]

getChangeListeners

()

Returns an array of all the

ChangeListener

s added
to this JSlider with addChangeListener().

int

getExtent

()

Returns the "extent" from the

BoundedRangeModel

.

boolean

getInverted

()

Returns true if the value-range shown for the slider is reversed,

Dictionary

getLabelTable

()

Returns the dictionary of what labels to draw at which values.

int

getMajorTickSpacing

()

This method returns the major tick spacing.

int

getMaximum

()

Returns the maximum value supported by the slider
from the

BoundedRangeModel

.

int

getMinimum

()

Returns the minimum value supported by the slider
from the

BoundedRangeModel

.

int

getMinorTickSpacing

()

This method returns the minor tick spacing.

BoundedRangeModel

getModel

()

Returns the

BoundedRangeModel

that handles the slider's three
fundamental properties: minimum, maximum, value.

int

getOrientation

()

Return this slider's vertical or horizontal orientation.

boolean

getPaintLabels

()

Tells if labels are to be painted.

boolean

getPaintTicks

()

Tells if tick marks are to be painted.

boolean

getPaintTrack

()

Tells if the track (area the slider slides in) is to be painted.

boolean

getSnapToTicks

()

Returns true if the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob.

SliderUI

getUI

()

Gets the UI object which implements the L&F for this component.

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

int

getValue

()

Returns the slider's current value
from the

BoundedRangeModel

.

boolean

getValueIsAdjusting

()

Returns the

valueIsAdjusting

property from the model.

boolean

imageUpdate

​(

Image

img,
int infoflags,
int x,
int y,
int w,
int h)

Repaints the component when the image has changed.

protected

String

paramString

()

Returns a string representation of this JSlider.

void

removeChangeListener

​(

ChangeListener

l)

Removes a ChangeListener from the slider.

void

setExtent

​(int extent)

Sets the size of the range "covered" by the knob.

void

setFont

​(

Font

font)

Sets the font for this component.

void

setInverted

​(boolean b)

Specify true to reverse the value-range shown for the slider and false to
put the value range in the normal order.

void

setLabelTable

​(

Dictionary

labels)

Used to specify what label will be drawn at any given value.

void

setMajorTickSpacing

​(int n)

This method sets the major tick spacing.

void

setMaximum

​(int maximum)

Sets the slider's maximum value to

maximum

.

void

setMinimum

​(int minimum)

Sets the slider's minimum value to

minimum

.

void

setMinorTickSpacing

​(int n)

This method sets the minor tick spacing.

void

setModel

​(

BoundedRangeModel

newModel)

Sets the

BoundedRangeModel

that handles the slider's three
fundamental properties: minimum, maximum, value.

void

setOrientation

​(int orientation)

Set the slider's orientation to either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

void

setPaintLabels

​(boolean b)

Determines whether labels are painted on the slider.

void

setPaintTicks

​(boolean b)

Determines whether tick marks are painted on the slider.

void

setPaintTrack

​(boolean b)

Determines whether the track is painted on the slider.

void

setSnapToTicks

​(boolean b)

Specifying true makes the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob.

void

setUI

​(

SliderUI

ui)

Sets the UI object which implements the L&F for this component.

void

setValue

​(int n)

Sets the slider's current value to

n

.

void

setValueIsAdjusting

​(boolean b)

Sets the model's

valueIsAdjusting

property.

protected void

updateLabelUIs

()

Updates the UIs for the labels in the label table by calling

updateUI

on each label.

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

JSlider.AccessibleJSlider

This class implements accessibility support for the

JSlider

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

JSlider

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

is needed per slider instance since the
event's only (read-only) state is the source property.

protected

ChangeListener

changeListener

The changeListener (no suffix) is the listener we add to the
slider's model.

protected int

majorTickSpacing

The number of values between the major tick marks -- the
larger marks that break up the minor tick marks.

protected int

minorTickSpacing

The number of values between the minor tick marks -- the
smaller marks that occur between the major tick marks.

protected int

orientation

Whether the slider is horizontal or vertical
The default is horizontal.

protected

BoundedRangeModel

sliderModel

The data model that handles the numeric maximum value,
minimum value, and current-position value for the slider.

protected boolean

snapToTicks

If true, the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob.

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

is needed per slider instance since the
event's only (read-only) state is the source property.

The changeListener (no suffix) is the listener we add to the
slider's model.

The number of values between the major tick marks -- the
larger marks that break up the minor tick marks.

The number of values between the minor tick marks -- the
smaller marks that occur between the major tick marks.

Whether the slider is horizontal or vertical
The default is horizontal.

The data model that handles the numeric maximum value,
minimum value, and current-position value for the slider.

If true, the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob.

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

JSlider

()

Creates a horizontal slider with the range 0 to 100 and
an initial value of 50.

JSlider

​(int orientation)

Creates a slider using the specified orientation with the
range

0

to

100

and an initial value of

50

.

JSlider

​(int min,
int max)

Creates a horizontal slider using the specified min and max
with an initial value equal to the average of the min plus max.

JSlider

​(int min,
int max,
int value)

Creates a horizontal slider using the specified min, max and value.

JSlider

​(int orientation,
int min,
int max,
int value)

Creates a slider with the specified orientation and the
specified minimum, maximum, and initial values.

JSlider

​(

BoundedRangeModel

brm)

Creates a horizontal slider using the specified
BoundedRangeModel.

---

#### Constructor Summary

Creates a horizontal slider with the range 0 to 100 and
an initial value of 50.

Creates a slider using the specified orientation with the
range

0

to

100

and an initial value of

50

.

Creates a horizontal slider using the specified min and max
with an initial value equal to the average of the min plus max.

Creates a horizontal slider using the specified min, max and value.

Creates a slider with the specified orientation and the
specified minimum, maximum, and initial values.

Creates a horizontal slider using the specified
BoundedRangeModel.

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

Adds a ChangeListener to the slider.

protected

ChangeListener

createChangeListener

()

Subclasses that want to handle

ChangeEvent

s
from the model differently
can override this to return
an instance of a custom

ChangeListener

implementation.

Hashtable

<

Integer

,​

JComponent

>

createStandardLabels

​(int increment)

Creates a

Hashtable

of numerical text labels, starting at the
slider minimum, and using the increment specified.

Hashtable

<

Integer

,​

JComponent

>

createStandardLabels

​(int increment,
int start)

Creates a

Hashtable

of numerical text labels, starting at the
starting point specified, and using the increment specified.

protected void

fireStateChanged

()

Send a

ChangeEvent

, whose source is this

JSlider

, to
all

ChangeListener

s that have registered interest in

ChangeEvent

s.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JSlider.

ChangeListener

[]

getChangeListeners

()

Returns an array of all the

ChangeListener

s added
to this JSlider with addChangeListener().

int

getExtent

()

Returns the "extent" from the

BoundedRangeModel

.

boolean

getInverted

()

Returns true if the value-range shown for the slider is reversed,

Dictionary

getLabelTable

()

Returns the dictionary of what labels to draw at which values.

int

getMajorTickSpacing

()

This method returns the major tick spacing.

int

getMaximum

()

Returns the maximum value supported by the slider
from the

BoundedRangeModel

.

int

getMinimum

()

Returns the minimum value supported by the slider
from the

BoundedRangeModel

.

int

getMinorTickSpacing

()

This method returns the minor tick spacing.

BoundedRangeModel

getModel

()

Returns the

BoundedRangeModel

that handles the slider's three
fundamental properties: minimum, maximum, value.

int

getOrientation

()

Return this slider's vertical or horizontal orientation.

boolean

getPaintLabels

()

Tells if labels are to be painted.

boolean

getPaintTicks

()

Tells if tick marks are to be painted.

boolean

getPaintTrack

()

Tells if the track (area the slider slides in) is to be painted.

boolean

getSnapToTicks

()

Returns true if the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob.

SliderUI

getUI

()

Gets the UI object which implements the L&F for this component.

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

int

getValue

()

Returns the slider's current value
from the

BoundedRangeModel

.

boolean

getValueIsAdjusting

()

Returns the

valueIsAdjusting

property from the model.

boolean

imageUpdate

​(

Image

img,
int infoflags,
int x,
int y,
int w,
int h)

Repaints the component when the image has changed.

protected

String

paramString

()

Returns a string representation of this JSlider.

void

removeChangeListener

​(

ChangeListener

l)

Removes a ChangeListener from the slider.

void

setExtent

​(int extent)

Sets the size of the range "covered" by the knob.

void

setFont

​(

Font

font)

Sets the font for this component.

void

setInverted

​(boolean b)

Specify true to reverse the value-range shown for the slider and false to
put the value range in the normal order.

void

setLabelTable

​(

Dictionary

labels)

Used to specify what label will be drawn at any given value.

void

setMajorTickSpacing

​(int n)

This method sets the major tick spacing.

void

setMaximum

​(int maximum)

Sets the slider's maximum value to

maximum

.

void

setMinimum

​(int minimum)

Sets the slider's minimum value to

minimum

.

void

setMinorTickSpacing

​(int n)

This method sets the minor tick spacing.

void

setModel

​(

BoundedRangeModel

newModel)

Sets the

BoundedRangeModel

that handles the slider's three
fundamental properties: minimum, maximum, value.

void

setOrientation

​(int orientation)

Set the slider's orientation to either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

void

setPaintLabels

​(boolean b)

Determines whether labels are painted on the slider.

void

setPaintTicks

​(boolean b)

Determines whether tick marks are painted on the slider.

void

setPaintTrack

​(boolean b)

Determines whether the track is painted on the slider.

void

setSnapToTicks

​(boolean b)

Specifying true makes the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob.

void

setUI

​(

SliderUI

ui)

Sets the UI object which implements the L&F for this component.

void

setValue

​(int n)

Sets the slider's current value to

n

.

void

setValueIsAdjusting

​(boolean b)

Sets the model's

valueIsAdjusting

property.

protected void

updateLabelUIs

()

Updates the UIs for the labels in the label table by calling

updateUI

on each label.

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

Adds a ChangeListener to the slider.

Subclasses that want to handle

ChangeEvent

s
from the model differently
can override this to return
an instance of a custom

ChangeListener

implementation.

Creates a

Hashtable

of numerical text labels, starting at the
slider minimum, and using the increment specified.

Creates a

Hashtable

of numerical text labels, starting at the
starting point specified, and using the increment specified.

Send a

ChangeEvent

, whose source is this

JSlider

, to
all

ChangeListener

s that have registered interest in

ChangeEvent

s.

Gets the AccessibleContext associated with this JSlider.

Returns an array of all the

ChangeListener

s added
to this JSlider with addChangeListener().

Returns the "extent" from the

BoundedRangeModel

.

Returns true if the value-range shown for the slider is reversed,

Returns the dictionary of what labels to draw at which values.

This method returns the major tick spacing.

Returns the maximum value supported by the slider
from the

BoundedRangeModel

.

Returns the minimum value supported by the slider
from the

BoundedRangeModel

.

This method returns the minor tick spacing.

Returns the

BoundedRangeModel

that handles the slider's three
fundamental properties: minimum, maximum, value.

Return this slider's vertical or horizontal orientation.

Tells if labels are to be painted.

Tells if tick marks are to be painted.

Tells if the track (area the slider slides in) is to be painted.

Returns true if the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob.

Gets the UI object which implements the L&F for this component.

Returns the name of the L&F class that renders this component.

Returns the slider's current value
from the

BoundedRangeModel

.

Returns the

valueIsAdjusting

property from the model.

Repaints the component when the image has changed.

Returns a string representation of this JSlider.

Removes a ChangeListener from the slider.

Sets the size of the range "covered" by the knob.

Sets the font for this component.

Specify true to reverse the value-range shown for the slider and false to
put the value range in the normal order.

Used to specify what label will be drawn at any given value.

This method sets the major tick spacing.

Sets the slider's maximum value to

maximum

.

Sets the slider's minimum value to

minimum

.

This method sets the minor tick spacing.

Sets the

BoundedRangeModel

that handles the slider's three
fundamental properties: minimum, maximum, value.

Set the slider's orientation to either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

Determines whether labels are painted on the slider.

Determines whether tick marks are painted on the slider.

Determines whether the track is painted on the slider.

Specifying true makes the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob.

Sets the UI object which implements the L&F for this component.

Sets the slider's current value to

n

.

Sets the model's

valueIsAdjusting

property.

Updates the UIs for the labels in the label table by calling

updateUI

on each label.

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

- sliderModel

```java
protected
BoundedRangeModel
sliderModel
```

The data model that handles the numeric maximum value,
minimum value, and current-position value for the slider.

- majorTickSpacing

```java
protected int majorTickSpacing
```

The number of values between the major tick marks -- the
larger marks that break up the minor tick marks.

- minorTickSpacing

```java
protected int minorTickSpacing
```

The number of values between the minor tick marks -- the
smaller marks that occur between the major tick marks.

**See Also:** setMinorTickSpacing(int)

- snapToTicks

```java
protected boolean snapToTicks
```

If true, the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob. The default is false.

**See Also:** setSnapToTicks(boolean)

- orientation

```java
protected int orientation
```

Whether the slider is horizontal or vertical
The default is horizontal.

**See Also:** setOrientation(int)

- changeListener

```java
protected
ChangeListener
changeListener
```

The changeListener (no suffix) is the listener we add to the
slider's model. This listener is initialized to the

ChangeListener

returned from

createChangeListener

,
which by default just forwards events
to

ChangeListener

s (if any) added directly to the slider.

**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

createChangeListener()

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one

ChangeEvent

is needed per slider instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this". The event is lazily
created the first time that an event notification is fired.

**See Also:** fireStateChanged()

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JSlider

```java
public JSlider()
```

Creates a horizontal slider with the range 0 to 100 and
an initial value of 50.

- JSlider

```java
public JSlider​(int orientation)
```

Creates a slider using the specified orientation with the
range

0

to

100

and an initial value of

50

.
The orientation can be
either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

**Parameters:** orientation

- the orientation of the slider
**Throws:** IllegalArgumentException

- if orientation is not one of

VERTICAL

,

HORIZONTAL
**See Also:** setOrientation(int)

- JSlider

```java
public JSlider​(int min,
int max)
```

Creates a horizontal slider using the specified min and max
with an initial value equal to the average of the min plus max.

The

BoundedRangeModel

that holds the slider's data
handles any issues that may arise from improperly setting the
minimum and maximum values on the slider. See the

BoundedRangeModel

documentation for details.

**Parameters:** min

- the minimum value of the slider
**Parameters:** max

- the maximum value of the slider
**See Also:** BoundedRangeModel

,

setMinimum(int)

,

setMaximum(int)

- JSlider

```java
public JSlider​(int min,
int max,
int value)
```

Creates a horizontal slider using the specified min, max and value.

The

BoundedRangeModel

that holds the slider's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the slider. See the

BoundedRangeModel

documentation for details.

**Parameters:** min

- the minimum value of the slider
**Parameters:** max

- the maximum value of the slider
**Parameters:** value

- the initial value of the slider
**See Also:** BoundedRangeModel

,

setMinimum(int)

,

setMaximum(int)

,

setValue(int)

- JSlider

```java
public JSlider​(int orientation,
int min,
int max,
int value)
```

Creates a slider with the specified orientation and the
specified minimum, maximum, and initial values.
The orientation can be
either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

The

BoundedRangeModel

that holds the slider's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the slider. See the

BoundedRangeModel

documentation for details.

**Parameters:** orientation

- the orientation of the slider
**Parameters:** min

- the minimum value of the slider
**Parameters:** max

- the maximum value of the slider
**Parameters:** value

- the initial value of the slider
**Throws:** IllegalArgumentException

- if orientation is not one of

VERTICAL

,

HORIZONTAL
**See Also:** BoundedRangeModel

,

setOrientation(int)

,

setMinimum(int)

,

setMaximum(int)

,

setValue(int)

- JSlider

```java
public JSlider​(
BoundedRangeModel
brm)
```

Creates a horizontal slider using the specified
BoundedRangeModel.

**Parameters:** brm

- a

BoundedRangeModel

for the slider

============ METHOD DETAIL ==========

- Method Detail

- getUI

```java
public
SliderUI
getUI()
```

Gets the UI object which implements the L&F for this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the SliderUI object that implements the Slider L&F

- setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the slider\'s LookAndFeel.")
public void setUI​(
SliderUI
ui)
```

Sets the UI object which implements the L&F for this component.

**Parameters:** ui

- the SliderUI L&F object
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

Returns the name of the L&F class that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** "SliderUI"
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

ChangeEvent

s
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
slider.

**Returns:** a instance of new

ChangeListener
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

Adds a ChangeListener to the slider.

**Parameters:** l

- the ChangeListener to add
**See Also:** fireStateChanged()

,

removeChangeListener(javax.swing.event.ChangeListener)

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a ChangeListener from the slider.

**Parameters:** l

- the ChangeListener to remove
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
to this JSlider with addChangeListener().

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

JSlider

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

Returns the

BoundedRangeModel

that handles the slider's three
fundamental properties: minimum, maximum, value.

**Returns:** the data model for this component
**See Also:** setModel(javax.swing.BoundedRangeModel)

,

BoundedRangeModel

- setModel

```java
@BeanProperty
(
description
="The sliders BoundedRangeModel.")
public void setModel​(
BoundedRangeModel
newModel)
```

Sets the

BoundedRangeModel

that handles the slider's three
fundamental properties: minimum, maximum, value.

Attempts to pass a

null

model to this method result in
undefined behavior, and, most likely, exceptions.

**Parameters:** newModel

- the new,

non-null

BoundedRangeModel

to use
**See Also:** getModel()

,

BoundedRangeModel

- getValue

```java
public int getValue()
```

Returns the slider's current value
from the

BoundedRangeModel

.

**Returns:** the current value of the slider
**See Also:** setValue(int)

,

BoundedRangeModel.getValue()

- setValue

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The sliders current value.")
public void setValue​(int n)
```

Sets the slider's current value to

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

- getMinimum

```java
public int getMinimum()
```

Returns the minimum value supported by the slider
from the

BoundedRangeModel

.

**Returns:** the value of the model's minimum property
**See Also:** setMinimum(int)

,

BoundedRangeModel.getMinimum()

- setMinimum

```java
@BeanProperty
(
preferred
=true,

description
="The sliders minimum value.")
public void setMinimum​(int minimum)
```

Sets the slider's minimum value to

minimum

. This method
forwards the new minimum value to the model.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new minimum value is different from the previous minimum value,
all change listeners are notified.

**Parameters:** minimum

- the new minimum
**See Also:** getMinimum()

,

addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.setMinimum(int)

- getMaximum

```java
public int getMaximum()
```

Returns the maximum value supported by the slider
from the

BoundedRangeModel

.

**Returns:** the value of the model's maximum property
**See Also:** setMaximum(int)

,

BoundedRangeModel.getMaximum()

- setMaximum

```java
@BeanProperty
(
preferred
=true,

description
="The sliders maximum value.")
public void setMaximum​(int maximum)
```

Sets the slider's maximum value to

maximum

. This method
forwards the new maximum value to the model.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new maximum value is different from the previous maximum value,
all change listeners are notified.

**Parameters:** maximum

- the new maximum
**See Also:** getMaximum()

,

addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.setMaximum(int)

- getValueIsAdjusting

```java
public boolean getValueIsAdjusting()
```

Returns the

valueIsAdjusting

property from the model. For
details on how this is used, see the

setValueIsAdjusting

documentation.

**Returns:** the value of the model's

valueIsAdjusting

property
**See Also:** setValueIsAdjusting(boolean)

- setValueIsAdjusting

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="True if the slider knob is being dragged.")
public void setValueIsAdjusting​(boolean b)
```

Sets the model's

valueIsAdjusting

property. Slider look and
feel implementations should set this property to

true

when
a knob drag begins, and to

false

when the drag ends.

**Parameters:** b

- the new value for the

valueIsAdjusting

property
**See Also:** getValueIsAdjusting()

,

BoundedRangeModel.setValueIsAdjusting(boolean)

- getExtent

```java
public int getExtent()
```

Returns the "extent" from the

BoundedRangeModel

.
This represents the range of values "covered" by the knob.

**Returns:** an int representing the extent
**See Also:** setExtent(int)

,

BoundedRangeModel.getExtent()

- setExtent

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="Size of the range covered by the knob.")
public void setExtent​(int extent)
```

Sets the size of the range "covered" by the knob. Most look
and feel implementations will change the value by this amount
if the user clicks on either side of the knob. This method just
forwards the new extent value to the model.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new extent value is different from the previous extent value,
all change listeners are notified.

**Parameters:** extent

- the new extent
**See Also:** getExtent()

,

BoundedRangeModel.setExtent(int)

- getOrientation

```java
public int getOrientation()
```

Return this slider's vertical or horizontal orientation.

**Returns:** SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL
**See Also:** setOrientation(int)

- setOrientation

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

enumerationValues
={"JSlider.VERTICAL","JSlider.HORIZONTAL"},

description
="Set the scrollbars orientation to either VERTICAL or HORIZONTAL.")
public void setOrientation​(int orientation)
```

Set the slider's orientation to either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

**Parameters:** orientation

-

HORIZONTAL

or

VERTICAL
**Throws:** IllegalArgumentException

- if orientation is not one of

VERTICAL

,

HORIZONTAL
**See Also:** getOrientation()

- setFont

```java
public void setFont​(
Font
font)
```

Sets the font for this component.

**Overrides:** setFont

in class

JComponent
**Parameters:** font

- the desired

Font

for this component
**Since:** 1.6
**See Also:** Component.getFont()

- imageUpdate

```java
public boolean imageUpdate​(
Image
img,
int infoflags,
int x,
int y,
int w,
int h)
```

Repaints the component when the image has changed.
This

imageUpdate

method of an

ImageObserver

is called when more information about an
image which had been previously requested using an asynchronous
routine such as the

drawImage

method of

Graphics

becomes available.
See the definition of

imageUpdate

for
more information on this method and its arguments.

The

imageUpdate

method of

Component

incrementally draws an image on the component as more of the bits
of the image are available.

If the system property

awt.image.incrementaldraw

is missing or has the value

true

, the image is
incrementally drawn. If the system property has any other value,
then the image is not drawn until it has been completely loaded.

Also, if incremental drawing is in effect, the value of the
system property

awt.image.redrawrate

is interpreted
as an integer to give the maximum redraw rate, in milliseconds. If
the system property is missing or cannot be interpreted as an
integer, the redraw rate is once every 100ms.

The interpretation of the

x

,

y

,

width

, and

height

arguments depends on
the value of the

infoflags

argument.

**Specified by:** imageUpdate

in interface

ImageObserver
**Overrides:** imageUpdate

in class

Component
**Parameters:** img

- the image being observed
**Parameters:** infoflags

- see

imageUpdate

for more information
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** w

- the width
**Parameters:** h

- the height
**Returns:** false

if the infoflags indicate that the
image is completely loaded;

true

otherwise.
**Since:** 1.7
**See Also:** ImageObserver

,

Graphics.drawImage(Image, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, java.awt.image.ImageObserver)

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

- getLabelTable

```java
public
Dictionary
getLabelTable()
```

Returns the dictionary of what labels to draw at which values.

**Returns:** the

Dictionary

containing labels and
where to draw them

- setLabelTable

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="Specifies what labels will be drawn for any given value.")
public void setLabelTable​(
Dictionary
labels)
```

Used to specify what label will be drawn at any given value.
The key-value pairs are of this format:

{ Integer value, java.swing.JComponent label }

.

An easy way to generate a standard table of value labels is by using the

createStandardLabels

method.

Once the labels have been set, this method calls

updateLabelUIs()

.
Note that the labels are only painted if the

paintLabels

property is

true

.

**Parameters:** labels

- new

Dictionary

of labels, or

null

to
remove all labels
**See Also:** createStandardLabels(int)

,

getLabelTable()

,

setPaintLabels(boolean)

- updateLabelUIs

```java
protected void updateLabelUIs()
```

Updates the UIs for the labels in the label table by calling

updateUI

on each label. The UIs are updated from
the current look and feel. The labels are also set to their
preferred size.

**See Also:** setLabelTable(java.util.Dictionary)

,

JComponent.updateUI()

- createStandardLabels

```java
public
Hashtable
<
Integer
,​
JComponent
> createStandardLabels​(int increment)
```

Creates a

Hashtable

of numerical text labels, starting at the
slider minimum, and using the increment specified.
For example, if you call

createStandardLabels( 10 )

and the slider minimum is zero,
then labels will be created for the values 0, 10, 20, 30, and so on.

For the labels to be drawn on the slider, the returned

Hashtable

must be passed into

setLabelTable

, and

setPaintLabels

must be set to

true

.

For further details on the makeup of the returned

Hashtable

, see
the

setLabelTable

documentation.

**Parameters:** increment

- distance between labels in the generated hashtable
**Returns:** a new

Hashtable

of labels
**Throws:** IllegalArgumentException

- if

increment

is less than or
equal to zero
**See Also:** setLabelTable(java.util.Dictionary)

,

setPaintLabels(boolean)

- createStandardLabels

```java
public
Hashtable
<
Integer
,​
JComponent
> createStandardLabels​(int increment,
int start)
```

Creates a

Hashtable

of numerical text labels, starting at the
starting point specified, and using the increment specified.
For example, if you call

createStandardLabels( 10, 2 )

,
then labels will be created for the values 2, 12, 22, 32, and so on.

For the labels to be drawn on the slider, the returned

Hashtable

must be passed into

setLabelTable

, and

setPaintLabels

must be set to

true

.

For further details on the makeup of the returned

Hashtable

, see
the

setLabelTable

documentation.

**Parameters:** increment

- distance between labels in the generated hashtable
**Parameters:** start

- value at which the labels will begin
**Returns:** a new

Hashtable

of labels
**Throws:** IllegalArgumentException

- if

start

is
out of range, or if

increment

is less than or equal
to zero
**See Also:** setLabelTable(java.util.Dictionary)

,

setPaintLabels(boolean)

- getInverted

```java
public boolean getInverted()
```

Returns true if the value-range shown for the slider is reversed,

**Returns:** true if the slider values are reversed from their normal order
**See Also:** setInverted(boolean)

- setInverted

```java
@BeanProperty
(
visualUpdate
=true,

description
="If true reverses the slider values from their normal order")
public void setInverted​(boolean b)
```

Specify true to reverse the value-range shown for the slider and false to
put the value range in the normal order. The order depends on the
slider's

ComponentOrientation

property. Normal (non-inverted)
horizontal sliders with a

ComponentOrientation

value of

LEFT_TO_RIGHT

have their maximum on the right.
Normal horizontal sliders with a

ComponentOrientation

value of

RIGHT_TO_LEFT

have their maximum on the left. Normal vertical
sliders have their maximum on the top. These labels are reversed when the
slider is inverted.

By default, the value of this property is

false

.

**Parameters:** b

- true to reverse the slider values from their normal order

- getMajorTickSpacing

```java
public int getMajorTickSpacing()
```

This method returns the major tick spacing. The number that is returned
represents the distance, measured in values, between each major tick mark.
If you have a slider with a range from 0 to 50 and the major tick spacing
is set to 10, you will get major ticks next to the following values:
0, 10, 20, 30, 40, 50.

**Returns:** the number of values between major ticks
**See Also:** setMajorTickSpacing(int)

- setMajorTickSpacing

```java
@BeanProperty
(
visualUpdate
=true,

description
="Sets the number of values between major tick marks.")
public void setMajorTickSpacing​(int n)
```

This method sets the major tick spacing. The number that is passed in
represents the distance, measured in values, between each major tick mark.
If you have a slider with a range from 0 to 50 and the major tick spacing
is set to 10, you will get major ticks next to the following values:
0, 10, 20, 30, 40, 50.

In order for major ticks to be painted,

setPaintTicks

must be
set to

true

.

This method will also set up a label table for you.
If there is not already a label table, and the major tick spacing is

> 0

, and

getPaintLabels

returns

true

, a standard label table will be generated (by calling

createStandardLabels

) with labels at the major tick marks.
For the example above, you would get text labels: "0",
"10", "20", "30", "40", "50".
The label table is then set on the slider by calling

setLabelTable

.

**Parameters:** n

- new value for the

majorTickSpacing

property
**See Also:** getMajorTickSpacing()

,

setPaintTicks(boolean)

,

setLabelTable(java.util.Dictionary)

,

createStandardLabels(int)

- getMinorTickSpacing

```java
public int getMinorTickSpacing()
```

This method returns the minor tick spacing. The number that is returned
represents the distance, measured in values, between each minor tick mark.
If you have a slider with a range from 0 to 50 and the minor tick spacing
is set to 10, you will get minor ticks next to the following values:
0, 10, 20, 30, 40, 50.

**Returns:** the number of values between minor ticks
**See Also:** getMinorTickSpacing()

- setMinorTickSpacing

```java
@BeanProperty
(
visualUpdate
=true,

description
="Sets the number of values between minor tick marks.")
public void setMinorTickSpacing​(int n)
```

This method sets the minor tick spacing. The number that is passed in
represents the distance, measured in values, between each minor tick mark.
If you have a slider with a range from 0 to 50 and the minor tick spacing
is set to 10, you will get minor ticks next to the following values:
0, 10, 20, 30, 40, 50.

In order for minor ticks to be painted,

setPaintTicks

must be
set to

true

.

**Parameters:** n

- new value for the

minorTickSpacing

property
**See Also:** getMinorTickSpacing()

,

setPaintTicks(boolean)

- getSnapToTicks

```java
public boolean getSnapToTicks()
```

Returns true if the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob.

**Returns:** true if the value snaps to the nearest tick mark, else false
**See Also:** setSnapToTicks(boolean)

- setSnapToTicks

```java
@BeanProperty
(
description
="If true snap the knob to the nearest tick mark.")
public void setSnapToTicks​(boolean b)
```

Specifying true makes the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob.
By default, this property is

false

.

**Parameters:** b

- true to snap the knob to the nearest tick mark
**See Also:** getSnapToTicks()

- getPaintTicks

```java
public boolean getPaintTicks()
```

Tells if tick marks are to be painted.

**Returns:** true if tick marks are painted, else false
**See Also:** setPaintTicks(boolean)

- setPaintTicks

```java
@BeanProperty
(
visualUpdate
=true,

description
="If true tick marks are painted on the slider.")
public void setPaintTicks​(boolean b)
```

Determines whether tick marks are painted on the slider.
By default, this property is

false

.

**Parameters:** b

- whether or not tick marks should be painted
**See Also:** getPaintTicks()

- getPaintTrack

```java
public boolean getPaintTrack()
```

Tells if the track (area the slider slides in) is to be painted.

**Returns:** true if track is painted, else false
**See Also:** setPaintTrack(boolean)

- setPaintTrack

```java
@BeanProperty
(
visualUpdate
=true,

description
="If true, the track is painted on the slider.")
public void setPaintTrack​(boolean b)
```

Determines whether the track is painted on the slider. By default, this
property is

true

. It is up to the look and feel to honor this
property, some may choose to ignore it.

**Parameters:** b

- whether or not to paint the slider track
**See Also:** getPaintTrack()

- getPaintLabels

```java
public boolean getPaintLabels()
```

Tells if labels are to be painted.

**Returns:** true if labels are painted, else false
**See Also:** setPaintLabels(boolean)

- setPaintLabels

```java
@BeanProperty
(
visualUpdate
=true,

description
="If true labels are painted on the slider.")
public void setPaintLabels​(boolean b)
```

Determines whether labels are painted on the slider.

This method will also set up a label table for you.
If there is not already a label table, and the major tick spacing is

> 0

,
a standard label table will be generated (by calling

createStandardLabels

) with labels at the major tick marks.
The label table is then set on the slider by calling

setLabelTable

.

By default, this property is

false

.

**Parameters:** b

- whether or not to paint labels
**See Also:** getPaintLabels()

,

getLabelTable()

,

createStandardLabels(int)

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this JSlider. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this JSlider.

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

Gets the AccessibleContext associated with this JSlider.
For sliders, the AccessibleContext takes the form of an
AccessibleJSlider.
A new AccessibleJSlider instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJSlider that serves as the
AccessibleContext of this JSlider

Field Detail

- sliderModel

```java
protected
BoundedRangeModel
sliderModel
```

The data model that handles the numeric maximum value,
minimum value, and current-position value for the slider.

- majorTickSpacing

```java
protected int majorTickSpacing
```

The number of values between the major tick marks -- the
larger marks that break up the minor tick marks.

- minorTickSpacing

```java
protected int minorTickSpacing
```

The number of values between the minor tick marks -- the
smaller marks that occur between the major tick marks.

**See Also:** setMinorTickSpacing(int)

- snapToTicks

```java
protected boolean snapToTicks
```

If true, the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob. The default is false.

**See Also:** setSnapToTicks(boolean)

- orientation

```java
protected int orientation
```

Whether the slider is horizontal or vertical
The default is horizontal.

**See Also:** setOrientation(int)

- changeListener

```java
protected
ChangeListener
changeListener
```

The changeListener (no suffix) is the listener we add to the
slider's model. This listener is initialized to the

ChangeListener

returned from

createChangeListener

,
which by default just forwards events
to

ChangeListener

s (if any) added directly to the slider.

**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

createChangeListener()

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one

ChangeEvent

is needed per slider instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this". The event is lazily
created the first time that an event notification is fired.

**See Also:** fireStateChanged()

---

#### Field Detail

sliderModel

```java
protected
BoundedRangeModel
sliderModel
```

The data model that handles the numeric maximum value,
minimum value, and current-position value for the slider.

---

#### sliderModel

protected

BoundedRangeModel

sliderModel

The data model that handles the numeric maximum value,
minimum value, and current-position value for the slider.

majorTickSpacing

```java
protected int majorTickSpacing
```

The number of values between the major tick marks -- the
larger marks that break up the minor tick marks.

---

#### majorTickSpacing

protected int majorTickSpacing

The number of values between the major tick marks -- the
larger marks that break up the minor tick marks.

minorTickSpacing

```java
protected int minorTickSpacing
```

The number of values between the minor tick marks -- the
smaller marks that occur between the major tick marks.

**See Also:** setMinorTickSpacing(int)

---

#### minorTickSpacing

protected int minorTickSpacing

The number of values between the minor tick marks -- the
smaller marks that occur between the major tick marks.

snapToTicks

```java
protected boolean snapToTicks
```

If true, the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob. The default is false.

**See Also:** setSnapToTicks(boolean)

---

#### snapToTicks

protected boolean snapToTicks

If true, the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob. The default is false.

orientation

```java
protected int orientation
```

Whether the slider is horizontal or vertical
The default is horizontal.

**See Also:** setOrientation(int)

---

#### orientation

protected int orientation

Whether the slider is horizontal or vertical
The default is horizontal.

changeListener

```java
protected
ChangeListener
changeListener
```

The changeListener (no suffix) is the listener we add to the
slider's model. This listener is initialized to the

ChangeListener

returned from

createChangeListener

,
which by default just forwards events
to

ChangeListener

s (if any) added directly to the slider.

**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

createChangeListener()

---

#### changeListener

protected

ChangeListener

changeListener

The changeListener (no suffix) is the listener we add to the
slider's model. This listener is initialized to the

ChangeListener

returned from

createChangeListener

,
which by default just forwards events
to

ChangeListener

s (if any) added directly to the slider.

changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one

ChangeEvent

is needed per slider instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this". The event is lazily
created the first time that an event notification is fired.

**See Also:** fireStateChanged()

---

#### changeEvent

protected transient

ChangeEvent

changeEvent

Only one

ChangeEvent

is needed per slider instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this". The event is lazily
created the first time that an event notification is fired.

Constructor Detail

- JSlider

```java
public JSlider()
```

Creates a horizontal slider with the range 0 to 100 and
an initial value of 50.

- JSlider

```java
public JSlider​(int orientation)
```

Creates a slider using the specified orientation with the
range

0

to

100

and an initial value of

50

.
The orientation can be
either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

**Parameters:** orientation

- the orientation of the slider
**Throws:** IllegalArgumentException

- if orientation is not one of

VERTICAL

,

HORIZONTAL
**See Also:** setOrientation(int)

- JSlider

```java
public JSlider​(int min,
int max)
```

Creates a horizontal slider using the specified min and max
with an initial value equal to the average of the min plus max.

The

BoundedRangeModel

that holds the slider's data
handles any issues that may arise from improperly setting the
minimum and maximum values on the slider. See the

BoundedRangeModel

documentation for details.

**Parameters:** min

- the minimum value of the slider
**Parameters:** max

- the maximum value of the slider
**See Also:** BoundedRangeModel

,

setMinimum(int)

,

setMaximum(int)

- JSlider

```java
public JSlider​(int min,
int max,
int value)
```

Creates a horizontal slider using the specified min, max and value.

The

BoundedRangeModel

that holds the slider's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the slider. See the

BoundedRangeModel

documentation for details.

**Parameters:** min

- the minimum value of the slider
**Parameters:** max

- the maximum value of the slider
**Parameters:** value

- the initial value of the slider
**See Also:** BoundedRangeModel

,

setMinimum(int)

,

setMaximum(int)

,

setValue(int)

- JSlider

```java
public JSlider​(int orientation,
int min,
int max,
int value)
```

Creates a slider with the specified orientation and the
specified minimum, maximum, and initial values.
The orientation can be
either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

The

BoundedRangeModel

that holds the slider's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the slider. See the

BoundedRangeModel

documentation for details.

**Parameters:** orientation

- the orientation of the slider
**Parameters:** min

- the minimum value of the slider
**Parameters:** max

- the maximum value of the slider
**Parameters:** value

- the initial value of the slider
**Throws:** IllegalArgumentException

- if orientation is not one of

VERTICAL

,

HORIZONTAL
**See Also:** BoundedRangeModel

,

setOrientation(int)

,

setMinimum(int)

,

setMaximum(int)

,

setValue(int)

- JSlider

```java
public JSlider​(
BoundedRangeModel
brm)
```

Creates a horizontal slider using the specified
BoundedRangeModel.

**Parameters:** brm

- a

BoundedRangeModel

for the slider

---

#### Constructor Detail

JSlider

```java
public JSlider()
```

Creates a horizontal slider with the range 0 to 100 and
an initial value of 50.

---

#### JSlider

public JSlider()

Creates a horizontal slider with the range 0 to 100 and
an initial value of 50.

JSlider

```java
public JSlider​(int orientation)
```

Creates a slider using the specified orientation with the
range

0

to

100

and an initial value of

50

.
The orientation can be
either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

**Parameters:** orientation

- the orientation of the slider
**Throws:** IllegalArgumentException

- if orientation is not one of

VERTICAL

,

HORIZONTAL
**See Also:** setOrientation(int)

---

#### JSlider

public JSlider​(int orientation)

Creates a slider using the specified orientation with the
range

0

to

100

and an initial value of

50

.
The orientation can be
either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

JSlider

```java
public JSlider​(int min,
int max)
```

Creates a horizontal slider using the specified min and max
with an initial value equal to the average of the min plus max.

The

BoundedRangeModel

that holds the slider's data
handles any issues that may arise from improperly setting the
minimum and maximum values on the slider. See the

BoundedRangeModel

documentation for details.

**Parameters:** min

- the minimum value of the slider
**Parameters:** max

- the maximum value of the slider
**See Also:** BoundedRangeModel

,

setMinimum(int)

,

setMaximum(int)

---

#### JSlider

public JSlider​(int min,
int max)

Creates a horizontal slider using the specified min and max
with an initial value equal to the average of the min plus max.

The

BoundedRangeModel

that holds the slider's data
handles any issues that may arise from improperly setting the
minimum and maximum values on the slider. See the

BoundedRangeModel

documentation for details.

The

BoundedRangeModel

that holds the slider's data
handles any issues that may arise from improperly setting the
minimum and maximum values on the slider. See the

BoundedRangeModel

documentation for details.

JSlider

```java
public JSlider​(int min,
int max,
int value)
```

Creates a horizontal slider using the specified min, max and value.

The

BoundedRangeModel

that holds the slider's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the slider. See the

BoundedRangeModel

documentation for details.

**Parameters:** min

- the minimum value of the slider
**Parameters:** max

- the maximum value of the slider
**Parameters:** value

- the initial value of the slider
**See Also:** BoundedRangeModel

,

setMinimum(int)

,

setMaximum(int)

,

setValue(int)

---

#### JSlider

public JSlider​(int min,
int max,
int value)

Creates a horizontal slider using the specified min, max and value.

The

BoundedRangeModel

that holds the slider's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the slider. See the

BoundedRangeModel

documentation for details.

The

BoundedRangeModel

that holds the slider's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the slider. See the

BoundedRangeModel

documentation for details.

JSlider

```java
public JSlider​(int orientation,
int min,
int max,
int value)
```

Creates a slider with the specified orientation and the
specified minimum, maximum, and initial values.
The orientation can be
either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

The

BoundedRangeModel

that holds the slider's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the slider. See the

BoundedRangeModel

documentation for details.

**Parameters:** orientation

- the orientation of the slider
**Parameters:** min

- the minimum value of the slider
**Parameters:** max

- the maximum value of the slider
**Parameters:** value

- the initial value of the slider
**Throws:** IllegalArgumentException

- if orientation is not one of

VERTICAL

,

HORIZONTAL
**See Also:** BoundedRangeModel

,

setOrientation(int)

,

setMinimum(int)

,

setMaximum(int)

,

setValue(int)

---

#### JSlider

public JSlider​(int orientation,
int min,
int max,
int value)

Creates a slider with the specified orientation and the
specified minimum, maximum, and initial values.
The orientation can be
either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

The

BoundedRangeModel

that holds the slider's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the slider. See the

BoundedRangeModel

documentation for details.

The

BoundedRangeModel

that holds the slider's data
handles any issues that may arise from improperly setting the
minimum, initial, and maximum values on the slider. See the

BoundedRangeModel

documentation for details.

JSlider

```java
public JSlider​(
BoundedRangeModel
brm)
```

Creates a horizontal slider using the specified
BoundedRangeModel.

**Parameters:** brm

- a

BoundedRangeModel

for the slider

---

#### JSlider

public JSlider​(

BoundedRangeModel

brm)

Creates a horizontal slider using the specified
BoundedRangeModel.

Method Detail

- getUI

```java
public
SliderUI
getUI()
```

Gets the UI object which implements the L&F for this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the SliderUI object that implements the Slider L&F

- setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the slider\'s LookAndFeel.")
public void setUI​(
SliderUI
ui)
```

Sets the UI object which implements the L&F for this component.

**Parameters:** ui

- the SliderUI L&F object
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

Returns the name of the L&F class that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** "SliderUI"
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

ChangeEvent

s
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
slider.

**Returns:** a instance of new

ChangeListener
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

Adds a ChangeListener to the slider.

**Parameters:** l

- the ChangeListener to add
**See Also:** fireStateChanged()

,

removeChangeListener(javax.swing.event.ChangeListener)

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a ChangeListener from the slider.

**Parameters:** l

- the ChangeListener to remove
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
to this JSlider with addChangeListener().

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

JSlider

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

Returns the

BoundedRangeModel

that handles the slider's three
fundamental properties: minimum, maximum, value.

**Returns:** the data model for this component
**See Also:** setModel(javax.swing.BoundedRangeModel)

,

BoundedRangeModel

- setModel

```java
@BeanProperty
(
description
="The sliders BoundedRangeModel.")
public void setModel​(
BoundedRangeModel
newModel)
```

Sets the

BoundedRangeModel

that handles the slider's three
fundamental properties: minimum, maximum, value.

Attempts to pass a

null

model to this method result in
undefined behavior, and, most likely, exceptions.

**Parameters:** newModel

- the new,

non-null

BoundedRangeModel

to use
**See Also:** getModel()

,

BoundedRangeModel

- getValue

```java
public int getValue()
```

Returns the slider's current value
from the

BoundedRangeModel

.

**Returns:** the current value of the slider
**See Also:** setValue(int)

,

BoundedRangeModel.getValue()

- setValue

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The sliders current value.")
public void setValue​(int n)
```

Sets the slider's current value to

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

- getMinimum

```java
public int getMinimum()
```

Returns the minimum value supported by the slider
from the

BoundedRangeModel

.

**Returns:** the value of the model's minimum property
**See Also:** setMinimum(int)

,

BoundedRangeModel.getMinimum()

- setMinimum

```java
@BeanProperty
(
preferred
=true,

description
="The sliders minimum value.")
public void setMinimum​(int minimum)
```

Sets the slider's minimum value to

minimum

. This method
forwards the new minimum value to the model.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new minimum value is different from the previous minimum value,
all change listeners are notified.

**Parameters:** minimum

- the new minimum
**See Also:** getMinimum()

,

addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.setMinimum(int)

- getMaximum

```java
public int getMaximum()
```

Returns the maximum value supported by the slider
from the

BoundedRangeModel

.

**Returns:** the value of the model's maximum property
**See Also:** setMaximum(int)

,

BoundedRangeModel.getMaximum()

- setMaximum

```java
@BeanProperty
(
preferred
=true,

description
="The sliders maximum value.")
public void setMaximum​(int maximum)
```

Sets the slider's maximum value to

maximum

. This method
forwards the new maximum value to the model.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new maximum value is different from the previous maximum value,
all change listeners are notified.

**Parameters:** maximum

- the new maximum
**See Also:** getMaximum()

,

addChangeListener(javax.swing.event.ChangeListener)

,

BoundedRangeModel.setMaximum(int)

- getValueIsAdjusting

```java
public boolean getValueIsAdjusting()
```

Returns the

valueIsAdjusting

property from the model. For
details on how this is used, see the

setValueIsAdjusting

documentation.

**Returns:** the value of the model's

valueIsAdjusting

property
**See Also:** setValueIsAdjusting(boolean)

- setValueIsAdjusting

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="True if the slider knob is being dragged.")
public void setValueIsAdjusting​(boolean b)
```

Sets the model's

valueIsAdjusting

property. Slider look and
feel implementations should set this property to

true

when
a knob drag begins, and to

false

when the drag ends.

**Parameters:** b

- the new value for the

valueIsAdjusting

property
**See Also:** getValueIsAdjusting()

,

BoundedRangeModel.setValueIsAdjusting(boolean)

- getExtent

```java
public int getExtent()
```

Returns the "extent" from the

BoundedRangeModel

.
This represents the range of values "covered" by the knob.

**Returns:** an int representing the extent
**See Also:** setExtent(int)

,

BoundedRangeModel.getExtent()

- setExtent

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="Size of the range covered by the knob.")
public void setExtent​(int extent)
```

Sets the size of the range "covered" by the knob. Most look
and feel implementations will change the value by this amount
if the user clicks on either side of the knob. This method just
forwards the new extent value to the model.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new extent value is different from the previous extent value,
all change listeners are notified.

**Parameters:** extent

- the new extent
**See Also:** getExtent()

,

BoundedRangeModel.setExtent(int)

- getOrientation

```java
public int getOrientation()
```

Return this slider's vertical or horizontal orientation.

**Returns:** SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL
**See Also:** setOrientation(int)

- setOrientation

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

enumerationValues
={"JSlider.VERTICAL","JSlider.HORIZONTAL"},

description
="Set the scrollbars orientation to either VERTICAL or HORIZONTAL.")
public void setOrientation​(int orientation)
```

Set the slider's orientation to either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

**Parameters:** orientation

-

HORIZONTAL

or

VERTICAL
**Throws:** IllegalArgumentException

- if orientation is not one of

VERTICAL

,

HORIZONTAL
**See Also:** getOrientation()

- setFont

```java
public void setFont​(
Font
font)
```

Sets the font for this component.

**Overrides:** setFont

in class

JComponent
**Parameters:** font

- the desired

Font

for this component
**Since:** 1.6
**See Also:** Component.getFont()

- imageUpdate

```java
public boolean imageUpdate​(
Image
img,
int infoflags,
int x,
int y,
int w,
int h)
```

Repaints the component when the image has changed.
This

imageUpdate

method of an

ImageObserver

is called when more information about an
image which had been previously requested using an asynchronous
routine such as the

drawImage

method of

Graphics

becomes available.
See the definition of

imageUpdate

for
more information on this method and its arguments.

The

imageUpdate

method of

Component

incrementally draws an image on the component as more of the bits
of the image are available.

If the system property

awt.image.incrementaldraw

is missing or has the value

true

, the image is
incrementally drawn. If the system property has any other value,
then the image is not drawn until it has been completely loaded.

Also, if incremental drawing is in effect, the value of the
system property

awt.image.redrawrate

is interpreted
as an integer to give the maximum redraw rate, in milliseconds. If
the system property is missing or cannot be interpreted as an
integer, the redraw rate is once every 100ms.

The interpretation of the

x

,

y

,

width

, and

height

arguments depends on
the value of the

infoflags

argument.

**Specified by:** imageUpdate

in interface

ImageObserver
**Overrides:** imageUpdate

in class

Component
**Parameters:** img

- the image being observed
**Parameters:** infoflags

- see

imageUpdate

for more information
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** w

- the width
**Parameters:** h

- the height
**Returns:** false

if the infoflags indicate that the
image is completely loaded;

true

otherwise.
**Since:** 1.7
**See Also:** ImageObserver

,

Graphics.drawImage(Image, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, java.awt.image.ImageObserver)

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

- getLabelTable

```java
public
Dictionary
getLabelTable()
```

Returns the dictionary of what labels to draw at which values.

**Returns:** the

Dictionary

containing labels and
where to draw them

- setLabelTable

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="Specifies what labels will be drawn for any given value.")
public void setLabelTable​(
Dictionary
labels)
```

Used to specify what label will be drawn at any given value.
The key-value pairs are of this format:

{ Integer value, java.swing.JComponent label }

.

An easy way to generate a standard table of value labels is by using the

createStandardLabels

method.

Once the labels have been set, this method calls

updateLabelUIs()

.
Note that the labels are only painted if the

paintLabels

property is

true

.

**Parameters:** labels

- new

Dictionary

of labels, or

null

to
remove all labels
**See Also:** createStandardLabels(int)

,

getLabelTable()

,

setPaintLabels(boolean)

- updateLabelUIs

```java
protected void updateLabelUIs()
```

Updates the UIs for the labels in the label table by calling

updateUI

on each label. The UIs are updated from
the current look and feel. The labels are also set to their
preferred size.

**See Also:** setLabelTable(java.util.Dictionary)

,

JComponent.updateUI()

- createStandardLabels

```java
public
Hashtable
<
Integer
,​
JComponent
> createStandardLabels​(int increment)
```

Creates a

Hashtable

of numerical text labels, starting at the
slider minimum, and using the increment specified.
For example, if you call

createStandardLabels( 10 )

and the slider minimum is zero,
then labels will be created for the values 0, 10, 20, 30, and so on.

For the labels to be drawn on the slider, the returned

Hashtable

must be passed into

setLabelTable

, and

setPaintLabels

must be set to

true

.

For further details on the makeup of the returned

Hashtable

, see
the

setLabelTable

documentation.

**Parameters:** increment

- distance between labels in the generated hashtable
**Returns:** a new

Hashtable

of labels
**Throws:** IllegalArgumentException

- if

increment

is less than or
equal to zero
**See Also:** setLabelTable(java.util.Dictionary)

,

setPaintLabels(boolean)

- createStandardLabels

```java
public
Hashtable
<
Integer
,​
JComponent
> createStandardLabels​(int increment,
int start)
```

Creates a

Hashtable

of numerical text labels, starting at the
starting point specified, and using the increment specified.
For example, if you call

createStandardLabels( 10, 2 )

,
then labels will be created for the values 2, 12, 22, 32, and so on.

For the labels to be drawn on the slider, the returned

Hashtable

must be passed into

setLabelTable

, and

setPaintLabels

must be set to

true

.

For further details on the makeup of the returned

Hashtable

, see
the

setLabelTable

documentation.

**Parameters:** increment

- distance between labels in the generated hashtable
**Parameters:** start

- value at which the labels will begin
**Returns:** a new

Hashtable

of labels
**Throws:** IllegalArgumentException

- if

start

is
out of range, or if

increment

is less than or equal
to zero
**See Also:** setLabelTable(java.util.Dictionary)

,

setPaintLabels(boolean)

- getInverted

```java
public boolean getInverted()
```

Returns true if the value-range shown for the slider is reversed,

**Returns:** true if the slider values are reversed from their normal order
**See Also:** setInverted(boolean)

- setInverted

```java
@BeanProperty
(
visualUpdate
=true,

description
="If true reverses the slider values from their normal order")
public void setInverted​(boolean b)
```

Specify true to reverse the value-range shown for the slider and false to
put the value range in the normal order. The order depends on the
slider's

ComponentOrientation

property. Normal (non-inverted)
horizontal sliders with a

ComponentOrientation

value of

LEFT_TO_RIGHT

have their maximum on the right.
Normal horizontal sliders with a

ComponentOrientation

value of

RIGHT_TO_LEFT

have their maximum on the left. Normal vertical
sliders have their maximum on the top. These labels are reversed when the
slider is inverted.

By default, the value of this property is

false

.

**Parameters:** b

- true to reverse the slider values from their normal order

- getMajorTickSpacing

```java
public int getMajorTickSpacing()
```

This method returns the major tick spacing. The number that is returned
represents the distance, measured in values, between each major tick mark.
If you have a slider with a range from 0 to 50 and the major tick spacing
is set to 10, you will get major ticks next to the following values:
0, 10, 20, 30, 40, 50.

**Returns:** the number of values between major ticks
**See Also:** setMajorTickSpacing(int)

- setMajorTickSpacing

```java
@BeanProperty
(
visualUpdate
=true,

description
="Sets the number of values between major tick marks.")
public void setMajorTickSpacing​(int n)
```

This method sets the major tick spacing. The number that is passed in
represents the distance, measured in values, between each major tick mark.
If you have a slider with a range from 0 to 50 and the major tick spacing
is set to 10, you will get major ticks next to the following values:
0, 10, 20, 30, 40, 50.

In order for major ticks to be painted,

setPaintTicks

must be
set to

true

.

This method will also set up a label table for you.
If there is not already a label table, and the major tick spacing is

> 0

, and

getPaintLabels

returns

true

, a standard label table will be generated (by calling

createStandardLabels

) with labels at the major tick marks.
For the example above, you would get text labels: "0",
"10", "20", "30", "40", "50".
The label table is then set on the slider by calling

setLabelTable

.

**Parameters:** n

- new value for the

majorTickSpacing

property
**See Also:** getMajorTickSpacing()

,

setPaintTicks(boolean)

,

setLabelTable(java.util.Dictionary)

,

createStandardLabels(int)

- getMinorTickSpacing

```java
public int getMinorTickSpacing()
```

This method returns the minor tick spacing. The number that is returned
represents the distance, measured in values, between each minor tick mark.
If you have a slider with a range from 0 to 50 and the minor tick spacing
is set to 10, you will get minor ticks next to the following values:
0, 10, 20, 30, 40, 50.

**Returns:** the number of values between minor ticks
**See Also:** getMinorTickSpacing()

- setMinorTickSpacing

```java
@BeanProperty
(
visualUpdate
=true,

description
="Sets the number of values between minor tick marks.")
public void setMinorTickSpacing​(int n)
```

This method sets the minor tick spacing. The number that is passed in
represents the distance, measured in values, between each minor tick mark.
If you have a slider with a range from 0 to 50 and the minor tick spacing
is set to 10, you will get minor ticks next to the following values:
0, 10, 20, 30, 40, 50.

In order for minor ticks to be painted,

setPaintTicks

must be
set to

true

.

**Parameters:** n

- new value for the

minorTickSpacing

property
**See Also:** getMinorTickSpacing()

,

setPaintTicks(boolean)

- getSnapToTicks

```java
public boolean getSnapToTicks()
```

Returns true if the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob.

**Returns:** true if the value snaps to the nearest tick mark, else false
**See Also:** setSnapToTicks(boolean)

- setSnapToTicks

```java
@BeanProperty
(
description
="If true snap the knob to the nearest tick mark.")
public void setSnapToTicks​(boolean b)
```

Specifying true makes the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob.
By default, this property is

false

.

**Parameters:** b

- true to snap the knob to the nearest tick mark
**See Also:** getSnapToTicks()

- getPaintTicks

```java
public boolean getPaintTicks()
```

Tells if tick marks are to be painted.

**Returns:** true if tick marks are painted, else false
**See Also:** setPaintTicks(boolean)

- setPaintTicks

```java
@BeanProperty
(
visualUpdate
=true,

description
="If true tick marks are painted on the slider.")
public void setPaintTicks​(boolean b)
```

Determines whether tick marks are painted on the slider.
By default, this property is

false

.

**Parameters:** b

- whether or not tick marks should be painted
**See Also:** getPaintTicks()

- getPaintTrack

```java
public boolean getPaintTrack()
```

Tells if the track (area the slider slides in) is to be painted.

**Returns:** true if track is painted, else false
**See Also:** setPaintTrack(boolean)

- setPaintTrack

```java
@BeanProperty
(
visualUpdate
=true,

description
="If true, the track is painted on the slider.")
public void setPaintTrack​(boolean b)
```

Determines whether the track is painted on the slider. By default, this
property is

true

. It is up to the look and feel to honor this
property, some may choose to ignore it.

**Parameters:** b

- whether or not to paint the slider track
**See Also:** getPaintTrack()

- getPaintLabels

```java
public boolean getPaintLabels()
```

Tells if labels are to be painted.

**Returns:** true if labels are painted, else false
**See Also:** setPaintLabels(boolean)

- setPaintLabels

```java
@BeanProperty
(
visualUpdate
=true,

description
="If true labels are painted on the slider.")
public void setPaintLabels​(boolean b)
```

Determines whether labels are painted on the slider.

This method will also set up a label table for you.
If there is not already a label table, and the major tick spacing is

> 0

,
a standard label table will be generated (by calling

createStandardLabels

) with labels at the major tick marks.
The label table is then set on the slider by calling

setLabelTable

.

By default, this property is

false

.

**Parameters:** b

- whether or not to paint labels
**See Also:** getPaintLabels()

,

getLabelTable()

,

createStandardLabels(int)

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this JSlider. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this JSlider.

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

Gets the AccessibleContext associated with this JSlider.
For sliders, the AccessibleContext takes the form of an
AccessibleJSlider.
A new AccessibleJSlider instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJSlider that serves as the
AccessibleContext of this JSlider

---

#### Method Detail

getUI

```java
public
SliderUI
getUI()
```

Gets the UI object which implements the L&F for this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the SliderUI object that implements the Slider L&F

---

#### getUI

public

SliderUI

getUI()

Gets the UI object which implements the L&F for this component.

setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the slider\'s LookAndFeel.")
public void setUI​(
SliderUI
ui)
```

Sets the UI object which implements the L&F for this component.

**Parameters:** ui

- the SliderUI L&F object
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

="The UI object that implements the slider\'s LookAndFeel.")
public void setUI​(

SliderUI

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

Returns the name of the L&F class that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** "SliderUI"
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

Returns the name of the L&F class that renders this component.

createChangeListener

```java
protected
ChangeListener
createChangeListener()
```

Subclasses that want to handle

ChangeEvent

s
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
slider.

**Returns:** a instance of new

ChangeListener
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

Subclasses that want to handle

ChangeEvent

s
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
slider.

addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a ChangeListener to the slider.

**Parameters:** l

- the ChangeListener to add
**See Also:** fireStateChanged()

,

removeChangeListener(javax.swing.event.ChangeListener)

---

#### addChangeListener

public void addChangeListener​(

ChangeListener

l)

Adds a ChangeListener to the slider.

removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a ChangeListener from the slider.

**Parameters:** l

- the ChangeListener to remove
**See Also:** fireStateChanged()

,

addChangeListener(javax.swing.event.ChangeListener)

---

#### removeChangeListener

public void removeChangeListener​(

ChangeListener

l)

Removes a ChangeListener from the slider.

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
to this JSlider with addChangeListener().

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
to this JSlider with addChangeListener().

fireStateChanged

```java
protected void fireStateChanged()
```

Send a

ChangeEvent

, whose source is this

JSlider

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

JSlider

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

Returns the

BoundedRangeModel

that handles the slider's three
fundamental properties: minimum, maximum, value.

**Returns:** the data model for this component
**See Also:** setModel(javax.swing.BoundedRangeModel)

,

BoundedRangeModel

---

#### getModel

public

BoundedRangeModel

getModel()

Returns the

BoundedRangeModel

that handles the slider's three
fundamental properties: minimum, maximum, value.

setModel

```java
@BeanProperty
(
description
="The sliders BoundedRangeModel.")
public void setModel​(
BoundedRangeModel
newModel)
```

Sets the

BoundedRangeModel

that handles the slider's three
fundamental properties: minimum, maximum, value.

Attempts to pass a

null

model to this method result in
undefined behavior, and, most likely, exceptions.

**Parameters:** newModel

- the new,

non-null

BoundedRangeModel

to use
**See Also:** getModel()

,

BoundedRangeModel

---

#### setModel

@BeanProperty

(

description

="The sliders BoundedRangeModel.")
public void setModel​(

BoundedRangeModel

newModel)

Sets the

BoundedRangeModel

that handles the slider's three
fundamental properties: minimum, maximum, value.

Attempts to pass a

null

model to this method result in
undefined behavior, and, most likely, exceptions.

Attempts to pass a

null

model to this method result in
undefined behavior, and, most likely, exceptions.

getValue

```java
public int getValue()
```

Returns the slider's current value
from the

BoundedRangeModel

.

**Returns:** the current value of the slider
**See Also:** setValue(int)

,

BoundedRangeModel.getValue()

---

#### getValue

public int getValue()

Returns the slider's current value
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
="The sliders current value.")
public void setValue​(int n)
```

Sets the slider's current value to

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

="The sliders current value.")
public void setValue​(int n)

Sets the slider's current value to

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

getMinimum

```java
public int getMinimum()
```

Returns the minimum value supported by the slider
from the

BoundedRangeModel

.

**Returns:** the value of the model's minimum property
**See Also:** setMinimum(int)

,

BoundedRangeModel.getMinimum()

---

#### getMinimum

public int getMinimum()

Returns the minimum value supported by the slider
from the

BoundedRangeModel

.

setMinimum

```java
@BeanProperty
(
preferred
=true,

description
="The sliders minimum value.")
public void setMinimum​(int minimum)
```

Sets the slider's minimum value to

minimum

. This method
forwards the new minimum value to the model.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new minimum value is different from the previous minimum value,
all change listeners are notified.

**Parameters:** minimum

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

preferred

=true,

description

="The sliders minimum value.")
public void setMinimum​(int minimum)

Sets the slider's minimum value to

minimum

. This method
forwards the new minimum value to the model.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new minimum value is different from the previous minimum value,
all change listeners are notified.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new minimum value is different from the previous minimum value,
all change listeners are notified.

If the new minimum value is different from the previous minimum value,
all change listeners are notified.

getMaximum

```java
public int getMaximum()
```

Returns the maximum value supported by the slider
from the

BoundedRangeModel

.

**Returns:** the value of the model's maximum property
**See Also:** setMaximum(int)

,

BoundedRangeModel.getMaximum()

---

#### getMaximum

public int getMaximum()

Returns the maximum value supported by the slider
from the

BoundedRangeModel

.

setMaximum

```java
@BeanProperty
(
preferred
=true,

description
="The sliders maximum value.")
public void setMaximum​(int maximum)
```

Sets the slider's maximum value to

maximum

. This method
forwards the new maximum value to the model.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new maximum value is different from the previous maximum value,
all change listeners are notified.

**Parameters:** maximum

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

preferred

=true,

description

="The sliders maximum value.")
public void setMaximum​(int maximum)

Sets the slider's maximum value to

maximum

. This method
forwards the new maximum value to the model.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new maximum value is different from the previous maximum value,
all change listeners are notified.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new maximum value is different from the previous maximum value,
all change listeners are notified.

If the new maximum value is different from the previous maximum value,
all change listeners are notified.

getValueIsAdjusting

```java
public boolean getValueIsAdjusting()
```

Returns the

valueIsAdjusting

property from the model. For
details on how this is used, see the

setValueIsAdjusting

documentation.

**Returns:** the value of the model's

valueIsAdjusting

property
**See Also:** setValueIsAdjusting(boolean)

---

#### getValueIsAdjusting

public boolean getValueIsAdjusting()

Returns the

valueIsAdjusting

property from the model. For
details on how this is used, see the

setValueIsAdjusting

documentation.

setValueIsAdjusting

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="True if the slider knob is being dragged.")
public void setValueIsAdjusting​(boolean b)
```

Sets the model's

valueIsAdjusting

property. Slider look and
feel implementations should set this property to

true

when
a knob drag begins, and to

false

when the drag ends.

**Parameters:** b

- the new value for the

valueIsAdjusting

property
**See Also:** getValueIsAdjusting()

,

BoundedRangeModel.setValueIsAdjusting(boolean)

---

#### setValueIsAdjusting

@BeanProperty

(

bound

=false,

expert

=true,

description

="True if the slider knob is being dragged.")
public void setValueIsAdjusting​(boolean b)

Sets the model's

valueIsAdjusting

property. Slider look and
feel implementations should set this property to

true

when
a knob drag begins, and to

false

when the drag ends.

getExtent

```java
public int getExtent()
```

Returns the "extent" from the

BoundedRangeModel

.
This represents the range of values "covered" by the knob.

**Returns:** an int representing the extent
**See Also:** setExtent(int)

,

BoundedRangeModel.getExtent()

---

#### getExtent

public int getExtent()

Returns the "extent" from the

BoundedRangeModel

.
This represents the range of values "covered" by the knob.

setExtent

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="Size of the range covered by the knob.")
public void setExtent​(int extent)
```

Sets the size of the range "covered" by the knob. Most look
and feel implementations will change the value by this amount
if the user clicks on either side of the knob. This method just
forwards the new extent value to the model.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new extent value is different from the previous extent value,
all change listeners are notified.

**Parameters:** extent

- the new extent
**See Also:** getExtent()

,

BoundedRangeModel.setExtent(int)

---

#### setExtent

@BeanProperty

(

bound

=false,

expert

=true,

description

="Size of the range covered by the knob.")
public void setExtent​(int extent)

Sets the size of the range "covered" by the knob. Most look
and feel implementations will change the value by this amount
if the user clicks on either side of the knob. This method just
forwards the new extent value to the model.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new extent value is different from the previous extent value,
all change listeners are notified.

The data model (an instance of

BoundedRangeModel

)
handles any mathematical
issues arising from assigning faulty values. See the

BoundedRangeModel

documentation for details.

If the new extent value is different from the previous extent value,
all change listeners are notified.

If the new extent value is different from the previous extent value,
all change listeners are notified.

getOrientation

```java
public int getOrientation()
```

Return this slider's vertical or horizontal orientation.

**Returns:** SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL
**See Also:** setOrientation(int)

---

#### getOrientation

public int getOrientation()

Return this slider's vertical or horizontal orientation.

setOrientation

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

enumerationValues
={"JSlider.VERTICAL","JSlider.HORIZONTAL"},

description
="Set the scrollbars orientation to either VERTICAL or HORIZONTAL.")
public void setOrientation​(int orientation)
```

Set the slider's orientation to either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

**Parameters:** orientation

-

HORIZONTAL

or

VERTICAL
**Throws:** IllegalArgumentException

- if orientation is not one of

VERTICAL

,

HORIZONTAL
**See Also:** getOrientation()

---

#### setOrientation

@BeanProperty

(

preferred

=true,

visualUpdate

=true,

enumerationValues

={"JSlider.VERTICAL","JSlider.HORIZONTAL"},

description

="Set the scrollbars orientation to either VERTICAL or HORIZONTAL.")
public void setOrientation​(int orientation)

Set the slider's orientation to either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL

.

setFont

```java
public void setFont​(
Font
font)
```

Sets the font for this component.

**Overrides:** setFont

in class

JComponent
**Parameters:** font

- the desired

Font

for this component
**Since:** 1.6
**See Also:** Component.getFont()

---

#### setFont

public void setFont​(

Font

font)

Sets the font for this component.

imageUpdate

```java
public boolean imageUpdate​(
Image
img,
int infoflags,
int x,
int y,
int w,
int h)
```

Repaints the component when the image has changed.
This

imageUpdate

method of an

ImageObserver

is called when more information about an
image which had been previously requested using an asynchronous
routine such as the

drawImage

method of

Graphics

becomes available.
See the definition of

imageUpdate

for
more information on this method and its arguments.

The

imageUpdate

method of

Component

incrementally draws an image on the component as more of the bits
of the image are available.

If the system property

awt.image.incrementaldraw

is missing or has the value

true

, the image is
incrementally drawn. If the system property has any other value,
then the image is not drawn until it has been completely loaded.

Also, if incremental drawing is in effect, the value of the
system property

awt.image.redrawrate

is interpreted
as an integer to give the maximum redraw rate, in milliseconds. If
the system property is missing or cannot be interpreted as an
integer, the redraw rate is once every 100ms.

The interpretation of the

x

,

y

,

width

, and

height

arguments depends on
the value of the

infoflags

argument.

**Specified by:** imageUpdate

in interface

ImageObserver
**Overrides:** imageUpdate

in class

Component
**Parameters:** img

- the image being observed
**Parameters:** infoflags

- see

imageUpdate

for more information
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** w

- the width
**Parameters:** h

- the height
**Returns:** false

if the infoflags indicate that the
image is completely loaded;

true

otherwise.
**Since:** 1.7
**See Also:** ImageObserver

,

Graphics.drawImage(Image, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, java.awt.image.ImageObserver)

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

---

#### imageUpdate

public boolean imageUpdate​(

Image

img,
int infoflags,
int x,
int y,
int w,
int h)

Repaints the component when the image has changed.
This

imageUpdate

method of an

ImageObserver

is called when more information about an
image which had been previously requested using an asynchronous
routine such as the

drawImage

method of

Graphics

becomes available.
See the definition of

imageUpdate

for
more information on this method and its arguments.

The

imageUpdate

method of

Component

incrementally draws an image on the component as more of the bits
of the image are available.

If the system property

awt.image.incrementaldraw

is missing or has the value

true

, the image is
incrementally drawn. If the system property has any other value,
then the image is not drawn until it has been completely loaded.

Also, if incremental drawing is in effect, the value of the
system property

awt.image.redrawrate

is interpreted
as an integer to give the maximum redraw rate, in milliseconds. If
the system property is missing or cannot be interpreted as an
integer, the redraw rate is once every 100ms.

The interpretation of the

x

,

y

,

width

, and

height

arguments depends on
the value of the

infoflags

argument.

The

imageUpdate

method of

Component

incrementally draws an image on the component as more of the bits
of the image are available.

If the system property

awt.image.incrementaldraw

is missing or has the value

true

, the image is
incrementally drawn. If the system property has any other value,
then the image is not drawn until it has been completely loaded.

Also, if incremental drawing is in effect, the value of the
system property

awt.image.redrawrate

is interpreted
as an integer to give the maximum redraw rate, in milliseconds. If
the system property is missing or cannot be interpreted as an
integer, the redraw rate is once every 100ms.

The interpretation of the

x

,

y

,

width

, and

height

arguments depends on
the value of the

infoflags

argument.

If the system property

awt.image.incrementaldraw

is missing or has the value

true

, the image is
incrementally drawn. If the system property has any other value,
then the image is not drawn until it has been completely loaded.

Also, if incremental drawing is in effect, the value of the
system property

awt.image.redrawrate

is interpreted
as an integer to give the maximum redraw rate, in milliseconds. If
the system property is missing or cannot be interpreted as an
integer, the redraw rate is once every 100ms.

The interpretation of the

x

,

y

,

width

, and

height

arguments depends on
the value of the

infoflags

argument.

Also, if incremental drawing is in effect, the value of the
system property

awt.image.redrawrate

is interpreted
as an integer to give the maximum redraw rate, in milliseconds. If
the system property is missing or cannot be interpreted as an
integer, the redraw rate is once every 100ms.

The interpretation of the

x

,

y

,

width

, and

height

arguments depends on
the value of the

infoflags

argument.

The interpretation of the

x

,

y

,

width

, and

height

arguments depends on
the value of the

infoflags

argument.

getLabelTable

```java
public
Dictionary
getLabelTable()
```

Returns the dictionary of what labels to draw at which values.

**Returns:** the

Dictionary

containing labels and
where to draw them

---

#### getLabelTable

public

Dictionary

getLabelTable()

Returns the dictionary of what labels to draw at which values.

setLabelTable

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="Specifies what labels will be drawn for any given value.")
public void setLabelTable​(
Dictionary
labels)
```

Used to specify what label will be drawn at any given value.
The key-value pairs are of this format:

{ Integer value, java.swing.JComponent label }

.

An easy way to generate a standard table of value labels is by using the

createStandardLabels

method.

Once the labels have been set, this method calls

updateLabelUIs()

.
Note that the labels are only painted if the

paintLabels

property is

true

.

**Parameters:** labels

- new

Dictionary

of labels, or

null

to
remove all labels
**See Also:** createStandardLabels(int)

,

getLabelTable()

,

setPaintLabels(boolean)

---

#### setLabelTable

@BeanProperty

(

hidden

=true,

visualUpdate

=true,

description

="Specifies what labels will be drawn for any given value.")
public void setLabelTable​(

Dictionary

labels)

Used to specify what label will be drawn at any given value.
The key-value pairs are of this format:

{ Integer value, java.swing.JComponent label }

.

An easy way to generate a standard table of value labels is by using the

createStandardLabels

method.

Once the labels have been set, this method calls

updateLabelUIs()

.
Note that the labels are only painted if the

paintLabels

property is

true

.

An easy way to generate a standard table of value labels is by using the

createStandardLabels

method.

Once the labels have been set, this method calls

updateLabelUIs()

.
Note that the labels are only painted if the

paintLabels

property is

true

.

Once the labels have been set, this method calls

updateLabelUIs()

.
Note that the labels are only painted if the

paintLabels

property is

true

.

updateLabelUIs

```java
protected void updateLabelUIs()
```

Updates the UIs for the labels in the label table by calling

updateUI

on each label. The UIs are updated from
the current look and feel. The labels are also set to their
preferred size.

**See Also:** setLabelTable(java.util.Dictionary)

,

JComponent.updateUI()

---

#### updateLabelUIs

protected void updateLabelUIs()

Updates the UIs for the labels in the label table by calling

updateUI

on each label. The UIs are updated from
the current look and feel. The labels are also set to their
preferred size.

createStandardLabels

```java
public
Hashtable
<
Integer
,​
JComponent
> createStandardLabels​(int increment)
```

Creates a

Hashtable

of numerical text labels, starting at the
slider minimum, and using the increment specified.
For example, if you call

createStandardLabels( 10 )

and the slider minimum is zero,
then labels will be created for the values 0, 10, 20, 30, and so on.

For the labels to be drawn on the slider, the returned

Hashtable

must be passed into

setLabelTable

, and

setPaintLabels

must be set to

true

.

For further details on the makeup of the returned

Hashtable

, see
the

setLabelTable

documentation.

**Parameters:** increment

- distance between labels in the generated hashtable
**Returns:** a new

Hashtable

of labels
**Throws:** IllegalArgumentException

- if

increment

is less than or
equal to zero
**See Also:** setLabelTable(java.util.Dictionary)

,

setPaintLabels(boolean)

---

#### createStandardLabels

public

Hashtable

<

Integer

,​

JComponent

> createStandardLabels​(int increment)

Creates a

Hashtable

of numerical text labels, starting at the
slider minimum, and using the increment specified.
For example, if you call

createStandardLabels( 10 )

and the slider minimum is zero,
then labels will be created for the values 0, 10, 20, 30, and so on.

For the labels to be drawn on the slider, the returned

Hashtable

must be passed into

setLabelTable

, and

setPaintLabels

must be set to

true

.

For further details on the makeup of the returned

Hashtable

, see
the

setLabelTable

documentation.

For the labels to be drawn on the slider, the returned

Hashtable

must be passed into

setLabelTable

, and

setPaintLabels

must be set to

true

.

For further details on the makeup of the returned

Hashtable

, see
the

setLabelTable

documentation.

For further details on the makeup of the returned

Hashtable

, see
the

setLabelTable

documentation.

createStandardLabels

```java
public
Hashtable
<
Integer
,​
JComponent
> createStandardLabels​(int increment,
int start)
```

Creates a

Hashtable

of numerical text labels, starting at the
starting point specified, and using the increment specified.
For example, if you call

createStandardLabels( 10, 2 )

,
then labels will be created for the values 2, 12, 22, 32, and so on.

For the labels to be drawn on the slider, the returned

Hashtable

must be passed into

setLabelTable

, and

setPaintLabels

must be set to

true

.

For further details on the makeup of the returned

Hashtable

, see
the

setLabelTable

documentation.

**Parameters:** increment

- distance between labels in the generated hashtable
**Parameters:** start

- value at which the labels will begin
**Returns:** a new

Hashtable

of labels
**Throws:** IllegalArgumentException

- if

start

is
out of range, or if

increment

is less than or equal
to zero
**See Also:** setLabelTable(java.util.Dictionary)

,

setPaintLabels(boolean)

---

#### createStandardLabels

public

Hashtable

<

Integer

,​

JComponent

> createStandardLabels​(int increment,
int start)

Creates a

Hashtable

of numerical text labels, starting at the
starting point specified, and using the increment specified.
For example, if you call

createStandardLabels( 10, 2 )

,
then labels will be created for the values 2, 12, 22, 32, and so on.

For the labels to be drawn on the slider, the returned

Hashtable

must be passed into

setLabelTable

, and

setPaintLabels

must be set to

true

.

For further details on the makeup of the returned

Hashtable

, see
the

setLabelTable

documentation.

For the labels to be drawn on the slider, the returned

Hashtable

must be passed into

setLabelTable

, and

setPaintLabels

must be set to

true

.

For further details on the makeup of the returned

Hashtable

, see
the

setLabelTable

documentation.

For further details on the makeup of the returned

Hashtable

, see
the

setLabelTable

documentation.

getInverted

```java
public boolean getInverted()
```

Returns true if the value-range shown for the slider is reversed,

**Returns:** true if the slider values are reversed from their normal order
**See Also:** setInverted(boolean)

---

#### getInverted

public boolean getInverted()

Returns true if the value-range shown for the slider is reversed,

setInverted

```java
@BeanProperty
(
visualUpdate
=true,

description
="If true reverses the slider values from their normal order")
public void setInverted​(boolean b)
```

Specify true to reverse the value-range shown for the slider and false to
put the value range in the normal order. The order depends on the
slider's

ComponentOrientation

property. Normal (non-inverted)
horizontal sliders with a

ComponentOrientation

value of

LEFT_TO_RIGHT

have their maximum on the right.
Normal horizontal sliders with a

ComponentOrientation

value of

RIGHT_TO_LEFT

have their maximum on the left. Normal vertical
sliders have their maximum on the top. These labels are reversed when the
slider is inverted.

By default, the value of this property is

false

.

**Parameters:** b

- true to reverse the slider values from their normal order

---

#### setInverted

@BeanProperty

(

visualUpdate

=true,

description

="If true reverses the slider values from their normal order")
public void setInverted​(boolean b)

Specify true to reverse the value-range shown for the slider and false to
put the value range in the normal order. The order depends on the
slider's

ComponentOrientation

property. Normal (non-inverted)
horizontal sliders with a

ComponentOrientation

value of

LEFT_TO_RIGHT

have their maximum on the right.
Normal horizontal sliders with a

ComponentOrientation

value of

RIGHT_TO_LEFT

have their maximum on the left. Normal vertical
sliders have their maximum on the top. These labels are reversed when the
slider is inverted.

By default, the value of this property is

false

.

By default, the value of this property is

false

.

getMajorTickSpacing

```java
public int getMajorTickSpacing()
```

This method returns the major tick spacing. The number that is returned
represents the distance, measured in values, between each major tick mark.
If you have a slider with a range from 0 to 50 and the major tick spacing
is set to 10, you will get major ticks next to the following values:
0, 10, 20, 30, 40, 50.

**Returns:** the number of values between major ticks
**See Also:** setMajorTickSpacing(int)

---

#### getMajorTickSpacing

public int getMajorTickSpacing()

This method returns the major tick spacing. The number that is returned
represents the distance, measured in values, between each major tick mark.
If you have a slider with a range from 0 to 50 and the major tick spacing
is set to 10, you will get major ticks next to the following values:
0, 10, 20, 30, 40, 50.

setMajorTickSpacing

```java
@BeanProperty
(
visualUpdate
=true,

description
="Sets the number of values between major tick marks.")
public void setMajorTickSpacing​(int n)
```

This method sets the major tick spacing. The number that is passed in
represents the distance, measured in values, between each major tick mark.
If you have a slider with a range from 0 to 50 and the major tick spacing
is set to 10, you will get major ticks next to the following values:
0, 10, 20, 30, 40, 50.

In order for major ticks to be painted,

setPaintTicks

must be
set to

true

.

This method will also set up a label table for you.
If there is not already a label table, and the major tick spacing is

> 0

, and

getPaintLabels

returns

true

, a standard label table will be generated (by calling

createStandardLabels

) with labels at the major tick marks.
For the example above, you would get text labels: "0",
"10", "20", "30", "40", "50".
The label table is then set on the slider by calling

setLabelTable

.

**Parameters:** n

- new value for the

majorTickSpacing

property
**See Also:** getMajorTickSpacing()

,

setPaintTicks(boolean)

,

setLabelTable(java.util.Dictionary)

,

createStandardLabels(int)

---

#### setMajorTickSpacing

@BeanProperty

(

visualUpdate

=true,

description

="Sets the number of values between major tick marks.")
public void setMajorTickSpacing​(int n)

This method sets the major tick spacing. The number that is passed in
represents the distance, measured in values, between each major tick mark.
If you have a slider with a range from 0 to 50 and the major tick spacing
is set to 10, you will get major ticks next to the following values:
0, 10, 20, 30, 40, 50.

In order for major ticks to be painted,

setPaintTicks

must be
set to

true

.

This method will also set up a label table for you.
If there is not already a label table, and the major tick spacing is

> 0

, and

getPaintLabels

returns

true

, a standard label table will be generated (by calling

createStandardLabels

) with labels at the major tick marks.
For the example above, you would get text labels: "0",
"10", "20", "30", "40", "50".
The label table is then set on the slider by calling

setLabelTable

.

In order for major ticks to be painted,

setPaintTicks

must be
set to

true

.

This method will also set up a label table for you.
If there is not already a label table, and the major tick spacing is

> 0

, and

getPaintLabels

returns

true

, a standard label table will be generated (by calling

createStandardLabels

) with labels at the major tick marks.
For the example above, you would get text labels: "0",
"10", "20", "30", "40", "50".
The label table is then set on the slider by calling

setLabelTable

.

This method will also set up a label table for you.
If there is not already a label table, and the major tick spacing is

> 0

, and

getPaintLabels

returns

true

, a standard label table will be generated (by calling

createStandardLabels

) with labels at the major tick marks.
For the example above, you would get text labels: "0",
"10", "20", "30", "40", "50".
The label table is then set on the slider by calling

setLabelTable

.

getMinorTickSpacing

```java
public int getMinorTickSpacing()
```

This method returns the minor tick spacing. The number that is returned
represents the distance, measured in values, between each minor tick mark.
If you have a slider with a range from 0 to 50 and the minor tick spacing
is set to 10, you will get minor ticks next to the following values:
0, 10, 20, 30, 40, 50.

**Returns:** the number of values between minor ticks
**See Also:** getMinorTickSpacing()

---

#### getMinorTickSpacing

public int getMinorTickSpacing()

This method returns the minor tick spacing. The number that is returned
represents the distance, measured in values, between each minor tick mark.
If you have a slider with a range from 0 to 50 and the minor tick spacing
is set to 10, you will get minor ticks next to the following values:
0, 10, 20, 30, 40, 50.

setMinorTickSpacing

```java
@BeanProperty
(
visualUpdate
=true,

description
="Sets the number of values between minor tick marks.")
public void setMinorTickSpacing​(int n)
```

This method sets the minor tick spacing. The number that is passed in
represents the distance, measured in values, between each minor tick mark.
If you have a slider with a range from 0 to 50 and the minor tick spacing
is set to 10, you will get minor ticks next to the following values:
0, 10, 20, 30, 40, 50.

In order for minor ticks to be painted,

setPaintTicks

must be
set to

true

.

**Parameters:** n

- new value for the

minorTickSpacing

property
**See Also:** getMinorTickSpacing()

,

setPaintTicks(boolean)

---

#### setMinorTickSpacing

@BeanProperty

(

visualUpdate

=true,

description

="Sets the number of values between minor tick marks.")
public void setMinorTickSpacing​(int n)

This method sets the minor tick spacing. The number that is passed in
represents the distance, measured in values, between each minor tick mark.
If you have a slider with a range from 0 to 50 and the minor tick spacing
is set to 10, you will get minor ticks next to the following values:
0, 10, 20, 30, 40, 50.

In order for minor ticks to be painted,

setPaintTicks

must be
set to

true

.

In order for minor ticks to be painted,

setPaintTicks

must be
set to

true

.

getSnapToTicks

```java
public boolean getSnapToTicks()
```

Returns true if the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob.

**Returns:** true if the value snaps to the nearest tick mark, else false
**See Also:** setSnapToTicks(boolean)

---

#### getSnapToTicks

public boolean getSnapToTicks()

Returns true if the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob.

setSnapToTicks

```java
@BeanProperty
(
description
="If true snap the knob to the nearest tick mark.")
public void setSnapToTicks​(boolean b)
```

Specifying true makes the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob.
By default, this property is

false

.

**Parameters:** b

- true to snap the knob to the nearest tick mark
**See Also:** getSnapToTicks()

---

#### setSnapToTicks

@BeanProperty

(

description

="If true snap the knob to the nearest tick mark.")
public void setSnapToTicks​(boolean b)

Specifying true makes the knob (and the data value it represents)
resolve to the closest tick mark next to where the user
positioned the knob.
By default, this property is

false

.

getPaintTicks

```java
public boolean getPaintTicks()
```

Tells if tick marks are to be painted.

**Returns:** true if tick marks are painted, else false
**See Also:** setPaintTicks(boolean)

---

#### getPaintTicks

public boolean getPaintTicks()

Tells if tick marks are to be painted.

setPaintTicks

```java
@BeanProperty
(
visualUpdate
=true,

description
="If true tick marks are painted on the slider.")
public void setPaintTicks​(boolean b)
```

Determines whether tick marks are painted on the slider.
By default, this property is

false

.

**Parameters:** b

- whether or not tick marks should be painted
**See Also:** getPaintTicks()

---

#### setPaintTicks

@BeanProperty

(

visualUpdate

=true,

description

="If true tick marks are painted on the slider.")
public void setPaintTicks​(boolean b)

Determines whether tick marks are painted on the slider.
By default, this property is

false

.

getPaintTrack

```java
public boolean getPaintTrack()
```

Tells if the track (area the slider slides in) is to be painted.

**Returns:** true if track is painted, else false
**See Also:** setPaintTrack(boolean)

---

#### getPaintTrack

public boolean getPaintTrack()

Tells if the track (area the slider slides in) is to be painted.

setPaintTrack

```java
@BeanProperty
(
visualUpdate
=true,

description
="If true, the track is painted on the slider.")
public void setPaintTrack​(boolean b)
```

Determines whether the track is painted on the slider. By default, this
property is

true

. It is up to the look and feel to honor this
property, some may choose to ignore it.

**Parameters:** b

- whether or not to paint the slider track
**See Also:** getPaintTrack()

---

#### setPaintTrack

@BeanProperty

(

visualUpdate

=true,

description

="If true, the track is painted on the slider.")
public void setPaintTrack​(boolean b)

Determines whether the track is painted on the slider. By default, this
property is

true

. It is up to the look and feel to honor this
property, some may choose to ignore it.

getPaintLabels

```java
public boolean getPaintLabels()
```

Tells if labels are to be painted.

**Returns:** true if labels are painted, else false
**See Also:** setPaintLabels(boolean)

---

#### getPaintLabels

public boolean getPaintLabels()

Tells if labels are to be painted.

setPaintLabels

```java
@BeanProperty
(
visualUpdate
=true,

description
="If true labels are painted on the slider.")
public void setPaintLabels​(boolean b)
```

Determines whether labels are painted on the slider.

This method will also set up a label table for you.
If there is not already a label table, and the major tick spacing is

> 0

,
a standard label table will be generated (by calling

createStandardLabels

) with labels at the major tick marks.
The label table is then set on the slider by calling

setLabelTable

.

By default, this property is

false

.

**Parameters:** b

- whether or not to paint labels
**See Also:** getPaintLabels()

,

getLabelTable()

,

createStandardLabels(int)

---

#### setPaintLabels

@BeanProperty

(

visualUpdate

=true,

description

="If true labels are painted on the slider.")
public void setPaintLabels​(boolean b)

Determines whether labels are painted on the slider.

This method will also set up a label table for you.
If there is not already a label table, and the major tick spacing is

> 0

,
a standard label table will be generated (by calling

createStandardLabels

) with labels at the major tick marks.
The label table is then set on the slider by calling

setLabelTable

.

By default, this property is

false

.

This method will also set up a label table for you.
If there is not already a label table, and the major tick spacing is

> 0

,
a standard label table will be generated (by calling

createStandardLabels

) with labels at the major tick marks.
The label table is then set on the slider by calling

setLabelTable

.

By default, this property is

false

.

By default, this property is

false

.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this JSlider. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this JSlider.

---

#### paramString

protected

String

paramString()

Returns a string representation of this JSlider. This method
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

Gets the AccessibleContext associated with this JSlider.
For sliders, the AccessibleContext takes the form of an
AccessibleJSlider.
A new AccessibleJSlider instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJSlider that serves as the
AccessibleContext of this JSlider

---

#### getAccessibleContext

@BeanProperty

(

bound

=false)
public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this JSlider.
For sliders, the AccessibleContext takes the form of an
AccessibleJSlider.
A new AccessibleJSlider instance is created if necessary.

---

