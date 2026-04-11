# Interface AttributeSet

**Source:** `java.desktop\javax\print\attribute\AttributeSet.html`

### Class Description

```java
public interface
AttributeSet
```

Interface

AttributeSet

specifies the interface for a set of printing
attributes. A printing attribute is an object whose class implements
interface

Attribute

.

An attribute set contains a group of

attribute values,

where duplicate
values are not allowed in the set. Furthermore, each value in an attribute
set is a member of some

category,

and at most one value in any
particular category is allowed in the set. For an attribute set, the values
are

Attribute

objects, and the categories are

Class

objects. An attribute's category is the class (or
interface) at the root of the class hierarchy for that kind of attribute.
Note that an attribute object's category may be a superclass of the attribute
object's class rather than the attribute object's class itself. An attribute
object's category is determined by calling the

getCategory()

method defined in interface

Attribute

.

The interfaces of an

AttributeSet

resemble those of the Java
Collections API's

java.util.Map

interface, but is more restrictive in
the types it will accept, and combines keys and values into an

Attribute

.

Attribute sets are used in several places in the Print Service API. In each
context, only certain kinds of attributes are allowed to appear in the
attribute set, as determined by the tagging interfaces which the attribute
class implements --

DocAttribute

,

PrintRequestAttribute

,

PrintJobAttribute

, and

PrintServiceAttribute

.
There are four specializations of an attribute set that are restricted to
contain just one of the four kinds of attribute --

DocAttributeSet

,

PrintRequestAttributeSet

,

PrintJobAttributeSet

, and

PrintServiceAttributeSet

, respectively. Note
that many attribute classes implement more than one tagging interface and so
may appear in more than one context.

- A

DocAttributeSet

, containing

DocAttribute

s, specifies the characteristics of an
individual doc and the print job settings to be applied to an individual
doc.

A

PrintRequestAttributeSet

, containing

PrintRequestAttribute

s, specifies the
settings to be applied to a whole print job and to all the docs in the
print job.

A

PrintJobAttributeSet

, containing

PrintJobAttribute

s, reports the status of a print
job.

A

PrintServiceAttributeSet

, containing

PrintServiceAttribute

s, reports the status of
a Print Service instance.

In some contexts, the client is only allowed to examine an attribute set's
contents but not change them (the set is read-only). In other places, the
client is allowed both to examine and to change an attribute set's contents
(the set is read-write). For a read-only attribute set, calling a mutating
operation throws an

UnmodifiableSetException

.

The Print Service API provides one implementation of interface

AttributeSet

, class

HashAttributeSet

. A
client can use class

HashAttributeSet

or provide its
own implementation of interface

AttributeSet

. The Print Service API
also provides implementations of interface

AttributeSet

's
subinterfaces -- classes

HashDocAttributeSet

,

HashPrintRequestAttributeSet

,

HashPrintJobAttributeSet

, and

HashPrintServiceAttributeSet

.

**All Known Subinterfaces:** DocAttributeSet

,

PrintJobAttributeSet

,

PrintRequestAttributeSet

,

PrintServiceAttributeSet

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Attribute
get​(
Class
<?> category)

Returns the attribute value which this attribute set contains in the
given attribute category. Returns

null

if this attribute set does
not contain any attribute value in the given attribute category.

**Parameters:**
- category

- attribute category whose associated attribute value is
to be returned. It must be a

Class

that implements
interface

Attribute

.

**Returns:**
- the attribute value in the given attribute category contained in
this attribute set, or

null

if this attribute set does
not contain any attribute value in the given attribute category

**Throws:**
- NullPointerException

- if the

category

is

null
- ClassCastException

- if the

category

is not a

Class

that implements interface

Attribute

---

#### boolean add​(
Attribute
attribute)

Adds the specified attribute to this attribute set if it is not already
present, first removing any existing value in the same attribute category
as the specified attribute value.

**Parameters:**
- attribute

- attribute value to be added to this attribute set

**Returns:**
- true

if this attribute set changed as a result of the
call, i.e., the given attribute value was not already a member of
this attribute set

**Throws:**
- NullPointerException

- if the

attribute

is

null
- UnmodifiableSetException

- if this attribute set does not support
the

add()

operation

---

#### boolean remove​(
Class
<?> category)

Removes any attribute for this category from this attribute set if
present. If

category

is

null

, then

remove()

does
nothing and returns

false

.

**Parameters:**
- category

- attribute category to be removed from this attribute set

**Returns:**
- true

if this attribute set changed as a result of the
call, i.e., the given attribute value had been a member of this
attribute set

**Throws:**
- UnmodifiableSetException

- if this attribute set does not support
the

remove()

operation

---

#### boolean remove​(
Attribute
attribute)

Removes the specified attribute from this attribute set if present. If

attribute

is

null

, then

remove()

does nothing and
returns

false

.

**Parameters:**
- attribute

- attribute value to be removed from this attribute set

**Returns:**
- true

if this attribute set changed as a result of the
call, i.e., the given attribute value had been a member of this
attribute set

**Throws:**
- UnmodifiableSetException

- if this attribute set does not support
the

remove()

operation

---

#### boolean containsKey​(
Class
<?> category)

Returns

true

if this attribute set contains an attribute for the
specified category.

**Parameters:**
- category

- whose presence in this attribute set is to be tested

**Returns:**
- true

if this attribute set contains an attribute value
for the specified category

---

#### boolean containsValue​(
Attribute
attribute)

Returns

true

if this attribute set contains the given attribute
value.

**Parameters:**
- attribute

- attribute value whose presence in this attribute set is
to be tested

**Returns:**
- true

if this attribute set contains the given attribute
value

---

#### boolean addAll​(
AttributeSet
attributes)

Adds all of the elements in the specified set to this attribute. The
outcome is the same as if the =

add(Attribute)

operation had been applied to this attribute set successively with each
element from the specified set. The behavior of the

addAll(AttributeSet)

operation is unspecified if the specified
set is modified while the operation is in progress.

If the

addAll(AttributeSet)

operation throws an exception, the
effect on this attribute set's state is implementation dependent;
elements from the specified set before the point of the exception may or
may not have been added to this attribute set.

**Parameters:**
- attributes

- whose elements are to be added to this attribute set

**Returns:**
- true

if this attribute set changed as a result of the
call

**Throws:**
- UnmodifiableSetException

- if this attribute set does not support
the

addAll(AttributeSet)

method
- NullPointerException

- if some element in the specified set is

null

**See Also:**
- add(Attribute)

---

#### int size()

Returns the number of attributes in this attribute set. If this attribute
set contains more than

Integer.MAX_VALUE

elements, returns

Integer.MAX_VALUE

.

**Returns:**
- the number of attributes in this attribute set

---

#### Attribute
[] toArray()

Returns an array of the attributes contained in this set.

**Returns:**
- the

Attributes

contained in this set as an array, zero
length if the

AttributeSet

is empty

---

#### void clear()

Removes all attributes from this attribute set.

**Throws:**
- UnmodifiableSetException

- if this attribute set does not support
the

clear()

operation

---

#### boolean isEmpty()

Returns

true

if this attribute set contains no attributes.

**Returns:**
- true

if this attribute set contains no attributes

---

#### boolean equals​(
Object
object)

Compares the specified object with this attribute set for equality.
Returns

true

if the given object is also an attribute set and the
two attribute sets contain the same attribute category-attribute value
mappings. This ensures that the

equals()

method works properly
across different implementations of the

AttributeSet

interface.

**Overrides:**
- equals

in class

Object

**Parameters:**
- object

- to be compared for equality with this attribute set

**Returns:**
- true

if the specified object is equal to this attribute
set

**See Also:**
- Object.hashCode()

,

HashMap

---

#### int hashCode()

Returns the hash code value for this attribute set. The hash code of an
attribute set is defined to be the sum of the hash codes of each entry in
the

AttributeSet

. This ensures that

t1.equals(t2)

implies
that

t1.hashCode()==t2.hashCode()

for any two attribute sets

t1

and

t2

, as required by the general contract of

Object.hashCode()

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this attribute set

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Interface AttributeSet

**All Known Subinterfaces:** DocAttributeSet

,

PrintJobAttributeSet

,

PrintRequestAttributeSet

,

PrintServiceAttributeSet

**All Known Implementing Classes:** HashAttributeSet

,

HashDocAttributeSet

,

HashPrintJobAttributeSet

,

HashPrintRequestAttributeSet

,

HashPrintServiceAttributeSet

```java
public interface
AttributeSet
```

Interface

AttributeSet

specifies the interface for a set of printing
attributes. A printing attribute is an object whose class implements
interface

Attribute

.

An attribute set contains a group of

attribute values,

where duplicate
values are not allowed in the set. Furthermore, each value in an attribute
set is a member of some

category,

and at most one value in any
particular category is allowed in the set. For an attribute set, the values
are

Attribute

objects, and the categories are

Class

objects. An attribute's category is the class (or
interface) at the root of the class hierarchy for that kind of attribute.
Note that an attribute object's category may be a superclass of the attribute
object's class rather than the attribute object's class itself. An attribute
object's category is determined by calling the

getCategory()

method defined in interface

Attribute

.

The interfaces of an

AttributeSet

resemble those of the Java
Collections API's

java.util.Map

interface, but is more restrictive in
the types it will accept, and combines keys and values into an

Attribute

.

Attribute sets are used in several places in the Print Service API. In each
context, only certain kinds of attributes are allowed to appear in the
attribute set, as determined by the tagging interfaces which the attribute
class implements --

DocAttribute

,

PrintRequestAttribute

,

PrintJobAttribute

, and

PrintServiceAttribute

.
There are four specializations of an attribute set that are restricted to
contain just one of the four kinds of attribute --

DocAttributeSet

,

PrintRequestAttributeSet

,

PrintJobAttributeSet

, and

PrintServiceAttributeSet

, respectively. Note
that many attribute classes implement more than one tagging interface and so
may appear in more than one context.

- A

DocAttributeSet

, containing

DocAttribute

s, specifies the characteristics of an
individual doc and the print job settings to be applied to an individual
doc.

A

PrintRequestAttributeSet

, containing

PrintRequestAttribute

s, specifies the
settings to be applied to a whole print job and to all the docs in the
print job.

A

PrintJobAttributeSet

, containing

PrintJobAttribute

s, reports the status of a print
job.

A

PrintServiceAttributeSet

, containing

PrintServiceAttribute

s, reports the status of
a Print Service instance.

In some contexts, the client is only allowed to examine an attribute set's
contents but not change them (the set is read-only). In other places, the
client is allowed both to examine and to change an attribute set's contents
(the set is read-write). For a read-only attribute set, calling a mutating
operation throws an

UnmodifiableSetException

.

The Print Service API provides one implementation of interface

AttributeSet

, class

HashAttributeSet

. A
client can use class

HashAttributeSet

or provide its
own implementation of interface

AttributeSet

. The Print Service API
also provides implementations of interface

AttributeSet

's
subinterfaces -- classes

HashDocAttributeSet

,

HashPrintRequestAttributeSet

,

HashPrintJobAttributeSet

, and

HashPrintServiceAttributeSet

.

public interface

AttributeSet

Interface

AttributeSet

specifies the interface for a set of printing
attributes. A printing attribute is an object whose class implements
interface

Attribute

.

An attribute set contains a group of

attribute values,

where duplicate
values are not allowed in the set. Furthermore, each value in an attribute
set is a member of some

category,

and at most one value in any
particular category is allowed in the set. For an attribute set, the values
are

Attribute

objects, and the categories are

Class

objects. An attribute's category is the class (or
interface) at the root of the class hierarchy for that kind of attribute.
Note that an attribute object's category may be a superclass of the attribute
object's class rather than the attribute object's class itself. An attribute
object's category is determined by calling the

getCategory()

method defined in interface

Attribute

.

The interfaces of an

AttributeSet

resemble those of the Java
Collections API's

java.util.Map

interface, but is more restrictive in
the types it will accept, and combines keys and values into an

Attribute

.

Attribute sets are used in several places in the Print Service API. In each
context, only certain kinds of attributes are allowed to appear in the
attribute set, as determined by the tagging interfaces which the attribute
class implements --

DocAttribute

,

PrintRequestAttribute

,

PrintJobAttribute

, and

PrintServiceAttribute

.
There are four specializations of an attribute set that are restricted to
contain just one of the four kinds of attribute --

DocAttributeSet

,

PrintRequestAttributeSet

,

PrintJobAttributeSet

, and

PrintServiceAttributeSet

, respectively. Note
that many attribute classes implement more than one tagging interface and so
may appear in more than one context.

- A

DocAttributeSet

, containing

DocAttribute

s, specifies the characteristics of an
individual doc and the print job settings to be applied to an individual
doc.

A

PrintRequestAttributeSet

, containing

PrintRequestAttribute

s, specifies the
settings to be applied to a whole print job and to all the docs in the
print job.

A

PrintJobAttributeSet

, containing

PrintJobAttribute

s, reports the status of a print
job.

A

PrintServiceAttributeSet

, containing

PrintServiceAttribute

s, reports the status of
a Print Service instance.

In some contexts, the client is only allowed to examine an attribute set's
contents but not change them (the set is read-only). In other places, the
client is allowed both to examine and to change an attribute set's contents
(the set is read-write). For a read-only attribute set, calling a mutating
operation throws an

UnmodifiableSetException

.

The Print Service API provides one implementation of interface

AttributeSet

, class

HashAttributeSet

. A
client can use class

HashAttributeSet

or provide its
own implementation of interface

AttributeSet

. The Print Service API
also provides implementations of interface

AttributeSet

's
subinterfaces -- classes

HashDocAttributeSet

,

HashPrintRequestAttributeSet

,

HashPrintJobAttributeSet

, and

HashPrintServiceAttributeSet

.

An attribute set contains a group of

attribute values,

where duplicate
values are not allowed in the set. Furthermore, each value in an attribute
set is a member of some

category,

and at most one value in any
particular category is allowed in the set. For an attribute set, the values
are

Attribute

objects, and the categories are

Class

objects. An attribute's category is the class (or
interface) at the root of the class hierarchy for that kind of attribute.
Note that an attribute object's category may be a superclass of the attribute
object's class rather than the attribute object's class itself. An attribute
object's category is determined by calling the

getCategory()

method defined in interface

Attribute

.

The interfaces of an

AttributeSet

resemble those of the Java
Collections API's

java.util.Map

interface, but is more restrictive in
the types it will accept, and combines keys and values into an

Attribute

.

Attribute sets are used in several places in the Print Service API. In each
context, only certain kinds of attributes are allowed to appear in the
attribute set, as determined by the tagging interfaces which the attribute
class implements --

DocAttribute

,

PrintRequestAttribute

,

PrintJobAttribute

, and

PrintServiceAttribute

.
There are four specializations of an attribute set that are restricted to
contain just one of the four kinds of attribute --

DocAttributeSet

,

PrintRequestAttributeSet

,

PrintJobAttributeSet

, and

PrintServiceAttributeSet

, respectively. Note
that many attribute classes implement more than one tagging interface and so
may appear in more than one context.

- A

DocAttributeSet

, containing

DocAttribute

s, specifies the characteristics of an
individual doc and the print job settings to be applied to an individual
doc.

A

PrintRequestAttributeSet

, containing

PrintRequestAttribute

s, specifies the
settings to be applied to a whole print job and to all the docs in the
print job.

A

PrintJobAttributeSet

, containing

PrintJobAttribute

s, reports the status of a print
job.

A

PrintServiceAttributeSet

, containing

PrintServiceAttribute

s, reports the status of
a Print Service instance.

In some contexts, the client is only allowed to examine an attribute set's
contents but not change them (the set is read-only). In other places, the
client is allowed both to examine and to change an attribute set's contents
(the set is read-write). For a read-only attribute set, calling a mutating
operation throws an

UnmodifiableSetException

.

The Print Service API provides one implementation of interface

AttributeSet

, class

HashAttributeSet

. A
client can use class

HashAttributeSet

or provide its
own implementation of interface

AttributeSet

. The Print Service API
also provides implementations of interface

AttributeSet

's
subinterfaces -- classes

HashDocAttributeSet

,

HashPrintRequestAttributeSet

,

HashPrintJobAttributeSet

, and

HashPrintServiceAttributeSet

.

The interfaces of an

AttributeSet

resemble those of the Java
Collections API's

java.util.Map

interface, but is more restrictive in
the types it will accept, and combines keys and values into an

Attribute

.

Attribute sets are used in several places in the Print Service API. In each
context, only certain kinds of attributes are allowed to appear in the
attribute set, as determined by the tagging interfaces which the attribute
class implements --

DocAttribute

,

PrintRequestAttribute

,

PrintJobAttribute

, and

PrintServiceAttribute

.
There are four specializations of an attribute set that are restricted to
contain just one of the four kinds of attribute --

DocAttributeSet

,

PrintRequestAttributeSet

,

PrintJobAttributeSet

, and

PrintServiceAttributeSet

, respectively. Note
that many attribute classes implement more than one tagging interface and so
may appear in more than one context.

- A

DocAttributeSet

, containing

DocAttribute

s, specifies the characteristics of an
individual doc and the print job settings to be applied to an individual
doc.

A

PrintRequestAttributeSet

, containing

PrintRequestAttribute

s, specifies the
settings to be applied to a whole print job and to all the docs in the
print job.

A

PrintJobAttributeSet

, containing

PrintJobAttribute

s, reports the status of a print
job.

A

PrintServiceAttributeSet

, containing

PrintServiceAttribute

s, reports the status of
a Print Service instance.

In some contexts, the client is only allowed to examine an attribute set's
contents but not change them (the set is read-only). In other places, the
client is allowed both to examine and to change an attribute set's contents
(the set is read-write). For a read-only attribute set, calling a mutating
operation throws an

UnmodifiableSetException

.

The Print Service API provides one implementation of interface

AttributeSet

, class

HashAttributeSet

. A
client can use class

HashAttributeSet

or provide its
own implementation of interface

AttributeSet

. The Print Service API
also provides implementations of interface

AttributeSet

's
subinterfaces -- classes

HashDocAttributeSet

,

HashPrintRequestAttributeSet

,

HashPrintJobAttributeSet

, and

HashPrintServiceAttributeSet

.

Attribute sets are used in several places in the Print Service API. In each
context, only certain kinds of attributes are allowed to appear in the
attribute set, as determined by the tagging interfaces which the attribute
class implements --

DocAttribute

,

PrintRequestAttribute

,

PrintJobAttribute

, and

PrintServiceAttribute

.
There are four specializations of an attribute set that are restricted to
contain just one of the four kinds of attribute --

DocAttributeSet

,

PrintRequestAttributeSet

,

PrintJobAttributeSet

, and

PrintServiceAttributeSet

, respectively. Note
that many attribute classes implement more than one tagging interface and so
may appear in more than one context.

- A

DocAttributeSet

, containing

DocAttribute

s, specifies the characteristics of an
individual doc and the print job settings to be applied to an individual
doc.

A

PrintRequestAttributeSet

, containing

PrintRequestAttribute

s, specifies the
settings to be applied to a whole print job and to all the docs in the
print job.

A

PrintJobAttributeSet

, containing

PrintJobAttribute

s, reports the status of a print
job.

A

PrintServiceAttributeSet

, containing

PrintServiceAttribute

s, reports the status of
a Print Service instance.

In some contexts, the client is only allowed to examine an attribute set's
contents but not change them (the set is read-only). In other places, the
client is allowed both to examine and to change an attribute set's contents
(the set is read-write). For a read-only attribute set, calling a mutating
operation throws an

UnmodifiableSetException

.

The Print Service API provides one implementation of interface

AttributeSet

, class

HashAttributeSet

. A
client can use class

HashAttributeSet

or provide its
own implementation of interface

AttributeSet

. The Print Service API
also provides implementations of interface

AttributeSet

's
subinterfaces -- classes

HashDocAttributeSet

,

HashPrintRequestAttributeSet

,

HashPrintJobAttributeSet

, and

HashPrintServiceAttributeSet

.

A

DocAttributeSet

, containing

DocAttribute

s, specifies the characteristics of an
individual doc and the print job settings to be applied to an individual
doc.

A

PrintRequestAttributeSet

, containing

PrintRequestAttribute

s, specifies the
settings to be applied to a whole print job and to all the docs in the
print job.

A

PrintJobAttributeSet

, containing

PrintJobAttribute

s, reports the status of a print
job.

A

PrintServiceAttributeSet

, containing

PrintServiceAttribute

s, reports the status of
a Print Service instance.

The Print Service API provides one implementation of interface

AttributeSet

, class

HashAttributeSet

. A
client can use class

HashAttributeSet

or provide its
own implementation of interface

AttributeSet

. The Print Service API
also provides implementations of interface

AttributeSet

's
subinterfaces -- classes

HashDocAttributeSet

,

HashPrintRequestAttributeSet

,

HashPrintJobAttributeSet

, and

HashPrintServiceAttributeSet

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

add

​(

Attribute

attribute)

Adds the specified attribute to this attribute set if it is not already
present, first removing any existing value in the same attribute category
as the specified attribute value.

boolean

addAll

​(

AttributeSet

attributes)

Adds all of the elements in the specified set to this attribute.

void

clear

()

Removes all attributes from this attribute set.

boolean

containsKey

​(

Class

<?> category)

Returns

true

if this attribute set contains an attribute for the
specified category.

boolean

containsValue

​(

Attribute

attribute)

Returns

true

if this attribute set contains the given attribute
value.

boolean

equals

​(

Object

object)

Compares the specified object with this attribute set for equality.

Attribute

get

​(

Class

<?> category)

Returns the attribute value which this attribute set contains in the
given attribute category.

int

hashCode

()

Returns the hash code value for this attribute set.

boolean

isEmpty

()

Returns

true

if this attribute set contains no attributes.

boolean

remove

​(

Class

<?> category)

Removes any attribute for this category from this attribute set if
present.

boolean

remove

​(

Attribute

attribute)

Removes the specified attribute from this attribute set if present.

int

size

()

Returns the number of attributes in this attribute set.

Attribute

[]

toArray

()

Returns an array of the attributes contained in this set.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

add

​(

Attribute

attribute)

Adds the specified attribute to this attribute set if it is not already
present, first removing any existing value in the same attribute category
as the specified attribute value.

boolean

addAll

​(

AttributeSet

attributes)

Adds all of the elements in the specified set to this attribute.

void

clear

()

Removes all attributes from this attribute set.

boolean

containsKey

​(

Class

<?> category)

Returns

true

if this attribute set contains an attribute for the
specified category.

boolean

containsValue

​(

Attribute

attribute)

Returns

true

if this attribute set contains the given attribute
value.

boolean

equals

​(

Object

object)

Compares the specified object with this attribute set for equality.

Attribute

get

​(

Class

<?> category)

Returns the attribute value which this attribute set contains in the
given attribute category.

int

hashCode

()

Returns the hash code value for this attribute set.

boolean

isEmpty

()

Returns

true

if this attribute set contains no attributes.

boolean

remove

​(

Class

<?> category)

Removes any attribute for this category from this attribute set if
present.

boolean

remove

​(

Attribute

attribute)

Removes the specified attribute from this attribute set if present.

int

size

()

Returns the number of attributes in this attribute set.

Attribute

[]

toArray

()

Returns an array of the attributes contained in this set.

---

#### Method Summary

Adds the specified attribute to this attribute set if it is not already
present, first removing any existing value in the same attribute category
as the specified attribute value.

Adds all of the elements in the specified set to this attribute.

Removes all attributes from this attribute set.

Returns

true

if this attribute set contains an attribute for the
specified category.

Returns

true

if this attribute set contains the given attribute
value.

Compares the specified object with this attribute set for equality.

Returns the attribute value which this attribute set contains in the
given attribute category.

Returns the hash code value for this attribute set.

Returns

true

if this attribute set contains no attributes.

Removes any attribute for this category from this attribute set if
present.

Removes the specified attribute from this attribute set if present.

Returns the number of attributes in this attribute set.

Returns an array of the attributes contained in this set.

============ METHOD DETAIL ==========

- Method Detail

- get

```java
Attribute
get​(
Class
<?> category)
```

Returns the attribute value which this attribute set contains in the
given attribute category. Returns

null

if this attribute set does
not contain any attribute value in the given attribute category.

**Parameters:** category

- attribute category whose associated attribute value is
to be returned. It must be a

Class

that implements
interface

Attribute

.
**Returns:** the attribute value in the given attribute category contained in
this attribute set, or

null

if this attribute set does
not contain any attribute value in the given attribute category
**Throws:** NullPointerException

- if the

category

is

null
**Throws:** ClassCastException

- if the

category

is not a

Class

that implements interface

Attribute

- add

```java
boolean add​(
Attribute
attribute)
```

Adds the specified attribute to this attribute set if it is not already
present, first removing any existing value in the same attribute category
as the specified attribute value.

**Parameters:** attribute

- attribute value to be added to this attribute set
**Returns:** true

if this attribute set changed as a result of the
call, i.e., the given attribute value was not already a member of
this attribute set
**Throws:** NullPointerException

- if the

attribute

is

null
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

add()

operation

- remove

```java
boolean remove​(
Class
<?> category)
```

Removes any attribute for this category from this attribute set if
present. If

category

is

null

, then

remove()

does
nothing and returns

false

.

**Parameters:** category

- attribute category to be removed from this attribute set
**Returns:** true

if this attribute set changed as a result of the
call, i.e., the given attribute value had been a member of this
attribute set
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

remove()

operation

- remove

```java
boolean remove​(
Attribute
attribute)
```

Removes the specified attribute from this attribute set if present. If

attribute

is

null

, then

remove()

does nothing and
returns

false

.

**Parameters:** attribute

- attribute value to be removed from this attribute set
**Returns:** true

if this attribute set changed as a result of the
call, i.e., the given attribute value had been a member of this
attribute set
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

remove()

operation

- containsKey

```java
boolean containsKey​(
Class
<?> category)
```

Returns

true

if this attribute set contains an attribute for the
specified category.

**Parameters:** category

- whose presence in this attribute set is to be tested
**Returns:** true

if this attribute set contains an attribute value
for the specified category

- containsValue

```java
boolean containsValue​(
Attribute
attribute)
```

Returns

true

if this attribute set contains the given attribute
value.

**Parameters:** attribute

- attribute value whose presence in this attribute set is
to be tested
**Returns:** true

if this attribute set contains the given attribute
value

- addAll

```java
boolean addAll​(
AttributeSet
attributes)
```

Adds all of the elements in the specified set to this attribute. The
outcome is the same as if the =

add(Attribute)

operation had been applied to this attribute set successively with each
element from the specified set. The behavior of the

addAll(AttributeSet)

operation is unspecified if the specified
set is modified while the operation is in progress.

If the

addAll(AttributeSet)

operation throws an exception, the
effect on this attribute set's state is implementation dependent;
elements from the specified set before the point of the exception may or
may not have been added to this attribute set.

**Parameters:** attributes

- whose elements are to be added to this attribute set
**Returns:** true

if this attribute set changed as a result of the
call
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

addAll(AttributeSet)

method
**Throws:** NullPointerException

- if some element in the specified set is

null
**See Also:** add(Attribute)

- size

```java
int size()
```

Returns the number of attributes in this attribute set. If this attribute
set contains more than

Integer.MAX_VALUE

elements, returns

Integer.MAX_VALUE

.

**Returns:** the number of attributes in this attribute set

- toArray

```java
Attribute
[] toArray()
```

Returns an array of the attributes contained in this set.

**Returns:** the

Attributes

contained in this set as an array, zero
length if the

AttributeSet

is empty

- clear

```java
void clear()
```

Removes all attributes from this attribute set.

**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

clear()

operation

- isEmpty

```java
boolean isEmpty()
```

Returns

true

if this attribute set contains no attributes.

**Returns:** true

if this attribute set contains no attributes

- equals

```java
boolean equals​(
Object
object)
```

Compares the specified object with this attribute set for equality.
Returns

true

if the given object is also an attribute set and the
two attribute sets contain the same attribute category-attribute value
mappings. This ensures that the

equals()

method works properly
across different implementations of the

AttributeSet

interface.

**Overrides:** equals

in class

Object
**Parameters:** object

- to be compared for equality with this attribute set
**Returns:** true

if the specified object is equal to this attribute
set
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this attribute set. The hash code of an
attribute set is defined to be the sum of the hash codes of each entry in
the

AttributeSet

. This ensures that

t1.equals(t2)

implies
that

t1.hashCode()==t2.hashCode()

for any two attribute sets

t1

and

t2

, as required by the general contract of

Object.hashCode()

.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this attribute set
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Method Detail

- get

```java
Attribute
get​(
Class
<?> category)
```

Returns the attribute value which this attribute set contains in the
given attribute category. Returns

null

if this attribute set does
not contain any attribute value in the given attribute category.

**Parameters:** category

- attribute category whose associated attribute value is
to be returned. It must be a

Class

that implements
interface

Attribute

.
**Returns:** the attribute value in the given attribute category contained in
this attribute set, or

null

if this attribute set does
not contain any attribute value in the given attribute category
**Throws:** NullPointerException

- if the

category

is

null
**Throws:** ClassCastException

- if the

category

is not a

Class

that implements interface

Attribute

- add

```java
boolean add​(
Attribute
attribute)
```

Adds the specified attribute to this attribute set if it is not already
present, first removing any existing value in the same attribute category
as the specified attribute value.

**Parameters:** attribute

- attribute value to be added to this attribute set
**Returns:** true

if this attribute set changed as a result of the
call, i.e., the given attribute value was not already a member of
this attribute set
**Throws:** NullPointerException

- if the

attribute

is

null
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

add()

operation

- remove

```java
boolean remove​(
Class
<?> category)
```

Removes any attribute for this category from this attribute set if
present. If

category

is

null

, then

remove()

does
nothing and returns

false

.

**Parameters:** category

- attribute category to be removed from this attribute set
**Returns:** true

if this attribute set changed as a result of the
call, i.e., the given attribute value had been a member of this
attribute set
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

remove()

operation

- remove

```java
boolean remove​(
Attribute
attribute)
```

Removes the specified attribute from this attribute set if present. If

attribute

is

null

, then

remove()

does nothing and
returns

false

.

**Parameters:** attribute

- attribute value to be removed from this attribute set
**Returns:** true

if this attribute set changed as a result of the
call, i.e., the given attribute value had been a member of this
attribute set
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

remove()

operation

- containsKey

```java
boolean containsKey​(
Class
<?> category)
```

Returns

true

if this attribute set contains an attribute for the
specified category.

**Parameters:** category

- whose presence in this attribute set is to be tested
**Returns:** true

if this attribute set contains an attribute value
for the specified category

- containsValue

```java
boolean containsValue​(
Attribute
attribute)
```

Returns

true

if this attribute set contains the given attribute
value.

**Parameters:** attribute

- attribute value whose presence in this attribute set is
to be tested
**Returns:** true

if this attribute set contains the given attribute
value

- addAll

```java
boolean addAll​(
AttributeSet
attributes)
```

Adds all of the elements in the specified set to this attribute. The
outcome is the same as if the =

add(Attribute)

operation had been applied to this attribute set successively with each
element from the specified set. The behavior of the

addAll(AttributeSet)

operation is unspecified if the specified
set is modified while the operation is in progress.

If the

addAll(AttributeSet)

operation throws an exception, the
effect on this attribute set's state is implementation dependent;
elements from the specified set before the point of the exception may or
may not have been added to this attribute set.

**Parameters:** attributes

- whose elements are to be added to this attribute set
**Returns:** true

if this attribute set changed as a result of the
call
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

addAll(AttributeSet)

method
**Throws:** NullPointerException

- if some element in the specified set is

null
**See Also:** add(Attribute)

- size

```java
int size()
```

Returns the number of attributes in this attribute set. If this attribute
set contains more than

Integer.MAX_VALUE

elements, returns

Integer.MAX_VALUE

.

**Returns:** the number of attributes in this attribute set

- toArray

```java
Attribute
[] toArray()
```

Returns an array of the attributes contained in this set.

**Returns:** the

Attributes

contained in this set as an array, zero
length if the

AttributeSet

is empty

- clear

```java
void clear()
```

Removes all attributes from this attribute set.

**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

clear()

operation

- isEmpty

```java
boolean isEmpty()
```

Returns

true

if this attribute set contains no attributes.

**Returns:** true

if this attribute set contains no attributes

- equals

```java
boolean equals​(
Object
object)
```

Compares the specified object with this attribute set for equality.
Returns

true

if the given object is also an attribute set and the
two attribute sets contain the same attribute category-attribute value
mappings. This ensures that the

equals()

method works properly
across different implementations of the

AttributeSet

interface.

**Overrides:** equals

in class

Object
**Parameters:** object

- to be compared for equality with this attribute set
**Returns:** true

if the specified object is equal to this attribute
set
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this attribute set. The hash code of an
attribute set is defined to be the sum of the hash codes of each entry in
the

AttributeSet

. This ensures that

t1.equals(t2)

implies
that

t1.hashCode()==t2.hashCode()

for any two attribute sets

t1

and

t2

, as required by the general contract of

Object.hashCode()

.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this attribute set
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

get

```java
Attribute
get​(
Class
<?> category)
```

Returns the attribute value which this attribute set contains in the
given attribute category. Returns

null

if this attribute set does
not contain any attribute value in the given attribute category.

**Parameters:** category

- attribute category whose associated attribute value is
to be returned. It must be a

Class

that implements
interface

Attribute

.
**Returns:** the attribute value in the given attribute category contained in
this attribute set, or

null

if this attribute set does
not contain any attribute value in the given attribute category
**Throws:** NullPointerException

- if the

category

is

null
**Throws:** ClassCastException

- if the

category

is not a

Class

that implements interface

Attribute

---

#### get

Attribute

get​(

Class

<?> category)

Returns the attribute value which this attribute set contains in the
given attribute category. Returns

null

if this attribute set does
not contain any attribute value in the given attribute category.

add

```java
boolean add​(
Attribute
attribute)
```

Adds the specified attribute to this attribute set if it is not already
present, first removing any existing value in the same attribute category
as the specified attribute value.

**Parameters:** attribute

- attribute value to be added to this attribute set
**Returns:** true

if this attribute set changed as a result of the
call, i.e., the given attribute value was not already a member of
this attribute set
**Throws:** NullPointerException

- if the

attribute

is

null
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

add()

operation

---

#### add

boolean add​(

Attribute

attribute)

Adds the specified attribute to this attribute set if it is not already
present, first removing any existing value in the same attribute category
as the specified attribute value.

remove

```java
boolean remove​(
Class
<?> category)
```

Removes any attribute for this category from this attribute set if
present. If

category

is

null

, then

remove()

does
nothing and returns

false

.

**Parameters:** category

- attribute category to be removed from this attribute set
**Returns:** true

if this attribute set changed as a result of the
call, i.e., the given attribute value had been a member of this
attribute set
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

remove()

operation

---

#### remove

boolean remove​(

Class

<?> category)

Removes any attribute for this category from this attribute set if
present. If

category

is

null

, then

remove()

does
nothing and returns

false

.

remove

```java
boolean remove​(
Attribute
attribute)
```

Removes the specified attribute from this attribute set if present. If

attribute

is

null

, then

remove()

does nothing and
returns

false

.

**Parameters:** attribute

- attribute value to be removed from this attribute set
**Returns:** true

if this attribute set changed as a result of the
call, i.e., the given attribute value had been a member of this
attribute set
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

remove()

operation

---

#### remove

boolean remove​(

Attribute

attribute)

Removes the specified attribute from this attribute set if present. If

attribute

is

null

, then

remove()

does nothing and
returns

false

.

containsKey

```java
boolean containsKey​(
Class
<?> category)
```

Returns

true

if this attribute set contains an attribute for the
specified category.

**Parameters:** category

- whose presence in this attribute set is to be tested
**Returns:** true

if this attribute set contains an attribute value
for the specified category

---

#### containsKey

boolean containsKey​(

Class

<?> category)

Returns

true

if this attribute set contains an attribute for the
specified category.

containsValue

```java
boolean containsValue​(
Attribute
attribute)
```

Returns

true

if this attribute set contains the given attribute
value.

**Parameters:** attribute

- attribute value whose presence in this attribute set is
to be tested
**Returns:** true

if this attribute set contains the given attribute
value

---

#### containsValue

boolean containsValue​(

Attribute

attribute)

Returns

true

if this attribute set contains the given attribute
value.

addAll

```java
boolean addAll​(
AttributeSet
attributes)
```

Adds all of the elements in the specified set to this attribute. The
outcome is the same as if the =

add(Attribute)

operation had been applied to this attribute set successively with each
element from the specified set. The behavior of the

addAll(AttributeSet)

operation is unspecified if the specified
set is modified while the operation is in progress.

If the

addAll(AttributeSet)

operation throws an exception, the
effect on this attribute set's state is implementation dependent;
elements from the specified set before the point of the exception may or
may not have been added to this attribute set.

**Parameters:** attributes

- whose elements are to be added to this attribute set
**Returns:** true

if this attribute set changed as a result of the
call
**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

addAll(AttributeSet)

method
**Throws:** NullPointerException

- if some element in the specified set is

null
**See Also:** add(Attribute)

---

#### addAll

boolean addAll​(

AttributeSet

attributes)

Adds all of the elements in the specified set to this attribute. The
outcome is the same as if the =

add(Attribute)

operation had been applied to this attribute set successively with each
element from the specified set. The behavior of the

addAll(AttributeSet)

operation is unspecified if the specified
set is modified while the operation is in progress.

If the

addAll(AttributeSet)

operation throws an exception, the
effect on this attribute set's state is implementation dependent;
elements from the specified set before the point of the exception may or
may not have been added to this attribute set.

If the

addAll(AttributeSet)

operation throws an exception, the
effect on this attribute set's state is implementation dependent;
elements from the specified set before the point of the exception may or
may not have been added to this attribute set.

size

```java
int size()
```

Returns the number of attributes in this attribute set. If this attribute
set contains more than

Integer.MAX_VALUE

elements, returns

Integer.MAX_VALUE

.

**Returns:** the number of attributes in this attribute set

---

#### size

int size()

Returns the number of attributes in this attribute set. If this attribute
set contains more than

Integer.MAX_VALUE

elements, returns

Integer.MAX_VALUE

.

toArray

```java
Attribute
[] toArray()
```

Returns an array of the attributes contained in this set.

**Returns:** the

Attributes

contained in this set as an array, zero
length if the

AttributeSet

is empty

---

#### toArray

Attribute

[] toArray()

Returns an array of the attributes contained in this set.

clear

```java
void clear()
```

Removes all attributes from this attribute set.

**Throws:** UnmodifiableSetException

- if this attribute set does not support
the

clear()

operation

---

#### clear

void clear()

Removes all attributes from this attribute set.

isEmpty

```java
boolean isEmpty()
```

Returns

true

if this attribute set contains no attributes.

**Returns:** true

if this attribute set contains no attributes

---

#### isEmpty

boolean isEmpty()

Returns

true

if this attribute set contains no attributes.

equals

```java
boolean equals​(
Object
object)
```

Compares the specified object with this attribute set for equality.
Returns

true

if the given object is also an attribute set and the
two attribute sets contain the same attribute category-attribute value
mappings. This ensures that the

equals()

method works properly
across different implementations of the

AttributeSet

interface.

**Overrides:** equals

in class

Object
**Parameters:** object

- to be compared for equality with this attribute set
**Returns:** true

if the specified object is equal to this attribute
set
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

boolean equals​(

Object

object)

Compares the specified object with this attribute set for equality.
Returns

true

if the given object is also an attribute set and the
two attribute sets contain the same attribute category-attribute value
mappings. This ensures that the

equals()

method works properly
across different implementations of the

AttributeSet

interface.

hashCode

```java
int hashCode()
```

Returns the hash code value for this attribute set. The hash code of an
attribute set is defined to be the sum of the hash codes of each entry in
the

AttributeSet

. This ensures that

t1.equals(t2)

implies
that

t1.hashCode()==t2.hashCode()

for any two attribute sets

t1

and

t2

, as required by the general contract of

Object.hashCode()

.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this attribute set
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

int hashCode()

Returns the hash code value for this attribute set. The hash code of an
attribute set is defined to be the sum of the hash codes of each entry in
the

AttributeSet

. This ensures that

t1.equals(t2)

implies
that

t1.hashCode()==t2.hashCode()

for any two attribute sets

t1

and

t2

, as required by the general contract of

Object.hashCode()

.

---

