# Class LockInfo

**Source:** `java.management\java\lang\management\LockInfo.html`

### Class Description

```java
public class
LockInfo

extends
Object
```

Information about a

lock

. A lock can be a built-in object monitor,
an

ownable synchronizer

, or the

Condition

object associated with synchronizers.

An ownable synchronizer

is
a synchronizer that may be exclusively owned by a thread and uses

AbstractOwnableSynchronizer

(or its subclass) to implement its synchronization property.

ReentrantLock

and the write-lock (but not
the read-lock) of

ReentrantReadWriteLock

are
two examples of ownable synchronizers provided by the platform.

MXBean Mapping

LockInfo

is mapped to a

CompositeData

as specified in the

from

method.

**Direct Known Subclasses:** MonitorInfo

---

### Field Details

*No entries found.*

### Constructor Details

#### public LockInfo​(
String
className,
int identityHashCode)

Constructs a

LockInfo

object.

**Parameters:**
- className

- the fully qualified name of the class of the lock object.
- identityHashCode

- the

identity hash code

of the lock object.

---

### Method Details

#### public
String
getClassName()

Returns the fully qualified name of the class of the lock object.

**Returns:**
- the fully qualified name of the class of the lock object.

---

#### public int getIdentityHashCode()

Returns the identity hash code of the lock object
returned from the

System.identityHashCode(java.lang.Object)

method.

**Returns:**
- the identity hash code of the lock object.

---

#### public static
LockInfo
from​(
CompositeData
cd)

Returns a

LockInfo

object represented by the
given

CompositeData

.
The given

CompositeData

must contain the following attributes:

The attributes and the types the given CompositeData contains

Attribute Name

Type

className

java.lang.String

identityHashCode

java.lang.Integer

**Parameters:**
- cd

-

CompositeData

representing a

LockInfo

**Returns:**
- a

LockInfo

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

LockInfo

with the attributes described
above.

**Since:**
- 1.8

---

#### public
String
toString()

Returns a string representation of a lock. The returned
string representation consists of the name of the class of the
lock object, the at-sign character `@', and the unsigned
hexadecimal representation of the

identity

hash code
of the object. This method returns a string equals to the value of:

```java
lock.getClass().getName() + '@' + Integer.toHexString(System.identityHashCode(lock))
```

where

lock

is the lock object.

**Overrides:**
- toString

in class

Object

**Returns:**
- the string representation of a lock.

---

### Additional Sections

#### Class LockInfo

java.lang.Object

- java.lang.management.LockInfo

java.lang.management.LockInfo

**Direct Known Subclasses:** MonitorInfo

```java
public class
LockInfo

extends
Object
```

Information about a

lock

. A lock can be a built-in object monitor,
an

ownable synchronizer

, or the

Condition

object associated with synchronizers.

An ownable synchronizer

is
a synchronizer that may be exclusively owned by a thread and uses

AbstractOwnableSynchronizer

(or its subclass) to implement its synchronization property.

ReentrantLock

and the write-lock (but not
the read-lock) of

ReentrantReadWriteLock

are
two examples of ownable synchronizers provided by the platform.

MXBean Mapping

LockInfo

is mapped to a

CompositeData

as specified in the

from

method.

**Since:** 1.6
**See Also:** AbstractOwnableSynchronizer

,

Condition

public class

LockInfo

extends

Object

Information about a

lock

. A lock can be a built-in object monitor,
an

ownable synchronizer

, or the

Condition

object associated with synchronizers.

An ownable synchronizer

is
a synchronizer that may be exclusively owned by a thread and uses

AbstractOwnableSynchronizer

(or its subclass) to implement its synchronization property.

ReentrantLock

and the write-lock (but not
the read-lock) of

ReentrantReadWriteLock

are
two examples of ownable synchronizers provided by the platform.

MXBean Mapping

LockInfo

is mapped to a

CompositeData

as specified in the

from

method.

An ownable synchronizer

is
a synchronizer that may be exclusively owned by a thread and uses

AbstractOwnableSynchronizer

(or its subclass) to implement its synchronization property.

ReentrantLock

and the write-lock (but not
the read-lock) of

ReentrantReadWriteLock

are
two examples of ownable synchronizers provided by the platform.

MXBean Mapping

LockInfo

is mapped to a

CompositeData

as specified in the

from

method.

---

#### MXBean Mapping

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LockInfo

​(

String

className,
int identityHashCode)

Constructs a

LockInfo

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

LockInfo

from

​(

CompositeData

cd)

Returns a

LockInfo

object represented by the
given

CompositeData

.

String

getClassName

()

Returns the fully qualified name of the class of the lock object.

int

getIdentityHashCode

()

Returns the identity hash code of the lock object
returned from the

System.identityHashCode(java.lang.Object)

method.

String

toString

()

Returns a string representation of a lock.

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

LockInfo

​(

String

className,
int identityHashCode)

Constructs a

LockInfo

object.

---

#### Constructor Summary

Constructs a

LockInfo

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

LockInfo

from

​(

CompositeData

cd)

Returns a

LockInfo

object represented by the
given

CompositeData

.

String

getClassName

()

Returns the fully qualified name of the class of the lock object.

int

getIdentityHashCode

()

Returns the identity hash code of the lock object
returned from the

System.identityHashCode(java.lang.Object)

method.

String

toString

()

Returns a string representation of a lock.

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

LockInfo

object represented by the
given

CompositeData

.

Returns the fully qualified name of the class of the lock object.

Returns the identity hash code of the lock object
returned from the

System.identityHashCode(java.lang.Object)

method.

Returns a string representation of a lock.

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

- LockInfo

```java
public LockInfo​(
String
className,
int identityHashCode)
```

Constructs a

LockInfo

object.

**Parameters:** className

- the fully qualified name of the class of the lock object.
**Parameters:** identityHashCode

- the

identity hash code

of the lock object.

============ METHOD DETAIL ==========

- Method Detail

- getClassName

```java
public
String
getClassName()
```

Returns the fully qualified name of the class of the lock object.

**Returns:** the fully qualified name of the class of the lock object.

- getIdentityHashCode

```java
public int getIdentityHashCode()
```

Returns the identity hash code of the lock object
returned from the

System.identityHashCode(java.lang.Object)

method.

**Returns:** the identity hash code of the lock object.

- from

```java
public static
LockInfo
from​(
CompositeData
cd)
```

Returns a

LockInfo

object represented by the
given

CompositeData

.
The given

CompositeData

must contain the following attributes:

The attributes and the types the given CompositeData contains

Attribute Name

Type

className

java.lang.String

identityHashCode

java.lang.Integer

**Parameters:** cd

-

CompositeData

representing a

LockInfo
**Returns:** a

LockInfo

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

LockInfo

with the attributes described
above.
**Since:** 1.8

- toString

```java
public
String
toString()
```

Returns a string representation of a lock. The returned
string representation consists of the name of the class of the
lock object, the at-sign character `@', and the unsigned
hexadecimal representation of the

identity

hash code
of the object. This method returns a string equals to the value of:

```java
lock.getClass().getName() + '@' + Integer.toHexString(System.identityHashCode(lock))
```

where

lock

is the lock object.

**Overrides:** toString

in class

Object
**Returns:** the string representation of a lock.

Constructor Detail

- LockInfo

```java
public LockInfo​(
String
className,
int identityHashCode)
```

Constructs a

LockInfo

object.

**Parameters:** className

- the fully qualified name of the class of the lock object.
**Parameters:** identityHashCode

- the

identity hash code

of the lock object.

---

#### Constructor Detail

LockInfo

```java
public LockInfo​(
String
className,
int identityHashCode)
```

Constructs a

LockInfo

object.

**Parameters:** className

- the fully qualified name of the class of the lock object.
**Parameters:** identityHashCode

- the

identity hash code

of the lock object.

---

#### LockInfo

public LockInfo​(

String

className,
int identityHashCode)

Constructs a

LockInfo

object.

Method Detail

- getClassName

```java
public
String
getClassName()
```

Returns the fully qualified name of the class of the lock object.

**Returns:** the fully qualified name of the class of the lock object.

- getIdentityHashCode

```java
public int getIdentityHashCode()
```

Returns the identity hash code of the lock object
returned from the

System.identityHashCode(java.lang.Object)

method.

**Returns:** the identity hash code of the lock object.

- from

```java
public static
LockInfo
from​(
CompositeData
cd)
```

Returns a

LockInfo

object represented by the
given

CompositeData

.
The given

CompositeData

must contain the following attributes:

The attributes and the types the given CompositeData contains

Attribute Name

Type

className

java.lang.String

identityHashCode

java.lang.Integer

**Parameters:** cd

-

CompositeData

representing a

LockInfo
**Returns:** a

LockInfo

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

LockInfo

with the attributes described
above.
**Since:** 1.8

- toString

```java
public
String
toString()
```

Returns a string representation of a lock. The returned
string representation consists of the name of the class of the
lock object, the at-sign character `@', and the unsigned
hexadecimal representation of the

identity

hash code
of the object. This method returns a string equals to the value of:

```java
lock.getClass().getName() + '@' + Integer.toHexString(System.identityHashCode(lock))
```

where

lock

is the lock object.

**Overrides:** toString

in class

Object
**Returns:** the string representation of a lock.

---

#### Method Detail

getClassName

```java
public
String
getClassName()
```

Returns the fully qualified name of the class of the lock object.

**Returns:** the fully qualified name of the class of the lock object.

---

#### getClassName

public

String

getClassName()

Returns the fully qualified name of the class of the lock object.

getIdentityHashCode

```java
public int getIdentityHashCode()
```

Returns the identity hash code of the lock object
returned from the

System.identityHashCode(java.lang.Object)

method.

**Returns:** the identity hash code of the lock object.

---

#### getIdentityHashCode

public int getIdentityHashCode()

Returns the identity hash code of the lock object
returned from the

System.identityHashCode(java.lang.Object)

method.

from

```java
public static
LockInfo
from​(
CompositeData
cd)
```

Returns a

LockInfo

object represented by the
given

CompositeData

.
The given

CompositeData

must contain the following attributes:

The attributes and the types the given CompositeData contains

Attribute Name

Type

className

java.lang.String

identityHashCode

java.lang.Integer

**Parameters:** cd

-

CompositeData

representing a

LockInfo
**Returns:** a

LockInfo

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

LockInfo

with the attributes described
above.
**Since:** 1.8

---

#### from

public static

LockInfo

from​(

CompositeData

cd)

Returns a

LockInfo

object represented by the
given

CompositeData

.
The given

CompositeData

must contain the following attributes:

The attributes and the types the given CompositeData contains

Attribute Name

Type

className

java.lang.String

identityHashCode

java.lang.Integer

toString

```java
public
String
toString()
```

Returns a string representation of a lock. The returned
string representation consists of the name of the class of the
lock object, the at-sign character `@', and the unsigned
hexadecimal representation of the

identity

hash code
of the object. This method returns a string equals to the value of:

```java
lock.getClass().getName() + '@' + Integer.toHexString(System.identityHashCode(lock))
```

where

lock

is the lock object.

**Overrides:** toString

in class

Object
**Returns:** the string representation of a lock.

---

#### toString

public

String

toString()

Returns a string representation of a lock. The returned
string representation consists of the name of the class of the
lock object, the at-sign character `@', and the unsigned
hexadecimal representation of the

identity

hash code
of the object. This method returns a string equals to the value of:

```java
lock.getClass().getName() + '@' + Integer.toHexString(System.identityHashCode(lock))
```

where

lock

is the lock object.

lock.getClass().getName() + '@' + Integer.toHexString(System.identityHashCode(lock))

---

