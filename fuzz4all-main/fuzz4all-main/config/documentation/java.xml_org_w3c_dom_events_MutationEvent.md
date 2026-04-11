# Interface MutationEvent

**Source:** `java.xml\org\w3c\dom\events\MutationEvent.html`

### Class Description

```java
public interface
MutationEvent

extends
Event
```

The

MutationEvent

interface provides specific contextual
information associated with Mutation events.

See also the

Document Object Model (DOM) Level 2 Events Specification

.

**All Superinterfaces:** Event

---

### Field Details

#### static final short MODIFICATION

The

Attr

was modified in place.

**See Also:**
- Constant Field Values

---

#### static final short ADDITION

The

Attr

was just added.

**See Also:**
- Constant Field Values

---

#### static final short REMOVAL

The

Attr

was just removed.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### Node
getRelatedNode()

relatedNode

is used to identify a secondary node related
to a mutation event. For example, if a mutation event is dispatched
to a node indicating that its parent has changed, the

relatedNode

is the changed parent. If an event is
instead dispatched to a subtree indicating a node was changed within
it, the

relatedNode

is the changed node. In the case of
the DOMAttrModified event it indicates the

Attr

node
which was modified, added, or removed.

---

#### String
getPrevValue()

prevValue

indicates the previous value of the

Attr

node in DOMAttrModified events, and of the

CharacterData

node in DOMCharacterDataModified events.

---

#### String
getNewValue()

newValue

indicates the new value of the

Attr

node in DOMAttrModified events, and of the

CharacterData

node in DOMCharacterDataModified events.

---

#### String
getAttrName()

attrName

indicates the name of the changed

Attr

node in a DOMAttrModified event.

---

#### short getAttrChange()

attrChange

indicates the type of change which triggered
the DOMAttrModified event. The values can be

MODIFICATION

,

ADDITION

, or

REMOVAL

.

---

#### void initMutationEvent​(
String
typeArg,
boolean canBubbleArg,
boolean cancelableArg,

Node
relatedNodeArg,

String
prevValueArg,

String
newValueArg,

String
attrNameArg,
short attrChangeArg)

The

initMutationEvent

method is used to initialize the
value of a

MutationEvent

created through the

DocumentEvent

interface. This method may only be called
before the

MutationEvent

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
- relatedNodeArg

- Specifies the

Event

's related Node.
- prevValueArg

- Specifies the

Event

's

prevValue

attribute. This value may be null.
- newValueArg

- Specifies the

Event

's

newValue

attribute. This value may be null.
- attrNameArg

- Specifies the

Event

's

attrName

attribute. This value may be null.
- attrChangeArg

- Specifies the

Event

's

attrChange

attribute

---

### Additional Sections

#### Interface MutationEvent

**All Superinterfaces:** Event

```java
public interface
MutationEvent

extends
Event
```

The

MutationEvent

interface provides specific contextual
information associated with Mutation events.

See also the

Document Object Model (DOM) Level 2 Events Specification

.

**Since:** 1.5, DOM Level 2

public interface

MutationEvent

extends

Event

The

MutationEvent

interface provides specific contextual
information associated with Mutation events.

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

ADDITION

The

Attr

was just added.

static short

MODIFICATION

The

Attr

was modified in place.

static short

REMOVAL

The

Attr

was just removed.

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

short

getAttrChange

()

attrChange

indicates the type of change which triggered
the DOMAttrModified event.

String

getAttrName

()

attrName

indicates the name of the changed

Attr

node in a DOMAttrModified event.

String

getNewValue

()

newValue

indicates the new value of the

Attr

node in DOMAttrModified events, and of the

CharacterData

node in DOMCharacterDataModified events.

String

getPrevValue

()

prevValue

indicates the previous value of the

Attr

node in DOMAttrModified events, and of the

CharacterData

node in DOMCharacterDataModified events.

Node

getRelatedNode

()

relatedNode

is used to identify a secondary node related
to a mutation event.

void

initMutationEvent

​(

String

typeArg,
boolean canBubbleArg,
boolean cancelableArg,

Node

relatedNodeArg,

String

prevValueArg,

String

newValueArg,

String

attrNameArg,
short attrChangeArg)

The

initMutationEvent

method is used to initialize the
value of a

MutationEvent

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

Fields

Modifier and Type

Field

Description

static short

ADDITION

The

Attr

was just added.

static short

MODIFICATION

The

Attr

was modified in place.

static short

REMOVAL

The

Attr

was just removed.

- Fields declared in interface org.w3c.dom.events.

Event

AT_TARGET

,

BUBBLING_PHASE

,

CAPTURING_PHASE

---

#### Field Summary

The

Attr

was just added.

The

Attr

was modified in place.

The

Attr

was just removed.

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

short

getAttrChange

()

attrChange

indicates the type of change which triggered
the DOMAttrModified event.

String

getAttrName

()

attrName

indicates the name of the changed

Attr

node in a DOMAttrModified event.

String

getNewValue

()

newValue

indicates the new value of the

Attr

node in DOMAttrModified events, and of the

CharacterData

node in DOMCharacterDataModified events.

String

getPrevValue

()

prevValue

indicates the previous value of the

Attr

node in DOMAttrModified events, and of the

CharacterData

node in DOMCharacterDataModified events.

Node

getRelatedNode

()

relatedNode

is used to identify a secondary node related
to a mutation event.

void

initMutationEvent

​(

String

typeArg,
boolean canBubbleArg,
boolean cancelableArg,

Node

relatedNodeArg,

String

prevValueArg,

String

newValueArg,

String

attrNameArg,
short attrChangeArg)

The

initMutationEvent

method is used to initialize the
value of a

MutationEvent

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

attrChange

indicates the type of change which triggered
the DOMAttrModified event.

attrName

indicates the name of the changed

Attr

node in a DOMAttrModified event.

newValue

indicates the new value of the

Attr

node in DOMAttrModified events, and of the

CharacterData

node in DOMCharacterDataModified events.

prevValue

indicates the previous value of the

Attr

node in DOMAttrModified events, and of the

CharacterData

node in DOMCharacterDataModified events.

relatedNode

is used to identify a secondary node related
to a mutation event.

The

initMutationEvent

method is used to initialize the
value of a

MutationEvent

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

============ FIELD DETAIL ===========

- Field Detail

- MODIFICATION

```java
static final short MODIFICATION
```

The

Attr

was modified in place.

**See Also:** Constant Field Values

- ADDITION

```java
static final short ADDITION
```

The

Attr

was just added.

**See Also:** Constant Field Values

- REMOVAL

```java
static final short REMOVAL
```

The

Attr

was just removed.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getRelatedNode

```java
Node
getRelatedNode()
```

relatedNode

is used to identify a secondary node related
to a mutation event. For example, if a mutation event is dispatched
to a node indicating that its parent has changed, the

relatedNode

is the changed parent. If an event is
instead dispatched to a subtree indicating a node was changed within
it, the

relatedNode

is the changed node. In the case of
the DOMAttrModified event it indicates the

Attr

node
which was modified, added, or removed.

- getPrevValue

```java
String
getPrevValue()
```

prevValue

indicates the previous value of the

Attr

node in DOMAttrModified events, and of the

CharacterData

node in DOMCharacterDataModified events.

- getNewValue

```java
String
getNewValue()
```

newValue

indicates the new value of the

Attr

node in DOMAttrModified events, and of the

CharacterData

node in DOMCharacterDataModified events.

- getAttrName

```java
String
getAttrName()
```

attrName

indicates the name of the changed

Attr

node in a DOMAttrModified event.

- getAttrChange

```java
short getAttrChange()
```

attrChange

indicates the type of change which triggered
the DOMAttrModified event. The values can be

MODIFICATION

,

ADDITION

, or

REMOVAL

.

- initMutationEvent

```java
void initMutationEvent​(
String
typeArg,
boolean canBubbleArg,
boolean cancelableArg,

Node
relatedNodeArg,

String
prevValueArg,

String
newValueArg,

String
attrNameArg,
short attrChangeArg)
```

The

initMutationEvent

method is used to initialize the
value of a

MutationEvent

created through the

DocumentEvent

interface. This method may only be called
before the

MutationEvent

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
**Parameters:** relatedNodeArg

- Specifies the

Event

's related Node.
**Parameters:** prevValueArg

- Specifies the

Event

's

prevValue

attribute. This value may be null.
**Parameters:** newValueArg

- Specifies the

Event

's

newValue

attribute. This value may be null.
**Parameters:** attrNameArg

- Specifies the

Event

's

attrName

attribute. This value may be null.
**Parameters:** attrChangeArg

- Specifies the

Event

's

attrChange

attribute

Field Detail

- MODIFICATION

```java
static final short MODIFICATION
```

The

Attr

was modified in place.

**See Also:** Constant Field Values

- ADDITION

```java
static final short ADDITION
```

The

Attr

was just added.

**See Also:** Constant Field Values

- REMOVAL

```java
static final short REMOVAL
```

The

Attr

was just removed.

**See Also:** Constant Field Values

---

#### Field Detail

MODIFICATION

```java
static final short MODIFICATION
```

The

Attr

was modified in place.

**See Also:** Constant Field Values

---

#### MODIFICATION

static final short MODIFICATION

The

Attr

was modified in place.

ADDITION

```java
static final short ADDITION
```

The

Attr

was just added.

**See Also:** Constant Field Values

---

#### ADDITION

static final short ADDITION

The

Attr

was just added.

REMOVAL

```java
static final short REMOVAL
```

The

Attr

was just removed.

**See Also:** Constant Field Values

---

#### REMOVAL

static final short REMOVAL

The

Attr

was just removed.

Method Detail

- getRelatedNode

```java
Node
getRelatedNode()
```

relatedNode

is used to identify a secondary node related
to a mutation event. For example, if a mutation event is dispatched
to a node indicating that its parent has changed, the

relatedNode

is the changed parent. If an event is
instead dispatched to a subtree indicating a node was changed within
it, the

relatedNode

is the changed node. In the case of
the DOMAttrModified event it indicates the

Attr

node
which was modified, added, or removed.

- getPrevValue

```java
String
getPrevValue()
```

prevValue

indicates the previous value of the

Attr

node in DOMAttrModified events, and of the

CharacterData

node in DOMCharacterDataModified events.

- getNewValue

```java
String
getNewValue()
```

newValue

indicates the new value of the

Attr

node in DOMAttrModified events, and of the

CharacterData

node in DOMCharacterDataModified events.

- getAttrName

```java
String
getAttrName()
```

attrName

indicates the name of the changed

Attr

node in a DOMAttrModified event.

- getAttrChange

```java
short getAttrChange()
```

attrChange

indicates the type of change which triggered
the DOMAttrModified event. The values can be

MODIFICATION

,

ADDITION

, or

REMOVAL

.

- initMutationEvent

```java
void initMutationEvent​(
String
typeArg,
boolean canBubbleArg,
boolean cancelableArg,

Node
relatedNodeArg,

String
prevValueArg,

String
newValueArg,

String
attrNameArg,
short attrChangeArg)
```

The

initMutationEvent

method is used to initialize the
value of a

MutationEvent

created through the

DocumentEvent

interface. This method may only be called
before the

MutationEvent

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
**Parameters:** relatedNodeArg

- Specifies the

Event

's related Node.
**Parameters:** prevValueArg

- Specifies the

Event

's

prevValue

attribute. This value may be null.
**Parameters:** newValueArg

- Specifies the

Event

's

newValue

attribute. This value may be null.
**Parameters:** attrNameArg

- Specifies the

Event

's

attrName

attribute. This value may be null.
**Parameters:** attrChangeArg

- Specifies the

Event

's

attrChange

attribute

---

#### Method Detail

getRelatedNode

```java
Node
getRelatedNode()
```

relatedNode

is used to identify a secondary node related
to a mutation event. For example, if a mutation event is dispatched
to a node indicating that its parent has changed, the

relatedNode

is the changed parent. If an event is
instead dispatched to a subtree indicating a node was changed within
it, the

relatedNode

is the changed node. In the case of
the DOMAttrModified event it indicates the

Attr

node
which was modified, added, or removed.

---

#### getRelatedNode

Node

getRelatedNode()

relatedNode

is used to identify a secondary node related
to a mutation event. For example, if a mutation event is dispatched
to a node indicating that its parent has changed, the

relatedNode

is the changed parent. If an event is
instead dispatched to a subtree indicating a node was changed within
it, the

relatedNode

is the changed node. In the case of
the DOMAttrModified event it indicates the

Attr

node
which was modified, added, or removed.

getPrevValue

```java
String
getPrevValue()
```

prevValue

indicates the previous value of the

Attr

node in DOMAttrModified events, and of the

CharacterData

node in DOMCharacterDataModified events.

---

#### getPrevValue

String

getPrevValue()

prevValue

indicates the previous value of the

Attr

node in DOMAttrModified events, and of the

CharacterData

node in DOMCharacterDataModified events.

getNewValue

```java
String
getNewValue()
```

newValue

indicates the new value of the

Attr

node in DOMAttrModified events, and of the

CharacterData

node in DOMCharacterDataModified events.

---

#### getNewValue

String

getNewValue()

newValue

indicates the new value of the

Attr

node in DOMAttrModified events, and of the

CharacterData

node in DOMCharacterDataModified events.

getAttrName

```java
String
getAttrName()
```

attrName

indicates the name of the changed

Attr

node in a DOMAttrModified event.

---

#### getAttrName

String

getAttrName()

attrName

indicates the name of the changed

Attr

node in a DOMAttrModified event.

getAttrChange

```java
short getAttrChange()
```

attrChange

indicates the type of change which triggered
the DOMAttrModified event. The values can be

MODIFICATION

,

ADDITION

, or

REMOVAL

.

---

#### getAttrChange

short getAttrChange()

attrChange

indicates the type of change which triggered
the DOMAttrModified event. The values can be

MODIFICATION

,

ADDITION

, or

REMOVAL

.

initMutationEvent

```java
void initMutationEvent​(
String
typeArg,
boolean canBubbleArg,
boolean cancelableArg,

Node
relatedNodeArg,

String
prevValueArg,

String
newValueArg,

String
attrNameArg,
short attrChangeArg)
```

The

initMutationEvent

method is used to initialize the
value of a

MutationEvent

created through the

DocumentEvent

interface. This method may only be called
before the

MutationEvent

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
**Parameters:** relatedNodeArg

- Specifies the

Event

's related Node.
**Parameters:** prevValueArg

- Specifies the

Event

's

prevValue

attribute. This value may be null.
**Parameters:** newValueArg

- Specifies the

Event

's

newValue

attribute. This value may be null.
**Parameters:** attrNameArg

- Specifies the

Event

's

attrName

attribute. This value may be null.
**Parameters:** attrChangeArg

- Specifies the

Event

's

attrChange

attribute

---

#### initMutationEvent

void initMutationEvent​(

String

typeArg,
boolean canBubbleArg,
boolean cancelableArg,

Node

relatedNodeArg,

String

prevValueArg,

String

newValueArg,

String

attrNameArg,
short attrChangeArg)

The

initMutationEvent

method is used to initialize the
value of a

MutationEvent

created through the

DocumentEvent

interface. This method may only be called
before the

MutationEvent

has been dispatched via the

dispatchEvent

method, though it may be called multiple
times during that phase if necessary. If called multiple times, the
final invocation takes precedence.

---

