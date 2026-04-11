# Class TIFFTagSet

**Source:** `java.desktop\javax\imageio\plugins\tiff\TIFFTagSet.html`

### Class Description

```java
public class
TIFFTagSet

extends
Object
```

A class representing a set of TIFF tags. Each tag in the set must have
a unique number (this is a limitation of the TIFF specification itself).

This class and its subclasses are responsible for mapping
between raw tag numbers and

TIFFTag

objects, which
contain additional information about each tag, such as the tag's
name, legal data types, and mnemonic names for some or all of its
data values.

**Direct Known Subclasses:** BaselineTIFFTagSet

,

ExifGPSTagSet

,

ExifInteroperabilityTagSet

,

ExifParentTIFFTagSet

,

ExifTIFFTagSet

,

FaxTIFFTagSet

,

GeoTIFFTagSet

---

### Field Details

*No entries found.*

### Constructor Details

#### public TIFFTagSet​(
List
<
TIFFTag
> tags)

Constructs a

TIFFTagSet

, given a

List

of

TIFFTag

objects.

**Parameters:**
- tags

- a

List

object containing

TIFFTag

objects to be added to this tag set.

**Throws:**
- IllegalArgumentException

- if

tags

is

null

, or contains objects that are not instances
of the

TIFFTag

class.

---

### Method Details

#### public
TIFFTag
getTag​(int tagNumber)

Returns the

TIFFTag

from this set that is
associated with the given tag number, or

null

if
no tag exists for that number.

**Parameters:**
- tagNumber

- the number of the tag to be retrieved.

**Returns:**
- the numbered

TIFFTag

, or

null

.

---

#### public
TIFFTag
getTag​(
String
tagName)

Returns the

TIFFTag

having the given tag name, or

null

if the named tag does not belong to this tag set.

**Parameters:**
- tagName

- the name of the tag to be retrieved, as a

String

.

**Returns:**
- the named

TIFFTag

, or

null

.

**Throws:**
- IllegalArgumentException

- if

tagName

is

null

.

---

#### public
SortedSet
<
Integer
> getTagNumbers()

Retrieves an unmodifiable numerically increasing set of tag numbers.

The returned object is unmodifiable and contains the tag
numbers of all

TIFFTag

s in this

TIFFTagSet

sorted into ascending order according to

Comparable.compareTo(Object)

.

**Returns:**
- All tag numbers in this set.

---

#### public
SortedSet
<
String
> getTagNames()

Retrieves an unmodifiable lexicographically increasing set of tag names.

The returned object is unmodifiable and contains the tag
names of all

TIFFTag

s in this

TIFFTagSet

sorted into ascending order according to

Comparable.compareTo(Object)

.

**Returns:**
- All tag names in this set.

---

### Additional Sections

#### Class TIFFTagSet

java.lang.Object

- javax.imageio.plugins.tiff.TIFFTagSet

javax.imageio.plugins.tiff.TIFFTagSet

**Direct Known Subclasses:** BaselineTIFFTagSet

,

ExifGPSTagSet

,

ExifInteroperabilityTagSet

,

ExifParentTIFFTagSet

,

ExifTIFFTagSet

,

FaxTIFFTagSet

,

GeoTIFFTagSet

```java
public class
TIFFTagSet

extends
Object
```

A class representing a set of TIFF tags. Each tag in the set must have
a unique number (this is a limitation of the TIFF specification itself).

This class and its subclasses are responsible for mapping
between raw tag numbers and

TIFFTag

objects, which
contain additional information about each tag, such as the tag's
name, legal data types, and mnemonic names for some or all of its
data values.

**Since:** 9
**See Also:** TIFFTag

public class

TIFFTagSet

extends

Object

A class representing a set of TIFF tags. Each tag in the set must have
a unique number (this is a limitation of the TIFF specification itself).

This class and its subclasses are responsible for mapping
between raw tag numbers and

TIFFTag

objects, which
contain additional information about each tag, such as the tag's
name, legal data types, and mnemonic names for some or all of its
data values.

This class and its subclasses are responsible for mapping
between raw tag numbers and

TIFFTag

objects, which
contain additional information about each tag, such as the tag's
name, legal data types, and mnemonic names for some or all of its
data values.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TIFFTagSet

​(

List

<

TIFFTag

> tags)

Constructs a

TIFFTagSet

, given a

List

of

TIFFTag

objects.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

TIFFTag

getTag

​(int tagNumber)

Returns the

TIFFTag

from this set that is
associated with the given tag number, or

null

if
no tag exists for that number.

TIFFTag

getTag

​(

String

tagName)

Returns the

TIFFTag

having the given tag name, or

null

if the named tag does not belong to this tag set.

SortedSet

<

String

>

getTagNames

()

Retrieves an unmodifiable lexicographically increasing set of tag names.

SortedSet

<

Integer

>

getTagNumbers

()

Retrieves an unmodifiable numerically increasing set of tag numbers.

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

TIFFTagSet

​(

List

<

TIFFTag

> tags)

Constructs a

TIFFTagSet

, given a

List

of

TIFFTag

objects.

---

#### Constructor Summary

Constructs a

TIFFTagSet

, given a

List

of

TIFFTag

objects.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

TIFFTag

getTag

​(int tagNumber)

Returns the

TIFFTag

from this set that is
associated with the given tag number, or

null

if
no tag exists for that number.

TIFFTag

getTag

​(

String

tagName)

Returns the

TIFFTag

having the given tag name, or

null

if the named tag does not belong to this tag set.

SortedSet

<

String

>

getTagNames

()

Retrieves an unmodifiable lexicographically increasing set of tag names.

SortedSet

<

Integer

>

getTagNumbers

()

Retrieves an unmodifiable numerically increasing set of tag numbers.

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

Returns the

TIFFTag

from this set that is
associated with the given tag number, or

null

if
no tag exists for that number.

Returns the

TIFFTag

having the given tag name, or

null

if the named tag does not belong to this tag set.

Retrieves an unmodifiable lexicographically increasing set of tag names.

Retrieves an unmodifiable numerically increasing set of tag numbers.

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

- TIFFTagSet

```java
public TIFFTagSet​(
List
<
TIFFTag
> tags)
```

Constructs a

TIFFTagSet

, given a

List

of

TIFFTag

objects.

**Parameters:** tags

- a

List

object containing

TIFFTag

objects to be added to this tag set.
**Throws:** IllegalArgumentException

- if

tags

is

null

, or contains objects that are not instances
of the

TIFFTag

class.

============ METHOD DETAIL ==========

- Method Detail

- getTag

```java
public
TIFFTag
getTag​(int tagNumber)
```

Returns the

TIFFTag

from this set that is
associated with the given tag number, or

null

if
no tag exists for that number.

**Parameters:** tagNumber

- the number of the tag to be retrieved.
**Returns:** the numbered

TIFFTag

, or

null

.

- getTag

```java
public
TIFFTag
getTag​(
String
tagName)
```

Returns the

TIFFTag

having the given tag name, or

null

if the named tag does not belong to this tag set.

**Parameters:** tagName

- the name of the tag to be retrieved, as a

String

.
**Returns:** the named

TIFFTag

, or

null

.
**Throws:** IllegalArgumentException

- if

tagName

is

null

.

- getTagNumbers

```java
public
SortedSet
<
Integer
> getTagNumbers()
```

Retrieves an unmodifiable numerically increasing set of tag numbers.

The returned object is unmodifiable and contains the tag
numbers of all

TIFFTag

s in this

TIFFTagSet

sorted into ascending order according to

Comparable.compareTo(Object)

.

**Returns:** All tag numbers in this set.

- getTagNames

```java
public
SortedSet
<
String
> getTagNames()
```

Retrieves an unmodifiable lexicographically increasing set of tag names.

The returned object is unmodifiable and contains the tag
names of all

TIFFTag

s in this

TIFFTagSet

sorted into ascending order according to

Comparable.compareTo(Object)

.

**Returns:** All tag names in this set.

Constructor Detail

- TIFFTagSet

```java
public TIFFTagSet​(
List
<
TIFFTag
> tags)
```

Constructs a

TIFFTagSet

, given a

List

of

TIFFTag

objects.

**Parameters:** tags

- a

List

object containing

TIFFTag

objects to be added to this tag set.
**Throws:** IllegalArgumentException

- if

tags

is

null

, or contains objects that are not instances
of the

TIFFTag

class.

---

#### Constructor Detail

TIFFTagSet

```java
public TIFFTagSet​(
List
<
TIFFTag
> tags)
```

Constructs a

TIFFTagSet

, given a

List

of

TIFFTag

objects.

**Parameters:** tags

- a

List

object containing

TIFFTag

objects to be added to this tag set.
**Throws:** IllegalArgumentException

- if

tags

is

null

, or contains objects that are not instances
of the

TIFFTag

class.

---

#### TIFFTagSet

public TIFFTagSet​(

List

<

TIFFTag

> tags)

Constructs a

TIFFTagSet

, given a

List

of

TIFFTag

objects.

Method Detail

- getTag

```java
public
TIFFTag
getTag​(int tagNumber)
```

Returns the

TIFFTag

from this set that is
associated with the given tag number, or

null

if
no tag exists for that number.

**Parameters:** tagNumber

- the number of the tag to be retrieved.
**Returns:** the numbered

TIFFTag

, or

null

.

- getTag

```java
public
TIFFTag
getTag​(
String
tagName)
```

Returns the

TIFFTag

having the given tag name, or

null

if the named tag does not belong to this tag set.

**Parameters:** tagName

- the name of the tag to be retrieved, as a

String

.
**Returns:** the named

TIFFTag

, or

null

.
**Throws:** IllegalArgumentException

- if

tagName

is

null

.

- getTagNumbers

```java
public
SortedSet
<
Integer
> getTagNumbers()
```

Retrieves an unmodifiable numerically increasing set of tag numbers.

The returned object is unmodifiable and contains the tag
numbers of all

TIFFTag

s in this

TIFFTagSet

sorted into ascending order according to

Comparable.compareTo(Object)

.

**Returns:** All tag numbers in this set.

- getTagNames

```java
public
SortedSet
<
String
> getTagNames()
```

Retrieves an unmodifiable lexicographically increasing set of tag names.

The returned object is unmodifiable and contains the tag
names of all

TIFFTag

s in this

TIFFTagSet

sorted into ascending order according to

Comparable.compareTo(Object)

.

**Returns:** All tag names in this set.

---

#### Method Detail

getTag

```java
public
TIFFTag
getTag​(int tagNumber)
```

Returns the

TIFFTag

from this set that is
associated with the given tag number, or

null

if
no tag exists for that number.

**Parameters:** tagNumber

- the number of the tag to be retrieved.
**Returns:** the numbered

TIFFTag

, or

null

.

---

#### getTag

public

TIFFTag

getTag​(int tagNumber)

Returns the

TIFFTag

from this set that is
associated with the given tag number, or

null

if
no tag exists for that number.

getTag

```java
public
TIFFTag
getTag​(
String
tagName)
```

Returns the

TIFFTag

having the given tag name, or

null

if the named tag does not belong to this tag set.

**Parameters:** tagName

- the name of the tag to be retrieved, as a

String

.
**Returns:** the named

TIFFTag

, or

null

.
**Throws:** IllegalArgumentException

- if

tagName

is

null

.

---

#### getTag

public

TIFFTag

getTag​(

String

tagName)

Returns the

TIFFTag

having the given tag name, or

null

if the named tag does not belong to this tag set.

getTagNumbers

```java
public
SortedSet
<
Integer
> getTagNumbers()
```

Retrieves an unmodifiable numerically increasing set of tag numbers.

The returned object is unmodifiable and contains the tag
numbers of all

TIFFTag

s in this

TIFFTagSet

sorted into ascending order according to

Comparable.compareTo(Object)

.

**Returns:** All tag numbers in this set.

---

#### getTagNumbers

public

SortedSet

<

Integer

> getTagNumbers()

Retrieves an unmodifiable numerically increasing set of tag numbers.

The returned object is unmodifiable and contains the tag
numbers of all

TIFFTag

s in this

TIFFTagSet

sorted into ascending order according to

Comparable.compareTo(Object)

.

The returned object is unmodifiable and contains the tag
numbers of all

TIFFTag

s in this

TIFFTagSet

sorted into ascending order according to

Comparable.compareTo(Object)

.

getTagNames

```java
public
SortedSet
<
String
> getTagNames()
```

Retrieves an unmodifiable lexicographically increasing set of tag names.

The returned object is unmodifiable and contains the tag
names of all

TIFFTag

s in this

TIFFTagSet

sorted into ascending order according to

Comparable.compareTo(Object)

.

**Returns:** All tag names in this set.

---

#### getTagNames

public

SortedSet

<

String

> getTagNames()

Retrieves an unmodifiable lexicographically increasing set of tag names.

The returned object is unmodifiable and contains the tag
names of all

TIFFTag

s in this

TIFFTagSet

sorted into ascending order according to

Comparable.compareTo(Object)

.

The returned object is unmodifiable and contains the tag
names of all

TIFFTag

s in this

TIFFTagSet

sorted into ascending order according to

Comparable.compareTo(Object)

.

---

