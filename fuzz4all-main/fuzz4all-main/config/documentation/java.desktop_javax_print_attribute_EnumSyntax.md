# Class EnumSyntax

**Source:** `java.desktop\javax\print\attribute\EnumSyntax.html`

### Class Description

```java
public abstract class
EnumSyntax

extends
Object

implements
Serializable
,
Cloneable
```

Class

EnumSyntax

is an abstract base class providing the common
implementation of all "type safe enumeration" objects. An enumeration class
(which extends class

EnumSyntax

) provides a group of enumeration
values (objects) that are singleton instances of the enumeration class; for
example:

```java
public class Bach extends EnumSyntax {
public static final Bach JOHANN_SEBASTIAN = new Bach(0);
public static final Bach WILHELM_FRIEDEMANN = new Bach(1);
public static final Bach CARL_PHILIP_EMMANUEL = new Bach(2);
public static final Bach JOHANN_CHRISTIAN = new Bach(3);
public static final Bach P_D_Q = new Bach(4);

private static final String[] stringTable = {
"Johann Sebastian Bach",
"Wilhelm Friedemann Bach",
"Carl Philip Emmanuel Bach",
"Johann Christian Bach",
"P.D.Q. Bach"
};

protected String[] getStringTable() {
return stringTable;
}

private static final Bach[] enumValueTable = {
JOHANN_SEBASTIAN,
WILHELM_FRIEDEMANN,
CARL_PHILIP_EMMANUEL,
JOHANN_CHRISTIAN,
P_D_Q
};

protected EnumSyntax[] getEnumValueTable() {
return enumValueTable;
}
}
```

You can then write code that uses the

==

and

!=

operators to
test enumeration values; for example:

```java
Bach theComposer;
. . .
if (theComposer == Bach.JOHANN_SEBASTIAN) {
System.out.println ("The greatest composer of all time!");
}
```

The

equals()

method for an enumeration class just does a test for
identical objects (

==

).

You can convert an enumeration value to a string by calling

toString()

. The string is obtained from a table supplied
by the enumeration class.

Under the hood, an enumeration value is just an integer, a different integer
for each enumeration value within an enumeration class. You can get an
enumeration value's integer value by calling

getValue()

.
An enumeration value's integer value is established when it is constructed
(see

EnumSyntax(int)

). Since the constructor is
protected, the only possible enumeration values are the singleton objects
declared in the enumeration class; additional enumeration values cannot be
created at run time.

You can define a subclass of an enumeration class that extends it with
additional enumeration values. The subclass's enumeration values' integer
values need not be distinct from the superclass's enumeration values' integer
values; the

==

,

!=

,

equals()

, and

toString()

methods will still work properly even if the subclass uses some of the same
integer values as the superclass. However, the application in which the
enumeration class and subclass are used may need to have distinct integer
values in the superclass and subclass.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected EnumSyntax​(int value)

Construct a new enumeration value with the given integer value.

**Parameters:**
- value

- Integer value

---

### Method Details

#### public int getValue()

Returns this enumeration value's integer value.

**Returns:**
- the value

---

#### public
Object
clone()

Returns a clone of this enumeration value, which to preserve the
semantics of enumeration values is the same object as this enumeration
value.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this instance.

**See Also:**
- Cloneable

---

#### public int hashCode()

Returns a hash code value for this enumeration value. The hash code is
just this enumeration value's integer value.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns a string value corresponding to this enumeration value.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

#### protected
Object
readResolve()
throws
ObjectStreamException

During object input, convert this deserialized enumeration instance to
the proper enumeration value defined in the enumeration attribute class.

**Returns:**
- The enumeration singleton value stored at index

i

-

L

in the enumeration value table returned by

getEnumValueTable()

, where

i

is this enumeration value's integer value and

L

is the
value returned by

getOffset()

**Throws:**
- ObjectStreamException

- if the stream can't be deserialised
- InvalidObjectException

- if the enumeration value table is

null

, this enumeration value's integer value does not
correspond to an element in the enumeration value table, or the
corresponding element in the enumeration value table is

null

. (Note:

InvalidObjectException

is a
subclass of

ObjectStreamException

,
which

readResolve()

is declared to throw.)

---

#### protected
String
[] getStringTable()

Returns the string table for this enumeration value's enumeration class.
The enumeration class's integer values are assumed to lie in the range

L

..

L

+

N

-1, where

L

is the value returned by

getOffset()

and

N

is the length of the string
table. The element in the string table at index

i

-

L

is the
value returned by

toString()

for the enumeration
value whose integer value is

i

. If an integer within the above
range is not used by any enumeration value, leave the corresponding table
element

null

.

The default implementation returns

null

. If the enumeration class
(a subclass of class

EnumSyntax

) does not override this method to
return a

non-null

string table, and the subclass does not
override the

toString()

method, the base class

toString()

method will return just a string
representation of this enumeration value's integer value.

**Returns:**
- the string table

---

#### protected
EnumSyntax
[] getEnumValueTable()

Returns the enumeration value table for this enumeration value's
enumeration class. The enumeration class's integer values are assumed to
lie in the range

L

..

L

+

N

-1, where

L

is the
value returned by

getOffset()

and

N

is the
length of the enumeration value table. The element in the enumeration
value table at index

i

-

L

is the enumeration value object
whose integer value is

i

; the

readResolve()

method needs this to preserve singleton semantics during deserialization
of an enumeration instance. If an integer within the above range is not
used by any enumeration value, leave the corresponding table element

null

.

The default implementation returns

null

. If the enumeration class
(a subclass of class EnumSyntax) does not override this method to return
a

non-null

enumeration value table, and the subclass does not
override the

readResolve()

method, the base class

readResolve()

method will throw an exception
whenever an enumeration instance is deserialized from an object input
stream.

**Returns:**
- the value table

---

#### protected int getOffset()

Returns the lowest integer value used by this enumeration value's
enumeration class.

The default implementation returns 0. If the enumeration class (a
subclass of class

EnumSyntax

) uses integer values starting at
other than 0, override this method in the subclass.

**Returns:**
- the offset of the lowest enumeration value

---

### Additional Sections

#### Class EnumSyntax

java.lang.Object

- javax.print.attribute.EnumSyntax

javax.print.attribute.EnumSyntax

**All Implemented Interfaces:** Serializable

,

Cloneable

**Direct Known Subclasses:** Chromaticity

,

ColorSupported

,

Compression

,

DialogTypeSelection

,

Fidelity

,

Finishings

,

JobSheets

,

JobState

,

JobStateReason

,

Media

,

MultipleDocumentHandling

,

OrientationRequested

,

PDLOverrideSupported

,

PresentationDirection

,

PrinterIsAcceptingJobs

,

PrinterState

,

PrinterStateReason

,

PrintQuality

,

ReferenceUriSchemesSupported

,

Severity

,

SheetCollate

,

Sides

```java
public abstract class
EnumSyntax

extends
Object

implements
Serializable
,
Cloneable
```

Class

EnumSyntax

is an abstract base class providing the common
implementation of all "type safe enumeration" objects. An enumeration class
(which extends class

EnumSyntax

) provides a group of enumeration
values (objects) that are singleton instances of the enumeration class; for
example:

```java
public class Bach extends EnumSyntax {
public static final Bach JOHANN_SEBASTIAN = new Bach(0);
public static final Bach WILHELM_FRIEDEMANN = new Bach(1);
public static final Bach CARL_PHILIP_EMMANUEL = new Bach(2);
public static final Bach JOHANN_CHRISTIAN = new Bach(3);
public static final Bach P_D_Q = new Bach(4);

private static final String[] stringTable = {
"Johann Sebastian Bach",
"Wilhelm Friedemann Bach",
"Carl Philip Emmanuel Bach",
"Johann Christian Bach",
"P.D.Q. Bach"
};

protected String[] getStringTable() {
return stringTable;
}

private static final Bach[] enumValueTable = {
JOHANN_SEBASTIAN,
WILHELM_FRIEDEMANN,
CARL_PHILIP_EMMANUEL,
JOHANN_CHRISTIAN,
P_D_Q
};

protected EnumSyntax[] getEnumValueTable() {
return enumValueTable;
}
}
```

You can then write code that uses the

==

and

!=

operators to
test enumeration values; for example:

```java
Bach theComposer;
. . .
if (theComposer == Bach.JOHANN_SEBASTIAN) {
System.out.println ("The greatest composer of all time!");
}
```

The

equals()

method for an enumeration class just does a test for
identical objects (

==

).

You can convert an enumeration value to a string by calling

toString()

. The string is obtained from a table supplied
by the enumeration class.

Under the hood, an enumeration value is just an integer, a different integer
for each enumeration value within an enumeration class. You can get an
enumeration value's integer value by calling

getValue()

.
An enumeration value's integer value is established when it is constructed
(see

EnumSyntax(int)

). Since the constructor is
protected, the only possible enumeration values are the singleton objects
declared in the enumeration class; additional enumeration values cannot be
created at run time.

You can define a subclass of an enumeration class that extends it with
additional enumeration values. The subclass's enumeration values' integer
values need not be distinct from the superclass's enumeration values' integer
values; the

==

,

!=

,

equals()

, and

toString()

methods will still work properly even if the subclass uses some of the same
integer values as the superclass. However, the application in which the
enumeration class and subclass are used may need to have distinct integer
values in the superclass and subclass.

**See Also:** Serialized Form

public abstract class

EnumSyntax

extends

Object

implements

Serializable

,

Cloneable

Class

EnumSyntax

is an abstract base class providing the common
implementation of all "type safe enumeration" objects. An enumeration class
(which extends class

EnumSyntax

) provides a group of enumeration
values (objects) that are singleton instances of the enumeration class; for
example:

```java
public class Bach extends EnumSyntax {
public static final Bach JOHANN_SEBASTIAN = new Bach(0);
public static final Bach WILHELM_FRIEDEMANN = new Bach(1);
public static final Bach CARL_PHILIP_EMMANUEL = new Bach(2);
public static final Bach JOHANN_CHRISTIAN = new Bach(3);
public static final Bach P_D_Q = new Bach(4);

private static final String[] stringTable = {
"Johann Sebastian Bach",
"Wilhelm Friedemann Bach",
"Carl Philip Emmanuel Bach",
"Johann Christian Bach",
"P.D.Q. Bach"
};

protected String[] getStringTable() {
return stringTable;
}

private static final Bach[] enumValueTable = {
JOHANN_SEBASTIAN,
WILHELM_FRIEDEMANN,
CARL_PHILIP_EMMANUEL,
JOHANN_CHRISTIAN,
P_D_Q
};

protected EnumSyntax[] getEnumValueTable() {
return enumValueTable;
}
}
```

You can then write code that uses the

==

and

!=

operators to
test enumeration values; for example:

```java
Bach theComposer;
. . .
if (theComposer == Bach.JOHANN_SEBASTIAN) {
System.out.println ("The greatest composer of all time!");
}
```

The

equals()

method for an enumeration class just does a test for
identical objects (

==

).

You can convert an enumeration value to a string by calling

toString()

. The string is obtained from a table supplied
by the enumeration class.

Under the hood, an enumeration value is just an integer, a different integer
for each enumeration value within an enumeration class. You can get an
enumeration value's integer value by calling

getValue()

.
An enumeration value's integer value is established when it is constructed
(see

EnumSyntax(int)

). Since the constructor is
protected, the only possible enumeration values are the singleton objects
declared in the enumeration class; additional enumeration values cannot be
created at run time.

You can define a subclass of an enumeration class that extends it with
additional enumeration values. The subclass's enumeration values' integer
values need not be distinct from the superclass's enumeration values' integer
values; the

==

,

!=

,

equals()

, and

toString()

methods will still work properly even if the subclass uses some of the same
integer values as the superclass. However, the application in which the
enumeration class and subclass are used may need to have distinct integer
values in the superclass and subclass.

public class Bach extends EnumSyntax {
public static final Bach JOHANN_SEBASTIAN = new Bach(0);
public static final Bach WILHELM_FRIEDEMANN = new Bach(1);
public static final Bach CARL_PHILIP_EMMANUEL = new Bach(2);
public static final Bach JOHANN_CHRISTIAN = new Bach(3);
public static final Bach P_D_Q = new Bach(4);

private static final String[] stringTable = {
"Johann Sebastian Bach",
"Wilhelm Friedemann Bach",
"Carl Philip Emmanuel Bach",
"Johann Christian Bach",
"P.D.Q. Bach"
};

protected String[] getStringTable() {
return stringTable;
}

private static final Bach[] enumValueTable = {
JOHANN_SEBASTIAN,
WILHELM_FRIEDEMANN,
CARL_PHILIP_EMMANUEL,
JOHANN_CHRISTIAN,
P_D_Q
};

protected EnumSyntax[] getEnumValueTable() {
return enumValueTable;
}
}

Bach theComposer;
. . .
if (theComposer == Bach.JOHANN_SEBASTIAN) {
System.out.println ("The greatest composer of all time!");
}

You can convert an enumeration value to a string by calling

toString()

. The string is obtained from a table supplied
by the enumeration class.

Under the hood, an enumeration value is just an integer, a different integer
for each enumeration value within an enumeration class. You can get an
enumeration value's integer value by calling

getValue()

.
An enumeration value's integer value is established when it is constructed
(see

EnumSyntax(int)

). Since the constructor is
protected, the only possible enumeration values are the singleton objects
declared in the enumeration class; additional enumeration values cannot be
created at run time.

You can define a subclass of an enumeration class that extends it with
additional enumeration values. The subclass's enumeration values' integer
values need not be distinct from the superclass's enumeration values' integer
values; the

==

,

!=

,

equals()

, and

toString()

methods will still work properly even if the subclass uses some of the same
integer values as the superclass. However, the application in which the
enumeration class and subclass are used may need to have distinct integer
values in the superclass and subclass.

Under the hood, an enumeration value is just an integer, a different integer
for each enumeration value within an enumeration class. You can get an
enumeration value's integer value by calling

getValue()

.
An enumeration value's integer value is established when it is constructed
(see

EnumSyntax(int)

). Since the constructor is
protected, the only possible enumeration values are the singleton objects
declared in the enumeration class; additional enumeration values cannot be
created at run time.

You can define a subclass of an enumeration class that extends it with
additional enumeration values. The subclass's enumeration values' integer
values need not be distinct from the superclass's enumeration values' integer
values; the

==

,

!=

,

equals()

, and

toString()

methods will still work properly even if the subclass uses some of the same
integer values as the superclass. However, the application in which the
enumeration class and subclass are used may need to have distinct integer
values in the superclass and subclass.

You can define a subclass of an enumeration class that extends it with
additional enumeration values. The subclass's enumeration values' integer
values need not be distinct from the superclass's enumeration values' integer
values; the

==

,

!=

,

equals()

, and

toString()

methods will still work properly even if the subclass uses some of the same
integer values as the superclass. However, the application in which the
enumeration class and subclass are used may need to have distinct integer
values in the superclass and subclass.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

EnumSyntax

​(int value)

Construct a new enumeration value with the given integer value.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a clone of this enumeration value, which to preserve the
semantics of enumeration values is the same object as this enumeration
value.

protected

EnumSyntax

[]

getEnumValueTable

()

Returns the enumeration value table for this enumeration value's
enumeration class.

protected int

getOffset

()

Returns the lowest integer value used by this enumeration value's
enumeration class.

protected

String

[]

getStringTable

()

Returns the string table for this enumeration value's enumeration class.

int

getValue

()

Returns this enumeration value's integer value.

int

hashCode

()

Returns a hash code value for this enumeration value.

protected

Object

readResolve

()

During object input, convert this deserialized enumeration instance to
the proper enumeration value defined in the enumeration attribute class.

String

toString

()

Returns a string value corresponding to this enumeration value.

- Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

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

Modifier

Constructor

Description

protected

EnumSyntax

​(int value)

Construct a new enumeration value with the given integer value.

---

#### Constructor Summary

Construct a new enumeration value with the given integer value.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a clone of this enumeration value, which to preserve the
semantics of enumeration values is the same object as this enumeration
value.

protected

EnumSyntax

[]

getEnumValueTable

()

Returns the enumeration value table for this enumeration value's
enumeration class.

protected int

getOffset

()

Returns the lowest integer value used by this enumeration value's
enumeration class.

protected

String

[]

getStringTable

()

Returns the string table for this enumeration value's enumeration class.

int

getValue

()

Returns this enumeration value's integer value.

int

hashCode

()

Returns a hash code value for this enumeration value.

protected

Object

readResolve

()

During object input, convert this deserialized enumeration instance to
the proper enumeration value defined in the enumeration attribute class.

String

toString

()

Returns a string value corresponding to this enumeration value.

- Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

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

Returns a clone of this enumeration value, which to preserve the
semantics of enumeration values is the same object as this enumeration
value.

Returns the enumeration value table for this enumeration value's
enumeration class.

Returns the lowest integer value used by this enumeration value's
enumeration class.

Returns the string table for this enumeration value's enumeration class.

Returns this enumeration value's integer value.

Returns a hash code value for this enumeration value.

During object input, convert this deserialized enumeration instance to
the proper enumeration value defined in the enumeration attribute class.

Returns a string value corresponding to this enumeration value.

Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

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

- EnumSyntax

```java
protected EnumSyntax​(int value)
```

Construct a new enumeration value with the given integer value.

**Parameters:** value

- Integer value

============ METHOD DETAIL ==========

- Method Detail

- getValue

```java
public int getValue()
```

Returns this enumeration value's integer value.

**Returns:** the value

- clone

```java
public
Object
clone()
```

Returns a clone of this enumeration value, which to preserve the
semantics of enumeration values is the same object as this enumeration
value.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this enumeration value. The hash code is
just this enumeration value's integer value.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string value corresponding to this enumeration value.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- readResolve

```java
protected
Object
readResolve()
throws
ObjectStreamException
```

During object input, convert this deserialized enumeration instance to
the proper enumeration value defined in the enumeration attribute class.

**Returns:** The enumeration singleton value stored at index

i

-

L

in the enumeration value table returned by

getEnumValueTable()

, where

i

is this enumeration value's integer value and

L

is the
value returned by

getOffset()
**Throws:** ObjectStreamException

- if the stream can't be deserialised
**Throws:** InvalidObjectException

- if the enumeration value table is

null

, this enumeration value's integer value does not
correspond to an element in the enumeration value table, or the
corresponding element in the enumeration value table is

null

. (Note:

InvalidObjectException

is a
subclass of

ObjectStreamException

,
which

readResolve()

is declared to throw.)

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for this enumeration value's enumeration class.
The enumeration class's integer values are assumed to lie in the range

L

..

L

+

N

-1, where

L

is the value returned by

getOffset()

and

N

is the length of the string
table. The element in the string table at index

i

-

L

is the
value returned by

toString()

for the enumeration
value whose integer value is

i

. If an integer within the above
range is not used by any enumeration value, leave the corresponding table
element

null

.

The default implementation returns

null

. If the enumeration class
(a subclass of class

EnumSyntax

) does not override this method to
return a

non-null

string table, and the subclass does not
override the

toString()

method, the base class

toString()

method will return just a string
representation of this enumeration value's integer value.

**Returns:** the string table

- getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for this enumeration value's
enumeration class. The enumeration class's integer values are assumed to
lie in the range

L

..

L

+

N

-1, where

L

is the
value returned by

getOffset()

and

N

is the
length of the enumeration value table. The element in the enumeration
value table at index

i

-

L

is the enumeration value object
whose integer value is

i

; the

readResolve()

method needs this to preserve singleton semantics during deserialization
of an enumeration instance. If an integer within the above range is not
used by any enumeration value, leave the corresponding table element

null

.

The default implementation returns

null

. If the enumeration class
(a subclass of class EnumSyntax) does not override this method to return
a

non-null

enumeration value table, and the subclass does not
override the

readResolve()

method, the base class

readResolve()

method will throw an exception
whenever an enumeration instance is deserialized from an object input
stream.

**Returns:** the value table

- getOffset

```java
protected int getOffset()
```

Returns the lowest integer value used by this enumeration value's
enumeration class.

The default implementation returns 0. If the enumeration class (a
subclass of class

EnumSyntax

) uses integer values starting at
other than 0, override this method in the subclass.

**Returns:** the offset of the lowest enumeration value

Constructor Detail

- EnumSyntax

```java
protected EnumSyntax​(int value)
```

Construct a new enumeration value with the given integer value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

EnumSyntax

```java
protected EnumSyntax​(int value)
```

Construct a new enumeration value with the given integer value.

**Parameters:** value

- Integer value

---

#### EnumSyntax

protected EnumSyntax​(int value)

Construct a new enumeration value with the given integer value.

Method Detail

- getValue

```java
public int getValue()
```

Returns this enumeration value's integer value.

**Returns:** the value

- clone

```java
public
Object
clone()
```

Returns a clone of this enumeration value, which to preserve the
semantics of enumeration values is the same object as this enumeration
value.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this enumeration value. The hash code is
just this enumeration value's integer value.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string value corresponding to this enumeration value.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- readResolve

```java
protected
Object
readResolve()
throws
ObjectStreamException
```

During object input, convert this deserialized enumeration instance to
the proper enumeration value defined in the enumeration attribute class.

**Returns:** The enumeration singleton value stored at index

i

-

L

in the enumeration value table returned by

getEnumValueTable()

, where

i

is this enumeration value's integer value and

L

is the
value returned by

getOffset()
**Throws:** ObjectStreamException

- if the stream can't be deserialised
**Throws:** InvalidObjectException

- if the enumeration value table is

null

, this enumeration value's integer value does not
correspond to an element in the enumeration value table, or the
corresponding element in the enumeration value table is

null

. (Note:

InvalidObjectException

is a
subclass of

ObjectStreamException

,
which

readResolve()

is declared to throw.)

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for this enumeration value's enumeration class.
The enumeration class's integer values are assumed to lie in the range

L

..

L

+

N

-1, where

L

is the value returned by

getOffset()

and

N

is the length of the string
table. The element in the string table at index

i

-

L

is the
value returned by

toString()

for the enumeration
value whose integer value is

i

. If an integer within the above
range is not used by any enumeration value, leave the corresponding table
element

null

.

The default implementation returns

null

. If the enumeration class
(a subclass of class

EnumSyntax

) does not override this method to
return a

non-null

string table, and the subclass does not
override the

toString()

method, the base class

toString()

method will return just a string
representation of this enumeration value's integer value.

**Returns:** the string table

- getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for this enumeration value's
enumeration class. The enumeration class's integer values are assumed to
lie in the range

L

..

L

+

N

-1, where

L

is the
value returned by

getOffset()

and

N

is the
length of the enumeration value table. The element in the enumeration
value table at index

i

-

L

is the enumeration value object
whose integer value is

i

; the

readResolve()

method needs this to preserve singleton semantics during deserialization
of an enumeration instance. If an integer within the above range is not
used by any enumeration value, leave the corresponding table element

null

.

The default implementation returns

null

. If the enumeration class
(a subclass of class EnumSyntax) does not override this method to return
a

non-null

enumeration value table, and the subclass does not
override the

readResolve()

method, the base class

readResolve()

method will throw an exception
whenever an enumeration instance is deserialized from an object input
stream.

**Returns:** the value table

- getOffset

```java
protected int getOffset()
```

Returns the lowest integer value used by this enumeration value's
enumeration class.

The default implementation returns 0. If the enumeration class (a
subclass of class

EnumSyntax

) uses integer values starting at
other than 0, override this method in the subclass.

**Returns:** the offset of the lowest enumeration value

---

#### Method Detail

getValue

```java
public int getValue()
```

Returns this enumeration value's integer value.

**Returns:** the value

---

#### getValue

public int getValue()

Returns this enumeration value's integer value.

clone

```java
public
Object
clone()
```

Returns a clone of this enumeration value, which to preserve the
semantics of enumeration values is the same object as this enumeration
value.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Returns a clone of this enumeration value, which to preserve the
semantics of enumeration values is the same object as this enumeration
value.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this enumeration value. The hash code is
just this enumeration value's integer value.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code value for this enumeration value. The hash code is
just this enumeration value's integer value.

toString

```java
public
String
toString()
```

Returns a string value corresponding to this enumeration value.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns a string value corresponding to this enumeration value.

readResolve

```java
protected
Object
readResolve()
throws
ObjectStreamException
```

During object input, convert this deserialized enumeration instance to
the proper enumeration value defined in the enumeration attribute class.

**Returns:** The enumeration singleton value stored at index

i

-

L

in the enumeration value table returned by

getEnumValueTable()

, where

i

is this enumeration value's integer value and

L

is the
value returned by

getOffset()
**Throws:** ObjectStreamException

- if the stream can't be deserialised
**Throws:** InvalidObjectException

- if the enumeration value table is

null

, this enumeration value's integer value does not
correspond to an element in the enumeration value table, or the
corresponding element in the enumeration value table is

null

. (Note:

InvalidObjectException

is a
subclass of

ObjectStreamException

,
which

readResolve()

is declared to throw.)

---

#### readResolve

protected

Object

readResolve()
throws

ObjectStreamException

During object input, convert this deserialized enumeration instance to
the proper enumeration value defined in the enumeration attribute class.

getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for this enumeration value's enumeration class.
The enumeration class's integer values are assumed to lie in the range

L

..

L

+

N

-1, where

L

is the value returned by

getOffset()

and

N

is the length of the string
table. The element in the string table at index

i

-

L

is the
value returned by

toString()

for the enumeration
value whose integer value is

i

. If an integer within the above
range is not used by any enumeration value, leave the corresponding table
element

null

.

The default implementation returns

null

. If the enumeration class
(a subclass of class

EnumSyntax

) does not override this method to
return a

non-null

string table, and the subclass does not
override the

toString()

method, the base class

toString()

method will return just a string
representation of this enumeration value's integer value.

**Returns:** the string table

---

#### getStringTable

protected

String

[] getStringTable()

Returns the string table for this enumeration value's enumeration class.
The enumeration class's integer values are assumed to lie in the range

L

..

L

+

N

-1, where

L

is the value returned by

getOffset()

and

N

is the length of the string
table. The element in the string table at index

i

-

L

is the
value returned by

toString()

for the enumeration
value whose integer value is

i

. If an integer within the above
range is not used by any enumeration value, leave the corresponding table
element

null

.

The default implementation returns

null

. If the enumeration class
(a subclass of class

EnumSyntax

) does not override this method to
return a

non-null

string table, and the subclass does not
override the

toString()

method, the base class

toString()

method will return just a string
representation of this enumeration value's integer value.

The default implementation returns

null

. If the enumeration class
(a subclass of class

EnumSyntax

) does not override this method to
return a

non-null

string table, and the subclass does not
override the

toString()

method, the base class

toString()

method will return just a string
representation of this enumeration value's integer value.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for this enumeration value's
enumeration class. The enumeration class's integer values are assumed to
lie in the range

L

..

L

+

N

-1, where

L

is the
value returned by

getOffset()

and

N

is the
length of the enumeration value table. The element in the enumeration
value table at index

i

-

L

is the enumeration value object
whose integer value is

i

; the

readResolve()

method needs this to preserve singleton semantics during deserialization
of an enumeration instance. If an integer within the above range is not
used by any enumeration value, leave the corresponding table element

null

.

The default implementation returns

null

. If the enumeration class
(a subclass of class EnumSyntax) does not override this method to return
a

non-null

enumeration value table, and the subclass does not
override the

readResolve()

method, the base class

readResolve()

method will throw an exception
whenever an enumeration instance is deserialized from an object input
stream.

**Returns:** the value table

---

#### getEnumValueTable

protected

EnumSyntax

[] getEnumValueTable()

Returns the enumeration value table for this enumeration value's
enumeration class. The enumeration class's integer values are assumed to
lie in the range

L

..

L

+

N

-1, where

L

is the
value returned by

getOffset()

and

N

is the
length of the enumeration value table. The element in the enumeration
value table at index

i

-

L

is the enumeration value object
whose integer value is

i

; the

readResolve()

method needs this to preserve singleton semantics during deserialization
of an enumeration instance. If an integer within the above range is not
used by any enumeration value, leave the corresponding table element

null

.

The default implementation returns

null

. If the enumeration class
(a subclass of class EnumSyntax) does not override this method to return
a

non-null

enumeration value table, and the subclass does not
override the

readResolve()

method, the base class

readResolve()

method will throw an exception
whenever an enumeration instance is deserialized from an object input
stream.

The default implementation returns

null

. If the enumeration class
(a subclass of class EnumSyntax) does not override this method to return
a

non-null

enumeration value table, and the subclass does not
override the

readResolve()

method, the base class

readResolve()

method will throw an exception
whenever an enumeration instance is deserialized from an object input
stream.

getOffset

```java
protected int getOffset()
```

Returns the lowest integer value used by this enumeration value's
enumeration class.

The default implementation returns 0. If the enumeration class (a
subclass of class

EnumSyntax

) uses integer values starting at
other than 0, override this method in the subclass.

**Returns:** the offset of the lowest enumeration value

---

#### getOffset

protected int getOffset()

Returns the lowest integer value used by this enumeration value's
enumeration class.

The default implementation returns 0. If the enumeration class (a
subclass of class

EnumSyntax

) uses integer values starting at
other than 0, override this method in the subclass.

The default implementation returns 0. If the enumeration class (a
subclass of class

EnumSyntax

) uses integer values starting at
other than 0, override this method in the subclass.

---

