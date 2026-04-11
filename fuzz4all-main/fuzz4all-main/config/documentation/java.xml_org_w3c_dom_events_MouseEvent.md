# Interface MouseEvent

**Source:** `java.xml\org\w3c\dom\events\MouseEvent.html`

### Class Description

```java
public interface
MouseEvent

extends
UIEvent
```

The

MouseEvent

interface provides specific contextual
information associated with Mouse events.

The

detail

attribute inherited from

UIEvent

indicates the number of times a mouse button has been pressed and
released over the same screen location during a user action. The
attribute value is 1 when the user begins this action and increments by 1
for each full sequence of pressing and releasing. If the user moves the
mouse between the mousedown and mouseup the value will be set to 0,
indicating that no click is occurring.

In the case of nested elements mouse events are always targeted at the
most deeply nested element. Ancestors of the targeted element may use
bubbling to obtain notification of mouse events which occur within its
descendent elements.

See also the

Document Object Model (DOM) Level 2 Events Specification

.

**All Superinterfaces:** Event

,

UIEvent

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getScreenX()

The horizontal coordinate at which the event occurred relative to the
origin of the screen coordinate system.

---

#### int getScreenY()

The vertical coordinate at which the event occurred relative to the
origin of the screen coordinate system.

---

#### int getClientX()

The horizontal coordinate at which the event occurred relative to the
DOM implementation's client area.

---

#### int getClientY()

The vertical coordinate at which the event occurred relative to the DOM
implementation's client area.

---

#### boolean getCtrlKey()

Used to indicate whether the 'ctrl' key was depressed during the firing
of the event.

---

#### boolean getShiftKey()

Used to indicate whether the 'shift' key was depressed during the
firing of the event.

---

#### boolean getAltKey()

Used to indicate whether the 'alt' key was depressed during the firing
of the event. On some platforms this key may map to an alternative
key name.

---

#### boolean getMetaKey()

Used to indicate whether the 'meta' key was depressed during the firing
of the event. On some platforms this key may map to an alternative
key name.

---

#### short getButton()

During mouse events caused by the depression or release of a mouse
button,

button

is used to indicate which mouse button
changed state. The values for

button

range from zero to
indicate the left button of the mouse, one to indicate the middle
button if present, and two to indicate the right button. For mice
configured for left handed use in which the button actions are
reversed the values are instead read from right to left.

---

#### EventTarget
getRelatedTarget()

Used to identify a secondary

EventTarget

related to a UI
event. Currently this attribute is used with the mouseover event to
indicate the

EventTarget

which the pointing device
exited and with the mouseout event to indicate the

EventTarget

which the pointing device entered.

---

#### void initMouseEvent​(
String
typeArg,
boolean canBubbleArg,
boolean cancelableArg,

AbstractView
viewArg,
int detailArg,
int screenXArg,
int screenYArg,
int clientXArg,
int clientYArg,
boolean ctrlKeyArg,
boolean altKeyArg,
boolean shiftKeyArg,
boolean metaKeyArg,
short buttonArg,

EventTarget
relatedTargetArg)

The

initMouseEvent

method is used to initialize the value
of a

MouseEvent

created through the

DocumentEvent

interface. This method may only be called
before the

MouseEvent

has been dispatched via the

dispatchEvent

method, though it may be called multiple
times during that phase if necessary. If called multiple times, the
final invocation takes precedence.

**Parameters:**
- typeArg

- Specifies the event type.
- canBubbleArg

- Specifies whether or not the event can bubble.
- cancelableArg

- Specifies whether or not the event's default
action can be prevented.
- viewArg

- Specifies the

Event

's

AbstractView

.
- detailArg

- Specifies the

Event

's mouse click count.
- screenXArg

- Specifies the

Event

's screen x
coordinate
- screenYArg

- Specifies the

Event

's screen y
coordinate
- clientXArg

- Specifies the

Event

's client x
coordinate
- clientYArg

- Specifies the

Event

's client y
coordinate
- ctrlKeyArg

- Specifies whether or not control key was depressed
during the

Event

.
- altKeyArg

- Specifies whether or not alt key was depressed during
the

Event

.
- shiftKeyArg

- Specifies whether or not shift key was depressed
during the

Event

.
- metaKeyArg

- Specifies whether or not meta key was depressed
during the

Event

.
- buttonArg

- Specifies the

Event

's mouse button.
- relatedTargetArg

- Specifies the

Event

's related

EventTarget

.

---

### Additional Sections

#### Interface MouseEvent

**All Superinterfaces:** Event

,

UIEvent

```java
public interface
MouseEvent

extends
UIEvent
```

The

MouseEvent

interface provides specific contextual
information associated with Mouse events.

The

detail

attribute inherited from

UIEvent

indicates the number of times a mouse button has been pressed and
released over the same screen location during a user action. The
attribute value is 1 when the user begins this action and increments by 1
for each full sequence of pressing and releasing. If the user moves the
mouse between the mousedown and mouseup the value will be set to 0,
indicating that no click is occurring.

In the case of nested elements mouse events are always targeted at the
most deeply nested element. Ancestors of the targeted element may use
bubbling to obtain notification of mouse events which occur within its
descendent elements.

See also the

Document Object Model (DOM) Level 2 Events Specification

.

**Since:** 1.5, DOM Level 2

public interface

MouseEvent

extends

UIEvent

The

MouseEvent

interface provides specific contextual
information associated with Mouse events.

The

detail

attribute inherited from

UIEvent

indicates the number of times a mouse button has been pressed and
released over the same screen location during a user action. The
attribute value is 1 when the user begins this action and increments by 1
for each full sequence of pressing and releasing. If the user moves the
mouse between the mousedown and mouseup the value will be set to 0,
indicating that no click is occurring.

In the case of nested elements mouse events are always targeted at the
most deeply nested element. Ancestors of the targeted element may use
bubbling to obtain notification of mouse events which occur within its
descendent elements.

See also the

Document Object Model (DOM) Level 2 Events Specification

.

The

detail

attribute inherited from

UIEvent

indicates the number of times a mouse button has been pressed and
released over the same screen location during a user action. The
attribute value is 1 when the user begins this action and increments by 1
for each full sequence of pressing and releasing. If the user moves the
mouse between the mousedown and mouseup the value will be set to 0,
indicating that no click is occurring.

In the case of nested elements mouse events are always targeted at the
most deeply nested element. Ancestors of the targeted element may use
bubbling to obtain notification of mouse events which occur within its
descendent elements.

See also the

Document Object Model (DOM) Level 2 Events Specification

.

In the case of nested elements mouse events are always targeted at the
most deeply nested element. Ancestors of the targeted element may use
bubbling to obtain notification of mouse events which occur within its
descendent elements.

See also the

Document Object Model (DOM) Level 2 Events Specification

.

See also the

Document Object Model (DOM) Level 2 Events Specification

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface org.w3c.dom.events.

Event

AT_TARGET

,

BUBBLING_PHASE

,

CAPTURING_PHASE

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

getAltKey

()

Used to indicate whether the 'alt' key was depressed during the firing
of the event.

short

getButton

()

During mouse events caused by the depression or release of a mouse
button,

button

is used to indicate which mouse button
changed state.

int

getClientX

()

The horizontal coordinate at which the event occurred relative to the
DOM implementation's client area.

int

getClientY

()

The vertical coordinate at which the event occurred relative to the DOM
implementation's client area.

boolean

getCtrlKey

()

Used to indicate whether the 'ctrl' key was depressed during the firing
of the event.

boolean

getMetaKey

()

Used to indicate whether the 'meta' key was depressed during the firing
of the event.

EventTarget

getRelatedTarget

()

Used to identify a secondary

EventTarget

related to a UI
event.

int

getScreenX

()

The horizontal coordinate at which the event occurred relative to the
origin of the screen coordinate system.

int

getScreenY

()

The vertical coordinate at which the event occurred relative to the
origin of the screen coordinate system.

boolean

getShiftKey

()

Used to indicate whether the 'shift' key was depressed during the
firing of the event.

void

initMouseEvent

​(

String

typeArg,
boolean canBubbleArg,
boolean cancelableArg,

AbstractView

viewArg,
int detailArg,
int screenXArg,
int screenYArg,
int clientXArg,
int clientYArg,
boolean ctrlKeyArg,
boolean altKeyArg,
boolean shiftKeyArg,
boolean metaKeyArg,
short buttonArg,

EventTarget

relatedTargetArg)

The

initMouseEvent

method is used to initialize the value
of a

MouseEvent

created through the

DocumentEvent

interface.

- Methods declared in interface org.w3c.dom.events.

Event

getBubbles

,

getCancelable

,

getCurrentTarget

,

getEventPhase

,

getTarget

,

getTimeStamp

,

getType

,

initEvent

,

preventDefault

,

stopPropagation

- Methods declared in interface org.w3c.dom.events.

UIEvent

getDetail

,

getView

,

initUIEvent

Field Summary

- Fields declared in interface org.w3c.dom.events.

Event

AT_TARGET

,

BUBBLING_PHASE

,

CAPTURING_PHASE

---

#### Field Summary

Fields declared in interface org.w3c.dom.events.

Event

AT_TARGET

,

BUBBLING_PHASE

,

CAPTURING_PHASE

---

#### Fields declared in interface org.w3c.dom.events. Event

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

getAltKey

()

Used to indicate whether the 'alt' key was depressed during the firing
of the event.

short

getButton

()

During mouse events caused by the depression or release of a mouse
button,

button

is used to indicate which mouse button
changed state.

int

getClientX

()

The horizontal coordinate at which the event occurred relative to the
DOM implementation's client area.

int

getClientY

()

The vertical coordinate at which the event occurred relative to the DOM
implementation's client area.

boolean

getCtrlKey

()

Used to indicate whether the 'ctrl' key was depressed during the firing
of the event.

boolean

getMetaKey

()

Used to indicate whether the 'meta' key was depressed during the firing
of the event.

EventTarget

getRelatedTarget

()

Used to identify a secondary

EventTarget

related to a UI
event.

int

getScreenX

()

The horizontal coordinate at which the event occurred relative to the
origin of the screen coordinate system.

int

getScreenY

()

The vertical coordinate at which the event occurred relative to the
origin of the screen coordinate system.

boolean

getShiftKey

()

Used to indicate whether the 'shift' key was depressed during the
firing of the event.

void

initMouseEvent

​(

String

typeArg,
boolean canBubbleArg,
boolean cancelableArg,

AbstractView

viewArg,
int detailArg,
int screenXArg,
int screenYArg,
int clientXArg,
int clientYArg,
boolean ctrlKeyArg,
boolean altKeyArg,
boolean shiftKeyArg,
boolean metaKeyArg,
short buttonArg,

EventTarget

relatedTargetArg)

The

initMouseEvent

method is used to initialize the value
of a

MouseEvent

created through the

DocumentEvent

interface.

- Methods declared in interface org.w3c.dom.events.

Event

getBubbles

,

getCancelable

,

getCurrentTarget

,

getEventPhase

,

getTarget

,

getTimeStamp

,

getType

,

initEvent

,

preventDefault

,

stopPropagation

- Methods declared in interface org.w3c.dom.events.

UIEvent

getDetail

,

getView

,

initUIEvent

---

#### Method Summary

Used to indicate whether the 'alt' key was depressed during the firing
of the event.

During mouse events caused by the depression or release of a mouse
button,

button

is used to indicate which mouse button
changed state.

The horizontal coordinate at which the event occurred relative to the
DOM implementation's client area.

The vertical coordinate at which the event occurred relative to the DOM
implementation's client area.

Used to indicate whether the 'ctrl' key was depressed during the firing
of the event.

Used to indicate whether the 'meta' key was depressed during the firing
of the event.

Used to identify a secondary

EventTarget

related to a UI
event.

The horizontal coordinate at which the event occurred relative to the
origin of the screen coordinate system.

The vertical coordinate at which the event occurred relative to the
origin of the screen coordinate system.

Used to indicate whether the 'shift' key was depressed during the
firing of the event.

The

initMouseEvent

method is used to initialize the value
of a

MouseEvent

created through the

DocumentEvent

interface.

Methods declared in interface org.w3c.dom.events.

Event

getBubbles

,

getCancelable

,

getCurrentTarget

,

getEventPhase

,

getTarget

,

getTimeStamp

,

getType

,

initEvent

,

preventDefault

,

stopPropagation

---

#### Methods declared in interface org.w3c.dom.events. Event

Methods declared in interface org.w3c.dom.events.

UIEvent

getDetail

,

getView

,

initUIEvent

---

#### Methods declared in interface org.w3c.dom.events. UIEvent

============ METHOD DETAIL ==========

- Method Detail

- getScreenX

```java
int getScreenX()
```

The horizontal coordinate at which the event occurred relative to the
origin of the screen coordinate system.

- getScreenY

```java
int getScreenY()
```

The vertical coordinate at which the event occurred relative to the
origin of the screen coordinate system.

- getClientX

```java
int getClientX()
```

The horizontal coordinate at which the event occurred relative to the
DOM implementation's client area.

- getClientY

```java
int getClientY()
```

The vertical coordinate at which the event occurred relative to the DOM
implementation's client area.

- getCtrlKey

```java
boolean getCtrlKey()
```

Used to indicate whether the 'ctrl' key was depressed during the firing
of the event.

- getShiftKey

```java
boolean getShiftKey()
```

Used to indicate whether the 'shift' key was depressed during the
firing of the event.

- getAltKey

```java
boolean getAltKey()
```

Used to indicate whether the 'alt' key was depressed during the firing
of the event. On some platforms this key may map to an alternative
key name.

- getMetaKey

```java
boolean getMetaKey()
```

Used to indicate whether the 'meta' key was depressed during the firing
of the event. On some platforms this key may map to an alternative
key name.

- getButton

```java
short getButton()
```

During mouse events caused by the depression or release of a mouse
button,

button

is used to indicate which mouse button
changed state. The values for

button

range from zero to
indicate the left button of the mouse, one to indicate the middle
button if present, and two to indicate the right button. For mice
configured for left handed use in which the button actions are
reversed the values are instead read from right to left.

- getRelatedTarget

```java
EventTarget
getRelatedTarget()
```

Used to identify a secondary

EventTarget

related to a UI
event. Currently this attribute is used with the mouseover event to
indicate the

EventTarget

which the pointing device
exited and with the mouseout event to indicate the

EventTarget

which the pointing device entered.

- initMouseEvent

```java
void initMouseEvent​(
String
typeArg,
boolean canBubbleArg,
boolean cancelableArg,

AbstractView
viewArg,
int detailArg,
int screenXArg,
int screenYArg,
int clientXArg,
int clientYArg,
boolean ctrlKeyArg,
boolean altKeyArg,
boolean shiftKeyArg,
boolean metaKeyArg,
short buttonArg,

EventTarget
relatedTargetArg)
```

The

initMouseEvent

method is used to initialize the value
of a

MouseEvent

created through the

DocumentEvent

interface. This method may only be called
before the

MouseEvent

has been dispatched via the

dispatchEvent

method, though it may be called multiple
times during that phase if necessary. If called multiple times, the
final invocation takes precedence.

**Parameters:** typeArg

- Specifies the event type.
**Parameters:** canBubbleArg

- Specifies whether or not the event can bubble.
**Parameters:** cancelableArg

- Specifies whether or not the event's default
action can be prevented.
**Parameters:** viewArg

- Specifies the

Event

's

AbstractView

.
**Parameters:** detailArg

- Specifies the

Event

's mouse click count.
**Parameters:** screenXArg

- Specifies the

Event

's screen x
coordinate
**Parameters:** screenYArg

- Specifies the

Event

's screen y
coordinate
**Parameters:** clientXArg

- Specifies the

Event

's client x
coordinate
**Parameters:** clientYArg

- Specifies the

Event

's client y
coordinate
**Parameters:** ctrlKeyArg

- Specifies whether or not control key was depressed
during the

Event

.
**Parameters:** altKeyArg

- Specifies whether or not alt key was depressed during
the

Event

.
**Parameters:** shiftKeyArg

- Specifies whether or not shift key was depressed
during the

Event

.
**Parameters:** metaKeyArg

- Specifies whether or not meta key was depressed
during the

Event

.
**Parameters:** buttonArg

- Specifies the

Event

's mouse button.
**Parameters:** relatedTargetArg

- Specifies the

Event

's related

EventTarget

.

Method Detail

- getScreenX

```java
int getScreenX()
```

The horizontal coordinate at which the event occurred relative to the
origin of the screen coordinate system.

- getScreenY

```java
int getScreenY()
```

The vertical coordinate at which the event occurred relative to the
origin of the screen coordinate system.

- getClientX

```java
int getClientX()
```

The horizontal coordinate at which the event occurred relative to the
DOM implementation's client area.

- getClientY

```java
int getClientY()
```

The vertical coordinate at which the event occurred relative to the DOM
implementation's client area.

- getCtrlKey

```java
boolean getCtrlKey()
```

Used to indicate whether the 'ctrl' key was depressed during the firing
of the event.

- getShiftKey

```java
boolean getShiftKey()
```

Used to indicate whether the 'shift' key was depressed during the
firing of the event.

- getAltKey

```java
boolean getAltKey()
```

Used to indicate whether the 'alt' key was depressed during the firing
of the event. On some platforms this key may map to an alternative
key name.

- getMetaKey

```java
boolean getMetaKey()
```

Used to indicate whether the 'meta' key was depressed during the firing
of the event. On some platforms this key may map to an alternative
key name.

- getButton

```java
short getButton()
```

During mouse events caused by the depression or release of a mouse
button,

button

is used to indicate which mouse button
changed state. The values for

button

range from zero to
indicate the left button of the mouse, one to indicate the middle
button if present, and two to indicate the right button. For mice
configured for left handed use in which the button actions are
reversed the values are instead read from right to left.

- getRelatedTarget

```java
EventTarget
getRelatedTarget()
```

Used to identify a secondary

EventTarget

related to a UI
event. Currently this attribute is used with the mouseover event to
indicate the

EventTarget

which the pointing device
exited and with the mouseout event to indicate the

EventTarget

which the pointing device entered.

- initMouseEvent

```java
void initMouseEvent​(
String
typeArg,
boolean canBubbleArg,
boolean cancelableArg,

AbstractView
viewArg,
int detailArg,
int screenXArg,
int screenYArg,
int clientXArg,
int clientYArg,
boolean ctrlKeyArg,
boolean altKeyArg,
boolean shiftKeyArg,
boolean metaKeyArg,
short buttonArg,

EventTarget
relatedTargetArg)
```

The

initMouseEvent

method is used to initialize the value
of a

MouseEvent

created through the

DocumentEvent

interface. This method may only be called
before the

MouseEvent

has been dispatched via the

dispatchEvent

method, though it may be called multiple
times during that phase if necessary. If called multiple times, the
final invocation takes precedence.

**Parameters:** typeArg

- Specifies the event type.
**Parameters:** canBubbleArg

- Specifies whether or not the event can bubble.
**Parameters:** cancelableArg

- Specifies whether or not the event's default
action can be prevented.
**Parameters:** viewArg

- Specifies the

Event

's

AbstractView

.
**Parameters:** detailArg

- Specifies the

Event

's mouse click count.
**Parameters:** screenXArg

- Specifies the

Event

's screen x
coordinate
**Parameters:** screenYArg

- Specifies the

Event

's screen y
coordinate
**Parameters:** clientXArg

- Specifies the

Event

's client x
coordinate
**Parameters:** clientYArg

- Specifies the

Event

's client y
coordinate
**Parameters:** ctrlKeyArg

- Specifies whether or not control key was depressed
during the

Event

.
**Parameters:** altKeyArg

- Specifies whether or not alt key was depressed during
the

Event

.
**Parameters:** shiftKeyArg

- Specifies whether or not shift key was depressed
during the

Event

.
**Parameters:** metaKeyArg

- Specifies whether or not meta key was depressed
during the

Event

.
**Parameters:** buttonArg

- Specifies the

Event

's mouse button.
**Parameters:** relatedTargetArg

- Specifies the

Event

's related

EventTarget

.

---

#### Method Detail

getScreenX

```java
int getScreenX()
```

The horizontal coordinate at which the event occurred relative to the
origin of the screen coordinate system.

---

#### getScreenX

int getScreenX()

The horizontal coordinate at which the event occurred relative to the
origin of the screen coordinate system.

getScreenY

```java
int getScreenY()
```

The vertical coordinate at which the event occurred relative to the
origin of the screen coordinate system.

---

#### getScreenY

int getScreenY()

The vertical coordinate at which the event occurred relative to the
origin of the screen coordinate system.

getClientX

```java
int getClientX()
```

The horizontal coordinate at which the event occurred relative to the
DOM implementation's client area.

---

#### getClientX

int getClientX()

The horizontal coordinate at which the event occurred relative to the
DOM implementation's client area.

getClientY

```java
int getClientY()
```

The vertical coordinate at which the event occurred relative to the DOM
implementation's client area.

---

#### getClientY

int getClientY()

The vertical coordinate at which the event occurred relative to the DOM
implementation's client area.

getCtrlKey

```java
boolean getCtrlKey()
```

Used to indicate whether the 'ctrl' key was depressed during the firing
of the event.

---

#### getCtrlKey

boolean getCtrlKey()

Used to indicate whether the 'ctrl' key was depressed during the firing
of the event.

getShiftKey

```java
boolean getShiftKey()
```

Used to indicate whether the 'shift' key was depressed during the
firing of the event.

---

#### getShiftKey

boolean getShiftKey()

Used to indicate whether the 'shift' key was depressed during the
firing of the event.

getAltKey

```java
boolean getAltKey()
```

Used to indicate whether the 'alt' key was depressed during the firing
of the event. On some platforms this key may map to an alternative
key name.

---

#### getAltKey

boolean getAltKey()

Used to indicate whether the 'alt' key was depressed during the firing
of the event. On some platforms this key may map to an alternative
key name.

getMetaKey

```java
boolean getMetaKey()
```

Used to indicate whether the 'meta' key was depressed during the firing
of the event. On some platforms this key may map to an alternative
key name.

---

#### getMetaKey

boolean getMetaKey()

Used to indicate whether the 'meta' key was depressed during the firing
of the event. On some platforms this key may map to an alternative
key name.

getButton

```java
short getButton()
```

During mouse events caused by the depression or release of a mouse
button,

button

is used to indicate which mouse button
changed state. The values for

button

range from zero to
indicate the left button of the mouse, one to indicate the middle
button if present, and two to indicate the right button. For mice
configured for left handed use in which the button actions are
reversed the values are instead read from right to left.

---

#### getButton

short getButton()

During mouse events caused by the depression or release of a mouse
button,

button

is used to indicate which mouse button
changed state. The values for

button

range from zero to
indicate the left button of the mouse, one to indicate the middle
button if present, and two to indicate the right button. For mice
configured for left handed use in which the button actions are
reversed the values are instead read from right to left.

getRelatedTarget

```java
EventTarget
getRelatedTarget()
```

Used to identify a secondary

EventTarget

related to a UI
event. Currently this attribute is used with the mouseover event to
indicate the

EventTarget

which the pointing device
exited and with the mouseout event to indicate the

EventTarget

which the pointing device entered.

---

#### getRelatedTarget

EventTarget

getRelatedTarget()

Used to identify a secondary

EventTarget

related to a UI
event. Currently this attribute is used with the mouseover event to
indicate the

EventTarget

which the pointing device
exited and with the mouseout event to indicate the

EventTarget

which the pointing device entered.

initMouseEvent

```java
void initMouseEvent​(
String
typeArg,
boolean canBubbleArg,
boolean cancelableArg,

AbstractView
viewArg,
int detailArg,
int screenXArg,
int screenYArg,
int clientXArg,
int clientYArg,
boolean ctrlKeyArg,
boolean altKeyArg,
boolean shiftKeyArg,
boolean metaKeyArg,
short buttonArg,

EventTarget
relatedTargetArg)
```

The

initMouseEvent

method is used to initialize the value
of a

MouseEvent

created through the

DocumentEvent

interface. This method may only be called
before the

MouseEvent

has been dispatched via the

dispatchEvent

method, though it may be called multiple
times during that phase if necessary. If called multiple times, the
final invocation takes precedence.

**Parameters:** typeArg

- Specifies the event type.
**Parameters:** canBubbleArg

- Specifies whether or not the event can bubble.
**Parameters:** cancelableArg

- Specifies whether or not the event's default
action can be prevented.
**Parameters:** viewArg

- Specifies the

Event

's

AbstractView

.
**Parameters:** detailArg

- Specifies the

Event

's mouse click count.
**Parameters:** screenXArg

- Specifies the

Event

's screen x
coordinate
**Parameters:** screenYArg

- Specifies the

Event

's screen y
coordinate
**Parameters:** clientXArg

- Specifies the

Event

's client x
coordinate
**Parameters:** clientYArg

- Specifies the

Event

's client y
coordinate
**Parameters:** ctrlKeyArg

- Specifies whether or not control key was depressed
during the

Event

.
**Parameters:** altKeyArg

- Specifies whether or not alt key was depressed during
the

Event

.
**Parameters:** shiftKeyArg

- Specifies whether or not shift key was depressed
during the

Event

.
**Parameters:** metaKeyArg

- Specifies whether or not meta key was depressed
during the

Event

.
**Parameters:** buttonArg

- Specifies the

Event

's mouse button.
**Parameters:** relatedTargetArg

- Specifies the

Event

's related

EventTarget

.

---

#### initMouseEvent

void initMouseEvent​(

String

typeArg,
boolean canBubbleArg,
boolean cancelableArg,

AbstractView

viewArg,
int detailArg,
int screenXArg,
int screenYArg,
int clientXArg,
int clientYArg,
boolean ctrlKeyArg,
boolean altKeyArg,
boolean shiftKeyArg,
boolean metaKeyArg,
short buttonArg,

EventTarget

relatedTargetArg)

The

initMouseEvent

method is used to initialize the value
of a

MouseEvent

created through the

DocumentEvent

interface. This method may only be called
before the

MouseEvent

has been dispatched via the

dispatchEvent

method, though it may be called multiple
times during that phase if necessary. If called multiple times, the
final invocation takes precedence.

---

