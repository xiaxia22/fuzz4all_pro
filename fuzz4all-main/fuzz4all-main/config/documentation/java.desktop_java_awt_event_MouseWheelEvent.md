# Class MouseWheelEvent

**Source:** `java.desktop\java\awt\event\MouseWheelEvent.html`

### Class Description

```java
public class
MouseWheelEvent

extends
MouseEvent
```

An event which indicates that the mouse wheel was rotated in a component.

A wheel mouse is a mouse which has a wheel in place of the middle button.
This wheel can be rotated towards or away from the user. Mouse wheels are
most often used for scrolling, though other uses are possible.

A MouseWheelEvent object is passed to every

MouseWheelListener

object which registered to receive the "interesting" mouse events using the
component's

addMouseWheelListener

method. Each such listener
object gets a

MouseEvent

containing the mouse event.

Due to the mouse wheel's special relationship to scrolling Components,
MouseWheelEvents are delivered somewhat differently than other MouseEvents.
This is because while other MouseEvents usually affect a change on
the Component directly under the mouse
cursor (for instance, when clicking a button), MouseWheelEvents often have
an effect away from the mouse cursor (moving the wheel while
over a Component inside a ScrollPane should scroll one of the
Scrollbars on the ScrollPane).

MouseWheelEvents start delivery from the Component underneath the
mouse cursor. If MouseWheelEvents are not enabled on the
Component, the event is delivered to the first ancestor
Container with MouseWheelEvents enabled. This will usually be
a ScrollPane with wheel scrolling enabled. The source
Component and x,y coordinates will be relative to the event's
final destination (the ScrollPane). This allows a complex
GUI to be installed without modification into a ScrollPane, and
for all MouseWheelEvents to be delivered to the ScrollPane for
scrolling.

Some AWT Components are implemented using native widgets which
display their own scrollbars and handle their own scrolling.
The particular Components for which this is true will vary from
platform to platform. When the mouse wheel is
moved over one of these Components, the event is delivered straight to
the native widget, and not propagated to ancestors.

Platforms offer customization of the amount of scrolling that
should take place when the mouse wheel is moved. The two most
common settings are to scroll a certain number of "units"
(commonly lines of text in a text-based component) or an entire "block"
(similar to page-up/page-down). The MouseWheelEvent offers
methods for conforming to the underlying platform settings. These
platform settings can be changed at any time by the user. MouseWheelEvents
reflect the most recent settings.

The

MouseWheelEvent

class includes methods for
getting the number of "clicks" by which the mouse wheel is rotated.
The

getWheelRotation()

method returns the integer number
of "clicks" corresponding to the number of notches by which the wheel was
rotated. In addition to this method, the

MouseWheelEvent

class provides the

getPreciseWheelRotation()

method which returns
a double number of "clicks" in case a partial rotation occurred.
The

getPreciseWheelRotation()

method is useful if a mouse supports
a high-resolution wheel, such as a freely rotating wheel with no
notches. Applications can benefit by using this method to process
mouse wheel events more precisely, and thus, making visual perception
smoother.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### @Native

public static final int WHEEL_UNIT_SCROLL

Constant representing scrolling by "units" (like scrolling with the
arrow keys)

**See Also:**
- getScrollType()

,

Constant Field Values

---

#### @Native

public static final int WHEEL_BLOCK_SCROLL

Constant representing scrolling by a "block" (like scrolling
with page-up, page-down keys)

**See Also:**
- getScrollType()

,

Constant Field Values

---

### Constructor Details

#### public MouseWheelEvent​(
Component
source,
int id,
long when,
int modifiers,
int x,
int y,
int clickCount,
boolean popupTrigger,
int scrollType,
int scrollAmount,
int wheelRotation)

Constructs a

MouseWheelEvent

object with the
specified source component, type, modifiers, coordinates,
scroll type, scroll amount, and wheel rotation.

Absolute coordinates xAbs and yAbs are set to source's location on screen plus
relative coordinates x and y. xAbs and yAbs are set to zero if the source is not showing.

Note that passing in an invalid

id

results in
unspecified behavior. This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:**
- source

- the

Component

that originated
the event
- id

- the integer that identifies the event
- when

- a long that gives the time the event occurred
- modifiers

- the modifier keys down during event
(shift, ctrl, alt, meta)
- x

- the horizontal x coordinate for the mouse location
- y

- the vertical y coordinate for the mouse location
- clickCount

- the number of mouse clicks associated with event
- popupTrigger

- a boolean, true if this event is a trigger for a
popup-menu
- scrollType

- the type of scrolling which should take place in
response to this event; valid values are

WHEEL_UNIT_SCROLL

and

WHEEL_BLOCK_SCROLL
- scrollAmount

- for scrollType

WHEEL_UNIT_SCROLL

,
the number of units to be scrolled
- wheelRotation

- the integer number of "clicks" by which the mouse
wheel was rotated

**Throws:**
- IllegalArgumentException

- if

source

is null

**See Also:**
- MouseEvent(java.awt.Component, int, long, int, int, int, int, boolean)

,

MouseEvent(java.awt.Component, int, long, int, int, int, int, int, int, boolean, int)

---

#### public MouseWheelEvent​(
Component
source,
int id,
long when,
int modifiers,
int x,
int y,
int xAbs,
int yAbs,
int clickCount,
boolean popupTrigger,
int scrollType,
int scrollAmount,
int wheelRotation)

Constructs a

MouseWheelEvent

object with the
specified source component, type, modifiers, coordinates,
absolute coordinates, scroll type, scroll amount, and wheel rotation.

Note that passing in an invalid

id

results in
unspecified behavior. This method throws an

IllegalArgumentException

if

source

is

null

.

Even if inconsistent values for relative and absolute coordinates are
passed to the constructor, the MouseWheelEvent instance is still
created and no exception is thrown.

**Parameters:**
- source

- the

Component

that originated
the event
- id

- the integer that identifies the event
- when

- a long that gives the time the event occurred
- modifiers

- the modifier keys down during event
(shift, ctrl, alt, meta)
- x

- the horizontal x coordinate for the mouse location
- y

- the vertical y coordinate for the mouse location
- xAbs

- the absolute horizontal x coordinate for the mouse location
- yAbs

- the absolute vertical y coordinate for the mouse location
- clickCount

- the number of mouse clicks associated with event
- popupTrigger

- a boolean, true if this event is a trigger for a
popup-menu
- scrollType

- the type of scrolling which should take place in
response to this event; valid values are

WHEEL_UNIT_SCROLL

and

WHEEL_BLOCK_SCROLL
- scrollAmount

- for scrollType

WHEEL_UNIT_SCROLL

,
the number of units to be scrolled
- wheelRotation

- the integer number of "clicks" by which the mouse
wheel was rotated

**Throws:**
- IllegalArgumentException

- if

source

is null

**See Also:**
- MouseEvent(java.awt.Component, int, long, int, int, int, int, boolean)

,

MouseEvent(java.awt.Component, int, long, int, int, int, int, int, int, boolean, int)

**Since:**
- 1.6

---

#### public MouseWheelEvent​(
Component
source,
int id,
long when,
int modifiers,
int x,
int y,
int xAbs,
int yAbs,
int clickCount,
boolean popupTrigger,
int scrollType,
int scrollAmount,
int wheelRotation,
double preciseWheelRotation)

Constructs a

MouseWheelEvent

object with the specified
source component, type, modifiers, coordinates, absolute coordinates,
scroll type, scroll amount, and wheel rotation.

Note that passing in an invalid

id

parameter results
in unspecified behavior. This method throws an

IllegalArgumentException

if

source

equals

null

.

Even if inconsistent values for relative and absolute coordinates
are passed to the constructor, a

MouseWheelEvent

instance
is still created and no exception is thrown.

**Parameters:**
- source

- the

Component

that originated the event
- id

- the integer value that identifies the event
- when

- a long value that gives the time when the event occurred
- modifiers

- the modifier keys down during event
(shift, ctrl, alt, meta)
- x

- the horizontal

x

coordinate for the
mouse location
- y

- the vertical

y

coordinate for the
mouse location
- xAbs

- the absolute horizontal

x

coordinate for
the mouse location
- yAbs

- the absolute vertical

y

coordinate for
the mouse location
- clickCount

- the number of mouse clicks associated with the event
- popupTrigger

- a boolean value,

true

if this event is a trigger
for a popup-menu
- scrollType

- the type of scrolling which should take place in
response to this event; valid values are

WHEEL_UNIT_SCROLL

and

WHEEL_BLOCK_SCROLL
- scrollAmount

- for scrollType

WHEEL_UNIT_SCROLL

,
the number of units to be scrolled
- wheelRotation

- the integer number of "clicks" by which the mouse wheel
was rotated
- preciseWheelRotation

- the double number of "clicks" by which the mouse wheel
was rotated

**Throws:**
- IllegalArgumentException

- if

source

is null

**See Also:**
- MouseEvent(java.awt.Component, int, long, int, int, int, int, boolean)

,

MouseEvent(java.awt.Component, int, long, int, int, int, int, int, int, boolean, int)

**Since:**
- 1.7

---

### Method Details

#### public int getScrollType()

Returns the type of scrolling that should take place in response to this
event. This is determined by the native platform. Legal values are:

- MouseWheelEvent.WHEEL_UNIT_SCROLL

MouseWheelEvent.WHEEL_BLOCK_SCROLL

**Returns:**
- either MouseWheelEvent.WHEEL_UNIT_SCROLL or
MouseWheelEvent.WHEEL_BLOCK_SCROLL, depending on the configuration of
the native platform.

**See Also:**
- Adjustable.getUnitIncrement()

,

Adjustable.getBlockIncrement()

,

Scrollable.getScrollableUnitIncrement(java.awt.Rectangle, int, int)

,

Scrollable.getScrollableBlockIncrement(java.awt.Rectangle, int, int)

---

#### public int getScrollAmount()

Returns the number of units that should be scrolled per
click of mouse wheel rotation.
Only valid if

getScrollType

returns

MouseWheelEvent.WHEEL_UNIT_SCROLL

**Returns:**
- number of units to scroll, or an undefined value if

getScrollType

returns

MouseWheelEvent.WHEEL_BLOCK_SCROLL

**See Also:**
- getScrollType()

---

#### public int getWheelRotation()

Returns the number of "clicks" the mouse wheel was rotated, as an integer.
A partial rotation may occur if the mouse supports a high-resolution wheel.
In this case, the method returns zero until a full "click" has been accumulated.

**Returns:**
- negative values if the mouse wheel was rotated up/away from
the user, and positive values if the mouse wheel was rotated down/
towards the user

**See Also:**
- getPreciseWheelRotation()

---

#### public double getPreciseWheelRotation()

Returns the number of "clicks" the mouse wheel was rotated, as a double.
A partial rotation may occur if the mouse supports a high-resolution wheel.
In this case, the return value will include a fractional "click".

**Returns:**
- negative values if the mouse wheel was rotated up or away from
the user, and positive values if the mouse wheel was rotated down or
towards the user

**See Also:**
- getWheelRotation()

**Since:**
- 1.7

---

#### public int getUnitsToScroll()

This is a convenience method to aid in the implementation of
the common-case MouseWheelListener - to scroll a ScrollPane or
JScrollPane by an amount which conforms to the platform settings.
(Note, however, that

ScrollPane

and

JScrollPane

already have this functionality built in.)

This method returns the number of units to scroll when scroll type is
MouseWheelEvent.WHEEL_UNIT_SCROLL, and should only be called if

getScrollType

returns MouseWheelEvent.WHEEL_UNIT_SCROLL.

Direction of scroll, amount of wheel movement,
and platform settings for wheel scrolling are all accounted for.
This method does not and cannot take into account value of the
Adjustable/Scrollable unit increment, as this will vary among
scrolling components.

A simplified example of how this method might be used in a
listener:

```java
mouseWheelMoved(MouseWheelEvent event) {
ScrollPane sp = getScrollPaneFromSomewhere();
Adjustable adj = sp.getVAdjustable()
if (MouseWheelEvent.getScrollType() == WHEEL_UNIT_SCROLL) {
int totalScrollAmount =
event.getUnitsToScroll() *
adj.getUnitIncrement();
adj.setValue(adj.getValue() + totalScrollAmount);
}
}
```

**Returns:**
- the number of units to scroll based on the direction and amount
of mouse wheel rotation, and on the wheel scrolling settings of the
native platform

**See Also:**
- getScrollType()

,

getScrollAmount()

,

MouseWheelListener

,

Adjustable

,

Adjustable.getUnitIncrement()

,

Scrollable

,

Scrollable.getScrollableUnitIncrement(java.awt.Rectangle, int, int)

,

ScrollPane

,

ScrollPane.setWheelScrollingEnabled(boolean)

,

JScrollPane

,

JScrollPane.setWheelScrollingEnabled(boolean)

---

#### public
String
paramString()

Returns a parameter string identifying this event.
This method is useful for event-logging and for debugging.

**Overrides:**
- paramString

in class

MouseEvent

**Returns:**
- a string identifying the event and its attributes

---

### Additional Sections

#### Class MouseWheelEvent

java.lang.Object

- java.util.EventObject
- - java.awt.AWTEvent
- - java.awt.event.ComponentEvent
- - java.awt.event.InputEvent
- - java.awt.event.MouseEvent
- - java.awt.event.MouseWheelEvent

java.util.EventObject

- java.awt.AWTEvent
- - java.awt.event.ComponentEvent
- - java.awt.event.InputEvent
- - java.awt.event.MouseEvent
- - java.awt.event.MouseWheelEvent

java.awt.AWTEvent

- java.awt.event.ComponentEvent
- - java.awt.event.InputEvent
- - java.awt.event.MouseEvent
- - java.awt.event.MouseWheelEvent

java.awt.event.ComponentEvent

- java.awt.event.InputEvent
- - java.awt.event.MouseEvent
- - java.awt.event.MouseWheelEvent

java.awt.event.InputEvent

- java.awt.event.MouseEvent
- - java.awt.event.MouseWheelEvent

java.awt.event.MouseEvent

- java.awt.event.MouseWheelEvent

java.awt.event.MouseWheelEvent

**All Implemented Interfaces:** Serializable

```java
public class
MouseWheelEvent

extends
MouseEvent
```

An event which indicates that the mouse wheel was rotated in a component.

A wheel mouse is a mouse which has a wheel in place of the middle button.
This wheel can be rotated towards or away from the user. Mouse wheels are
most often used for scrolling, though other uses are possible.

A MouseWheelEvent object is passed to every

MouseWheelListener

object which registered to receive the "interesting" mouse events using the
component's

addMouseWheelListener

method. Each such listener
object gets a

MouseEvent

containing the mouse event.

Due to the mouse wheel's special relationship to scrolling Components,
MouseWheelEvents are delivered somewhat differently than other MouseEvents.
This is because while other MouseEvents usually affect a change on
the Component directly under the mouse
cursor (for instance, when clicking a button), MouseWheelEvents often have
an effect away from the mouse cursor (moving the wheel while
over a Component inside a ScrollPane should scroll one of the
Scrollbars on the ScrollPane).

MouseWheelEvents start delivery from the Component underneath the
mouse cursor. If MouseWheelEvents are not enabled on the
Component, the event is delivered to the first ancestor
Container with MouseWheelEvents enabled. This will usually be
a ScrollPane with wheel scrolling enabled. The source
Component and x,y coordinates will be relative to the event's
final destination (the ScrollPane). This allows a complex
GUI to be installed without modification into a ScrollPane, and
for all MouseWheelEvents to be delivered to the ScrollPane for
scrolling.

Some AWT Components are implemented using native widgets which
display their own scrollbars and handle their own scrolling.
The particular Components for which this is true will vary from
platform to platform. When the mouse wheel is
moved over one of these Components, the event is delivered straight to
the native widget, and not propagated to ancestors.

Platforms offer customization of the amount of scrolling that
should take place when the mouse wheel is moved. The two most
common settings are to scroll a certain number of "units"
(commonly lines of text in a text-based component) or an entire "block"
(similar to page-up/page-down). The MouseWheelEvent offers
methods for conforming to the underlying platform settings. These
platform settings can be changed at any time by the user. MouseWheelEvents
reflect the most recent settings.

The

MouseWheelEvent

class includes methods for
getting the number of "clicks" by which the mouse wheel is rotated.
The

getWheelRotation()

method returns the integer number
of "clicks" corresponding to the number of notches by which the wheel was
rotated. In addition to this method, the

MouseWheelEvent

class provides the

getPreciseWheelRotation()

method which returns
a double number of "clicks" in case a partial rotation occurred.
The

getPreciseWheelRotation()

method is useful if a mouse supports
a high-resolution wheel, such as a freely rotating wheel with no
notches. Applications can benefit by using this method to process
mouse wheel events more precisely, and thus, making visual perception
smoother.

**Since:** 1.4
**See Also:** MouseWheelListener

,

ScrollPane

,

ScrollPane.setWheelScrollingEnabled(boolean)

,

JScrollPane

,

JScrollPane.setWheelScrollingEnabled(boolean)

,

Serialized Form

public class

MouseWheelEvent

extends

MouseEvent

An event which indicates that the mouse wheel was rotated in a component.

A wheel mouse is a mouse which has a wheel in place of the middle button.
This wheel can be rotated towards or away from the user. Mouse wheels are
most often used for scrolling, though other uses are possible.

A MouseWheelEvent object is passed to every

MouseWheelListener

object which registered to receive the "interesting" mouse events using the
component's

addMouseWheelListener

method. Each such listener
object gets a

MouseEvent

containing the mouse event.

Due to the mouse wheel's special relationship to scrolling Components,
MouseWheelEvents are delivered somewhat differently than other MouseEvents.
This is because while other MouseEvents usually affect a change on
the Component directly under the mouse
cursor (for instance, when clicking a button), MouseWheelEvents often have
an effect away from the mouse cursor (moving the wheel while
over a Component inside a ScrollPane should scroll one of the
Scrollbars on the ScrollPane).

MouseWheelEvents start delivery from the Component underneath the
mouse cursor. If MouseWheelEvents are not enabled on the
Component, the event is delivered to the first ancestor
Container with MouseWheelEvents enabled. This will usually be
a ScrollPane with wheel scrolling enabled. The source
Component and x,y coordinates will be relative to the event's
final destination (the ScrollPane). This allows a complex
GUI to be installed without modification into a ScrollPane, and
for all MouseWheelEvents to be delivered to the ScrollPane for
scrolling.

Some AWT Components are implemented using native widgets which
display their own scrollbars and handle their own scrolling.
The particular Components for which this is true will vary from
platform to platform. When the mouse wheel is
moved over one of these Components, the event is delivered straight to
the native widget, and not propagated to ancestors.

Platforms offer customization of the amount of scrolling that
should take place when the mouse wheel is moved. The two most
common settings are to scroll a certain number of "units"
(commonly lines of text in a text-based component) or an entire "block"
(similar to page-up/page-down). The MouseWheelEvent offers
methods for conforming to the underlying platform settings. These
platform settings can be changed at any time by the user. MouseWheelEvents
reflect the most recent settings.

The

MouseWheelEvent

class includes methods for
getting the number of "clicks" by which the mouse wheel is rotated.
The

getWheelRotation()

method returns the integer number
of "clicks" corresponding to the number of notches by which the wheel was
rotated. In addition to this method, the

MouseWheelEvent

class provides the

getPreciseWheelRotation()

method which returns
a double number of "clicks" in case a partial rotation occurred.
The

getPreciseWheelRotation()

method is useful if a mouse supports
a high-resolution wheel, such as a freely rotating wheel with no
notches. Applications can benefit by using this method to process
mouse wheel events more precisely, and thus, making visual perception
smoother.

A wheel mouse is a mouse which has a wheel in place of the middle button.
This wheel can be rotated towards or away from the user. Mouse wheels are
most often used for scrolling, though other uses are possible.

A MouseWheelEvent object is passed to every

MouseWheelListener

object which registered to receive the "interesting" mouse events using the
component's

addMouseWheelListener

method. Each such listener
object gets a

MouseEvent

containing the mouse event.

Due to the mouse wheel's special relationship to scrolling Components,
MouseWheelEvents are delivered somewhat differently than other MouseEvents.
This is because while other MouseEvents usually affect a change on
the Component directly under the mouse
cursor (for instance, when clicking a button), MouseWheelEvents often have
an effect away from the mouse cursor (moving the wheel while
over a Component inside a ScrollPane should scroll one of the
Scrollbars on the ScrollPane).

MouseWheelEvents start delivery from the Component underneath the
mouse cursor. If MouseWheelEvents are not enabled on the
Component, the event is delivered to the first ancestor
Container with MouseWheelEvents enabled. This will usually be
a ScrollPane with wheel scrolling enabled. The source
Component and x,y coordinates will be relative to the event's
final destination (the ScrollPane). This allows a complex
GUI to be installed without modification into a ScrollPane, and
for all MouseWheelEvents to be delivered to the ScrollPane for
scrolling.

Some AWT Components are implemented using native widgets which
display their own scrollbars and handle their own scrolling.
The particular Components for which this is true will vary from
platform to platform. When the mouse wheel is
moved over one of these Components, the event is delivered straight to
the native widget, and not propagated to ancestors.

Platforms offer customization of the amount of scrolling that
should take place when the mouse wheel is moved. The two most
common settings are to scroll a certain number of "units"
(commonly lines of text in a text-based component) or an entire "block"
(similar to page-up/page-down). The MouseWheelEvent offers
methods for conforming to the underlying platform settings. These
platform settings can be changed at any time by the user. MouseWheelEvents
reflect the most recent settings.

The

MouseWheelEvent

class includes methods for
getting the number of "clicks" by which the mouse wheel is rotated.
The

getWheelRotation()

method returns the integer number
of "clicks" corresponding to the number of notches by which the wheel was
rotated. In addition to this method, the

MouseWheelEvent

class provides the

getPreciseWheelRotation()

method which returns
a double number of "clicks" in case a partial rotation occurred.
The

getPreciseWheelRotation()

method is useful if a mouse supports
a high-resolution wheel, such as a freely rotating wheel with no
notches. Applications can benefit by using this method to process
mouse wheel events more precisely, and thus, making visual perception
smoother.

A MouseWheelEvent object is passed to every

MouseWheelListener

object which registered to receive the "interesting" mouse events using the
component's

addMouseWheelListener

method. Each such listener
object gets a

MouseEvent

containing the mouse event.

Due to the mouse wheel's special relationship to scrolling Components,
MouseWheelEvents are delivered somewhat differently than other MouseEvents.
This is because while other MouseEvents usually affect a change on
the Component directly under the mouse
cursor (for instance, when clicking a button), MouseWheelEvents often have
an effect away from the mouse cursor (moving the wheel while
over a Component inside a ScrollPane should scroll one of the
Scrollbars on the ScrollPane).

MouseWheelEvents start delivery from the Component underneath the
mouse cursor. If MouseWheelEvents are not enabled on the
Component, the event is delivered to the first ancestor
Container with MouseWheelEvents enabled. This will usually be
a ScrollPane with wheel scrolling enabled. The source
Component and x,y coordinates will be relative to the event's
final destination (the ScrollPane). This allows a complex
GUI to be installed without modification into a ScrollPane, and
for all MouseWheelEvents to be delivered to the ScrollPane for
scrolling.

Some AWT Components are implemented using native widgets which
display their own scrollbars and handle their own scrolling.
The particular Components for which this is true will vary from
platform to platform. When the mouse wheel is
moved over one of these Components, the event is delivered straight to
the native widget, and not propagated to ancestors.

Platforms offer customization of the amount of scrolling that
should take place when the mouse wheel is moved. The two most
common settings are to scroll a certain number of "units"
(commonly lines of text in a text-based component) or an entire "block"
(similar to page-up/page-down). The MouseWheelEvent offers
methods for conforming to the underlying platform settings. These
platform settings can be changed at any time by the user. MouseWheelEvents
reflect the most recent settings.

The

MouseWheelEvent

class includes methods for
getting the number of "clicks" by which the mouse wheel is rotated.
The

getWheelRotation()

method returns the integer number
of "clicks" corresponding to the number of notches by which the wheel was
rotated. In addition to this method, the

MouseWheelEvent

class provides the

getPreciseWheelRotation()

method which returns
a double number of "clicks" in case a partial rotation occurred.
The

getPreciseWheelRotation()

method is useful if a mouse supports
a high-resolution wheel, such as a freely rotating wheel with no
notches. Applications can benefit by using this method to process
mouse wheel events more precisely, and thus, making visual perception
smoother.

Due to the mouse wheel's special relationship to scrolling Components,
MouseWheelEvents are delivered somewhat differently than other MouseEvents.
This is because while other MouseEvents usually affect a change on
the Component directly under the mouse
cursor (for instance, when clicking a button), MouseWheelEvents often have
an effect away from the mouse cursor (moving the wheel while
over a Component inside a ScrollPane should scroll one of the
Scrollbars on the ScrollPane).

MouseWheelEvents start delivery from the Component underneath the
mouse cursor. If MouseWheelEvents are not enabled on the
Component, the event is delivered to the first ancestor
Container with MouseWheelEvents enabled. This will usually be
a ScrollPane with wheel scrolling enabled. The source
Component and x,y coordinates will be relative to the event's
final destination (the ScrollPane). This allows a complex
GUI to be installed without modification into a ScrollPane, and
for all MouseWheelEvents to be delivered to the ScrollPane for
scrolling.

Some AWT Components are implemented using native widgets which
display their own scrollbars and handle their own scrolling.
The particular Components for which this is true will vary from
platform to platform. When the mouse wheel is
moved over one of these Components, the event is delivered straight to
the native widget, and not propagated to ancestors.

Platforms offer customization of the amount of scrolling that
should take place when the mouse wheel is moved. The two most
common settings are to scroll a certain number of "units"
(commonly lines of text in a text-based component) or an entire "block"
(similar to page-up/page-down). The MouseWheelEvent offers
methods for conforming to the underlying platform settings. These
platform settings can be changed at any time by the user. MouseWheelEvents
reflect the most recent settings.

The

MouseWheelEvent

class includes methods for
getting the number of "clicks" by which the mouse wheel is rotated.
The

getWheelRotation()

method returns the integer number
of "clicks" corresponding to the number of notches by which the wheel was
rotated. In addition to this method, the

MouseWheelEvent

class provides the

getPreciseWheelRotation()

method which returns
a double number of "clicks" in case a partial rotation occurred.
The

getPreciseWheelRotation()

method is useful if a mouse supports
a high-resolution wheel, such as a freely rotating wheel with no
notches. Applications can benefit by using this method to process
mouse wheel events more precisely, and thus, making visual perception
smoother.

MouseWheelEvents start delivery from the Component underneath the
mouse cursor. If MouseWheelEvents are not enabled on the
Component, the event is delivered to the first ancestor
Container with MouseWheelEvents enabled. This will usually be
a ScrollPane with wheel scrolling enabled. The source
Component and x,y coordinates will be relative to the event's
final destination (the ScrollPane). This allows a complex
GUI to be installed without modification into a ScrollPane, and
for all MouseWheelEvents to be delivered to the ScrollPane for
scrolling.

Some AWT Components are implemented using native widgets which
display their own scrollbars and handle their own scrolling.
The particular Components for which this is true will vary from
platform to platform. When the mouse wheel is
moved over one of these Components, the event is delivered straight to
the native widget, and not propagated to ancestors.

Platforms offer customization of the amount of scrolling that
should take place when the mouse wheel is moved. The two most
common settings are to scroll a certain number of "units"
(commonly lines of text in a text-based component) or an entire "block"
(similar to page-up/page-down). The MouseWheelEvent offers
methods for conforming to the underlying platform settings. These
platform settings can be changed at any time by the user. MouseWheelEvents
reflect the most recent settings.

The

MouseWheelEvent

class includes methods for
getting the number of "clicks" by which the mouse wheel is rotated.
The

getWheelRotation()

method returns the integer number
of "clicks" corresponding to the number of notches by which the wheel was
rotated. In addition to this method, the

MouseWheelEvent

class provides the

getPreciseWheelRotation()

method which returns
a double number of "clicks" in case a partial rotation occurred.
The

getPreciseWheelRotation()

method is useful if a mouse supports
a high-resolution wheel, such as a freely rotating wheel with no
notches. Applications can benefit by using this method to process
mouse wheel events more precisely, and thus, making visual perception
smoother.

Some AWT Components are implemented using native widgets which
display their own scrollbars and handle their own scrolling.
The particular Components for which this is true will vary from
platform to platform. When the mouse wheel is
moved over one of these Components, the event is delivered straight to
the native widget, and not propagated to ancestors.

Platforms offer customization of the amount of scrolling that
should take place when the mouse wheel is moved. The two most
common settings are to scroll a certain number of "units"
(commonly lines of text in a text-based component) or an entire "block"
(similar to page-up/page-down). The MouseWheelEvent offers
methods for conforming to the underlying platform settings. These
platform settings can be changed at any time by the user. MouseWheelEvents
reflect the most recent settings.

The

MouseWheelEvent

class includes methods for
getting the number of "clicks" by which the mouse wheel is rotated.
The

getWheelRotation()

method returns the integer number
of "clicks" corresponding to the number of notches by which the wheel was
rotated. In addition to this method, the

MouseWheelEvent

class provides the

getPreciseWheelRotation()

method which returns
a double number of "clicks" in case a partial rotation occurred.
The

getPreciseWheelRotation()

method is useful if a mouse supports
a high-resolution wheel, such as a freely rotating wheel with no
notches. Applications can benefit by using this method to process
mouse wheel events more precisely, and thus, making visual perception
smoother.

Platforms offer customization of the amount of scrolling that
should take place when the mouse wheel is moved. The two most
common settings are to scroll a certain number of "units"
(commonly lines of text in a text-based component) or an entire "block"
(similar to page-up/page-down). The MouseWheelEvent offers
methods for conforming to the underlying platform settings. These
platform settings can be changed at any time by the user. MouseWheelEvents
reflect the most recent settings.

The

MouseWheelEvent

class includes methods for
getting the number of "clicks" by which the mouse wheel is rotated.
The

getWheelRotation()

method returns the integer number
of "clicks" corresponding to the number of notches by which the wheel was
rotated. In addition to this method, the

MouseWheelEvent

class provides the

getPreciseWheelRotation()

method which returns
a double number of "clicks" in case a partial rotation occurred.
The

getPreciseWheelRotation()

method is useful if a mouse supports
a high-resolution wheel, such as a freely rotating wheel with no
notches. Applications can benefit by using this method to process
mouse wheel events more precisely, and thus, making visual perception
smoother.

The

MouseWheelEvent

class includes methods for
getting the number of "clicks" by which the mouse wheel is rotated.
The

getWheelRotation()

method returns the integer number
of "clicks" corresponding to the number of notches by which the wheel was
rotated. In addition to this method, the

MouseWheelEvent

class provides the

getPreciseWheelRotation()

method which returns
a double number of "clicks" in case a partial rotation occurred.
The

getPreciseWheelRotation()

method is useful if a mouse supports
a high-resolution wheel, such as a freely rotating wheel with no
notches. Applications can benefit by using this method to process
mouse wheel events more precisely, and thus, making visual perception
smoother.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

WHEEL_BLOCK_SCROLL

Constant representing scrolling by a "block" (like scrolling
with page-up, page-down keys)

static int

WHEEL_UNIT_SCROLL

Constant representing scrolling by "units" (like scrolling with the
arrow keys)

- Fields declared in class java.awt.event.

MouseEvent

BUTTON1

,

BUTTON2

,

BUTTON3

,

MOUSE_CLICKED

,

MOUSE_DRAGGED

,

MOUSE_ENTERED

,

MOUSE_EXITED

,

MOUSE_FIRST

,

MOUSE_LAST

,

MOUSE_MOVED

,

MOUSE_PRESSED

,

MOUSE_RELEASED

,

MOUSE_WHEEL

,

NOBUTTON

- Fields declared in class java.awt.event.

InputEvent

ALT_DOWN_MASK

,

ALT_GRAPH_DOWN_MASK

,

ALT_GRAPH_MASK

,

ALT_MASK

,

BUTTON1_DOWN_MASK

,

BUTTON1_MASK

,

BUTTON2_DOWN_MASK

,

BUTTON2_MASK

,

BUTTON3_DOWN_MASK

,

BUTTON3_MASK

,

CTRL_DOWN_MASK

,

CTRL_MASK

,

META_DOWN_MASK

,

META_MASK

,

SHIFT_DOWN_MASK

,

SHIFT_MASK

- Fields declared in class java.awt.event.

ComponentEvent

COMPONENT_FIRST

,

COMPONENT_HIDDEN

,

COMPONENT_LAST

,

COMPONENT_MOVED

,

COMPONENT_RESIZED

,

COMPONENT_SHOWN

- Fields declared in class java.awt.

AWTEvent

ACTION_EVENT_MASK

,

ADJUSTMENT_EVENT_MASK

,

COMPONENT_EVENT_MASK

,

consumed

,

CONTAINER_EVENT_MASK

,

FOCUS_EVENT_MASK

,

HIERARCHY_BOUNDS_EVENT_MASK

,

HIERARCHY_EVENT_MASK

,

id

,

INPUT_METHOD_EVENT_MASK

,

INVOCATION_EVENT_MASK

,

ITEM_EVENT_MASK

,

KEY_EVENT_MASK

,

MOUSE_EVENT_MASK

,

MOUSE_MOTION_EVENT_MASK

,

MOUSE_WHEEL_EVENT_MASK

,

PAINT_EVENT_MASK

,

RESERVED_ID_MAX

,

TEXT_EVENT_MASK

,

WINDOW_EVENT_MASK

,

WINDOW_FOCUS_EVENT_MASK

,

WINDOW_STATE_EVENT_MASK

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MouseWheelEvent

​(

Component

source,
int id,
long when,
int modifiers,
int x,
int y,
int clickCount,
boolean popupTrigger,
int scrollType,
int scrollAmount,
int wheelRotation)

Constructs a

MouseWheelEvent

object with the
specified source component, type, modifiers, coordinates,
scroll type, scroll amount, and wheel rotation.

MouseWheelEvent

​(

Component

source,
int id,
long when,
int modifiers,
int x,
int y,
int xAbs,
int yAbs,
int clickCount,
boolean popupTrigger,
int scrollType,
int scrollAmount,
int wheelRotation)

Constructs a

MouseWheelEvent

object with the
specified source component, type, modifiers, coordinates,
absolute coordinates, scroll type, scroll amount, and wheel rotation.

MouseWheelEvent

​(

Component

source,
int id,
long when,
int modifiers,
int x,
int y,
int xAbs,
int yAbs,
int clickCount,
boolean popupTrigger,
int scrollType,
int scrollAmount,
int wheelRotation,
double preciseWheelRotation)

Constructs a

MouseWheelEvent

object with the specified
source component, type, modifiers, coordinates, absolute coordinates,
scroll type, scroll amount, and wheel rotation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

double

getPreciseWheelRotation

()

Returns the number of "clicks" the mouse wheel was rotated, as a double.

int

getScrollAmount

()

Returns the number of units that should be scrolled per
click of mouse wheel rotation.

int

getScrollType

()

Returns the type of scrolling that should take place in response to this
event.

int

getUnitsToScroll

()

This is a convenience method to aid in the implementation of
the common-case MouseWheelListener - to scroll a ScrollPane or
JScrollPane by an amount which conforms to the platform settings.

int

getWheelRotation

()

Returns the number of "clicks" the mouse wheel was rotated, as an integer.

String

paramString

()

Returns a parameter string identifying this event.

- Methods declared in class java.awt.event.

MouseEvent

getButton

,

getClickCount

,

getLocationOnScreen

,

getMouseModifiersText

,

getPoint

,

getX

,

getXOnScreen

,

getY

,

getYOnScreen

,

isPopupTrigger

,

translatePoint

- Methods declared in class java.awt.event.

InputEvent

consume

,

getMaskForButton

,

getModifiers

,

getModifiersEx

,

getModifiersExText

,

getWhen

,

isAltDown

,

isAltGraphDown

,

isConsumed

,

isControlDown

,

isMetaDown

,

isShiftDown

- Methods declared in class java.awt.event.

ComponentEvent

getComponent

- Methods declared in class java.awt.

AWTEvent

getID

,

setSource

,

toString

- Methods declared in class java.util.

EventObject

getSource

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

static int

WHEEL_BLOCK_SCROLL

Constant representing scrolling by a "block" (like scrolling
with page-up, page-down keys)

static int

WHEEL_UNIT_SCROLL

Constant representing scrolling by "units" (like scrolling with the
arrow keys)

- Fields declared in class java.awt.event.

MouseEvent

BUTTON1

,

BUTTON2

,

BUTTON3

,

MOUSE_CLICKED

,

MOUSE_DRAGGED

,

MOUSE_ENTERED

,

MOUSE_EXITED

,

MOUSE_FIRST

,

MOUSE_LAST

,

MOUSE_MOVED

,

MOUSE_PRESSED

,

MOUSE_RELEASED

,

MOUSE_WHEEL

,

NOBUTTON

- Fields declared in class java.awt.event.

InputEvent

ALT_DOWN_MASK

,

ALT_GRAPH_DOWN_MASK

,

ALT_GRAPH_MASK

,

ALT_MASK

,

BUTTON1_DOWN_MASK

,

BUTTON1_MASK

,

BUTTON2_DOWN_MASK

,

BUTTON2_MASK

,

BUTTON3_DOWN_MASK

,

BUTTON3_MASK

,

CTRL_DOWN_MASK

,

CTRL_MASK

,

META_DOWN_MASK

,

META_MASK

,

SHIFT_DOWN_MASK

,

SHIFT_MASK

- Fields declared in class java.awt.event.

ComponentEvent

COMPONENT_FIRST

,

COMPONENT_HIDDEN

,

COMPONENT_LAST

,

COMPONENT_MOVED

,

COMPONENT_RESIZED

,

COMPONENT_SHOWN

- Fields declared in class java.awt.

AWTEvent

ACTION_EVENT_MASK

,

ADJUSTMENT_EVENT_MASK

,

COMPONENT_EVENT_MASK

,

consumed

,

CONTAINER_EVENT_MASK

,

FOCUS_EVENT_MASK

,

HIERARCHY_BOUNDS_EVENT_MASK

,

HIERARCHY_EVENT_MASK

,

id

,

INPUT_METHOD_EVENT_MASK

,

INVOCATION_EVENT_MASK

,

ITEM_EVENT_MASK

,

KEY_EVENT_MASK

,

MOUSE_EVENT_MASK

,

MOUSE_MOTION_EVENT_MASK

,

MOUSE_WHEEL_EVENT_MASK

,

PAINT_EVENT_MASK

,

RESERVED_ID_MAX

,

TEXT_EVENT_MASK

,

WINDOW_EVENT_MASK

,

WINDOW_FOCUS_EVENT_MASK

,

WINDOW_STATE_EVENT_MASK

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

Constant representing scrolling by a "block" (like scrolling
with page-up, page-down keys)

Constant representing scrolling by "units" (like scrolling with the
arrow keys)

Fields declared in class java.awt.event.

MouseEvent

BUTTON1

,

BUTTON2

,

BUTTON3

,

MOUSE_CLICKED

,

MOUSE_DRAGGED

,

MOUSE_ENTERED

,

MOUSE_EXITED

,

MOUSE_FIRST

,

MOUSE_LAST

,

MOUSE_MOVED

,

MOUSE_PRESSED

,

MOUSE_RELEASED

,

MOUSE_WHEEL

,

NOBUTTON

---

#### Fields declared in class java.awt.event. MouseEvent

Fields declared in class java.awt.event.

InputEvent

ALT_DOWN_MASK

,

ALT_GRAPH_DOWN_MASK

,

ALT_GRAPH_MASK

,

ALT_MASK

,

BUTTON1_DOWN_MASK

,

BUTTON1_MASK

,

BUTTON2_DOWN_MASK

,

BUTTON2_MASK

,

BUTTON3_DOWN_MASK

,

BUTTON3_MASK

,

CTRL_DOWN_MASK

,

CTRL_MASK

,

META_DOWN_MASK

,

META_MASK

,

SHIFT_DOWN_MASK

,

SHIFT_MASK

---

#### Fields declared in class java.awt.event. InputEvent

Fields declared in class java.awt.event.

ComponentEvent

COMPONENT_FIRST

,

COMPONENT_HIDDEN

,

COMPONENT_LAST

,

COMPONENT_MOVED

,

COMPONENT_RESIZED

,

COMPONENT_SHOWN

---

#### Fields declared in class java.awt.event. ComponentEvent

Fields declared in class java.awt.

AWTEvent

ACTION_EVENT_MASK

,

ADJUSTMENT_EVENT_MASK

,

COMPONENT_EVENT_MASK

,

consumed

,

CONTAINER_EVENT_MASK

,

FOCUS_EVENT_MASK

,

HIERARCHY_BOUNDS_EVENT_MASK

,

HIERARCHY_EVENT_MASK

,

id

,

INPUT_METHOD_EVENT_MASK

,

INVOCATION_EVENT_MASK

,

ITEM_EVENT_MASK

,

KEY_EVENT_MASK

,

MOUSE_EVENT_MASK

,

MOUSE_MOTION_EVENT_MASK

,

MOUSE_WHEEL_EVENT_MASK

,

PAINT_EVENT_MASK

,

RESERVED_ID_MAX

,

TEXT_EVENT_MASK

,

WINDOW_EVENT_MASK

,

WINDOW_FOCUS_EVENT_MASK

,

WINDOW_STATE_EVENT_MASK

---

#### Fields declared in class java.awt. AWTEvent

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

MouseWheelEvent

​(

Component

source,
int id,
long when,
int modifiers,
int x,
int y,
int clickCount,
boolean popupTrigger,
int scrollType,
int scrollAmount,
int wheelRotation)

Constructs a

MouseWheelEvent

object with the
specified source component, type, modifiers, coordinates,
scroll type, scroll amount, and wheel rotation.

MouseWheelEvent

​(

Component

source,
int id,
long when,
int modifiers,
int x,
int y,
int xAbs,
int yAbs,
int clickCount,
boolean popupTrigger,
int scrollType,
int scrollAmount,
int wheelRotation)

Constructs a

MouseWheelEvent

object with the
specified source component, type, modifiers, coordinates,
absolute coordinates, scroll type, scroll amount, and wheel rotation.

MouseWheelEvent

​(

Component

source,
int id,
long when,
int modifiers,
int x,
int y,
int xAbs,
int yAbs,
int clickCount,
boolean popupTrigger,
int scrollType,
int scrollAmount,
int wheelRotation,
double preciseWheelRotation)

Constructs a

MouseWheelEvent

object with the specified
source component, type, modifiers, coordinates, absolute coordinates,
scroll type, scroll amount, and wheel rotation.

---

#### Constructor Summary

Constructs a

MouseWheelEvent

object with the
specified source component, type, modifiers, coordinates,
scroll type, scroll amount, and wheel rotation.

Constructs a

MouseWheelEvent

object with the
specified source component, type, modifiers, coordinates,
absolute coordinates, scroll type, scroll amount, and wheel rotation.

Constructs a

MouseWheelEvent

object with the specified
source component, type, modifiers, coordinates, absolute coordinates,
scroll type, scroll amount, and wheel rotation.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

double

getPreciseWheelRotation

()

Returns the number of "clicks" the mouse wheel was rotated, as a double.

int

getScrollAmount

()

Returns the number of units that should be scrolled per
click of mouse wheel rotation.

int

getScrollType

()

Returns the type of scrolling that should take place in response to this
event.

int

getUnitsToScroll

()

This is a convenience method to aid in the implementation of
the common-case MouseWheelListener - to scroll a ScrollPane or
JScrollPane by an amount which conforms to the platform settings.

int

getWheelRotation

()

Returns the number of "clicks" the mouse wheel was rotated, as an integer.

String

paramString

()

Returns a parameter string identifying this event.

- Methods declared in class java.awt.event.

MouseEvent

getButton

,

getClickCount

,

getLocationOnScreen

,

getMouseModifiersText

,

getPoint

,

getX

,

getXOnScreen

,

getY

,

getYOnScreen

,

isPopupTrigger

,

translatePoint

- Methods declared in class java.awt.event.

InputEvent

consume

,

getMaskForButton

,

getModifiers

,

getModifiersEx

,

getModifiersExText

,

getWhen

,

isAltDown

,

isAltGraphDown

,

isConsumed

,

isControlDown

,

isMetaDown

,

isShiftDown

- Methods declared in class java.awt.event.

ComponentEvent

getComponent

- Methods declared in class java.awt.

AWTEvent

getID

,

setSource

,

toString

- Methods declared in class java.util.

EventObject

getSource

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

Returns the number of "clicks" the mouse wheel was rotated, as a double.

Returns the number of units that should be scrolled per
click of mouse wheel rotation.

Returns the type of scrolling that should take place in response to this
event.

This is a convenience method to aid in the implementation of
the common-case MouseWheelListener - to scroll a ScrollPane or
JScrollPane by an amount which conforms to the platform settings.

Returns the number of "clicks" the mouse wheel was rotated, as an integer.

Returns a parameter string identifying this event.

Methods declared in class java.awt.event.

MouseEvent

getButton

,

getClickCount

,

getLocationOnScreen

,

getMouseModifiersText

,

getPoint

,

getX

,

getXOnScreen

,

getY

,

getYOnScreen

,

isPopupTrigger

,

translatePoint

---

#### Methods declared in class java.awt.event. MouseEvent

Methods declared in class java.awt.event.

InputEvent

consume

,

getMaskForButton

,

getModifiers

,

getModifiersEx

,

getModifiersExText

,

getWhen

,

isAltDown

,

isAltGraphDown

,

isConsumed

,

isControlDown

,

isMetaDown

,

isShiftDown

---

#### Methods declared in class java.awt.event. InputEvent

Methods declared in class java.awt.event.

ComponentEvent

getComponent

---

#### Methods declared in class java.awt.event. ComponentEvent

Methods declared in class java.awt.

AWTEvent

getID

,

setSource

,

toString

---

#### Methods declared in class java.awt. AWTEvent

Methods declared in class java.util.

EventObject

getSource

---

#### Methods declared in class java.util. EventObject

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

- WHEEL_UNIT_SCROLL

```java
@Native

public static final int WHEEL_UNIT_SCROLL
```

Constant representing scrolling by "units" (like scrolling with the
arrow keys)

**See Also:** getScrollType()

,

Constant Field Values

- WHEEL_BLOCK_SCROLL

```java
@Native

public static final int WHEEL_BLOCK_SCROLL
```

Constant representing scrolling by a "block" (like scrolling
with page-up, page-down keys)

**See Also:** getScrollType()

,

Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MouseWheelEvent

```java
public MouseWheelEvent​(
Component
source,
int id,
long when,
int modifiers,
int x,
int y,
int clickCount,
boolean popupTrigger,
int scrollType,
int scrollAmount,
int wheelRotation)
```

Constructs a

MouseWheelEvent

object with the
specified source component, type, modifiers, coordinates,
scroll type, scroll amount, and wheel rotation.

Absolute coordinates xAbs and yAbs are set to source's location on screen plus
relative coordinates x and y. xAbs and yAbs are set to zero if the source is not showing.

Note that passing in an invalid

id

results in
unspecified behavior. This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- the

Component

that originated
the event
**Parameters:** id

- the integer that identifies the event
**Parameters:** when

- a long that gives the time the event occurred
**Parameters:** modifiers

- the modifier keys down during event
(shift, ctrl, alt, meta)
**Parameters:** x

- the horizontal x coordinate for the mouse location
**Parameters:** y

- the vertical y coordinate for the mouse location
**Parameters:** clickCount

- the number of mouse clicks associated with event
**Parameters:** popupTrigger

- a boolean, true if this event is a trigger for a
popup-menu
**Parameters:** scrollType

- the type of scrolling which should take place in
response to this event; valid values are

WHEEL_UNIT_SCROLL

and

WHEEL_BLOCK_SCROLL
**Parameters:** scrollAmount

- for scrollType

WHEEL_UNIT_SCROLL

,
the number of units to be scrolled
**Parameters:** wheelRotation

- the integer number of "clicks" by which the mouse
wheel was rotated
**Throws:** IllegalArgumentException

- if

source

is null
**See Also:** MouseEvent(java.awt.Component, int, long, int, int, int, int, boolean)

,

MouseEvent(java.awt.Component, int, long, int, int, int, int, int, int, boolean, int)

- MouseWheelEvent

```java
public MouseWheelEvent​(
Component
source,
int id,
long when,
int modifiers,
int x,
int y,
int xAbs,
int yAbs,
int clickCount,
boolean popupTrigger,
int scrollType,
int scrollAmount,
int wheelRotation)
```

Constructs a

MouseWheelEvent

object with the
specified source component, type, modifiers, coordinates,
absolute coordinates, scroll type, scroll amount, and wheel rotation.

Note that passing in an invalid

id

results in
unspecified behavior. This method throws an

IllegalArgumentException

if

source

is

null

.

Even if inconsistent values for relative and absolute coordinates are
passed to the constructor, the MouseWheelEvent instance is still
created and no exception is thrown.

**Parameters:** source

- the

Component

that originated
the event
**Parameters:** id

- the integer that identifies the event
**Parameters:** when

- a long that gives the time the event occurred
**Parameters:** modifiers

- the modifier keys down during event
(shift, ctrl, alt, meta)
**Parameters:** x

- the horizontal x coordinate for the mouse location
**Parameters:** y

- the vertical y coordinate for the mouse location
**Parameters:** xAbs

- the absolute horizontal x coordinate for the mouse location
**Parameters:** yAbs

- the absolute vertical y coordinate for the mouse location
**Parameters:** clickCount

- the number of mouse clicks associated with event
**Parameters:** popupTrigger

- a boolean, true if this event is a trigger for a
popup-menu
**Parameters:** scrollType

- the type of scrolling which should take place in
response to this event; valid values are

WHEEL_UNIT_SCROLL

and

WHEEL_BLOCK_SCROLL
**Parameters:** scrollAmount

- for scrollType

WHEEL_UNIT_SCROLL

,
the number of units to be scrolled
**Parameters:** wheelRotation

- the integer number of "clicks" by which the mouse
wheel was rotated
**Throws:** IllegalArgumentException

- if

source

is null
**Since:** 1.6
**See Also:** MouseEvent(java.awt.Component, int, long, int, int, int, int, boolean)

,

MouseEvent(java.awt.Component, int, long, int, int, int, int, int, int, boolean, int)

- MouseWheelEvent

```java
public MouseWheelEvent​(
Component
source,
int id,
long when,
int modifiers,
int x,
int y,
int xAbs,
int yAbs,
int clickCount,
boolean popupTrigger,
int scrollType,
int scrollAmount,
int wheelRotation,
double preciseWheelRotation)
```

Constructs a

MouseWheelEvent

object with the specified
source component, type, modifiers, coordinates, absolute coordinates,
scroll type, scroll amount, and wheel rotation.

Note that passing in an invalid

id

parameter results
in unspecified behavior. This method throws an

IllegalArgumentException

if

source

equals

null

.

Even if inconsistent values for relative and absolute coordinates
are passed to the constructor, a

MouseWheelEvent

instance
is still created and no exception is thrown.

**Parameters:** source

- the

Component

that originated the event
**Parameters:** id

- the integer value that identifies the event
**Parameters:** when

- a long value that gives the time when the event occurred
**Parameters:** modifiers

- the modifier keys down during event
(shift, ctrl, alt, meta)
**Parameters:** x

- the horizontal

x

coordinate for the
mouse location
**Parameters:** y

- the vertical

y

coordinate for the
mouse location
**Parameters:** xAbs

- the absolute horizontal

x

coordinate for
the mouse location
**Parameters:** yAbs

- the absolute vertical

y

coordinate for
the mouse location
**Parameters:** clickCount

- the number of mouse clicks associated with the event
**Parameters:** popupTrigger

- a boolean value,

true

if this event is a trigger
for a popup-menu
**Parameters:** scrollType

- the type of scrolling which should take place in
response to this event; valid values are

WHEEL_UNIT_SCROLL

and

WHEEL_BLOCK_SCROLL
**Parameters:** scrollAmount

- for scrollType

WHEEL_UNIT_SCROLL

,
the number of units to be scrolled
**Parameters:** wheelRotation

- the integer number of "clicks" by which the mouse wheel
was rotated
**Parameters:** preciseWheelRotation

- the double number of "clicks" by which the mouse wheel
was rotated
**Throws:** IllegalArgumentException

- if

source

is null
**Since:** 1.7
**See Also:** MouseEvent(java.awt.Component, int, long, int, int, int, int, boolean)

,

MouseEvent(java.awt.Component, int, long, int, int, int, int, int, int, boolean, int)

============ METHOD DETAIL ==========

- Method Detail

- getScrollType

```java
public int getScrollType()
```

Returns the type of scrolling that should take place in response to this
event. This is determined by the native platform. Legal values are:

- MouseWheelEvent.WHEEL_UNIT_SCROLL

MouseWheelEvent.WHEEL_BLOCK_SCROLL

**Returns:** either MouseWheelEvent.WHEEL_UNIT_SCROLL or
MouseWheelEvent.WHEEL_BLOCK_SCROLL, depending on the configuration of
the native platform.
**See Also:** Adjustable.getUnitIncrement()

,

Adjustable.getBlockIncrement()

,

Scrollable.getScrollableUnitIncrement(java.awt.Rectangle, int, int)

,

Scrollable.getScrollableBlockIncrement(java.awt.Rectangle, int, int)

- getScrollAmount

```java
public int getScrollAmount()
```

Returns the number of units that should be scrolled per
click of mouse wheel rotation.
Only valid if

getScrollType

returns

MouseWheelEvent.WHEEL_UNIT_SCROLL

**Returns:** number of units to scroll, or an undefined value if

getScrollType

returns

MouseWheelEvent.WHEEL_BLOCK_SCROLL
**See Also:** getScrollType()

- getWheelRotation

```java
public int getWheelRotation()
```

Returns the number of "clicks" the mouse wheel was rotated, as an integer.
A partial rotation may occur if the mouse supports a high-resolution wheel.
In this case, the method returns zero until a full "click" has been accumulated.

**Returns:** negative values if the mouse wheel was rotated up/away from
the user, and positive values if the mouse wheel was rotated down/
towards the user
**See Also:** getPreciseWheelRotation()

- getPreciseWheelRotation

```java
public double getPreciseWheelRotation()
```

Returns the number of "clicks" the mouse wheel was rotated, as a double.
A partial rotation may occur if the mouse supports a high-resolution wheel.
In this case, the return value will include a fractional "click".

**Returns:** negative values if the mouse wheel was rotated up or away from
the user, and positive values if the mouse wheel was rotated down or
towards the user
**Since:** 1.7
**See Also:** getWheelRotation()

- getUnitsToScroll

```java
public int getUnitsToScroll()
```

This is a convenience method to aid in the implementation of
the common-case MouseWheelListener - to scroll a ScrollPane or
JScrollPane by an amount which conforms to the platform settings.
(Note, however, that

ScrollPane

and

JScrollPane

already have this functionality built in.)

This method returns the number of units to scroll when scroll type is
MouseWheelEvent.WHEEL_UNIT_SCROLL, and should only be called if

getScrollType

returns MouseWheelEvent.WHEEL_UNIT_SCROLL.

Direction of scroll, amount of wheel movement,
and platform settings for wheel scrolling are all accounted for.
This method does not and cannot take into account value of the
Adjustable/Scrollable unit increment, as this will vary among
scrolling components.

A simplified example of how this method might be used in a
listener:

```java
mouseWheelMoved(MouseWheelEvent event) {
ScrollPane sp = getScrollPaneFromSomewhere();
Adjustable adj = sp.getVAdjustable()
if (MouseWheelEvent.getScrollType() == WHEEL_UNIT_SCROLL) {
int totalScrollAmount =
event.getUnitsToScroll() *
adj.getUnitIncrement();
adj.setValue(adj.getValue() + totalScrollAmount);
}
}
```

**Returns:** the number of units to scroll based on the direction and amount
of mouse wheel rotation, and on the wheel scrolling settings of the
native platform
**See Also:** getScrollType()

,

getScrollAmount()

,

MouseWheelListener

,

Adjustable

,

Adjustable.getUnitIncrement()

,

Scrollable

,

Scrollable.getScrollableUnitIncrement(java.awt.Rectangle, int, int)

,

ScrollPane

,

ScrollPane.setWheelScrollingEnabled(boolean)

,

JScrollPane

,

JScrollPane.setWheelScrollingEnabled(boolean)

- paramString

```java
public
String
paramString()
```

Returns a parameter string identifying this event.
This method is useful for event-logging and for debugging.

**Overrides:** paramString

in class

MouseEvent
**Returns:** a string identifying the event and its attributes

Field Detail

- WHEEL_UNIT_SCROLL

```java
@Native

public static final int WHEEL_UNIT_SCROLL
```

Constant representing scrolling by "units" (like scrolling with the
arrow keys)

**See Also:** getScrollType()

,

Constant Field Values

- WHEEL_BLOCK_SCROLL

```java
@Native

public static final int WHEEL_BLOCK_SCROLL
```

Constant representing scrolling by a "block" (like scrolling
with page-up, page-down keys)

**See Also:** getScrollType()

,

Constant Field Values

---

#### Field Detail

WHEEL_UNIT_SCROLL

```java
@Native

public static final int WHEEL_UNIT_SCROLL
```

Constant representing scrolling by "units" (like scrolling with the
arrow keys)

**See Also:** getScrollType()

,

Constant Field Values

---

#### WHEEL_UNIT_SCROLL

@Native

public static final int WHEEL_UNIT_SCROLL

Constant representing scrolling by "units" (like scrolling with the
arrow keys)

WHEEL_BLOCK_SCROLL

```java
@Native

public static final int WHEEL_BLOCK_SCROLL
```

Constant representing scrolling by a "block" (like scrolling
with page-up, page-down keys)

**See Also:** getScrollType()

,

Constant Field Values

---

#### WHEEL_BLOCK_SCROLL

@Native

public static final int WHEEL_BLOCK_SCROLL

Constant representing scrolling by a "block" (like scrolling
with page-up, page-down keys)

Constructor Detail

- MouseWheelEvent

```java
public MouseWheelEvent​(
Component
source,
int id,
long when,
int modifiers,
int x,
int y,
int clickCount,
boolean popupTrigger,
int scrollType,
int scrollAmount,
int wheelRotation)
```

Constructs a

MouseWheelEvent

object with the
specified source component, type, modifiers, coordinates,
scroll type, scroll amount, and wheel rotation.

Absolute coordinates xAbs and yAbs are set to source's location on screen plus
relative coordinates x and y. xAbs and yAbs are set to zero if the source is not showing.

Note that passing in an invalid

id

results in
unspecified behavior. This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- the

Component

that originated
the event
**Parameters:** id

- the integer that identifies the event
**Parameters:** when

- a long that gives the time the event occurred
**Parameters:** modifiers

- the modifier keys down during event
(shift, ctrl, alt, meta)
**Parameters:** x

- the horizontal x coordinate for the mouse location
**Parameters:** y

- the vertical y coordinate for the mouse location
**Parameters:** clickCount

- the number of mouse clicks associated with event
**Parameters:** popupTrigger

- a boolean, true if this event is a trigger for a
popup-menu
**Parameters:** scrollType

- the type of scrolling which should take place in
response to this event; valid values are

WHEEL_UNIT_SCROLL

and

WHEEL_BLOCK_SCROLL
**Parameters:** scrollAmount

- for scrollType

WHEEL_UNIT_SCROLL

,
the number of units to be scrolled
**Parameters:** wheelRotation

- the integer number of "clicks" by which the mouse
wheel was rotated
**Throws:** IllegalArgumentException

- if

source

is null
**See Also:** MouseEvent(java.awt.Component, int, long, int, int, int, int, boolean)

,

MouseEvent(java.awt.Component, int, long, int, int, int, int, int, int, boolean, int)

- MouseWheelEvent

```java
public MouseWheelEvent​(
Component
source,
int id,
long when,
int modifiers,
int x,
int y,
int xAbs,
int yAbs,
int clickCount,
boolean popupTrigger,
int scrollType,
int scrollAmount,
int wheelRotation)
```

Constructs a

MouseWheelEvent

object with the
specified source component, type, modifiers, coordinates,
absolute coordinates, scroll type, scroll amount, and wheel rotation.

Note that passing in an invalid

id

results in
unspecified behavior. This method throws an

IllegalArgumentException

if

source

is

null

.

Even if inconsistent values for relative and absolute coordinates are
passed to the constructor, the MouseWheelEvent instance is still
created and no exception is thrown.

**Parameters:** source

- the

Component

that originated
the event
**Parameters:** id

- the integer that identifies the event
**Parameters:** when

- a long that gives the time the event occurred
**Parameters:** modifiers

- the modifier keys down during event
(shift, ctrl, alt, meta)
**Parameters:** x

- the horizontal x coordinate for the mouse location
**Parameters:** y

- the vertical y coordinate for the mouse location
**Parameters:** xAbs

- the absolute horizontal x coordinate for the mouse location
**Parameters:** yAbs

- the absolute vertical y coordinate for the mouse location
**Parameters:** clickCount

- the number of mouse clicks associated with event
**Parameters:** popupTrigger

- a boolean, true if this event is a trigger for a
popup-menu
**Parameters:** scrollType

- the type of scrolling which should take place in
response to this event; valid values are

WHEEL_UNIT_SCROLL

and

WHEEL_BLOCK_SCROLL
**Parameters:** scrollAmount

- for scrollType

WHEEL_UNIT_SCROLL

,
the number of units to be scrolled
**Parameters:** wheelRotation

- the integer number of "clicks" by which the mouse
wheel was rotated
**Throws:** IllegalArgumentException

- if

source

is null
**Since:** 1.6
**See Also:** MouseEvent(java.awt.Component, int, long, int, int, int, int, boolean)

,

MouseEvent(java.awt.Component, int, long, int, int, int, int, int, int, boolean, int)

- MouseWheelEvent

```java
public MouseWheelEvent​(
Component
source,
int id,
long when,
int modifiers,
int x,
int y,
int xAbs,
int yAbs,
int clickCount,
boolean popupTrigger,
int scrollType,
int scrollAmount,
int wheelRotation,
double preciseWheelRotation)
```

Constructs a

MouseWheelEvent

object with the specified
source component, type, modifiers, coordinates, absolute coordinates,
scroll type, scroll amount, and wheel rotation.

Note that passing in an invalid

id

parameter results
in unspecified behavior. This method throws an

IllegalArgumentException

if

source

equals

null

.

Even if inconsistent values for relative and absolute coordinates
are passed to the constructor, a

MouseWheelEvent

instance
is still created and no exception is thrown.

**Parameters:** source

- the

Component

that originated the event
**Parameters:** id

- the integer value that identifies the event
**Parameters:** when

- a long value that gives the time when the event occurred
**Parameters:** modifiers

- the modifier keys down during event
(shift, ctrl, alt, meta)
**Parameters:** x

- the horizontal

x

coordinate for the
mouse location
**Parameters:** y

- the vertical

y

coordinate for the
mouse location
**Parameters:** xAbs

- the absolute horizontal

x

coordinate for
the mouse location
**Parameters:** yAbs

- the absolute vertical

y

coordinate for
the mouse location
**Parameters:** clickCount

- the number of mouse clicks associated with the event
**Parameters:** popupTrigger

- a boolean value,

true

if this event is a trigger
for a popup-menu
**Parameters:** scrollType

- the type of scrolling which should take place in
response to this event; valid values are

WHEEL_UNIT_SCROLL

and

WHEEL_BLOCK_SCROLL
**Parameters:** scrollAmount

- for scrollType

WHEEL_UNIT_SCROLL

,
the number of units to be scrolled
**Parameters:** wheelRotation

- the integer number of "clicks" by which the mouse wheel
was rotated
**Parameters:** preciseWheelRotation

- the double number of "clicks" by which the mouse wheel
was rotated
**Throws:** IllegalArgumentException

- if

source

is null
**Since:** 1.7
**See Also:** MouseEvent(java.awt.Component, int, long, int, int, int, int, boolean)

,

MouseEvent(java.awt.Component, int, long, int, int, int, int, int, int, boolean, int)

---

#### Constructor Detail

MouseWheelEvent

```java
public MouseWheelEvent​(
Component
source,
int id,
long when,
int modifiers,
int x,
int y,
int clickCount,
boolean popupTrigger,
int scrollType,
int scrollAmount,
int wheelRotation)
```

Constructs a

MouseWheelEvent

object with the
specified source component, type, modifiers, coordinates,
scroll type, scroll amount, and wheel rotation.

Absolute coordinates xAbs and yAbs are set to source's location on screen plus
relative coordinates x and y. xAbs and yAbs are set to zero if the source is not showing.

Note that passing in an invalid

id

results in
unspecified behavior. This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- the

Component

that originated
the event
**Parameters:** id

- the integer that identifies the event
**Parameters:** when

- a long that gives the time the event occurred
**Parameters:** modifiers

- the modifier keys down during event
(shift, ctrl, alt, meta)
**Parameters:** x

- the horizontal x coordinate for the mouse location
**Parameters:** y

- the vertical y coordinate for the mouse location
**Parameters:** clickCount

- the number of mouse clicks associated with event
**Parameters:** popupTrigger

- a boolean, true if this event is a trigger for a
popup-menu
**Parameters:** scrollType

- the type of scrolling which should take place in
response to this event; valid values are

WHEEL_UNIT_SCROLL

and

WHEEL_BLOCK_SCROLL
**Parameters:** scrollAmount

- for scrollType

WHEEL_UNIT_SCROLL

,
the number of units to be scrolled
**Parameters:** wheelRotation

- the integer number of "clicks" by which the mouse
wheel was rotated
**Throws:** IllegalArgumentException

- if

source

is null
**See Also:** MouseEvent(java.awt.Component, int, long, int, int, int, int, boolean)

,

MouseEvent(java.awt.Component, int, long, int, int, int, int, int, int, boolean, int)

---

#### MouseWheelEvent

public MouseWheelEvent​(

Component

source,
int id,
long when,
int modifiers,
int x,
int y,
int clickCount,
boolean popupTrigger,
int scrollType,
int scrollAmount,
int wheelRotation)

Constructs a

MouseWheelEvent

object with the
specified source component, type, modifiers, coordinates,
scroll type, scroll amount, and wheel rotation.

Absolute coordinates xAbs and yAbs are set to source's location on screen plus
relative coordinates x and y. xAbs and yAbs are set to zero if the source is not showing.

Note that passing in an invalid

id

results in
unspecified behavior. This method throws an

IllegalArgumentException

if

source

is

null

.

Absolute coordinates xAbs and yAbs are set to source's location on screen plus
relative coordinates x and y. xAbs and yAbs are set to zero if the source is not showing.

Note that passing in an invalid

id

results in
unspecified behavior. This method throws an

IllegalArgumentException

if

source

is

null

.

Note that passing in an invalid

id

results in
unspecified behavior. This method throws an

IllegalArgumentException

if

source

is

null

.

MouseWheelEvent

```java
public MouseWheelEvent​(
Component
source,
int id,
long when,
int modifiers,
int x,
int y,
int xAbs,
int yAbs,
int clickCount,
boolean popupTrigger,
int scrollType,
int scrollAmount,
int wheelRotation)
```

Constructs a

MouseWheelEvent

object with the
specified source component, type, modifiers, coordinates,
absolute coordinates, scroll type, scroll amount, and wheel rotation.

Note that passing in an invalid

id

results in
unspecified behavior. This method throws an

IllegalArgumentException

if

source

is

null

.

Even if inconsistent values for relative and absolute coordinates are
passed to the constructor, the MouseWheelEvent instance is still
created and no exception is thrown.

**Parameters:** source

- the

Component

that originated
the event
**Parameters:** id

- the integer that identifies the event
**Parameters:** when

- a long that gives the time the event occurred
**Parameters:** modifiers

- the modifier keys down during event
(shift, ctrl, alt, meta)
**Parameters:** x

- the horizontal x coordinate for the mouse location
**Parameters:** y

- the vertical y coordinate for the mouse location
**Parameters:** xAbs

- the absolute horizontal x coordinate for the mouse location
**Parameters:** yAbs

- the absolute vertical y coordinate for the mouse location
**Parameters:** clickCount

- the number of mouse clicks associated with event
**Parameters:** popupTrigger

- a boolean, true if this event is a trigger for a
popup-menu
**Parameters:** scrollType

- the type of scrolling which should take place in
response to this event; valid values are

WHEEL_UNIT_SCROLL

and

WHEEL_BLOCK_SCROLL
**Parameters:** scrollAmount

- for scrollType

WHEEL_UNIT_SCROLL

,
the number of units to be scrolled
**Parameters:** wheelRotation

- the integer number of "clicks" by which the mouse
wheel was rotated
**Throws:** IllegalArgumentException

- if

source

is null
**Since:** 1.6
**See Also:** MouseEvent(java.awt.Component, int, long, int, int, int, int, boolean)

,

MouseEvent(java.awt.Component, int, long, int, int, int, int, int, int, boolean, int)

---

#### MouseWheelEvent

public MouseWheelEvent​(

Component

source,
int id,
long when,
int modifiers,
int x,
int y,
int xAbs,
int yAbs,
int clickCount,
boolean popupTrigger,
int scrollType,
int scrollAmount,
int wheelRotation)

Constructs a

MouseWheelEvent

object with the
specified source component, type, modifiers, coordinates,
absolute coordinates, scroll type, scroll amount, and wheel rotation.

Note that passing in an invalid

id

results in
unspecified behavior. This method throws an

IllegalArgumentException

if

source

is

null

.

Even if inconsistent values for relative and absolute coordinates are
passed to the constructor, the MouseWheelEvent instance is still
created and no exception is thrown.

Note that passing in an invalid

id

results in
unspecified behavior. This method throws an

IllegalArgumentException

if

source

is

null

.

Even if inconsistent values for relative and absolute coordinates are
passed to the constructor, the MouseWheelEvent instance is still
created and no exception is thrown.

Even if inconsistent values for relative and absolute coordinates are
passed to the constructor, the MouseWheelEvent instance is still
created and no exception is thrown.

MouseWheelEvent

```java
public MouseWheelEvent​(
Component
source,
int id,
long when,
int modifiers,
int x,
int y,
int xAbs,
int yAbs,
int clickCount,
boolean popupTrigger,
int scrollType,
int scrollAmount,
int wheelRotation,
double preciseWheelRotation)
```

Constructs a

MouseWheelEvent

object with the specified
source component, type, modifiers, coordinates, absolute coordinates,
scroll type, scroll amount, and wheel rotation.

Note that passing in an invalid

id

parameter results
in unspecified behavior. This method throws an

IllegalArgumentException

if

source

equals

null

.

Even if inconsistent values for relative and absolute coordinates
are passed to the constructor, a

MouseWheelEvent

instance
is still created and no exception is thrown.

**Parameters:** source

- the

Component

that originated the event
**Parameters:** id

- the integer value that identifies the event
**Parameters:** when

- a long value that gives the time when the event occurred
**Parameters:** modifiers

- the modifier keys down during event
(shift, ctrl, alt, meta)
**Parameters:** x

- the horizontal

x

coordinate for the
mouse location
**Parameters:** y

- the vertical

y

coordinate for the
mouse location
**Parameters:** xAbs

- the absolute horizontal

x

coordinate for
the mouse location
**Parameters:** yAbs

- the absolute vertical

y

coordinate for
the mouse location
**Parameters:** clickCount

- the number of mouse clicks associated with the event
**Parameters:** popupTrigger

- a boolean value,

true

if this event is a trigger
for a popup-menu
**Parameters:** scrollType

- the type of scrolling which should take place in
response to this event; valid values are

WHEEL_UNIT_SCROLL

and

WHEEL_BLOCK_SCROLL
**Parameters:** scrollAmount

- for scrollType

WHEEL_UNIT_SCROLL

,
the number of units to be scrolled
**Parameters:** wheelRotation

- the integer number of "clicks" by which the mouse wheel
was rotated
**Parameters:** preciseWheelRotation

- the double number of "clicks" by which the mouse wheel
was rotated
**Throws:** IllegalArgumentException

- if

source

is null
**Since:** 1.7
**See Also:** MouseEvent(java.awt.Component, int, long, int, int, int, int, boolean)

,

MouseEvent(java.awt.Component, int, long, int, int, int, int, int, int, boolean, int)

---

#### MouseWheelEvent

public MouseWheelEvent​(

Component

source,
int id,
long when,
int modifiers,
int x,
int y,
int xAbs,
int yAbs,
int clickCount,
boolean popupTrigger,
int scrollType,
int scrollAmount,
int wheelRotation,
double preciseWheelRotation)

Constructs a

MouseWheelEvent

object with the specified
source component, type, modifiers, coordinates, absolute coordinates,
scroll type, scroll amount, and wheel rotation.

Note that passing in an invalid

id

parameter results
in unspecified behavior. This method throws an

IllegalArgumentException

if

source

equals

null

.

Even if inconsistent values for relative and absolute coordinates
are passed to the constructor, a

MouseWheelEvent

instance
is still created and no exception is thrown.

Note that passing in an invalid

id

parameter results
in unspecified behavior. This method throws an

IllegalArgumentException

if

source

equals

null

.

Even if inconsistent values for relative and absolute coordinates
are passed to the constructor, a

MouseWheelEvent

instance
is still created and no exception is thrown.

Even if inconsistent values for relative and absolute coordinates
are passed to the constructor, a

MouseWheelEvent

instance
is still created and no exception is thrown.

Method Detail

- getScrollType

```java
public int getScrollType()
```

Returns the type of scrolling that should take place in response to this
event. This is determined by the native platform. Legal values are:

- MouseWheelEvent.WHEEL_UNIT_SCROLL

MouseWheelEvent.WHEEL_BLOCK_SCROLL

**Returns:** either MouseWheelEvent.WHEEL_UNIT_SCROLL or
MouseWheelEvent.WHEEL_BLOCK_SCROLL, depending on the configuration of
the native platform.
**See Also:** Adjustable.getUnitIncrement()

,

Adjustable.getBlockIncrement()

,

Scrollable.getScrollableUnitIncrement(java.awt.Rectangle, int, int)

,

Scrollable.getScrollableBlockIncrement(java.awt.Rectangle, int, int)

- getScrollAmount

```java
public int getScrollAmount()
```

Returns the number of units that should be scrolled per
click of mouse wheel rotation.
Only valid if

getScrollType

returns

MouseWheelEvent.WHEEL_UNIT_SCROLL

**Returns:** number of units to scroll, or an undefined value if

getScrollType

returns

MouseWheelEvent.WHEEL_BLOCK_SCROLL
**See Also:** getScrollType()

- getWheelRotation

```java
public int getWheelRotation()
```

Returns the number of "clicks" the mouse wheel was rotated, as an integer.
A partial rotation may occur if the mouse supports a high-resolution wheel.
In this case, the method returns zero until a full "click" has been accumulated.

**Returns:** negative values if the mouse wheel was rotated up/away from
the user, and positive values if the mouse wheel was rotated down/
towards the user
**See Also:** getPreciseWheelRotation()

- getPreciseWheelRotation

```java
public double getPreciseWheelRotation()
```

Returns the number of "clicks" the mouse wheel was rotated, as a double.
A partial rotation may occur if the mouse supports a high-resolution wheel.
In this case, the return value will include a fractional "click".

**Returns:** negative values if the mouse wheel was rotated up or away from
the user, and positive values if the mouse wheel was rotated down or
towards the user
**Since:** 1.7
**See Also:** getWheelRotation()

- getUnitsToScroll

```java
public int getUnitsToScroll()
```

This is a convenience method to aid in the implementation of
the common-case MouseWheelListener - to scroll a ScrollPane or
JScrollPane by an amount which conforms to the platform settings.
(Note, however, that

ScrollPane

and

JScrollPane

already have this functionality built in.)

This method returns the number of units to scroll when scroll type is
MouseWheelEvent.WHEEL_UNIT_SCROLL, and should only be called if

getScrollType

returns MouseWheelEvent.WHEEL_UNIT_SCROLL.

Direction of scroll, amount of wheel movement,
and platform settings for wheel scrolling are all accounted for.
This method does not and cannot take into account value of the
Adjustable/Scrollable unit increment, as this will vary among
scrolling components.

A simplified example of how this method might be used in a
listener:

```java
mouseWheelMoved(MouseWheelEvent event) {
ScrollPane sp = getScrollPaneFromSomewhere();
Adjustable adj = sp.getVAdjustable()
if (MouseWheelEvent.getScrollType() == WHEEL_UNIT_SCROLL) {
int totalScrollAmount =
event.getUnitsToScroll() *
adj.getUnitIncrement();
adj.setValue(adj.getValue() + totalScrollAmount);
}
}
```

**Returns:** the number of units to scroll based on the direction and amount
of mouse wheel rotation, and on the wheel scrolling settings of the
native platform
**See Also:** getScrollType()

,

getScrollAmount()

,

MouseWheelListener

,

Adjustable

,

Adjustable.getUnitIncrement()

,

Scrollable

,

Scrollable.getScrollableUnitIncrement(java.awt.Rectangle, int, int)

,

ScrollPane

,

ScrollPane.setWheelScrollingEnabled(boolean)

,

JScrollPane

,

JScrollPane.setWheelScrollingEnabled(boolean)

- paramString

```java
public
String
paramString()
```

Returns a parameter string identifying this event.
This method is useful for event-logging and for debugging.

**Overrides:** paramString

in class

MouseEvent
**Returns:** a string identifying the event and its attributes

---

#### Method Detail

getScrollType

```java
public int getScrollType()
```

Returns the type of scrolling that should take place in response to this
event. This is determined by the native platform. Legal values are:

- MouseWheelEvent.WHEEL_UNIT_SCROLL

MouseWheelEvent.WHEEL_BLOCK_SCROLL

**Returns:** either MouseWheelEvent.WHEEL_UNIT_SCROLL or
MouseWheelEvent.WHEEL_BLOCK_SCROLL, depending on the configuration of
the native platform.
**See Also:** Adjustable.getUnitIncrement()

,

Adjustable.getBlockIncrement()

,

Scrollable.getScrollableUnitIncrement(java.awt.Rectangle, int, int)

,

Scrollable.getScrollableBlockIncrement(java.awt.Rectangle, int, int)

---

#### getScrollType

public int getScrollType()

Returns the type of scrolling that should take place in response to this
event. This is determined by the native platform. Legal values are:

- MouseWheelEvent.WHEEL_UNIT_SCROLL

MouseWheelEvent.WHEEL_BLOCK_SCROLL

MouseWheelEvent.WHEEL_UNIT_SCROLL

MouseWheelEvent.WHEEL_BLOCK_SCROLL

getScrollAmount

```java
public int getScrollAmount()
```

Returns the number of units that should be scrolled per
click of mouse wheel rotation.
Only valid if

getScrollType

returns

MouseWheelEvent.WHEEL_UNIT_SCROLL

**Returns:** number of units to scroll, or an undefined value if

getScrollType

returns

MouseWheelEvent.WHEEL_BLOCK_SCROLL
**See Also:** getScrollType()

---

#### getScrollAmount

public int getScrollAmount()

Returns the number of units that should be scrolled per
click of mouse wheel rotation.
Only valid if

getScrollType

returns

MouseWheelEvent.WHEEL_UNIT_SCROLL

getWheelRotation

```java
public int getWheelRotation()
```

Returns the number of "clicks" the mouse wheel was rotated, as an integer.
A partial rotation may occur if the mouse supports a high-resolution wheel.
In this case, the method returns zero until a full "click" has been accumulated.

**Returns:** negative values if the mouse wheel was rotated up/away from
the user, and positive values if the mouse wheel was rotated down/
towards the user
**See Also:** getPreciseWheelRotation()

---

#### getWheelRotation

public int getWheelRotation()

Returns the number of "clicks" the mouse wheel was rotated, as an integer.
A partial rotation may occur if the mouse supports a high-resolution wheel.
In this case, the method returns zero until a full "click" has been accumulated.

getPreciseWheelRotation

```java
public double getPreciseWheelRotation()
```

Returns the number of "clicks" the mouse wheel was rotated, as a double.
A partial rotation may occur if the mouse supports a high-resolution wheel.
In this case, the return value will include a fractional "click".

**Returns:** negative values if the mouse wheel was rotated up or away from
the user, and positive values if the mouse wheel was rotated down or
towards the user
**Since:** 1.7
**See Also:** getWheelRotation()

---

#### getPreciseWheelRotation

public double getPreciseWheelRotation()

Returns the number of "clicks" the mouse wheel was rotated, as a double.
A partial rotation may occur if the mouse supports a high-resolution wheel.
In this case, the return value will include a fractional "click".

getUnitsToScroll

```java
public int getUnitsToScroll()
```

This is a convenience method to aid in the implementation of
the common-case MouseWheelListener - to scroll a ScrollPane or
JScrollPane by an amount which conforms to the platform settings.
(Note, however, that

ScrollPane

and

JScrollPane

already have this functionality built in.)

This method returns the number of units to scroll when scroll type is
MouseWheelEvent.WHEEL_UNIT_SCROLL, and should only be called if

getScrollType

returns MouseWheelEvent.WHEEL_UNIT_SCROLL.

Direction of scroll, amount of wheel movement,
and platform settings for wheel scrolling are all accounted for.
This method does not and cannot take into account value of the
Adjustable/Scrollable unit increment, as this will vary among
scrolling components.

A simplified example of how this method might be used in a
listener:

```java
mouseWheelMoved(MouseWheelEvent event) {
ScrollPane sp = getScrollPaneFromSomewhere();
Adjustable adj = sp.getVAdjustable()
if (MouseWheelEvent.getScrollType() == WHEEL_UNIT_SCROLL) {
int totalScrollAmount =
event.getUnitsToScroll() *
adj.getUnitIncrement();
adj.setValue(adj.getValue() + totalScrollAmount);
}
}
```

**Returns:** the number of units to scroll based on the direction and amount
of mouse wheel rotation, and on the wheel scrolling settings of the
native platform
**See Also:** getScrollType()

,

getScrollAmount()

,

MouseWheelListener

,

Adjustable

,

Adjustable.getUnitIncrement()

,

Scrollable

,

Scrollable.getScrollableUnitIncrement(java.awt.Rectangle, int, int)

,

ScrollPane

,

ScrollPane.setWheelScrollingEnabled(boolean)

,

JScrollPane

,

JScrollPane.setWheelScrollingEnabled(boolean)

---

#### getUnitsToScroll

public int getUnitsToScroll()

This is a convenience method to aid in the implementation of
the common-case MouseWheelListener - to scroll a ScrollPane or
JScrollPane by an amount which conforms to the platform settings.
(Note, however, that

ScrollPane

and

JScrollPane

already have this functionality built in.)

This method returns the number of units to scroll when scroll type is
MouseWheelEvent.WHEEL_UNIT_SCROLL, and should only be called if

getScrollType

returns MouseWheelEvent.WHEEL_UNIT_SCROLL.

Direction of scroll, amount of wheel movement,
and platform settings for wheel scrolling are all accounted for.
This method does not and cannot take into account value of the
Adjustable/Scrollable unit increment, as this will vary among
scrolling components.

A simplified example of how this method might be used in a
listener:

```java
mouseWheelMoved(MouseWheelEvent event) {
ScrollPane sp = getScrollPaneFromSomewhere();
Adjustable adj = sp.getVAdjustable()
if (MouseWheelEvent.getScrollType() == WHEEL_UNIT_SCROLL) {
int totalScrollAmount =
event.getUnitsToScroll() *
adj.getUnitIncrement();
adj.setValue(adj.getValue() + totalScrollAmount);
}
}
```

This method returns the number of units to scroll when scroll type is
MouseWheelEvent.WHEEL_UNIT_SCROLL, and should only be called if

getScrollType

returns MouseWheelEvent.WHEEL_UNIT_SCROLL.

Direction of scroll, amount of wheel movement,
and platform settings for wheel scrolling are all accounted for.
This method does not and cannot take into account value of the
Adjustable/Scrollable unit increment, as this will vary among
scrolling components.

A simplified example of how this method might be used in a
listener:

```java
mouseWheelMoved(MouseWheelEvent event) {
ScrollPane sp = getScrollPaneFromSomewhere();
Adjustable adj = sp.getVAdjustable()
if (MouseWheelEvent.getScrollType() == WHEEL_UNIT_SCROLL) {
int totalScrollAmount =
event.getUnitsToScroll() *
adj.getUnitIncrement();
adj.setValue(adj.getValue() + totalScrollAmount);
}
}
```

Direction of scroll, amount of wheel movement,
and platform settings for wheel scrolling are all accounted for.
This method does not and cannot take into account value of the
Adjustable/Scrollable unit increment, as this will vary among
scrolling components.

A simplified example of how this method might be used in a
listener:

```java
mouseWheelMoved(MouseWheelEvent event) {
ScrollPane sp = getScrollPaneFromSomewhere();
Adjustable adj = sp.getVAdjustable()
if (MouseWheelEvent.getScrollType() == WHEEL_UNIT_SCROLL) {
int totalScrollAmount =
event.getUnitsToScroll() *
adj.getUnitIncrement();
adj.setValue(adj.getValue() + totalScrollAmount);
}
}
```

A simplified example of how this method might be used in a
listener:

```java
mouseWheelMoved(MouseWheelEvent event) {
ScrollPane sp = getScrollPaneFromSomewhere();
Adjustable adj = sp.getVAdjustable()
if (MouseWheelEvent.getScrollType() == WHEEL_UNIT_SCROLL) {
int totalScrollAmount =
event.getUnitsToScroll() *
adj.getUnitIncrement();
adj.setValue(adj.getValue() + totalScrollAmount);
}
}
```

mouseWheelMoved(MouseWheelEvent event) {
ScrollPane sp = getScrollPaneFromSomewhere();
Adjustable adj = sp.getVAdjustable()
if (MouseWheelEvent.getScrollType() == WHEEL_UNIT_SCROLL) {
int totalScrollAmount =
event.getUnitsToScroll() *
adj.getUnitIncrement();
adj.setValue(adj.getValue() + totalScrollAmount);
}
}

paramString

```java
public
String
paramString()
```

Returns a parameter string identifying this event.
This method is useful for event-logging and for debugging.

**Overrides:** paramString

in class

MouseEvent
**Returns:** a string identifying the event and its attributes

---

#### paramString

public

String

paramString()

Returns a parameter string identifying this event.
This method is useful for event-logging and for debugging.

---

