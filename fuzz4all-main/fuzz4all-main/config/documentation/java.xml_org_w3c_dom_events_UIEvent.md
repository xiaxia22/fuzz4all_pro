# Interface UIEvent

**Source:** `java.xml\org\w3c\dom\events\UIEvent.html`

### Class Description

```java
public interface
UIEvent

extends
Event
```

The

UIEvent

interface provides specific contextual information
associated with User Interface events.

See also the

Document Object Model (DOM) Level 2 Events Specification

.

**All Superinterfaces:** Event

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### AbstractView
getView()

The

view

attribute identifies the

AbstractView

from which the event was generated.

---

#### int getDetail()

Specifies some detail information about the

Event

,
depending on the type of event.

---

#### void initUIEvent​(
String
typeArg,
boolean canBubbleArg,
boolean cancelableArg,

AbstractView
viewArg,
int detailArg)

The

initUIEvent

method is used to initialize the value of
a

UIEvent

created through the

DocumentEvent

interface. This method may only be called before the

UIEvent

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

's detail.

---

### Additional Sections

#### Interface UIEvent

**All Superinterfaces:** Event

**All Known Subinterfaces:** MouseEvent

```java
public interface
UIEvent

extends
Event
```

The

UIEvent

interface provides specific contextual information
associated with User Interface events.

See also the

Document Object Model (DOM) Level 2 Events Specification

.

**Since:** 1.5, DOM Level 2

public interface

UIEvent

extends

Event

The

UIEvent

interface provides specific contextual information
associated with User Interface events.

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

int

getDetail

()

Specifies some detail information about the

Event

,
depending on the type of event.

AbstractView

getView

()

The

view

attribute identifies the

AbstractView

from which the event was generated.

void

initUIEvent

​(

String

typeArg,
boolean canBubbleArg,
boolean cancelableArg,

AbstractView

viewArg,
int detailArg)

The

initUIEvent

method is used to initialize the value of
a

UIEvent

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

int

getDetail

()

Specifies some detail information about the

Event

,
depending on the type of event.

AbstractView

getView

()

The

view

attribute identifies the

AbstractView

from which the event was generated.

void

initUIEvent

​(

String

typeArg,
boolean canBubbleArg,
boolean cancelableArg,

AbstractView

viewArg,
int detailArg)

The

initUIEvent

method is used to initialize the value of
a

UIEvent

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

---

#### Method Summary

Specifies some detail information about the

Event

,
depending on the type of event.

The

view

attribute identifies the

AbstractView

from which the event was generated.

The

initUIEvent

method is used to initialize the value of
a

UIEvent

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

============ METHOD DETAIL ==========

- Method Detail

- getView

```java
AbstractView
getView()
```

The

view

attribute identifies the

AbstractView

from which the event was generated.

- getDetail

```java
int getDetail()
```

Specifies some detail information about the

Event

,
depending on the type of event.

- initUIEvent

```java
void initUIEvent​(
String
typeArg,
boolean canBubbleArg,
boolean cancelableArg,

AbstractView
viewArg,
int detailArg)
```

The

initUIEvent

method is used to initialize the value of
a

UIEvent

created through the

DocumentEvent

interface. This method may only be called before the

UIEvent

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

's detail.

Method Detail

- getView

```java
AbstractView
getView()
```

The

view

attribute identifies the

AbstractView

from which the event was generated.

- getDetail

```java
int getDetail()
```

Specifies some detail information about the

Event

,
depending on the type of event.

- initUIEvent

```java
void initUIEvent​(
String
typeArg,
boolean canBubbleArg,
boolean cancelableArg,

AbstractView
viewArg,
int detailArg)
```

The

initUIEvent

method is used to initialize the value of
a

UIEvent

created through the

DocumentEvent

interface. This method may only be called before the

UIEvent

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

's detail.

---

#### Method Detail

getView

```java
AbstractView
getView()
```

The

view

attribute identifies the

AbstractView

from which the event was generated.

---

#### getView

AbstractView

getView()

The

view

attribute identifies the

AbstractView

from which the event was generated.

getDetail

```java
int getDetail()
```

Specifies some detail information about the

Event

,
depending on the type of event.

---

#### getDetail

int getDetail()

Specifies some detail information about the

Event

,
depending on the type of event.

initUIEvent

```java
void initUIEvent​(
String
typeArg,
boolean canBubbleArg,
boolean cancelableArg,

AbstractView
viewArg,
int detailArg)
```

The

initUIEvent

method is used to initialize the value of
a

UIEvent

created through the

DocumentEvent

interface. This method may only be called before the

UIEvent

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

's detail.

---

#### initUIEvent

void initUIEvent​(

String

typeArg,
boolean canBubbleArg,
boolean cancelableArg,

AbstractView

viewArg,
int detailArg)

The

initUIEvent

method is used to initialize the value of
a

UIEvent

created through the

DocumentEvent

interface. This method may only be called before the

UIEvent

has been dispatched via the

dispatchEvent

method, though it may be called multiple
times during that phase if necessary. If called multiple times, the
final invocation takes precedence.

---

