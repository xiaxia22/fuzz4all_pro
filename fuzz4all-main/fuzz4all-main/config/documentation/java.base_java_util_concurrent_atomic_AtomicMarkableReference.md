# Class AtomicMarkableReference<V>

**Source:** `java.base\java\util\concurrent\atomic\AtomicMarkableReference.html`

### Class Description

```java
public class
AtomicMarkableReference<V>

extends
Object
```

An

AtomicMarkableReference

maintains an object reference
along with a mark bit, that can be updated atomically.

Implementation note: This implementation maintains markable
references by creating internal objects representing "boxed"
[reference, boolean] pairs.

**Type Parameters:** V

- The type of object referred to by this reference

---

### Field Details

*No entries found.*

### Constructor Details

#### public AtomicMarkableReference​(
V
initialRef,
boolean initialMark)

Creates a new

AtomicMarkableReference

with the given
initial values.

**Parameters:**
- initialRef

- the initial reference
- initialMark

- the initial mark

---

### Method Details

#### public
V
getReference()

Returns the current value of the reference.

**Returns:**
- the current value of the reference

---

#### public boolean isMarked()

Returns the current value of the mark.

**Returns:**
- the current value of the mark

---

#### public
V
get​(boolean[] markHolder)

Returns the current values of both the reference and the mark.
Typical usage is

boolean[1] holder; ref = v.get(holder);

.

**Parameters:**
- markHolder

- an array of size of at least one. On return,

markHolder[0]

will hold the value of the mark.

**Returns:**
- the current value of the reference

---

#### public boolean weakCompareAndSet​(
V
expectedReference,

V
newReference,
boolean expectedMark,
boolean newMark)

Atomically sets the value of both the reference and mark
to the given update values if the
current reference is

==

to the expected reference
and the current mark is equal to the expected mark.

May fail
spuriously and does not provide ordering guarantees

, so is
only rarely an appropriate alternative to

compareAndSet

.

**Parameters:**
- expectedReference

- the expected value of the reference
- newReference

- the new value for the reference
- expectedMark

- the expected value of the mark
- newMark

- the new value for the mark

**Returns:**
- true

if successful

---

#### public boolean compareAndSet​(
V
expectedReference,

V
newReference,
boolean expectedMark,
boolean newMark)

Atomically sets the value of both the reference and mark
to the given update values if the
current reference is

==

to the expected reference
and the current mark is equal to the expected mark.

**Parameters:**
- expectedReference

- the expected value of the reference
- newReference

- the new value for the reference
- expectedMark

- the expected value of the mark
- newMark

- the new value for the mark

**Returns:**
- true

if successful

---

#### public void set​(
V
newReference,
boolean newMark)

Unconditionally sets the value of both the reference and mark.

**Parameters:**
- newReference

- the new value for the reference
- newMark

- the new value for the mark

---

#### public boolean attemptMark​(
V
expectedReference,
boolean newMark)

Atomically sets the value of the mark to the given update value
if the current reference is

==

to the expected
reference. Any given invocation of this operation may fail
(return

false

) spuriously, but repeated invocation
when the current value holds the expected value and no other
thread is also attempting to set the value will eventually
succeed.

**Parameters:**
- expectedReference

- the expected value of the reference
- newMark

- the new value for the mark

**Returns:**
- true

if successful

---

### Additional Sections

#### Class AtomicMarkableReference<V>

java.lang.Object

- java.util.concurrent.atomic.AtomicMarkableReference<V>

java.util.concurrent.atomic.AtomicMarkableReference<V>

**Type Parameters:** V

- The type of object referred to by this reference

```java
public class
AtomicMarkableReference<V>

extends
Object
```

An

AtomicMarkableReference

maintains an object reference
along with a mark bit, that can be updated atomically.

Implementation note: This implementation maintains markable
references by creating internal objects representing "boxed"
[reference, boolean] pairs.

**Since:** 1.5

public class

AtomicMarkableReference<V>

extends

Object

An

AtomicMarkableReference

maintains an object reference
along with a mark bit, that can be updated atomically.

Implementation note: This implementation maintains markable
references by creating internal objects representing "boxed"
[reference, boolean] pairs.

Implementation note: This implementation maintains markable
references by creating internal objects representing "boxed"
[reference, boolean] pairs.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AtomicMarkableReference

​(

V

initialRef,
boolean initialMark)

Creates a new

AtomicMarkableReference

with the given
initial values.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

attemptMark

​(

V

expectedReference,
boolean newMark)

Atomically sets the value of the mark to the given update value
if the current reference is

==

to the expected
reference.

boolean

compareAndSet

​(

V

expectedReference,

V

newReference,
boolean expectedMark,
boolean newMark)

Atomically sets the value of both the reference and mark
to the given update values if the
current reference is

==

to the expected reference
and the current mark is equal to the expected mark.

V

get

​(boolean[] markHolder)

Returns the current values of both the reference and the mark.

V

getReference

()

Returns the current value of the reference.

boolean

isMarked

()

Returns the current value of the mark.

void

set

​(

V

newReference,
boolean newMark)

Unconditionally sets the value of both the reference and mark.

boolean

weakCompareAndSet

​(

V

expectedReference,

V

newReference,
boolean expectedMark,
boolean newMark)

Atomically sets the value of both the reference and mark
to the given update values if the
current reference is

==

to the expected reference
and the current mark is equal to the expected mark.

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

Constructor Summary

Constructors

Constructor

Description

AtomicMarkableReference

​(

V

initialRef,
boolean initialMark)

Creates a new

AtomicMarkableReference

with the given
initial values.

---

#### Constructor Summary

Creates a new

AtomicMarkableReference

with the given
initial values.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

attemptMark

​(

V

expectedReference,
boolean newMark)

Atomically sets the value of the mark to the given update value
if the current reference is

==

to the expected
reference.

boolean

compareAndSet

​(

V

expectedReference,

V

newReference,
boolean expectedMark,
boolean newMark)

Atomically sets the value of both the reference and mark
to the given update values if the
current reference is

==

to the expected reference
and the current mark is equal to the expected mark.

V

get

​(boolean[] markHolder)

Returns the current values of both the reference and the mark.

V

getReference

()

Returns the current value of the reference.

boolean

isMarked

()

Returns the current value of the mark.

void

set

​(

V

newReference,
boolean newMark)

Unconditionally sets the value of both the reference and mark.

boolean

weakCompareAndSet

​(

V

expectedReference,

V

newReference,
boolean expectedMark,
boolean newMark)

Atomically sets the value of both the reference and mark
to the given update values if the
current reference is

==

to the expected reference
and the current mark is equal to the expected mark.

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

Atomically sets the value of the mark to the given update value
if the current reference is

==

to the expected
reference.

Atomically sets the value of both the reference and mark
to the given update values if the
current reference is

==

to the expected reference
and the current mark is equal to the expected mark.

Returns the current values of both the reference and the mark.

Returns the current value of the reference.

Returns the current value of the mark.

Unconditionally sets the value of both the reference and mark.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AtomicMarkableReference

```java
public AtomicMarkableReference​(
V
initialRef,
boolean initialMark)
```

Creates a new

AtomicMarkableReference

with the given
initial values.

**Parameters:** initialRef

- the initial reference
**Parameters:** initialMark

- the initial mark

============ METHOD DETAIL ==========

- Method Detail

- getReference

```java
public
V
getReference()
```

Returns the current value of the reference.

**Returns:** the current value of the reference

- isMarked

```java
public boolean isMarked()
```

Returns the current value of the mark.

**Returns:** the current value of the mark

- get

```java
public
V
get​(boolean[] markHolder)
```

Returns the current values of both the reference and the mark.
Typical usage is

boolean[1] holder; ref = v.get(holder);

.

**Parameters:** markHolder

- an array of size of at least one. On return,

markHolder[0]

will hold the value of the mark.
**Returns:** the current value of the reference

- weakCompareAndSet

```java
public boolean weakCompareAndSet​(
V
expectedReference,

V
newReference,
boolean expectedMark,
boolean newMark)
```

Atomically sets the value of both the reference and mark
to the given update values if the
current reference is

==

to the expected reference
and the current mark is equal to the expected mark.

May fail
spuriously and does not provide ordering guarantees

, so is
only rarely an appropriate alternative to

compareAndSet

.

**Parameters:** expectedReference

- the expected value of the reference
**Parameters:** newReference

- the new value for the reference
**Parameters:** expectedMark

- the expected value of the mark
**Parameters:** newMark

- the new value for the mark
**Returns:** true

if successful

- compareAndSet

```java
public boolean compareAndSet​(
V
expectedReference,

V
newReference,
boolean expectedMark,
boolean newMark)
```

Atomically sets the value of both the reference and mark
to the given update values if the
current reference is

==

to the expected reference
and the current mark is equal to the expected mark.

**Parameters:** expectedReference

- the expected value of the reference
**Parameters:** newReference

- the new value for the reference
**Parameters:** expectedMark

- the expected value of the mark
**Parameters:** newMark

- the new value for the mark
**Returns:** true

if successful

- set

```java
public void set​(
V
newReference,
boolean newMark)
```

Unconditionally sets the value of both the reference and mark.

**Parameters:** newReference

- the new value for the reference
**Parameters:** newMark

- the new value for the mark

- attemptMark

```java
public boolean attemptMark​(
V
expectedReference,
boolean newMark)
```

Atomically sets the value of the mark to the given update value
if the current reference is

==

to the expected
reference. Any given invocation of this operation may fail
(return

false

) spuriously, but repeated invocation
when the current value holds the expected value and no other
thread is also attempting to set the value will eventually
succeed.

**Parameters:** expectedReference

- the expected value of the reference
**Parameters:** newMark

- the new value for the mark
**Returns:** true

if successful

Constructor Detail

- AtomicMarkableReference

```java
public AtomicMarkableReference​(
V
initialRef,
boolean initialMark)
```

Creates a new

AtomicMarkableReference

with the given
initial values.

**Parameters:** initialRef

- the initial reference
**Parameters:** initialMark

- the initial mark

---

#### Constructor Detail

AtomicMarkableReference

```java
public AtomicMarkableReference​(
V
initialRef,
boolean initialMark)
```

Creates a new

AtomicMarkableReference

with the given
initial values.

**Parameters:** initialRef

- the initial reference
**Parameters:** initialMark

- the initial mark

---

#### AtomicMarkableReference

public AtomicMarkableReference​(

V

initialRef,
boolean initialMark)

Creates a new

AtomicMarkableReference

with the given
initial values.

Method Detail

- getReference

```java
public
V
getReference()
```

Returns the current value of the reference.

**Returns:** the current value of the reference

- isMarked

```java
public boolean isMarked()
```

Returns the current value of the mark.

**Returns:** the current value of the mark

- get

```java
public
V
get​(boolean[] markHolder)
```

Returns the current values of both the reference and the mark.
Typical usage is

boolean[1] holder; ref = v.get(holder);

.

**Parameters:** markHolder

- an array of size of at least one. On return,

markHolder[0]

will hold the value of the mark.
**Returns:** the current value of the reference

- weakCompareAndSet

```java
public boolean weakCompareAndSet​(
V
expectedReference,

V
newReference,
boolean expectedMark,
boolean newMark)
```

Atomically sets the value of both the reference and mark
to the given update values if the
current reference is

==

to the expected reference
and the current mark is equal to the expected mark.

May fail
spuriously and does not provide ordering guarantees

, so is
only rarely an appropriate alternative to

compareAndSet

.

**Parameters:** expectedReference

- the expected value of the reference
**Parameters:** newReference

- the new value for the reference
**Parameters:** expectedMark

- the expected value of the mark
**Parameters:** newMark

- the new value for the mark
**Returns:** true

if successful

- compareAndSet

```java
public boolean compareAndSet​(
V
expectedReference,

V
newReference,
boolean expectedMark,
boolean newMark)
```

Atomically sets the value of both the reference and mark
to the given update values if the
current reference is

==

to the expected reference
and the current mark is equal to the expected mark.

**Parameters:** expectedReference

- the expected value of the reference
**Parameters:** newReference

- the new value for the reference
**Parameters:** expectedMark

- the expected value of the mark
**Parameters:** newMark

- the new value for the mark
**Returns:** true

if successful

- set

```java
public void set​(
V
newReference,
boolean newMark)
```

Unconditionally sets the value of both the reference and mark.

**Parameters:** newReference

- the new value for the reference
**Parameters:** newMark

- the new value for the mark

- attemptMark

```java
public boolean attemptMark​(
V
expectedReference,
boolean newMark)
```

Atomically sets the value of the mark to the given update value
if the current reference is

==

to the expected
reference. Any given invocation of this operation may fail
(return

false

) spuriously, but repeated invocation
when the current value holds the expected value and no other
thread is also attempting to set the value will eventually
succeed.

**Parameters:** expectedReference

- the expected value of the reference
**Parameters:** newMark

- the new value for the mark
**Returns:** true

if successful

---

#### Method Detail

getReference

```java
public
V
getReference()
```

Returns the current value of the reference.

**Returns:** the current value of the reference

---

#### getReference

public

V

getReference()

Returns the current value of the reference.

isMarked

```java
public boolean isMarked()
```

Returns the current value of the mark.

**Returns:** the current value of the mark

---

#### isMarked

public boolean isMarked()

Returns the current value of the mark.

get

```java
public
V
get​(boolean[] markHolder)
```

Returns the current values of both the reference and the mark.
Typical usage is

boolean[1] holder; ref = v.get(holder);

.

**Parameters:** markHolder

- an array of size of at least one. On return,

markHolder[0]

will hold the value of the mark.
**Returns:** the current value of the reference

---

#### get

public

V

get​(boolean[] markHolder)

Returns the current values of both the reference and the mark.
Typical usage is

boolean[1] holder; ref = v.get(holder);

.

weakCompareAndSet

```java
public boolean weakCompareAndSet​(
V
expectedReference,

V
newReference,
boolean expectedMark,
boolean newMark)
```

Atomically sets the value of both the reference and mark
to the given update values if the
current reference is

==

to the expected reference
and the current mark is equal to the expected mark.

May fail
spuriously and does not provide ordering guarantees

, so is
only rarely an appropriate alternative to

compareAndSet

.

**Parameters:** expectedReference

- the expected value of the reference
**Parameters:** newReference

- the new value for the reference
**Parameters:** expectedMark

- the expected value of the mark
**Parameters:** newMark

- the new value for the mark
**Returns:** true

if successful

---

#### weakCompareAndSet

public boolean weakCompareAndSet​(

V

expectedReference,

V

newReference,
boolean expectedMark,
boolean newMark)

Atomically sets the value of both the reference and mark
to the given update values if the
current reference is

==

to the expected reference
and the current mark is equal to the expected mark.

May fail
spuriously and does not provide ordering guarantees

, so is
only rarely an appropriate alternative to

compareAndSet

.

May fail
spuriously and does not provide ordering guarantees

, so is
only rarely an appropriate alternative to

compareAndSet

.

compareAndSet

```java
public boolean compareAndSet​(
V
expectedReference,

V
newReference,
boolean expectedMark,
boolean newMark)
```

Atomically sets the value of both the reference and mark
to the given update values if the
current reference is

==

to the expected reference
and the current mark is equal to the expected mark.

**Parameters:** expectedReference

- the expected value of the reference
**Parameters:** newReference

- the new value for the reference
**Parameters:** expectedMark

- the expected value of the mark
**Parameters:** newMark

- the new value for the mark
**Returns:** true

if successful

---

#### compareAndSet

public boolean compareAndSet​(

V

expectedReference,

V

newReference,
boolean expectedMark,
boolean newMark)

Atomically sets the value of both the reference and mark
to the given update values if the
current reference is

==

to the expected reference
and the current mark is equal to the expected mark.

set

```java
public void set​(
V
newReference,
boolean newMark)
```

Unconditionally sets the value of both the reference and mark.

**Parameters:** newReference

- the new value for the reference
**Parameters:** newMark

- the new value for the mark

---

#### set

public void set​(

V

newReference,
boolean newMark)

Unconditionally sets the value of both the reference and mark.

attemptMark

```java
public boolean attemptMark​(
V
expectedReference,
boolean newMark)
```

Atomically sets the value of the mark to the given update value
if the current reference is

==

to the expected
reference. Any given invocation of this operation may fail
(return

false

) spuriously, but repeated invocation
when the current value holds the expected value and no other
thread is also attempting to set the value will eventually
succeed.

**Parameters:** expectedReference

- the expected value of the reference
**Parameters:** newMark

- the new value for the mark
**Returns:** true

if successful

---

#### attemptMark

public boolean attemptMark​(

V

expectedReference,
boolean newMark)

Atomically sets the value of the mark to the given update value
if the current reference is

==

to the expected
reference. Any given invocation of this operation may fail
(return

false

) spuriously, but repeated invocation
when the current value holds the expected value and no other
thread is also attempting to set the value will eventually
succeed.

---

