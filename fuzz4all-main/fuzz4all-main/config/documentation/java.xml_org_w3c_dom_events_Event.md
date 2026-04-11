# Interface Event

**Source:** `java.xml\org\w3c\dom\events\Event.html`

### Class Description

```java
public interface
Event
```

The

Event

interface is used to provide contextual information
about an event to the handler processing the event. An object which
implements the

Event

interface is generally passed as the
first parameter to an event handler. More specific context information is
passed to event handlers by deriving additional interfaces from

Event

which contain information directly relating to the
type of event they accompany. These derived interfaces are also
implemented by the object passed to the event listener.

See also the

Document Object Model (DOM) Level 2 Events Specification

.

**All Known Subinterfaces:** LSLoadEvent

,

LSProgressEvent

,

MouseEvent

,

MutationEvent

,

UIEvent

---

### Field Details

#### static final short CAPTURING_PHASE

The current event phase is the capturing phase.

**See Also:**
- Constant Field Values

---

#### static final short AT_TARGET

The event is currently being evaluated at the target

EventTarget

.

**See Also:**
- Constant Field Values

---

#### static final short BUBBLING_PHASE

The current event phase is the bubbling phase.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### String
getType()

The name of the event (case-insensitive). The name must be an XML name.

---

#### EventTarget
getTarget()

Used to indicate the

EventTarget

to which the event was
originally dispatched.

---

#### EventTarget
getCurrentTarget()

Used to indicate the

EventTarget

whose

EventListeners

are currently being processed. This is
particularly useful during capturing and bubbling.

---

#### short getEventPhase()

Used to indicate which phase of event flow is currently being
evaluated.

---

#### boolean getBubbles()

Used to indicate whether or not an event is a bubbling event. If the
event can bubble the value is true, else the value is false.

---

#### boolean getCancelable()

Used to indicate whether or not an event can have its default action
prevented. If the default action can be prevented the value is true,
else the value is false.

---

#### long getTimeStamp()

Used to specify the time (in milliseconds relative to the epoch) at
which the event was created. Due to the fact that some systems may
not provide this information the value of

timeStamp

may
be not available for all events. When not available, a value of 0
will be returned. Examples of epoch time are the time of the system
start or 0:0:0 UTC 1st January 1970.

---

#### void stopPropagation()

The

stopPropagation

method is used prevent further
propagation of an event during event flow. If this method is called
by any

EventListener

the event will cease propagating
through the tree. The event will complete dispatch to all listeners
on the current

EventTarget

before event flow stops. This
method may be used during any stage of event flow.

---

#### void preventDefault()

If an event is cancelable, the

preventDefault

method is
used to signify that the event is to be canceled, meaning any default
action normally taken by the implementation as a result of the event
will not occur. If, during any stage of event flow, the

preventDefault

method is called the event is canceled.
Any default action associated with the event will not occur. Calling
this method for a non-cancelable event has no effect. Once

preventDefault

has been called it will remain in effect
throughout the remainder of the event's propagation. This method may
be used during any stage of event flow.

---

#### void initEvent​(
String
eventTypeArg,
boolean canBubbleArg,
boolean cancelableArg)

The

initEvent

method is used to initialize the value of an

Event

created through the

DocumentEvent

interface. This method may only be called before the

Event

has been dispatched via the

dispatchEvent

method, though it may be called multiple
times during that phase if necessary. If called multiple times the
final invocation takes precedence. If called from a subclass of

Event

interface only the values specified in the

initEvent

method are modified, all other attributes are
left unchanged.

**Parameters:**
- eventTypeArg

- Specifies the event type. This type may be any
event type currently defined in this specification or a new event
type.. The string must be an XML name. Any new event type must not
begin with any upper, lower, or mixed case version of the string
"DOM". This prefix is reserved for future DOM event sets. It is
also strongly recommended that third parties adding their own
events use their own prefix to avoid confusion and lessen the
probability of conflicts with other new events.
- canBubbleArg

- Specifies whether or not the event can bubble.
- cancelableArg

- Specifies whether or not the event's default
action can be prevented.

---

### Additional Sections

#### Interface Event

**All Known Subinterfaces:** LSLoadEvent

,

LSProgressEvent

,

MouseEvent

,

MutationEvent

,

UIEvent

```java
public interface
Event
```

The

Event

interface is used to provide contextual information
about an event to the handler processing the event. An object which
implements the

Event

interface is generally passed as the
first parameter to an event handler. More specific context information is
passed to event handlers by deriving additional interfaces from

Event

which contain information directly relating to the
type of event they accompany. These derived interfaces are also
implemented by the object passed to the event listener.

See also the

Document Object Model (DOM) Level 2 Events Specification

.

**Since:** 1.5, DOM Level 2

public interface

Event

The

Event

interface is used to provide contextual information
about an event to the handler processing the event. An object which
implements the

Event

interface is generally passed as the
first parameter to an event handler. More specific context information is
passed to event handlers by deriving additional interfaces from

Event

which contain information directly relating to the
type of event they accompany. These derived interfaces are also
implemented by the object passed to the event listener.

See also the

Document Object Model (DOM) Level 2 Events Specification

.

See also the

Document Object Model (DOM) Level 2 Events Specification

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static short

AT_TARGET

The event is currently being evaluated at the target

EventTarget

.

static short

BUBBLING_PHASE

The current event phase is the bubbling phase.

static short

CAPTURING_PHASE

The current event phase is the capturing phase.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

getBubbles

()

Used to indicate whether or not an event is a bubbling event.

boolean

getCancelable

()

Used to indicate whether or not an event can have its default action
prevented.

EventTarget

getCurrentTarget

()

Used to indicate the

EventTarget

whose

EventListeners

are currently being processed.

short

getEventPhase

()

Used to indicate which phase of event flow is currently being
evaluated.

EventTarget

getTarget

()

Used to indicate the

EventTarget

to which the event was
originally dispatched.

long

getTimeStamp

()

Used to specify the time (in milliseconds relative to the epoch) at
which the event was created.

String

getType

()

The name of the event (case-insensitive).

void

initEvent

​(

String

eventTypeArg,
boolean canBubbleArg,
boolean cancelableArg)

The

initEvent

method is used to initialize the value of an

Event

created through the

DocumentEvent

interface.

void

preventDefault

()

If an event is cancelable, the

preventDefault

method is
used to signify that the event is to be canceled, meaning any default
action normally taken by the implementation as a result of the event
will not occur.

void

stopPropagation

()

The

stopPropagation

method is used prevent further
propagation of an event during event flow.

Field Summary

Fields

Modifier and Type

Field

Description

static short

AT_TARGET

The event is currently being evaluated at the target

EventTarget

.

static short

BUBBLING_PHASE

The current event phase is the bubbling phase.

static short

CAPTURING_PHASE

The current event phase is the capturing phase.

---

#### Field Summary

The event is currently being evaluated at the target

EventTarget

.

The current event phase is the bubbling phase.

The current event phase is the capturing phase.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

getBubbles

()

Used to indicate whether or not an event is a bubbling event.

boolean

getCancelable

()

Used to indicate whether or not an event can have its default action
prevented.

EventTarget

getCurrentTarget

()

Used to indicate the

EventTarget

whose

EventListeners

are currently being processed.

short

getEventPhase

()

Used to indicate which phase of event flow is currently being
evaluated.

EventTarget

getTarget

()

Used to indicate the

EventTarget

to which the event was
originally dispatched.

long

getTimeStamp

()

Used to specify the time (in milliseconds relative to the epoch) at
which the event was created.

String

getType

()

The name of the event (case-insensitive).

void

initEvent

​(

String

eventTypeArg,
boolean canBubbleArg,
boolean cancelableArg)

The

initEvent

method is used to initialize the value of an

Event

created through the

DocumentEvent

interface.

void

preventDefault

()

If an event is cancelable, the

preventDefault

method is
used to signify that the event is to be canceled, meaning any default
action normally taken by the implementation as a result of the event
will not occur.

void

stopPropagation

()

The

stopPropagation

method is used prevent further
propagation of an event during event flow.

---

#### Method Summary

Used to indicate whether or not an event is a bubbling event.

Used to indicate whether or not an event can have its default action
prevented.

Used to indicate the

EventTarget

whose

EventListeners

are currently being processed.

Used to indicate which phase of event flow is currently being
evaluated.

Used to indicate the

EventTarget

to which the event was
originally dispatched.

Used to specify the time (in milliseconds relative to the epoch) at
which the event was created.

The name of the event (case-insensitive).

The

initEvent

method is used to initialize the value of an

Event

created through the

DocumentEvent

interface.

If an event is cancelable, the

preventDefault

method is
used to signify that the event is to be canceled, meaning any default
action normally taken by the implementation as a result of the event
will not occur.

The

stopPropagation

method is used prevent further
propagation of an event during event flow.

============ FIELD DETAIL ===========

- Field Detail

- CAPTURING_PHASE

```java
static final short CAPTURING_PHASE
```

The current event phase is the capturing phase.

**See Also:** Constant Field Values

- AT_TARGET

```java
static final short AT_TARGET
```

The event is currently being evaluated at the target

EventTarget

.

**See Also:** Constant Field Values

- BUBBLING_PHASE

```java
static final short BUBBLING_PHASE
```

The current event phase is the bubbling phase.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getType

```java
String
getType()
```

The name of the event (case-insensitive). The name must be an XML name.

- getTarget

```java
EventTarget
getTarget()
```

Used to indicate the

EventTarget

to which the event was
originally dispatched.

- getCurrentTarget

```java
EventTarget
getCurrentTarget()
```

Used to indicate the

EventTarget

whose

EventListeners

are currently being processed. This is
particularly useful during capturing and bubbling.

- getEventPhase

```java
short getEventPhase()
```

Used to indicate which phase of event flow is currently being
evaluated.

- getBubbles

```java
boolean getBubbles()
```

Used to indicate whether or not an event is a bubbling event. If the
event can bubble the value is true, else the value is false.

- getCancelable

```java
boolean getCancelable()
```

Used to indicate whether or not an event can have its default action
prevented. If the default action can be prevented the value is true,
else the value is false.

- getTimeStamp

```java
long getTimeStamp()
```

Used to specify the time (in milliseconds relative to the epoch) at
which the event was created. Due to the fact that some systems may
not provide this information the value of

timeStamp

may
be not available for all events. When not available, a value of 0
will be returned. Examples of epoch time are the time of the system
start or 0:0:0 UTC 1st January 1970.

- stopPropagation

```java
void stopPropagation()
```

The

stopPropagation

method is used prevent further
propagation of an event during event flow. If this method is called
by any

EventListener

the event will cease propagating
through the tree. The event will complete dispatch to all listeners
on the current

EventTarget

before event flow stops. This
method may be used during any stage of event flow.

- preventDefault

```java
void preventDefault()
```

If an event is cancelable, the

preventDefault

method is
used to signify that the event is to be canceled, meaning any default
action normally taken by the implementation as a result of the event
will not occur. If, during any stage of event flow, the

preventDefault

method is called the event is canceled.
Any default action associated with the event will not occur. Calling
this method for a non-cancelable event has no effect. Once

preventDefault

has been called it will remain in effect
throughout the remainder of the event's propagation. This method may
be used during any stage of event flow.

- initEvent

```java
void initEvent​(
String
eventTypeArg,
boolean canBubbleArg,
boolean cancelableArg)
```

The

initEvent

method is used to initialize the value of an

Event

created through the

DocumentEvent

interface. This method may only be called before the

Event

has been dispatched via the

dispatchEvent

method, though it may be called multiple
times during that phase if necessary. If called multiple times the
final invocation takes precedence. If called from a subclass of

Event

interface only the values specified in the

initEvent

method are modified, all other attributes are
left unchanged.

**Parameters:** eventTypeArg

- Specifies the event type. This type may be any
event type currently defined in this specification or a new event
type.. The string must be an XML name. Any new event type must not
begin with any upper, lower, or mixed case version of the string
"DOM". This prefix is reserved for future DOM event sets. It is
also strongly recommended that third parties adding their own
events use their own prefix to avoid confusion and lessen the
probability of conflicts with other new events.
**Parameters:** canBubbleArg

- Specifies whether or not the event can bubble.
**Parameters:** cancelableArg

- Specifies whether or not the event's default
action can be prevented.

Field Detail

- CAPTURING_PHASE

```java
static final short CAPTURING_PHASE
```

The current event phase is the capturing phase.

**See Also:** Constant Field Values

- AT_TARGET

```java
static final short AT_TARGET
```

The event is currently being evaluated at the target

EventTarget

.

**See Also:** Constant Field Values

- BUBBLING_PHASE

```java
static final short BUBBLING_PHASE
```

The current event phase is the bubbling phase.

**See Also:** Constant Field Values

---

#### Field Detail

CAPTURING_PHASE

```java
static final short CAPTURING_PHASE
```

The current event phase is the capturing phase.

**See Also:** Constant Field Values

---

#### CAPTURING_PHASE

static final short CAPTURING_PHASE

The current event phase is the capturing phase.

AT_TARGET

```java
static final short AT_TARGET
```

The event is currently being evaluated at the target

EventTarget

.

**See Also:** Constant Field Values

---

#### AT_TARGET

static final short AT_TARGET

The event is currently being evaluated at the target

EventTarget

.

BUBBLING_PHASE

```java
static final short BUBBLING_PHASE
```

The current event phase is the bubbling phase.

**See Also:** Constant Field Values

---

#### BUBBLING_PHASE

static final short BUBBLING_PHASE

The current event phase is the bubbling phase.

Method Detail

- getType

```java
String
getType()
```

The name of the event (case-insensitive). The name must be an XML name.

- getTarget

```java
EventTarget
getTarget()
```

Used to indicate the

EventTarget

to which the event was
originally dispatched.

- getCurrentTarget

```java
EventTarget
getCurrentTarget()
```

Used to indicate the

EventTarget

whose

EventListeners

are currently being processed. This is
particularly useful during capturing and bubbling.

- getEventPhase

```java
short getEventPhase()
```

Used to indicate which phase of event flow is currently being
evaluated.

- getBubbles

```java
boolean getBubbles()
```

Used to indicate whether or not an event is a bubbling event. If the
event can bubble the value is true, else the value is false.

- getCancelable

```java
boolean getCancelable()
```

Used to indicate whether or not an event can have its default action
prevented. If the default action can be prevented the value is true,
else the value is false.

- getTimeStamp

```java
long getTimeStamp()
```

Used to specify the time (in milliseconds relative to the epoch) at
which the event was created. Due to the fact that some systems may
not provide this information the value of

timeStamp

may
be not available for all events. When not available, a value of 0
will be returned. Examples of epoch time are the time of the system
start or 0:0:0 UTC 1st January 1970.

- stopPropagation

```java
void stopPropagation()
```

The

stopPropagation

method is used prevent further
propagation of an event during event flow. If this method is called
by any

EventListener

the event will cease propagating
through the tree. The event will complete dispatch to all listeners
on the current

EventTarget

before event flow stops. This
method may be used during any stage of event flow.

- preventDefault

```java
void preventDefault()
```

If an event is cancelable, the

preventDefault

method is
used to signify that the event is to be canceled, meaning any default
action normally taken by the implementation as a result of the event
will not occur. If, during any stage of event flow, the

preventDefault

method is called the event is canceled.
Any default action associated with the event will not occur. Calling
this method for a non-cancelable event has no effect. Once

preventDefault

has been called it will remain in effect
throughout the remainder of the event's propagation. This method may
be used during any stage of event flow.

- initEvent

```java
void initEvent​(
String
eventTypeArg,
boolean canBubbleArg,
boolean cancelableArg)
```

The

initEvent

method is used to initialize the value of an

Event

created through the

DocumentEvent

interface. This method may only be called before the

Event

has been dispatched via the

dispatchEvent

method, though it may be called multiple
times during that phase if necessary. If called multiple times the
final invocation takes precedence. If called from a subclass of

Event

interface only the values specified in the

initEvent

method are modified, all other attributes are
left unchanged.

**Parameters:** eventTypeArg

- Specifies the event type. This type may be any
event type currently defined in this specification or a new event
type.. The string must be an XML name. Any new event type must not
begin with any upper, lower, or mixed case version of the string
"DOM". This prefix is reserved for future DOM event sets. It is
also strongly recommended that third parties adding their own
events use their own prefix to avoid confusion and lessen the
probability of conflicts with other new events.
**Parameters:** canBubbleArg

- Specifies whether or not the event can bubble.
**Parameters:** cancelableArg

- Specifies whether or not the event's default
action can be prevented.

---

#### Method Detail

getType

```java
String
getType()
```

The name of the event (case-insensitive). The name must be an XML name.

---

#### getType

String

getType()

The name of the event (case-insensitive). The name must be an XML name.

getTarget

```java
EventTarget
getTarget()
```

Used to indicate the

EventTarget

to which the event was
originally dispatched.

---

#### getTarget

EventTarget

getTarget()

Used to indicate the

EventTarget

to which the event was
originally dispatched.

getCurrentTarget

```java
EventTarget
getCurrentTarget()
```

Used to indicate the

EventTarget

whose

EventListeners

are currently being processed. This is
particularly useful during capturing and bubbling.

---

#### getCurrentTarget

EventTarget

getCurrentTarget()

Used to indicate the

EventTarget

whose

EventListeners

are currently being processed. This is
particularly useful during capturing and bubbling.

getEventPhase

```java
short getEventPhase()
```

Used to indicate which phase of event flow is currently being
evaluated.

---

#### getEventPhase

short getEventPhase()

Used to indicate which phase of event flow is currently being
evaluated.

getBubbles

```java
boolean getBubbles()
```

Used to indicate whether or not an event is a bubbling event. If the
event can bubble the value is true, else the value is false.

---

#### getBubbles

boolean getBubbles()

Used to indicate whether or not an event is a bubbling event. If the
event can bubble the value is true, else the value is false.

getCancelable

```java
boolean getCancelable()
```

Used to indicate whether or not an event can have its default action
prevented. If the default action can be prevented the value is true,
else the value is false.

---

#### getCancelable

boolean getCancelable()

Used to indicate whether or not an event can have its default action
prevented. If the default action can be prevented the value is true,
else the value is false.

getTimeStamp

```java
long getTimeStamp()
```

Used to specify the time (in milliseconds relative to the epoch) at
which the event was created. Due to the fact that some systems may
not provide this information the value of

timeStamp

may
be not available for all events. When not available, a value of 0
will be returned. Examples of epoch time are the time of the system
start or 0:0:0 UTC 1st January 1970.

---

#### getTimeStamp

long getTimeStamp()

Used to specify the time (in milliseconds relative to the epoch) at
which the event was created. Due to the fact that some systems may
not provide this information the value of

timeStamp

may
be not available for all events. When not available, a value of 0
will be returned. Examples of epoch time are the time of the system
start or 0:0:0 UTC 1st January 1970.

stopPropagation

```java
void stopPropagation()
```

The

stopPropagation

method is used prevent further
propagation of an event during event flow. If this method is called
by any

EventListener

the event will cease propagating
through the tree. The event will complete dispatch to all listeners
on the current

EventTarget

before event flow stops. This
method may be used during any stage of event flow.

---

#### stopPropagation

void stopPropagation()

The

stopPropagation

method is used prevent further
propagation of an event during event flow. If this method is called
by any

EventListener

the event will cease propagating
through the tree. The event will complete dispatch to all listeners
on the current

EventTarget

before event flow stops. This
method may be used during any stage of event flow.

preventDefault

```java
void preventDefault()
```

If an event is cancelable, the

preventDefault

method is
used to signify that the event is to be canceled, meaning any default
action normally taken by the implementation as a result of the event
will not occur. If, during any stage of event flow, the

preventDefault

method is called the event is canceled.
Any default action associated with the event will not occur. Calling
this method for a non-cancelable event has no effect. Once

preventDefault

has been called it will remain in effect
throughout the remainder of the event's propagation. This method may
be used during any stage of event flow.

---

#### preventDefault

void preventDefault()

If an event is cancelable, the

preventDefault

method is
used to signify that the event is to be canceled, meaning any default
action normally taken by the implementation as a result of the event
will not occur. If, during any stage of event flow, the

preventDefault

method is called the event is canceled.
Any default action associated with the event will not occur. Calling
this method for a non-cancelable event has no effect. Once

preventDefault

has been called it will remain in effect
throughout the remainder of the event's propagation. This method may
be used during any stage of event flow.

initEvent

```java
void initEvent​(
String
eventTypeArg,
boolean canBubbleArg,
boolean cancelableArg)
```

The

initEvent

method is used to initialize the value of an

Event

created through the

DocumentEvent

interface. This method may only be called before the

Event

has been dispatched via the

dispatchEvent

method, though it may be called multiple
times during that phase if necessary. If called multiple times the
final invocation takes precedence. If called from a subclass of

Event

interface only the values specified in the

initEvent

method are modified, all other attributes are
left unchanged.

**Parameters:** eventTypeArg

- Specifies the event type. This type may be any
event type currently defined in this specification or a new event
type.. The string must be an XML name. Any new event type must not
begin with any upper, lower, or mixed case version of the string
"DOM". This prefix is reserved for future DOM event sets. It is
also strongly recommended that third parties adding their own
events use their own prefix to avoid confusion and lessen the
probability of conflicts with other new events.
**Parameters:** canBubbleArg

- Specifies whether or not the event can bubble.
**Parameters:** cancelableArg

- Specifies whether or not the event's default
action can be prevented.

---

#### initEvent

void initEvent​(

String

eventTypeArg,
boolean canBubbleArg,
boolean cancelableArg)

The

initEvent

method is used to initialize the value of an

Event

created through the

DocumentEvent

interface. This method may only be called before the

Event

has been dispatched via the

dispatchEvent

method, though it may be called multiple
times during that phase if necessary. If called multiple times the
final invocation takes precedence. If called from a subclass of

Event

interface only the values specified in the

initEvent

method are modified, all other attributes are
left unchanged.

---

