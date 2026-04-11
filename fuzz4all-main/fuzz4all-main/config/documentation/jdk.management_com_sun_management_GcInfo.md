# Class GcInfo

**Source:** `jdk.management\com\sun\management\GcInfo.html`

### Class Description

```java
public class
GcInfo

extends
Object

implements
CompositeData
,
CompositeDataView
```

Garbage collection information. It contains the following
information for one garbage collection as well as GC-specific
attributes:

- Start time
- End time
- Duration
- Memory usage before the collection starts
- Memory usage after the collection ends

GcInfo

is a

CompositeData

The GC-specific attributes can be obtained via the CompositeData
interface. This is a historical relic, and other classes should
not copy this pattern. Use

CompositeDataView

instead.

MXBean Mapping

GcInfo

is mapped to a

CompositeData

with attributes as specified in the

from

method.

**All Implemented Interfaces:** CompositeData

,

CompositeDataView

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public long getId()

Returns the identifier of this garbage collection which is
the number of collections that this collector has done.

**Returns:**
- the identifier of this garbage collection which is
the number of collections that this collector has done.

---

#### public long getStartTime()

Returns the start time of this GC in milliseconds
since the Java virtual machine was started.

**Returns:**
- the start time of this GC.

---

#### public long getEndTime()

Returns the end time of this GC in milliseconds
since the Java virtual machine was started.

**Returns:**
- the end time of this GC.

---

#### public long getDuration()

Returns the elapsed time of this GC in milliseconds.

**Returns:**
- the elapsed time of this GC in milliseconds.

---

#### public
Map
<
String
,​
MemoryUsage
> getMemoryUsageBeforeGc()

Returns the memory usage of all memory pools
at the beginning of this GC.
This method returns
a

Map

of the name of a memory pool
to the memory usage of the corresponding
memory pool before GC starts.

**Returns:**
- a

Map

of memory pool names to the memory
usage of a memory pool before GC starts.

---

#### public
Map
<
String
,​
MemoryUsage
> getMemoryUsageAfterGc()

Returns the memory usage of all memory pools
at the end of this GC.
This method returns
a

Map

of the name of a memory pool
to the memory usage of the corresponding
memory pool when GC finishes.

**Returns:**
- a

Map

of memory pool names to the memory
usage of a memory pool when GC finishes.

---

#### public static
GcInfo
from​(
CompositeData
cd)

Returns a

GcInfo

object represented by the
given

CompositeData

. The given

CompositeData

must contain
all the following attributes:

description

Attribute Name

Type

index

java.lang.Long

startTime

java.lang.Long

endTime

java.lang.Long

memoryUsageBeforeGc

javax.management.openmbean.TabularData

memoryUsageAfterGc

javax.management.openmbean.TabularData

**Returns:**
- a

GcInfo

object represented by

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

GcInfo

object with the attributes
described above.

---

#### public
CompositeData
toCompositeData​(
CompositeType
ct)

Return the

CompositeData

representation of this

GcInfo

, including any GC-specific attributes. The
returned value will have at least all the attributes described
in the

from

method, plus optionally
other attributes.

**Specified by:**
- toCompositeData

in interface

CompositeDataView

**Parameters:**
- ct

- the

CompositeType

that the caller expects.
This parameter is ignored and can be null.

**Returns:**
- the

CompositeData

representation.

---

### Additional Sections

#### Class GcInfo

java.lang.Object

- com.sun.management.GcInfo

com.sun.management.GcInfo

**All Implemented Interfaces:** CompositeData

,

CompositeDataView

```java
public class
GcInfo

extends
Object

implements
CompositeData
,
CompositeDataView
```

Garbage collection information. It contains the following
information for one garbage collection as well as GC-specific
attributes:

- Start time
- End time
- Duration
- Memory usage before the collection starts
- Memory usage after the collection ends

GcInfo

is a

CompositeData

The GC-specific attributes can be obtained via the CompositeData
interface. This is a historical relic, and other classes should
not copy this pattern. Use

CompositeDataView

instead.

MXBean Mapping

GcInfo

is mapped to a

CompositeData

with attributes as specified in the

from

method.

**Since:** 1.5

public class

GcInfo

extends

Object

implements

CompositeData

,

CompositeDataView

Garbage collection information. It contains the following
information for one garbage collection as well as GC-specific
attributes:

- Start time
- End time
- Duration
- Memory usage before the collection starts
- Memory usage after the collection ends

GcInfo

is a

CompositeData

The GC-specific attributes can be obtained via the CompositeData
interface. This is a historical relic, and other classes should
not copy this pattern. Use

CompositeDataView

instead.

MXBean Mapping

GcInfo

is mapped to a

CompositeData

with attributes as specified in the

from

method.

Start time

End time

Duration

Memory usage before the collection starts

Memory usage after the collection ends

GcInfo

is a

CompositeData

The GC-specific attributes can be obtained via the CompositeData
interface. This is a historical relic, and other classes should
not copy this pattern. Use

CompositeDataView

instead.

MXBean Mapping

GcInfo

is mapped to a

CompositeData

with attributes as specified in the

from

method.

---

#### MXBean Mapping

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

GcInfo

from

​(

CompositeData

cd)

Returns a

GcInfo

object represented by the
given

CompositeData

.

long

getDuration

()

Returns the elapsed time of this GC in milliseconds.

long

getEndTime

()

Returns the end time of this GC in milliseconds
since the Java virtual machine was started.

long

getId

()

Returns the identifier of this garbage collection which is
the number of collections that this collector has done.

Map

<

String

,​

MemoryUsage

>

getMemoryUsageAfterGc

()

Returns the memory usage of all memory pools
at the end of this GC.

Map

<

String

,​

MemoryUsage

>

getMemoryUsageBeforeGc

()

Returns the memory usage of all memory pools
at the beginning of this GC.

long

getStartTime

()

Returns the start time of this GC in milliseconds
since the Java virtual machine was started.

CompositeData

toCompositeData

​(

CompositeType

ct)

Return the

CompositeData

representation of this

GcInfo

, including any GC-specific attributes.

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

- Methods declared in interface javax.management.openmbean.

CompositeData

containsKey

,

containsValue

,

equals

,

get

,

getAll

,

getCompositeType

,

hashCode

,

toString

,

values

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

GcInfo

from

​(

CompositeData

cd)

Returns a

GcInfo

object represented by the
given

CompositeData

.

long

getDuration

()

Returns the elapsed time of this GC in milliseconds.

long

getEndTime

()

Returns the end time of this GC in milliseconds
since the Java virtual machine was started.

long

getId

()

Returns the identifier of this garbage collection which is
the number of collections that this collector has done.

Map

<

String

,​

MemoryUsage

>

getMemoryUsageAfterGc

()

Returns the memory usage of all memory pools
at the end of this GC.

Map

<

String

,​

MemoryUsage

>

getMemoryUsageBeforeGc

()

Returns the memory usage of all memory pools
at the beginning of this GC.

long

getStartTime

()

Returns the start time of this GC in milliseconds
since the Java virtual machine was started.

CompositeData

toCompositeData

​(

CompositeType

ct)

Return the

CompositeData

representation of this

GcInfo

, including any GC-specific attributes.

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

- Methods declared in interface javax.management.openmbean.

CompositeData

containsKey

,

containsValue

,

equals

,

get

,

getAll

,

getCompositeType

,

hashCode

,

toString

,

values

---

#### Method Summary

Returns a

GcInfo

object represented by the
given

CompositeData

.

Returns the elapsed time of this GC in milliseconds.

Returns the end time of this GC in milliseconds
since the Java virtual machine was started.

Returns the identifier of this garbage collection which is
the number of collections that this collector has done.

Returns the memory usage of all memory pools
at the end of this GC.

Returns the memory usage of all memory pools
at the beginning of this GC.

Returns the start time of this GC in milliseconds
since the Java virtual machine was started.

Return the

CompositeData

representation of this

GcInfo

, including any GC-specific attributes.

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

Methods declared in interface javax.management.openmbean.

CompositeData

containsKey

,

containsValue

,

equals

,

get

,

getAll

,

getCompositeType

,

hashCode

,

toString

,

values

---

#### Methods declared in interface javax.management.openmbean. CompositeData

============ METHOD DETAIL ==========

- Method Detail

- getId

```java
public long getId()
```

Returns the identifier of this garbage collection which is
the number of collections that this collector has done.

**Returns:** the identifier of this garbage collection which is
the number of collections that this collector has done.

- getStartTime

```java
public long getStartTime()
```

Returns the start time of this GC in milliseconds
since the Java virtual machine was started.

**Returns:** the start time of this GC.

- getEndTime

```java
public long getEndTime()
```

Returns the end time of this GC in milliseconds
since the Java virtual machine was started.

**Returns:** the end time of this GC.

- getDuration

```java
public long getDuration()
```

Returns the elapsed time of this GC in milliseconds.

**Returns:** the elapsed time of this GC in milliseconds.

- getMemoryUsageBeforeGc

```java
public
Map
<
String
,​
MemoryUsage
> getMemoryUsageBeforeGc()
```

Returns the memory usage of all memory pools
at the beginning of this GC.
This method returns
a

Map

of the name of a memory pool
to the memory usage of the corresponding
memory pool before GC starts.

**Returns:** a

Map

of memory pool names to the memory
usage of a memory pool before GC starts.

- getMemoryUsageAfterGc

```java
public
Map
<
String
,​
MemoryUsage
> getMemoryUsageAfterGc()
```

Returns the memory usage of all memory pools
at the end of this GC.
This method returns
a

Map

of the name of a memory pool
to the memory usage of the corresponding
memory pool when GC finishes.

**Returns:** a

Map

of memory pool names to the memory
usage of a memory pool when GC finishes.

- from

```java
public static
GcInfo
from​(
CompositeData
cd)
```

Returns a

GcInfo

object represented by the
given

CompositeData

. The given

CompositeData

must contain
all the following attributes:

description

Attribute Name

Type

index

java.lang.Long

startTime

java.lang.Long

endTime

java.lang.Long

memoryUsageBeforeGc

javax.management.openmbean.TabularData

memoryUsageAfterGc

javax.management.openmbean.TabularData

**Returns:** a

GcInfo

object represented by

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

GcInfo

object with the attributes
described above.

- toCompositeData

```java
public
CompositeData
toCompositeData​(
CompositeType
ct)
```

Return the

CompositeData

representation of this

GcInfo

, including any GC-specific attributes. The
returned value will have at least all the attributes described
in the

from

method, plus optionally
other attributes.

**Specified by:** toCompositeData

in interface

CompositeDataView
**Parameters:** ct

- the

CompositeType

that the caller expects.
This parameter is ignored and can be null.
**Returns:** the

CompositeData

representation.

Method Detail

- getId

```java
public long getId()
```

Returns the identifier of this garbage collection which is
the number of collections that this collector has done.

**Returns:** the identifier of this garbage collection which is
the number of collections that this collector has done.

- getStartTime

```java
public long getStartTime()
```

Returns the start time of this GC in milliseconds
since the Java virtual machine was started.

**Returns:** the start time of this GC.

- getEndTime

```java
public long getEndTime()
```

Returns the end time of this GC in milliseconds
since the Java virtual machine was started.

**Returns:** the end time of this GC.

- getDuration

```java
public long getDuration()
```

Returns the elapsed time of this GC in milliseconds.

**Returns:** the elapsed time of this GC in milliseconds.

- getMemoryUsageBeforeGc

```java
public
Map
<
String
,​
MemoryUsage
> getMemoryUsageBeforeGc()
```

Returns the memory usage of all memory pools
at the beginning of this GC.
This method returns
a

Map

of the name of a memory pool
to the memory usage of the corresponding
memory pool before GC starts.

**Returns:** a

Map

of memory pool names to the memory
usage of a memory pool before GC starts.

- getMemoryUsageAfterGc

```java
public
Map
<
String
,​
MemoryUsage
> getMemoryUsageAfterGc()
```

Returns the memory usage of all memory pools
at the end of this GC.
This method returns
a

Map

of the name of a memory pool
to the memory usage of the corresponding
memory pool when GC finishes.

**Returns:** a

Map

of memory pool names to the memory
usage of a memory pool when GC finishes.

- from

```java
public static
GcInfo
from​(
CompositeData
cd)
```

Returns a

GcInfo

object represented by the
given

CompositeData

. The given

CompositeData

must contain
all the following attributes:

description

Attribute Name

Type

index

java.lang.Long

startTime

java.lang.Long

endTime

java.lang.Long

memoryUsageBeforeGc

javax.management.openmbean.TabularData

memoryUsageAfterGc

javax.management.openmbean.TabularData

**Returns:** a

GcInfo

object represented by

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

GcInfo

object with the attributes
described above.

- toCompositeData

```java
public
CompositeData
toCompositeData​(
CompositeType
ct)
```

Return the

CompositeData

representation of this

GcInfo

, including any GC-specific attributes. The
returned value will have at least all the attributes described
in the

from

method, plus optionally
other attributes.

**Specified by:** toCompositeData

in interface

CompositeDataView
**Parameters:** ct

- the

CompositeType

that the caller expects.
This parameter is ignored and can be null.
**Returns:** the

CompositeData

representation.

---

#### Method Detail

getId

```java
public long getId()
```

Returns the identifier of this garbage collection which is
the number of collections that this collector has done.

**Returns:** the identifier of this garbage collection which is
the number of collections that this collector has done.

---

#### getId

public long getId()

Returns the identifier of this garbage collection which is
the number of collections that this collector has done.

getStartTime

```java
public long getStartTime()
```

Returns the start time of this GC in milliseconds
since the Java virtual machine was started.

**Returns:** the start time of this GC.

---

#### getStartTime

public long getStartTime()

Returns the start time of this GC in milliseconds
since the Java virtual machine was started.

getEndTime

```java
public long getEndTime()
```

Returns the end time of this GC in milliseconds
since the Java virtual machine was started.

**Returns:** the end time of this GC.

---

#### getEndTime

public long getEndTime()

Returns the end time of this GC in milliseconds
since the Java virtual machine was started.

getDuration

```java
public long getDuration()
```

Returns the elapsed time of this GC in milliseconds.

**Returns:** the elapsed time of this GC in milliseconds.

---

#### getDuration

public long getDuration()

Returns the elapsed time of this GC in milliseconds.

getMemoryUsageBeforeGc

```java
public
Map
<
String
,​
MemoryUsage
> getMemoryUsageBeforeGc()
```

Returns the memory usage of all memory pools
at the beginning of this GC.
This method returns
a

Map

of the name of a memory pool
to the memory usage of the corresponding
memory pool before GC starts.

**Returns:** a

Map

of memory pool names to the memory
usage of a memory pool before GC starts.

---

#### getMemoryUsageBeforeGc

public

Map

<

String

,​

MemoryUsage

> getMemoryUsageBeforeGc()

Returns the memory usage of all memory pools
at the beginning of this GC.
This method returns
a

Map

of the name of a memory pool
to the memory usage of the corresponding
memory pool before GC starts.

getMemoryUsageAfterGc

```java
public
Map
<
String
,​
MemoryUsage
> getMemoryUsageAfterGc()
```

Returns the memory usage of all memory pools
at the end of this GC.
This method returns
a

Map

of the name of a memory pool
to the memory usage of the corresponding
memory pool when GC finishes.

**Returns:** a

Map

of memory pool names to the memory
usage of a memory pool when GC finishes.

---

#### getMemoryUsageAfterGc

public

Map

<

String

,​

MemoryUsage

> getMemoryUsageAfterGc()

Returns the memory usage of all memory pools
at the end of this GC.
This method returns
a

Map

of the name of a memory pool
to the memory usage of the corresponding
memory pool when GC finishes.

from

```java
public static
GcInfo
from​(
CompositeData
cd)
```

Returns a

GcInfo

object represented by the
given

CompositeData

. The given

CompositeData

must contain
all the following attributes:

description

Attribute Name

Type

index

java.lang.Long

startTime

java.lang.Long

endTime

java.lang.Long

memoryUsageBeforeGc

javax.management.openmbean.TabularData

memoryUsageAfterGc

javax.management.openmbean.TabularData

**Returns:** a

GcInfo

object represented by

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

GcInfo

object with the attributes
described above.

---

#### from

public static

GcInfo

from​(

CompositeData

cd)

Returns a

GcInfo

object represented by the
given

CompositeData

. The given

CompositeData

must contain
all the following attributes:

description

Attribute Name

Type

index

java.lang.Long

startTime

java.lang.Long

endTime

java.lang.Long

memoryUsageBeforeGc

javax.management.openmbean.TabularData

memoryUsageAfterGc

javax.management.openmbean.TabularData

toCompositeData

```java
public
CompositeData
toCompositeData​(
CompositeType
ct)
```

Return the

CompositeData

representation of this

GcInfo

, including any GC-specific attributes. The
returned value will have at least all the attributes described
in the

from

method, plus optionally
other attributes.

**Specified by:** toCompositeData

in interface

CompositeDataView
**Parameters:** ct

- the

CompositeType

that the caller expects.
This parameter is ignored and can be null.
**Returns:** the

CompositeData

representation.

---

#### toCompositeData

public

CompositeData

toCompositeData​(

CompositeType

ct)

Return the

CompositeData

representation of this

GcInfo

, including any GC-specific attributes. The
returned value will have at least all the attributes described
in the

from

method, plus optionally
other attributes.

---

