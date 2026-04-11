# Class MonitorInfo

**Source:** `java.management\java\lang\management\MonitorInfo.html`

### Class Description

```java
public class
MonitorInfo

extends
LockInfo
```

Information about an object monitor lock. An object monitor is locked
when entering a synchronization block or method on that object.

MXBean Mapping

MonitorInfo

is mapped to a

CompositeData

with attributes as specified in
the

from

method.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### public MonitorInfo​(
String
className,
int identityHashCode,
int stackDepth,

StackTraceElement
stackFrame)

Construct a

MonitorInfo

object.

**Parameters:**
- className

- the fully qualified name of the class of the lock object.
- identityHashCode

- the

identity hash code

of the lock object.
- stackDepth

- the depth in the stack trace where the object monitor
was locked.
- stackFrame

- the stack frame that locked the object monitor.

**Throws:**
- IllegalArgumentException

- if

stackDepth

≥ 0 but

stackFrame

is

null

,
or

stackDepth

< 0 but

stackFrame

is not

null

.

---

### Method Details

#### public int getLockedStackDepth()

Returns the depth in the stack trace where the object monitor
was locked. The depth is the index to the

StackTraceElement

array returned in the

ThreadInfo.getStackTrace()

method.

**Returns:**
- the depth in the stack trace where the object monitor
was locked, or a negative number if not available.

---

#### public
StackTraceElement
getLockedStackFrame()

Returns the stack frame that locked the object monitor.

**Returns:**
- StackTraceElement

that locked the object monitor,
or

null

if not available.

---

#### public static
MonitorInfo
from​(
CompositeData
cd)

Returns a

MonitorInfo

object represented by the
given

CompositeData

.
The given

CompositeData

must contain the following attributes
as well as the attributes specified in the

mapped type

for the

LockInfo

class:

The attributes and their types the given CompositeData contains

Attribute Name

Type

lockedStackFrame

CompositeData

for

StackTraceElement

as specified
in

ThreadInfo.from(CompositeData)

method.

lockedStackDepth

java.lang.Integer

**Parameters:**
- cd

-

CompositeData

representing a

MonitorInfo

**Returns:**
- a

MonitorInfo

object represented
by

cd

if

cd

is not

null

;

null

otherwise.

**Throws:**
- IllegalArgumentException

- if

cd

does not
represent a

MonitorInfo

with the attributes described
above.

---

### Additional Sections

#### Class MonitorInfo

java.lang.Object

- java.lang.management.LockInfo
- - java.lang.management.MonitorInfo

java.lang.management.LockInfo

- java.lang.management.MonitorInfo

java.lang.management.MonitorInfo

```java
public class
MonitorInfo

extends
LockInfo
```

Information about an object monitor lock. An object monitor is locked
when entering a synchronization block or method on that object.

MXBean Mapping

MonitorInfo

is mapped to a

CompositeData

with attributes as specified in
the

from

method.

**Since:** 1.6

public class

MonitorInfo

extends

LockInfo

Information about an object monitor lock. An object monitor is locked
when entering a synchronization block or method on that object.

MXBean Mapping

MonitorInfo

is mapped to a

CompositeData

with attributes as specified in
the

from

method.

---

#### MXBean Mapping

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MonitorInfo

​(

String

className,
int identityHashCode,
int stackDepth,

StackTraceElement

stackFrame)

Construct a

MonitorInfo

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

MonitorInfo

from

​(

CompositeData

cd)

Returns a

MonitorInfo

object represented by the
given

CompositeData

.

int

getLockedStackDepth

()

Returns the depth in the stack trace where the object monitor
was locked.

StackTraceElement

getLockedStackFrame

()

Returns the stack frame that locked the object monitor.

- Methods declared in class java.lang.management.

LockInfo

getClassName

,

getIdentityHashCode

,

toString

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

Constructor Summary

Constructors

Constructor

Description

MonitorInfo

​(

String

className,
int identityHashCode,
int stackDepth,

StackTraceElement

stackFrame)

Construct a

MonitorInfo

object.

---

#### Constructor Summary

Construct a

MonitorInfo

object.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

MonitorInfo

from

​(

CompositeData

cd)

Returns a

MonitorInfo

object represented by the
given

CompositeData

.

int

getLockedStackDepth

()

Returns the depth in the stack trace where the object monitor
was locked.

StackTraceElement

getLockedStackFrame

()

Returns the stack frame that locked the object monitor.

- Methods declared in class java.lang.management.

LockInfo

getClassName

,

getIdentityHashCode

,

toString

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

Returns a

MonitorInfo

object represented by the
given

CompositeData

.

Returns the depth in the stack trace where the object monitor
was locked.

Returns the stack frame that locked the object monitor.

Methods declared in class java.lang.management.

LockInfo

getClassName

,

getIdentityHashCode

,

toString

---

#### Methods declared in class java.lang.management. LockInfo

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MonitorInfo

```java
public MonitorInfo​(
String
className,
int identityHashCode,
int stackDepth,

StackTraceElement
stackFrame)
```

Construct a

MonitorInfo

object.

**Parameters:** className

- the fully qualified name of the class of the lock object.
**Parameters:** identityHashCode

- the

identity hash code

of the lock object.
**Parameters:** stackDepth

- the depth in the stack trace where the object monitor
was locked.
**Parameters:** stackFrame

- the stack frame that locked the object monitor.
**Throws:** IllegalArgumentException

- if

stackDepth

≥ 0 but

stackFrame

is

null

,
or

stackDepth

< 0 but

stackFrame

is not

null

.

============ METHOD DETAIL ==========

- Method Detail

- getLockedStackDepth

```java
public int getLockedStackDepth()
```

Returns the depth in the stack trace where the object monitor
was locked. The depth is the index to the

StackTraceElement

array returned in the

ThreadInfo.getStackTrace()

method.

**Returns:** the depth in the stack trace where the object monitor
was locked, or a negative number if not available.

- getLockedStackFrame

```java
public
StackTraceElement
getLockedStackFrame()
```

Returns the stack frame that locked the object monitor.

**Returns:** StackTraceElement

that locked the object monitor,
or

null

if not available.

- from

```java
public static
MonitorInfo
from​(
CompositeData
cd)
```

Returns a

MonitorInfo

object represented by the
given

CompositeData

.
The given

CompositeData

must contain the following attributes
as well as the attributes specified in the

mapped type

for the

LockInfo

class:

The attributes and their types the given CompositeData contains

Attribute Name

Type

lockedStackFrame

CompositeData

for

StackTraceElement

as specified
in

ThreadInfo.from(CompositeData)

method.

lockedStackDepth

java.lang.Integer

**Parameters:** cd

-

CompositeData

representing a

MonitorInfo
**Returns:** a

MonitorInfo

object represented
by

cd

if

cd

is not

null

;

null

otherwise.
**Throws:** IllegalArgumentException

- if

cd

does not
represent a

MonitorInfo

with the attributes described
above.

Constructor Detail

- MonitorInfo

```java
public MonitorInfo​(
String
className,
int identityHashCode,
int stackDepth,

StackTraceElement
stackFrame)
```

Construct a

MonitorInfo

object.

**Parameters:** className

- the fully qualified name of the class of the lock object.
**Parameters:** identityHashCode

- the

identity hash code

of the lock object.
**Parameters:** stackDepth

- the depth in the stack trace where the object monitor
was locked.
**Parameters:** stackFrame

- the stack frame that locked the object monitor.
**Throws:** IllegalArgumentException

- if

stackDepth

≥ 0 but

stackFrame

is

null

,
or

stackDepth

< 0 but

stackFrame

is not

null

.

---

#### Constructor Detail

MonitorInfo

```java
public MonitorInfo​(
String
className,
int identityHashCode,
int stackDepth,

StackTraceElement
stackFrame)
```

Construct a

MonitorInfo

object.

**Parameters:** className

- the fully qualified name of the class of the lock object.
**Parameters:** identityHashCode

- the

identity hash code

of the lock object.
**Parameters:** stackDepth

- the depth in the stack trace where the object monitor
was locked.
**Parameters:** stackFrame

- the stack frame that locked the object monitor.
**Throws:** IllegalArgumentException

- if

stackDepth

≥ 0 but

stackFrame

is

null

,
or

stackDepth

< 0 but

stackFrame

is not

null

.

---

#### MonitorInfo

public MonitorInfo​(

String

className,
int identityHashCode,
int stackDepth,

StackTraceElement

stackFrame)

Construct a

MonitorInfo

object.

Method Detail

- getLockedStackDepth

```java
public int getLockedStackDepth()
```

Returns the depth in the stack trace where the object monitor
was locked. The depth is the index to the

StackTraceElement

array returned in the

ThreadInfo.getStackTrace()

method.

**Returns:** the depth in the stack trace where the object monitor
was locked, or a negative number if not available.

- getLockedStackFrame

```java
public
StackTraceElement
getLockedStackFrame()
```

Returns the stack frame that locked the object monitor.

**Returns:** StackTraceElement

that locked the object monitor,
or

null

if not available.

- from

```java
public static
MonitorInfo
from​(
CompositeData
cd)
```

Returns a

MonitorInfo

object represented by the
given

CompositeData

.
The given

CompositeData

must contain the following attributes
as well as the attributes specified in the

mapped type

for the

LockInfo

class:

The attributes and their types the given CompositeData contains

Attribute Name

Type

lockedStackFrame

CompositeData

for

StackTraceElement

as specified
in

ThreadInfo.from(CompositeData)

method.

lockedStackDepth

java.lang.Integer

**Parameters:** cd

-

CompositeData

representing a

MonitorInfo
**Returns:** a

MonitorInfo

object represented
by

cd

if

cd

is not

null

;

null

otherwise.
**Throws:** IllegalArgumentException

- if

cd

does not
represent a

MonitorInfo

with the attributes described
above.

---

#### Method Detail

getLockedStackDepth

```java
public int getLockedStackDepth()
```

Returns the depth in the stack trace where the object monitor
was locked. The depth is the index to the

StackTraceElement

array returned in the

ThreadInfo.getStackTrace()

method.

**Returns:** the depth in the stack trace where the object monitor
was locked, or a negative number if not available.

---

#### getLockedStackDepth

public int getLockedStackDepth()

Returns the depth in the stack trace where the object monitor
was locked. The depth is the index to the

StackTraceElement

array returned in the

ThreadInfo.getStackTrace()

method.

getLockedStackFrame

```java
public
StackTraceElement
getLockedStackFrame()
```

Returns the stack frame that locked the object monitor.

**Returns:** StackTraceElement

that locked the object monitor,
or

null

if not available.

---

#### getLockedStackFrame

public

StackTraceElement

getLockedStackFrame()

Returns the stack frame that locked the object monitor.

from

```java
public static
MonitorInfo
from​(
CompositeData
cd)
```

Returns a

MonitorInfo

object represented by the
given

CompositeData

.
The given

CompositeData

must contain the following attributes
as well as the attributes specified in the

mapped type

for the

LockInfo

class:

The attributes and their types the given CompositeData contains

Attribute Name

Type

lockedStackFrame

CompositeData

for

StackTraceElement

as specified
in

ThreadInfo.from(CompositeData)

method.

lockedStackDepth

java.lang.Integer

**Parameters:** cd

-

CompositeData

representing a

MonitorInfo
**Returns:** a

MonitorInfo

object represented
by

cd

if

cd

is not

null

;

null

otherwise.
**Throws:** IllegalArgumentException

- if

cd

does not
represent a

MonitorInfo

with the attributes described
above.

---

#### from

public static

MonitorInfo

from​(

CompositeData

cd)

Returns a

MonitorInfo

object represented by the
given

CompositeData

.
The given

CompositeData

must contain the following attributes
as well as the attributes specified in the

mapped type

for the

LockInfo

class:

The attributes and their types the given CompositeData contains

Attribute Name

Type

lockedStackFrame

CompositeData

for

StackTraceElement

as specified
in

ThreadInfo.from(CompositeData)

method.

lockedStackDepth

java.lang.Integer

---

