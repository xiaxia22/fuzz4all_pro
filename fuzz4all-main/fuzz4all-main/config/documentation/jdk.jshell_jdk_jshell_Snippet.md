# Class Snippet

**Source:** `jdk.jshell\jdk\jshell\Snippet.html`

### Class Description

```java
public abstract class
Snippet

extends
Object
```

A Snippet represents a snippet of Java source code as passed to

JShell.eval(java.lang.String)

. It is associated only with the

JShell

instance that created it.
An instance of Snippet (including its subclasses) is immutable: an access to
any of its methods will always return the same result.
For information about the current state of the snippet within the JShell
state engine, query

JShell

passing the Snippet.

Because it is immutable,

Snippet

(and subclasses) is thread-safe.

**Direct Known Subclasses:** ErroneousSnippet

,

ExpressionSnippet

,

PersistentSnippet

,

StatementSnippet

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
String
id()

The unique identifier for the snippet. No two active snippets will have
the same id(). Value of id has no prescribed meaning. The details of
how the id is generated and the mechanism to change it is documented in

JShell.Builder.idGenerator(BiFunction)

.

**Returns:**
- the snippet id string.

---

#### public
Snippet.Kind
kind()

The

Snippet.Kind

for the snippet.
Indicates the subclass of Snippet.

**Returns:**
- the Kind of the snippet

**See Also:**
- Snippet.Kind

---

#### public
Snippet.SubKind
subKind()

Return the

Snippet.SubKind

of snippet.
The SubKind is useful for feedback to users.

**Returns:**
- the SubKind corresponding to this snippet

---

#### public
String
source()

Return the source code of the snippet.

**Returns:**
- the source code corresponding to this snippet

---

### Additional Sections

#### Class Snippet

java.lang.Object

- jdk.jshell.Snippet

jdk.jshell.Snippet

**Direct Known Subclasses:** ErroneousSnippet

,

ExpressionSnippet

,

PersistentSnippet

,

StatementSnippet

```java
public abstract class
Snippet

extends
Object
```

A Snippet represents a snippet of Java source code as passed to

JShell.eval(java.lang.String)

. It is associated only with the

JShell

instance that created it.
An instance of Snippet (including its subclasses) is immutable: an access to
any of its methods will always return the same result.
For information about the current state of the snippet within the JShell
state engine, query

JShell

passing the Snippet.

Because it is immutable,

Snippet

(and subclasses) is thread-safe.

**Since:** 9
**See Also:** JShell.status(jdk.jshell.Snippet)

public abstract class

Snippet

extends

Object

A Snippet represents a snippet of Java source code as passed to

JShell.eval(java.lang.String)

. It is associated only with the

JShell

instance that created it.
An instance of Snippet (including its subclasses) is immutable: an access to
any of its methods will always return the same result.
For information about the current state of the snippet within the JShell
state engine, query

JShell

passing the Snippet.

Because it is immutable,

Snippet

(and subclasses) is thread-safe.

Because it is immutable,

Snippet

(and subclasses) is thread-safe.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Snippet.Kind

Describes the general kind of snippet.

static class

Snippet.Status

Describes the current state of a Snippet.

static class

Snippet.SubKind

The detailed variety of a snippet.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

id

()

The unique identifier for the snippet.

Snippet.Kind

kind

()

The

Snippet.Kind

for the snippet.

String

source

()

Return the source code of the snippet.

Snippet.SubKind

subKind

()

Return the

Snippet.SubKind

of snippet.

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

static class

Snippet.Kind

Describes the general kind of snippet.

static class

Snippet.Status

Describes the current state of a Snippet.

static class

Snippet.SubKind

The detailed variety of a snippet.

---

#### Nested Class Summary

Describes the general kind of snippet.

Describes the current state of a Snippet.

The detailed variety of a snippet.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

id

()

The unique identifier for the snippet.

Snippet.Kind

kind

()

The

Snippet.Kind

for the snippet.

String

source

()

Return the source code of the snippet.

Snippet.SubKind

subKind

()

Return the

Snippet.SubKind

of snippet.

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

The unique identifier for the snippet.

The

Snippet.Kind

for the snippet.

Return the source code of the snippet.

Return the

Snippet.SubKind

of snippet.

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

============ METHOD DETAIL ==========

- Method Detail

- id

```java
public
String
id()
```

The unique identifier for the snippet. No two active snippets will have
the same id(). Value of id has no prescribed meaning. The details of
how the id is generated and the mechanism to change it is documented in

JShell.Builder.idGenerator(BiFunction)

.

**Returns:** the snippet id string.

- kind

```java
public
Snippet.Kind
kind()
```

The

Snippet.Kind

for the snippet.
Indicates the subclass of Snippet.

**Returns:** the Kind of the snippet
**See Also:** Snippet.Kind

- subKind

```java
public
Snippet.SubKind
subKind()
```

Return the

Snippet.SubKind

of snippet.
The SubKind is useful for feedback to users.

**Returns:** the SubKind corresponding to this snippet

- source

```java
public
String
source()
```

Return the source code of the snippet.

**Returns:** the source code corresponding to this snippet

Method Detail

- id

```java
public
String
id()
```

The unique identifier for the snippet. No two active snippets will have
the same id(). Value of id has no prescribed meaning. The details of
how the id is generated and the mechanism to change it is documented in

JShell.Builder.idGenerator(BiFunction)

.

**Returns:** the snippet id string.

- kind

```java
public
Snippet.Kind
kind()
```

The

Snippet.Kind

for the snippet.
Indicates the subclass of Snippet.

**Returns:** the Kind of the snippet
**See Also:** Snippet.Kind

- subKind

```java
public
Snippet.SubKind
subKind()
```

Return the

Snippet.SubKind

of snippet.
The SubKind is useful for feedback to users.

**Returns:** the SubKind corresponding to this snippet

- source

```java
public
String
source()
```

Return the source code of the snippet.

**Returns:** the source code corresponding to this snippet

---

#### Method Detail

id

```java
public
String
id()
```

The unique identifier for the snippet. No two active snippets will have
the same id(). Value of id has no prescribed meaning. The details of
how the id is generated and the mechanism to change it is documented in

JShell.Builder.idGenerator(BiFunction)

.

**Returns:** the snippet id string.

---

#### id

public

String

id()

The unique identifier for the snippet. No two active snippets will have
the same id(). Value of id has no prescribed meaning. The details of
how the id is generated and the mechanism to change it is documented in

JShell.Builder.idGenerator(BiFunction)

.

kind

```java
public
Snippet.Kind
kind()
```

The

Snippet.Kind

for the snippet.
Indicates the subclass of Snippet.

**Returns:** the Kind of the snippet
**See Also:** Snippet.Kind

---

#### kind

public

Snippet.Kind

kind()

The

Snippet.Kind

for the snippet.
Indicates the subclass of Snippet.

subKind

```java
public
Snippet.SubKind
subKind()
```

Return the

Snippet.SubKind

of snippet.
The SubKind is useful for feedback to users.

**Returns:** the SubKind corresponding to this snippet

---

#### subKind

public

Snippet.SubKind

subKind()

Return the

Snippet.SubKind

of snippet.
The SubKind is useful for feedback to users.

source

```java
public
String
source()
```

Return the source code of the snippet.

**Returns:** the source code corresponding to this snippet

---

#### source

public

String

source()

Return the source code of the snippet.

---

