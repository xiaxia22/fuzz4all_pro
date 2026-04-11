# Class ErroneousSnippet

**Source:** `jdk.jshell\jdk\jshell\ErroneousSnippet.html`

### Class Description

```java
public class
ErroneousSnippet

extends
Snippet
```

A snippet of code that is not valid Java programming language code.
The Kind is

ERRONEOUS

.

ErroneousSnippet

is immutable: an access to
any of its methods will always return the same result.
and thus is thread-safe.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
Snippet.Kind
probableKind()

Returns what appears to be the intended Kind in this erroneous snippet.

**Returns:**
- the probable Kind; or

Snippet.Kind.ERRONEOUS

if that cannot be
determined.

---

### Additional Sections

#### Class ErroneousSnippet

java.lang.Object

- jdk.jshell.Snippet
- - jdk.jshell.ErroneousSnippet

jdk.jshell.Snippet

- jdk.jshell.ErroneousSnippet

jdk.jshell.ErroneousSnippet

```java
public class
ErroneousSnippet

extends
Snippet
```

A snippet of code that is not valid Java programming language code.
The Kind is

ERRONEOUS

.

ErroneousSnippet

is immutable: an access to
any of its methods will always return the same result.
and thus is thread-safe.

**Since:** 9

public class

ErroneousSnippet

extends

Snippet

A snippet of code that is not valid Java programming language code.
The Kind is

ERRONEOUS

.

ErroneousSnippet

is immutable: an access to
any of its methods will always return the same result.
and thus is thread-safe.

ErroneousSnippet

is immutable: an access to
any of its methods will always return the same result.
and thus is thread-safe.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class jdk.jshell.

Snippet

Snippet.Kind

,

Snippet.Status

,

Snippet.SubKind

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Snippet.Kind

probableKind

()

Returns what appears to be the intended Kind in this erroneous snippet.

- Methods declared in class jdk.jshell.

Snippet

id

,

kind

,

source

,

subKind

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

- Nested classes/interfaces declared in class jdk.jshell.

Snippet

Snippet.Kind

,

Snippet.Status

,

Snippet.SubKind

---

#### Nested Class Summary

Nested classes/interfaces declared in class jdk.jshell.

Snippet

Snippet.Kind

,

Snippet.Status

,

Snippet.SubKind

---

#### Nested classes/interfaces declared in class jdk.jshell. Snippet

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Snippet.Kind

probableKind

()

Returns what appears to be the intended Kind in this erroneous snippet.

- Methods declared in class jdk.jshell.

Snippet

id

,

kind

,

source

,

subKind

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

Returns what appears to be the intended Kind in this erroneous snippet.

Methods declared in class jdk.jshell.

Snippet

id

,

kind

,

source

,

subKind

---

#### Methods declared in class jdk.jshell. Snippet

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

- probableKind

```java
public
Snippet.Kind
probableKind()
```

Returns what appears to be the intended Kind in this erroneous snippet.

**Returns:** the probable Kind; or

Snippet.Kind.ERRONEOUS

if that cannot be
determined.

Method Detail

- probableKind

```java
public
Snippet.Kind
probableKind()
```

Returns what appears to be the intended Kind in this erroneous snippet.

**Returns:** the probable Kind; or

Snippet.Kind.ERRONEOUS

if that cannot be
determined.

---

#### Method Detail

probableKind

```java
public
Snippet.Kind
probableKind()
```

Returns what appears to be the intended Kind in this erroneous snippet.

**Returns:** the probable Kind; or

Snippet.Kind.ERRONEOUS

if that cannot be
determined.

---

#### probableKind

public

Snippet.Kind

probableKind()

Returns what appears to be the intended Kind in this erroneous snippet.

---

