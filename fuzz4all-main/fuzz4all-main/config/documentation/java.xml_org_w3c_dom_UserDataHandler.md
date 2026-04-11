# Interface UserDataHandler

**Source:** `java.xml\org\w3c\dom\UserDataHandler.html`

### Class Description

```java
public interface
UserDataHandler
```

When associating an object to a key on a node using

Node.setUserData()

the application can provide a handler
that gets called when the node the object is associated to is being
cloned, imported, or renamed. This can be used by the application to
implement various behaviors regarding the data it associates to the DOM
nodes. This interface defines that handler.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

**Since:** 1.5, DOM Level 3

---

### Field Details

#### static final short NODE_CLONED

The node is cloned, using

Node.cloneNode()

.

**See Also:**
- Constant Field Values

---

#### static final short NODE_IMPORTED

The node is imported, using

Document.importNode()

.

**See Also:**
- Constant Field Values

---

#### static final short NODE_DELETED

The node is deleted.

Note:

This may not be supported or may not be reliable in
certain environments, such as Java, where the implementation has no
real control over when objects are actually deleted.

**See Also:**
- Constant Field Values

---

#### static final short NODE_RENAMED

The node is renamed, using

Document.renameNode()

.

**See Also:**
- Constant Field Values

---

#### static final short NODE_ADOPTED

The node is adopted, using

Document.adoptNode()

.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### void handle​(short operation,

String
key,

Object
data,

Node
src,

Node
dst)

This method is called whenever the node for which this handler is
registered is imported or cloned.

DOM applications must not raise exceptions in a

UserDataHandler

. The effect of throwing exceptions from
the handler is DOM implementation dependent.

**Parameters:**
- operation

- Specifies the type of operation that is being
performed on the node.
- key

- Specifies the key for which this handler is being called.
- data

- Specifies the data for which this handler is being called.
- src

- Specifies the node being cloned, adopted, imported, or
renamed. This is

null

when the node is being deleted.
- dst

- Specifies the node newly created if any, or

null

.

---

### Additional Sections

#### Interface UserDataHandler

```java
public interface
UserDataHandler
```

When associating an object to a key on a node using

Node.setUserData()

the application can provide a handler
that gets called when the node the object is associated to is being
cloned, imported, or renamed. This can be used by the application to
implement various behaviors regarding the data it associates to the DOM
nodes. This interface defines that handler.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

**Since:** 1.5, DOM Level 3

public interface

UserDataHandler

When associating an object to a key on a node using

Node.setUserData()

the application can provide a handler
that gets called when the node the object is associated to is being
cloned, imported, or renamed. This can be used by the application to
implement various behaviors regarding the data it associates to the DOM
nodes. This interface defines that handler.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static short

NODE_ADOPTED

The node is adopted, using

Document.adoptNode()

.

static short

NODE_CLONED

The node is cloned, using

Node.cloneNode()

.

static short

NODE_DELETED

The node is deleted.

static short

NODE_IMPORTED

The node is imported, using

Document.importNode()

.

static short

NODE_RENAMED

The node is renamed, using

Document.renameNode()

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

handle

​(short operation,

String

key,

Object

data,

Node

src,

Node

dst)

This method is called whenever the node for which this handler is
registered is imported or cloned.

Field Summary

Fields

Modifier and Type

Field

Description

static short

NODE_ADOPTED

The node is adopted, using

Document.adoptNode()

.

static short

NODE_CLONED

The node is cloned, using

Node.cloneNode()

.

static short

NODE_DELETED

The node is deleted.

static short

NODE_IMPORTED

The node is imported, using

Document.importNode()

.

static short

NODE_RENAMED

The node is renamed, using

Document.renameNode()

.

---

#### Field Summary

The node is adopted, using

Document.adoptNode()

.

The node is cloned, using

Node.cloneNode()

.

The node is deleted.

The node is imported, using

Document.importNode()

.

The node is renamed, using

Document.renameNode()

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

handle

​(short operation,

String

key,

Object

data,

Node

src,

Node

dst)

This method is called whenever the node for which this handler is
registered is imported or cloned.

---

#### Method Summary

This method is called whenever the node for which this handler is
registered is imported or cloned.

============ FIELD DETAIL ===========

- Field Detail

- NODE_CLONED

```java
static final short NODE_CLONED
```

The node is cloned, using

Node.cloneNode()

.

**See Also:** Constant Field Values

- NODE_IMPORTED

```java
static final short NODE_IMPORTED
```

The node is imported, using

Document.importNode()

.

**See Also:** Constant Field Values

- NODE_DELETED

```java
static final short NODE_DELETED
```

The node is deleted.

Note:

This may not be supported or may not be reliable in
certain environments, such as Java, where the implementation has no
real control over when objects are actually deleted.

**See Also:** Constant Field Values

- NODE_RENAMED

```java
static final short NODE_RENAMED
```

The node is renamed, using

Document.renameNode()

.

**See Also:** Constant Field Values

- NODE_ADOPTED

```java
static final short NODE_ADOPTED
```

The node is adopted, using

Document.adoptNode()

.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- handle

```java
void handle​(short operation,

String
key,

Object
data,

Node
src,

Node
dst)
```

This method is called whenever the node for which this handler is
registered is imported or cloned.

DOM applications must not raise exceptions in a

UserDataHandler

. The effect of throwing exceptions from
the handler is DOM implementation dependent.

**Parameters:** operation

- Specifies the type of operation that is being
performed on the node.
**Parameters:** key

- Specifies the key for which this handler is being called.
**Parameters:** data

- Specifies the data for which this handler is being called.
**Parameters:** src

- Specifies the node being cloned, adopted, imported, or
renamed. This is

null

when the node is being deleted.
**Parameters:** dst

- Specifies the node newly created if any, or

null

.

Field Detail

- NODE_CLONED

```java
static final short NODE_CLONED
```

The node is cloned, using

Node.cloneNode()

.

**See Also:** Constant Field Values

- NODE_IMPORTED

```java
static final short NODE_IMPORTED
```

The node is imported, using

Document.importNode()

.

**See Also:** Constant Field Values

- NODE_DELETED

```java
static final short NODE_DELETED
```

The node is deleted.

Note:

This may not be supported or may not be reliable in
certain environments, such as Java, where the implementation has no
real control over when objects are actually deleted.

**See Also:** Constant Field Values

- NODE_RENAMED

```java
static final short NODE_RENAMED
```

The node is renamed, using

Document.renameNode()

.

**See Also:** Constant Field Values

- NODE_ADOPTED

```java
static final short NODE_ADOPTED
```

The node is adopted, using

Document.adoptNode()

.

**See Also:** Constant Field Values

---

#### Field Detail

NODE_CLONED

```java
static final short NODE_CLONED
```

The node is cloned, using

Node.cloneNode()

.

**See Also:** Constant Field Values

---

#### NODE_CLONED

static final short NODE_CLONED

The node is cloned, using

Node.cloneNode()

.

NODE_IMPORTED

```java
static final short NODE_IMPORTED
```

The node is imported, using

Document.importNode()

.

**See Also:** Constant Field Values

---

#### NODE_IMPORTED

static final short NODE_IMPORTED

The node is imported, using

Document.importNode()

.

NODE_DELETED

```java
static final short NODE_DELETED
```

The node is deleted.

Note:

This may not be supported or may not be reliable in
certain environments, such as Java, where the implementation has no
real control over when objects are actually deleted.

**See Also:** Constant Field Values

---

#### NODE_DELETED

static final short NODE_DELETED

The node is deleted.

Note:

This may not be supported or may not be reliable in
certain environments, such as Java, where the implementation has no
real control over when objects are actually deleted.

Note:

This may not be supported or may not be reliable in
certain environments, such as Java, where the implementation has no
real control over when objects are actually deleted.

NODE_RENAMED

```java
static final short NODE_RENAMED
```

The node is renamed, using

Document.renameNode()

.

**See Also:** Constant Field Values

---

#### NODE_RENAMED

static final short NODE_RENAMED

The node is renamed, using

Document.renameNode()

.

NODE_ADOPTED

```java
static final short NODE_ADOPTED
```

The node is adopted, using

Document.adoptNode()

.

**See Also:** Constant Field Values

---

#### NODE_ADOPTED

static final short NODE_ADOPTED

The node is adopted, using

Document.adoptNode()

.

Method Detail

- handle

```java
void handle​(short operation,

String
key,

Object
data,

Node
src,

Node
dst)
```

This method is called whenever the node for which this handler is
registered is imported or cloned.

DOM applications must not raise exceptions in a

UserDataHandler

. The effect of throwing exceptions from
the handler is DOM implementation dependent.

**Parameters:** operation

- Specifies the type of operation that is being
performed on the node.
**Parameters:** key

- Specifies the key for which this handler is being called.
**Parameters:** data

- Specifies the data for which this handler is being called.
**Parameters:** src

- Specifies the node being cloned, adopted, imported, or
renamed. This is

null

when the node is being deleted.
**Parameters:** dst

- Specifies the node newly created if any, or

null

.

---

#### Method Detail

handle

```java
void handle​(short operation,

String
key,

Object
data,

Node
src,

Node
dst)
```

This method is called whenever the node for which this handler is
registered is imported or cloned.

DOM applications must not raise exceptions in a

UserDataHandler

. The effect of throwing exceptions from
the handler is DOM implementation dependent.

**Parameters:** operation

- Specifies the type of operation that is being
performed on the node.
**Parameters:** key

- Specifies the key for which this handler is being called.
**Parameters:** data

- Specifies the data for which this handler is being called.
**Parameters:** src

- Specifies the node being cloned, adopted, imported, or
renamed. This is

null

when the node is being deleted.
**Parameters:** dst

- Specifies the node newly created if any, or

null

.

---

#### handle

void handle​(short operation,

String

key,

Object

data,

Node

src,

Node

dst)

This method is called whenever the node for which this handler is
registered is imported or cloned.

DOM applications must not raise exceptions in a

UserDataHandler

. The effect of throwing exceptions from
the handler is DOM implementation dependent.

---

