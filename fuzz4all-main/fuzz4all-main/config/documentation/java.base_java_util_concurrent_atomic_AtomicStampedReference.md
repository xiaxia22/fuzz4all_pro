# Class AtomicStampedReference<V>

**Source:** `java.base\java\util\concurrent\atomic\AtomicStampedReference.html`

### Class Description

```java
public class
AtomicStampedReference<V>

extends
Object
```

An

AtomicStampedReference

maintains an object reference
along with an integer "stamp", that can be updated atomically.

Implementation note: This implementation maintains stamped
references by creating internal objects representing "boxed"
[reference, integer] pairs.

**Type Parameters:** V

- The type of object referred to by this reference

---

### Field Details

*No entries found.*

### Constructor Details

#### public AtomicStampedReference​(
V
initialRef,
int initialStamp)

Creates a new

AtomicStampedReference

with the given
initial values.

**Parameters:**
- initialRef

- the initial reference
- initialStamp

- the initial stamp

---

### Method Details

#### public
V
getReference()

Returns the current value of the reference.

**Returns:**
- the current value of the reference

---

#### public int getStamp()

Returns the current value of the stamp.

**Returns:**
- the current value of the stamp

---

#### public
V
get​(int[] stampHolder)

Returns the current values of both the reference and the stamp.
Typical usage is

int[1] holder; ref = v.get(holder);

.

**Parameters:**
- stampHolder

- an array of size of at least one. On return,

stampHolder[0]

will hold the value of the stamp.

**Returns:**
- the current value of the reference

---

#### public boolean weakCompareAndSet​(
V
expectedReference,

V
newReference,
int expectedStamp,
int newStamp)

Atomically sets the value of both the reference and stamp
to the given update values if the
current reference is

==

to the expected reference
and the current stamp is equal to the expected stamp.

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
- expectedStamp

- the expected value of the stamp
- newStamp

- the new value for the stamp

**Returns:**
- true

if successful

---

#### public boolean compareAndSet​(
V
expectedReference,

V
newReference,
int expectedStamp,
int newStamp)

Atomically sets the value of both the reference and stamp
to the given update values if the
current reference is

==

to the expected reference
and the current stamp is equal to the expected stamp.

**Parameters:**
- expectedReference

- the expected value of the reference
- newReference

- the new value for the reference
- expectedStamp

- the expected value of the stamp
- newStamp

- the new value for the stamp

**Returns:**
- true

if successful

---

#### public void set​(
V
newReference,
int newStamp)

Unconditionally sets the value of both the reference and stamp.

**Parameters:**
- newReference

- the new value for the reference
- newStamp

- the new value for the stamp

---

#### public boolean attemptStamp​(
V
expectedReference,
int newStamp)

Atomically sets the value of the stamp to the given update value
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
- newStamp

- the new value for the stamp

**Returns:**
- true

if successful

---

### Additional Sections

#### Class AtomicStampedReference<V>

java.lang.Object

- java.util.concurrent.atomic.AtomicStampedReference<V>

java.util.concurrent.atomic.AtomicStampedReference<V>

**Type Parameters:** V

- The type of object referred to by this reference

```java
public class
AtomicStampedReference<V>

extends
Object
```

An

AtomicStampedReference

maintains an object reference
along with an integer "stamp", that can be updated atomically.

Implementation note: This implementation maintains stamped
references by creating internal objects representing "boxed"
[reference, integer] pairs.

**Since:** 1.5

public class

AtomicStampedReference<V>

extends

Object

An

AtomicStampedReference

maintains an object reference
along with an integer "stamp", that can be updated atomically.

Implementation note: This implementation maintains stamped
references by creating internal objects representing "boxed"
[reference, integer] pairs.

Implementation note: This implementation maintains stamped
references by creating internal objects representing "boxed"
[reference, integer] pairs.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AtomicStampedReference

​(

V

initialRef,
int initialStamp)

Creates a new

AtomicStampedReference

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

attemptStamp

​(

V

expectedReference,
int newStamp)

Atomically sets the value of the stamp to the given update value
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
int expectedStamp,
int newStamp)

Atomically sets the value of both the reference and stamp
to the given update values if the
current reference is

==

to the expected reference
and the current stamp is equal to the expected stamp.

V

get

​(int[] stampHolder)

Returns the current values of both the reference and the stamp.

V

getReference

()

Returns the current value of the reference.

int

getStamp

()

Returns the current value of the stamp.

void

set

​(

V

newReference,
int newStamp)

Unconditionally sets the value of both the reference and stamp.

boolean

weakCompareAndSet

​(

V

expectedReference,

V

newReference,
int expectedStamp,
int newStamp)

Atomically sets the value of both the reference and stamp
to the given update values if the
current reference is

==

to the expected reference
and the current stamp is equal to the expected stamp.

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

AtomicStampedReference

​(

V

initialRef,
int initialStamp)

Creates a new

AtomicStampedReference

with the given
initial values.

---

#### Constructor Summary

Creates a new

AtomicStampedReference

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

attemptStamp

​(

V

expectedReference,
int newStamp)

Atomically sets the value of the stamp to the given update value
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
int expectedStamp,
int newStamp)

Atomically sets the value of both the reference and stamp
to the given update values if the
current reference is

==

to the expected reference
and the current stamp is equal to the expected stamp.

V

get

​(int[] stampHolder)

Returns the current values of both the reference and the stamp.

V

getReference

()

Returns the current value of the reference.

int

getStamp

()

Returns the current value of the stamp.

void

set

​(

V

newReference,
int newStamp)

Unconditionally sets the value of both the reference and stamp.

boolean

weakCompareAndSet

​(

V

expectedReference,

V

newReference,
int expectedStamp,
int newStamp)

Atomically sets the value of both the reference and stamp
to the given update values if the
current reference is

==

to the expected reference
and the current stamp is equal to the expected stamp.

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

Atomically sets the value of the stamp to the given update value
if the current reference is

==

to the expected
reference.

Atomically sets the value of both the reference and stamp
to the given update values if the
current reference is

==

to the expected reference
and the current stamp is equal to the expected stamp.

Returns the current values of both the reference and the stamp.

Returns the current value of the reference.

Returns the current value of the stamp.

Unconditionally sets the value of both the reference and stamp.

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

- AtomicStampedReference

```java
public AtomicStampedReference​(
V
initialRef,
int initialStamp)
```

Creates a new

AtomicStampedReference

with the given
initial values.

**Parameters:** initialRef

- the initial reference
**Parameters:** initialStamp

- the initial stamp

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

- getStamp

```java
public int getStamp()
```

Returns the current value of the stamp.

**Returns:** the current value of the stamp

- get

```java
public
V
get​(int[] stampHolder)
```

Returns the current values of both the reference and the stamp.
Typical usage is

int[1] holder; ref = v.get(holder);

.

**Parameters:** stampHolder

- an array of size of at least one. On return,

stampHolder[0]

will hold the value of the stamp.
**Returns:** the current value of the reference

- weakCompareAndSet

```java
public boolean weakCompareAndSet​(
V
expectedReference,

V
newReference,
int expectedStamp,
int newStamp)
```

Atomically sets the value of both the reference and stamp
to the given update values if the
current reference is

==

to the expected reference
and the current stamp is equal to the expected stamp.

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
**Parameters:** expectedStamp

- the expected value of the stamp
**Parameters:** newStamp

- the new value for the stamp
**Returns:** true

if successful

- compareAndSet

```java
public boolean compareAndSet​(
V
expectedReference,

V
newReference,
int expectedStamp,
int newStamp)
```

Atomically sets the value of both the reference and stamp
to the given update values if the
current reference is

==

to the expected reference
and the current stamp is equal to the expected stamp.

**Parameters:** expectedReference

- the expected value of the reference
**Parameters:** newReference

- the new value for the reference
**Parameters:** expectedStamp

- the expected value of the stamp
**Parameters:** newStamp

- the new value for the stamp
**Returns:** true

if successful

- set

```java
public void set​(
V
newReference,
int newStamp)
```

Unconditionally sets the value of both the reference and stamp.

**Parameters:** newReference

- the new value for the reference
**Parameters:** newStamp

- the new value for the stamp

- attemptStamp

```java
public boolean attemptStamp​(
V
expectedReference,
int newStamp)
```

Atomically sets the value of the stamp to the given update value
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
**Parameters:** newStamp

- the new value for the stamp
**Returns:** true

if successful

Constructor Detail

- AtomicStampedReference

```java
public AtomicStampedReference​(
V
initialRef,
int initialStamp)
```

Creates a new

AtomicStampedReference

with the given
initial values.

**Parameters:** initialRef

- the initial reference
**Parameters:** initialStamp

- the initial stamp

---

#### Constructor Detail

AtomicStampedReference

```java
public AtomicStampedReference​(
V
initialRef,
int initialStamp)
```

Creates a new

AtomicStampedReference

with the given
initial values.

**Parameters:** initialRef

- the initial reference
**Parameters:** initialStamp

- the initial stamp

---

#### AtomicStampedReference

public AtomicStampedReference​(

V

initialRef,
int initialStamp)

Creates a new

AtomicStampedReference

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

- getStamp

```java
public int getStamp()
```

Returns the current value of the stamp.

**Returns:** the current value of the stamp

- get

```java
public
V
get​(int[] stampHolder)
```

Returns the current values of both the reference and the stamp.
Typical usage is

int[1] holder; ref = v.get(holder);

.

**Parameters:** stampHolder

- an array of size of at least one. On return,

stampHolder[0]

will hold the value of the stamp.
**Returns:** the current value of the reference

- weakCompareAndSet

```java
public boolean weakCompareAndSet​(
V
expectedReference,

V
newReference,
int expectedStamp,
int newStamp)
```

Atomically sets the value of both the reference and stamp
to the given update values if the
current reference is

==

to the expected reference
and the current stamp is equal to the expected stamp.

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
**Parameters:** expectedStamp

- the expected value of the stamp
**Parameters:** newStamp

- the new value for the stamp
**Returns:** true

if successful

- compareAndSet

```java
public boolean compareAndSet​(
V
expectedReference,

V
newReference,
int expectedStamp,
int newStamp)
```

Atomically sets the value of both the reference and stamp
to the given update values if the
current reference is

==

to the expected reference
and the current stamp is equal to the expected stamp.

**Parameters:** expectedReference

- the expected value of the reference
**Parameters:** newReference

- the new value for the reference
**Parameters:** expectedStamp

- the expected value of the stamp
**Parameters:** newStamp

- the new value for the stamp
**Returns:** true

if successful

- set

```java
public void set​(
V
newReference,
int newStamp)
```

Unconditionally sets the value of both the reference and stamp.

**Parameters:** newReference

- the new value for the reference
**Parameters:** newStamp

- the new value for the stamp

- attemptStamp

```java
public boolean attemptStamp​(
V
expectedReference,
int newStamp)
```

Atomically sets the value of the stamp to the given update value
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
**Parameters:** newStamp

- the new value for the stamp
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

getStamp

```java
public int getStamp()
```

Returns the current value of the stamp.

**Returns:** the current value of the stamp

---

#### getStamp

public int getStamp()

Returns the current value of the stamp.

get

```java
public
V
get​(int[] stampHolder)
```

Returns the current values of both the reference and the stamp.
Typical usage is

int[1] holder; ref = v.get(holder);

.

**Parameters:** stampHolder

- an array of size of at least one. On return,

stampHolder[0]

will hold the value of the stamp.
**Returns:** the current value of the reference

---

#### get

public

V

get​(int[] stampHolder)

Returns the current values of both the reference and the stamp.
Typical usage is

int[1] holder; ref = v.get(holder);

.

weakCompareAndSet

```java
public boolean weakCompareAndSet​(
V
expectedReference,

V
newReference,
int expectedStamp,
int newStamp)
```

Atomically sets the value of both the reference and stamp
to the given update values if the
current reference is

==

to the expected reference
and the current stamp is equal to the expected stamp.

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
**Parameters:** expectedStamp

- the expected value of the stamp
**Parameters:** newStamp

- the new value for the stamp
**Returns:** true

if successful

---

#### weakCompareAndSet

public boolean weakCompareAndSet​(

V

expectedReference,

V

newReference,
int expectedStamp,
int newStamp)

Atomically sets the value of both the reference and stamp
to the given update values if the
current reference is

==

to the expected reference
and the current stamp is equal to the expected stamp.

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
int expectedStamp,
int newStamp)
```

Atomically sets the value of both the reference and stamp
to the given update values if the
current reference is

==

to the expected reference
and the current stamp is equal to the expected stamp.

**Parameters:** expectedReference

- the expected value of the reference
**Parameters:** newReference

- the new value for the reference
**Parameters:** expectedStamp

- the expected value of the stamp
**Parameters:** newStamp

- the new value for the stamp
**Returns:** true

if successful

---

#### compareAndSet

public boolean compareAndSet​(

V

expectedReference,

V

newReference,
int expectedStamp,
int newStamp)

Atomically sets the value of both the reference and stamp
to the given update values if the
current reference is

==

to the expected reference
and the current stamp is equal to the expected stamp.

set

```java
public void set​(
V
newReference,
int newStamp)
```

Unconditionally sets the value of both the reference and stamp.

**Parameters:** newReference

- the new value for the reference
**Parameters:** newStamp

- the new value for the stamp

---

#### set

public void set​(

V

newReference,
int newStamp)

Unconditionally sets the value of both the reference and stamp.

attemptStamp

```java
public boolean attemptStamp​(
V
expectedReference,
int newStamp)
```

Atomically sets the value of the stamp to the given update value
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
**Parameters:** newStamp

- the new value for the stamp
**Returns:** true

if successful

---

#### attemptStamp

public boolean attemptStamp​(

V

expectedReference,
int newStamp)

Atomically sets the value of the stamp to the given update value
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

