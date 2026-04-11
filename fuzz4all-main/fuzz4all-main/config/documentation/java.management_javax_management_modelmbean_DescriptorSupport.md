# Class DescriptorSupport

**Source:** `java.management\javax\management\modelmbean\DescriptorSupport.html`

### Class Description

```java
public class
DescriptorSupport

extends
Object

implements
Descriptor
```

This class represents the metadata set for a ModelMBean element. A
descriptor is part of the ModelMBeanInfo,
ModelMBeanNotificationInfo, ModelMBeanAttributeInfo,
ModelMBeanConstructorInfo, and ModelMBeanParameterInfo.

A descriptor consists of a collection of fields. Each field is in
fieldname=fieldvalue format. Field names are not case sensitive,
case will be preserved on field values.

All field names and values are not predefined. New fields can be
defined and added by any program. Some fields have been predefined
for consistency of implementation and support by the
ModelMBeanInfo, ModelMBeanAttributeInfo, ModelMBeanConstructorInfo,
ModelMBeanNotificationInfo, ModelMBeanOperationInfo and ModelMBean
classes.

The

serialVersionUID

of this class is

-6292969195866300415L

.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Descriptor

---

### Field Details

*No entries found.*

### Constructor Details

#### public DescriptorSupport()

Descriptor default constructor.
Default initial descriptor size is 20. It will grow as needed.

Note that the created empty descriptor is not a valid descriptor
(the method

isValid

returns

false

)

---

#### public DescriptorSupport​(int initNumFields)
throws
MBeanException
,

RuntimeOperationsException

Descriptor constructor. Takes as parameter the initial
capacity of the Map that stores the descriptor fields.
Capacity will grow as needed.

Note that the created empty
descriptor is not a valid descriptor (the method

isValid

returns

false

).

**Parameters:**
- initNumFields

- The initial capacity of the Map that
stores the descriptor fields.

**Throws:**
- RuntimeOperationsException

- for illegal value for
initNumFields (<= 0)
- MBeanException

- Wraps a distributed communication Exception.

---

#### public DescriptorSupport​(
DescriptorSupport
inDescr)

Descriptor constructor taking a Descriptor as parameter.
Creates a new descriptor initialized to the values of the
descriptor passed in parameter.

**Parameters:**
- inDescr

- the descriptor to be used to initialize the
constructed descriptor. If it is null or contains no descriptor
fields, an empty Descriptor will be created.

---

#### public DescriptorSupport​(
String
inStr)
throws
MBeanException
,

RuntimeOperationsException
,

XMLParseException

Descriptor constructor taking an XML String.

The format of the XML string is not defined, but an
implementation must ensure that the string returned by

toXMLString()

on an existing
descriptor can be used to instantiate an equivalent
descriptor using this constructor.

In this implementation, all field values will be created
as Strings. If the field values are not Strings, the
programmer will have to reset or convert these fields
correctly.

**Parameters:**
- inStr

- An XML-formatted string used to populate this
Descriptor. The format is not defined, but any
implementation must ensure that the string returned by
method

toXMLString

on an existing
descriptor can be used to instantiate an equivalent
descriptor when instantiated using this constructor.

**Throws:**
- RuntimeOperationsException

- If the String inStr
passed in parameter is null
- XMLParseException

- XML parsing problem while parsing
the input String
- MBeanException

- Wraps a distributed communication Exception.

---

#### public DescriptorSupport​(
String
[] fieldNames,

Object
[] fieldValues)
throws
RuntimeOperationsException

Constructor taking field names and field values. Neither array
can be null.

**Parameters:**
- fieldNames

- String array of field names. No elements of
this array can be null.
- fieldValues

- Object array of the corresponding field
values. Elements of the array can be null. The

fieldValue

must be valid for the

fieldName

(as defined in method

isValid

)

Note: array sizes of parameters should match. If both arrays
are empty, then an empty descriptor is created.

**Throws:**
- RuntimeOperationsException

- for illegal value for
field Names or field Values. The array lengths must be equal.
If the descriptor construction fails for any reason, this
exception will be thrown.

---

#### public DescriptorSupport​(
String
... fields)

Constructor taking fields in the

fieldName=fieldValue

format.

**Parameters:**
- fields

- String array with each element containing a
field name and value. If this array is null or empty, then the
default constructor will be executed. Null strings or empty
strings will be ignored.

All field values should be Strings. If the field values are
not Strings, the programmer will have to reset or convert these
fields correctly.

Note: Each string should be of the form

fieldName=fieldValue

. The field name
ends at the first

=

character; for example if the String
is

a=b=c

then the field name is

a

and its value
is

b=c

.

**Throws:**
- RuntimeOperationsException

- for illegal value for
field Names or field Values. The field must contain an
"=". "=fieldValue", "fieldName", and "fieldValue" are illegal.
FieldName cannot be null. "fieldName=" will cause the value to
be null. If the descriptor construction fails for any reason,
this exception will be thrown.

---

### Method Details

#### public
Object
clone()
throws
RuntimeOperationsException

Returns a new Descriptor which is a duplicate of the Descriptor.

**Specified by:**
- clone

in interface

Descriptor

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this instance.

**Throws:**
- RuntimeOperationsException

- for illegal value for
field Names or field Values. If the descriptor construction
fails for any reason, this exception will be thrown.

**See Also:**
- Cloneable

---

#### public boolean equals​(
Object
o)

Compares this descriptor to the given object. The objects are equal if
the given object is also a Descriptor, and if the two Descriptors have
the same field names (possibly differing in case) and the same
associated values. The respective values for a field in the two
Descriptors are equal if the following conditions hold:

- If one value is null then the other must be too.
- If one value is a primitive array then the other must be a primitive
array of the same type with the same elements.
- If one value is an object array then the other must be too and

Arrays.deepEquals

must return true.
- Otherwise

Object.equals(Object)

must return true.

**Specified by:**
- equals

in interface

Descriptor

**Overrides:**
- equals

in class

Object

**Parameters:**
- o

- the object to compare with.

**Returns:**
- true

if the objects are the same;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this descriptor. The hash
code is computed as the sum of the hash codes for each field in
the descriptor. The hash code of a field with name

n

and value

v

is

n.toLowerCase().hashCode() ^ h

.
Here

h

is the hash code of

v

, computed as
follows:

- If

v

is null then

h

is 0.
- If

v

is a primitive array then

h

is computed using
the appropriate overloading of

java.util.Arrays.hashCode

.
- If

v

is an object array then

h

is computed using

Arrays.deepHashCode

.
- Otherwise

h

is

v.hashCode()

.

**Specified by:**
- hashCode

in interface

Descriptor

**Overrides:**
- hashCode

in class

Object

**Returns:**
- A hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean isValid()
throws
RuntimeOperationsException

Returns true if all of the fields have legal values given their
names.

This implementation does not support interoperating with a directory
or lookup service. Thus, conforming to the specification, no checking is
done on the

"export"

field.

Otherwise this implementation returns false if:

- name and descriptorType fieldNames are not defined, or
null, or empty, or not String

class, role, getMethod, setMethod fieldNames, if defined,
are null or not String

persistPeriod, currencyTimeLimit, lastUpdatedTimeStamp,
lastReturnedTimeStamp if defined, are null, or not a Numeric
String or not a Numeric Value >= -1

log fieldName, if defined, is null, or not a Boolean or
not a String with value "t", "f", "true", "false". These String
values must not be case sensitive.

visibility fieldName, if defined, is null, or not a
Numeric String or a not Numeric Value >= 1 and <= 4

severity fieldName, if defined, is null, or not a Numeric
String or not a Numeric Value >= 0 and <= 6

persistPolicy fieldName, if defined, is null, or not one of
the following strings:

"OnUpdate", "OnTimer", "NoMoreOftenThan", "OnUnregister", "Always",
"Never". These String values must not be case sensitive.

**Specified by:**
- isValid

in interface

Descriptor

**Returns:**
- true if the values are legal.

**Throws:**
- RuntimeOperationsException

- If the validity checking
fails for any reason, this exception will be thrown.

---

#### public
String
toXMLString()

Returns an XML String representing the descriptor.

The format is not defined, but an implementation must
ensure that the string returned by this method can be
used to build an equivalent descriptor when instantiated
using the constructor

DescriptorSupport(String inStr)

.

Fields which are not String objects will have toString()
called on them to create the value. The value will be
enclosed in parentheses. It is not guaranteed that you can
reconstruct these objects unless they have been
specifically set up to support toString() in a meaningful
format and have a matching constructor that accepts a
String in the same format.

If the descriptor is empty the following String is
returned: <Descriptor></Descriptor>

**Returns:**
- the XML string.

**Throws:**
- RuntimeOperationsException

- for illegal value for
field Names or field Values. If the XML formatted string
construction fails for any reason, this exception will be
thrown.

---

#### public
String
toString()

Returns a human readable string representing the
descriptor. The string will be in the format of
"fieldName=fieldValue,fieldName2=fieldValue2,..."

If there are no fields in the descriptor, then an empty String
is returned.

If a fieldValue is an object then the toString() method is
called on it and its returned value is used as the value for
the field enclosed in parenthesis.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

**Throws:**
- RuntimeOperationsException

- for illegal value for
field Names or field Values. If the descriptor string fails
for any reason, this exception will be thrown.

---

### Additional Sections

#### Class DescriptorSupport

java.lang.Object

- javax.management.modelmbean.DescriptorSupport

javax.management.modelmbean.DescriptorSupport

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Descriptor

```java
public class
DescriptorSupport

extends
Object

implements
Descriptor
```

This class represents the metadata set for a ModelMBean element. A
descriptor is part of the ModelMBeanInfo,
ModelMBeanNotificationInfo, ModelMBeanAttributeInfo,
ModelMBeanConstructorInfo, and ModelMBeanParameterInfo.

A descriptor consists of a collection of fields. Each field is in
fieldname=fieldvalue format. Field names are not case sensitive,
case will be preserved on field values.

All field names and values are not predefined. New fields can be
defined and added by any program. Some fields have been predefined
for consistency of implementation and support by the
ModelMBeanInfo, ModelMBeanAttributeInfo, ModelMBeanConstructorInfo,
ModelMBeanNotificationInfo, ModelMBeanOperationInfo and ModelMBean
classes.

The

serialVersionUID

of this class is

-6292969195866300415L

.

**Since:** 1.5
**See Also:** Serialized Form

public class

DescriptorSupport

extends

Object

implements

Descriptor

This class represents the metadata set for a ModelMBean element. A
descriptor is part of the ModelMBeanInfo,
ModelMBeanNotificationInfo, ModelMBeanAttributeInfo,
ModelMBeanConstructorInfo, and ModelMBeanParameterInfo.

A descriptor consists of a collection of fields. Each field is in
fieldname=fieldvalue format. Field names are not case sensitive,
case will be preserved on field values.

All field names and values are not predefined. New fields can be
defined and added by any program. Some fields have been predefined
for consistency of implementation and support by the
ModelMBeanInfo, ModelMBeanAttributeInfo, ModelMBeanConstructorInfo,
ModelMBeanNotificationInfo, ModelMBeanOperationInfo and ModelMBean
classes.

The

serialVersionUID

of this class is

-6292969195866300415L

.

A descriptor consists of a collection of fields. Each field is in
fieldname=fieldvalue format. Field names are not case sensitive,
case will be preserved on field values.

All field names and values are not predefined. New fields can be
defined and added by any program. Some fields have been predefined
for consistency of implementation and support by the
ModelMBeanInfo, ModelMBeanAttributeInfo, ModelMBeanConstructorInfo,
ModelMBeanNotificationInfo, ModelMBeanOperationInfo and ModelMBean
classes.

The

serialVersionUID

of this class is

-6292969195866300415L

.

All field names and values are not predefined. New fields can be
defined and added by any program. Some fields have been predefined
for consistency of implementation and support by the
ModelMBeanInfo, ModelMBeanAttributeInfo, ModelMBeanConstructorInfo,
ModelMBeanNotificationInfo, ModelMBeanOperationInfo and ModelMBean
classes.

The

serialVersionUID

of this class is

-6292969195866300415L

.

The

serialVersionUID

of this class is

-6292969195866300415L

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DescriptorSupport

()

Descriptor default constructor.

DescriptorSupport

​(int initNumFields)

Descriptor constructor.

DescriptorSupport

​(

String

inStr)

Descriptor constructor taking an XML String.

DescriptorSupport

​(

String

... fields)

Constructor taking fields in the

fieldName=fieldValue

format.

DescriptorSupport

​(

String

[] fieldNames,

Object

[] fieldValues)

Constructor taking field names and field values.

DescriptorSupport

​(

DescriptorSupport

inDescr)

Descriptor constructor taking a Descriptor as parameter.

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

Returns a new Descriptor which is a duplicate of the Descriptor.

boolean

equals

​(

Object

o)

Compares this descriptor to the given object.

int

hashCode

()

Returns the hash code value for this descriptor.

boolean

isValid

()

Returns true if all of the fields have legal values given their
names.

String

toString

()

Returns a human readable string representing the
descriptor.

String

toXMLString

()

Returns an XML String representing the descriptor.

- Methods declared in class java.lang.

Object

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

- Methods declared in interface javax.management.

Descriptor

getFieldNames

,

getFields

,

getFieldValue

,

getFieldValues

,

removeField

,

setField

,

setFields

Constructor Summary

Constructors

Constructor

Description

DescriptorSupport

()

Descriptor default constructor.

DescriptorSupport

​(int initNumFields)

Descriptor constructor.

DescriptorSupport

​(

String

inStr)

Descriptor constructor taking an XML String.

DescriptorSupport

​(

String

... fields)

Constructor taking fields in the

fieldName=fieldValue

format.

DescriptorSupport

​(

String

[] fieldNames,

Object

[] fieldValues)

Constructor taking field names and field values.

DescriptorSupport

​(

DescriptorSupport

inDescr)

Descriptor constructor taking a Descriptor as parameter.

---

#### Constructor Summary

Descriptor default constructor.

Descriptor constructor.

Descriptor constructor taking an XML String.

Constructor taking fields in the

fieldName=fieldValue

format.

Constructor taking field names and field values.

Descriptor constructor taking a Descriptor as parameter.

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

Returns a new Descriptor which is a duplicate of the Descriptor.

boolean

equals

​(

Object

o)

Compares this descriptor to the given object.

int

hashCode

()

Returns the hash code value for this descriptor.

boolean

isValid

()

Returns true if all of the fields have legal values given their
names.

String

toString

()

Returns a human readable string representing the
descriptor.

String

toXMLString

()

Returns an XML String representing the descriptor.

- Methods declared in class java.lang.

Object

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

- Methods declared in interface javax.management.

Descriptor

getFieldNames

,

getFields

,

getFieldValue

,

getFieldValues

,

removeField

,

setField

,

setFields

---

#### Method Summary

Returns a new Descriptor which is a duplicate of the Descriptor.

Compares this descriptor to the given object.

Returns the hash code value for this descriptor.

Returns true if all of the fields have legal values given their
names.

Returns a human readable string representing the
descriptor.

Returns an XML String representing the descriptor.

Methods declared in class java.lang.

Object

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

Methods declared in interface javax.management.

Descriptor

getFieldNames

,

getFields

,

getFieldValue

,

getFieldValues

,

removeField

,

setField

,

setFields

---

#### Methods declared in interface javax.management. Descriptor

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DescriptorSupport

```java
public DescriptorSupport()
```

Descriptor default constructor.
Default initial descriptor size is 20. It will grow as needed.

Note that the created empty descriptor is not a valid descriptor
(the method

isValid

returns

false

)

- DescriptorSupport

```java
public DescriptorSupport​(int initNumFields)
throws
MBeanException
,

RuntimeOperationsException
```

Descriptor constructor. Takes as parameter the initial
capacity of the Map that stores the descriptor fields.
Capacity will grow as needed.

Note that the created empty
descriptor is not a valid descriptor (the method

isValid

returns

false

).

**Parameters:** initNumFields

- The initial capacity of the Map that
stores the descriptor fields.
**Throws:** RuntimeOperationsException

- for illegal value for
initNumFields (<= 0)
**Throws:** MBeanException

- Wraps a distributed communication Exception.

- DescriptorSupport

```java
public DescriptorSupport​(
DescriptorSupport
inDescr)
```

Descriptor constructor taking a Descriptor as parameter.
Creates a new descriptor initialized to the values of the
descriptor passed in parameter.

**Parameters:** inDescr

- the descriptor to be used to initialize the
constructed descriptor. If it is null or contains no descriptor
fields, an empty Descriptor will be created.

- DescriptorSupport

```java
public DescriptorSupport​(
String
inStr)
throws
MBeanException
,

RuntimeOperationsException
,

XMLParseException
```

Descriptor constructor taking an XML String.

The format of the XML string is not defined, but an
implementation must ensure that the string returned by

toXMLString()

on an existing
descriptor can be used to instantiate an equivalent
descriptor using this constructor.

In this implementation, all field values will be created
as Strings. If the field values are not Strings, the
programmer will have to reset or convert these fields
correctly.

**Parameters:** inStr

- An XML-formatted string used to populate this
Descriptor. The format is not defined, but any
implementation must ensure that the string returned by
method

toXMLString

on an existing
descriptor can be used to instantiate an equivalent
descriptor when instantiated using this constructor.
**Throws:** RuntimeOperationsException

- If the String inStr
passed in parameter is null
**Throws:** XMLParseException

- XML parsing problem while parsing
the input String
**Throws:** MBeanException

- Wraps a distributed communication Exception.

- DescriptorSupport

```java
public DescriptorSupport​(
String
[] fieldNames,

Object
[] fieldValues)
throws
RuntimeOperationsException
```

Constructor taking field names and field values. Neither array
can be null.

**Parameters:** fieldNames

- String array of field names. No elements of
this array can be null.
**Parameters:** fieldValues

- Object array of the corresponding field
values. Elements of the array can be null. The

fieldValue

must be valid for the

fieldName

(as defined in method

isValid

)

Note: array sizes of parameters should match. If both arrays
are empty, then an empty descriptor is created.
**Throws:** RuntimeOperationsException

- for illegal value for
field Names or field Values. The array lengths must be equal.
If the descriptor construction fails for any reason, this
exception will be thrown.

- DescriptorSupport

```java
public DescriptorSupport​(
String
... fields)
```

Constructor taking fields in the

fieldName=fieldValue

format.

**Parameters:** fields

- String array with each element containing a
field name and value. If this array is null or empty, then the
default constructor will be executed. Null strings or empty
strings will be ignored.

All field values should be Strings. If the field values are
not Strings, the programmer will have to reset or convert these
fields correctly.

Note: Each string should be of the form

fieldName=fieldValue

. The field name
ends at the first

=

character; for example if the String
is

a=b=c

then the field name is

a

and its value
is

b=c

.
**Throws:** RuntimeOperationsException

- for illegal value for
field Names or field Values. The field must contain an
"=". "=fieldValue", "fieldName", and "fieldValue" are illegal.
FieldName cannot be null. "fieldName=" will cause the value to
be null. If the descriptor construction fails for any reason,
this exception will be thrown.

============ METHOD DETAIL ==========

- Method Detail

- clone

```java
public
Object
clone()
throws
RuntimeOperationsException
```

Returns a new Descriptor which is a duplicate of the Descriptor.

**Specified by:** clone

in interface

Descriptor
**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** RuntimeOperationsException

- for illegal value for
field Names or field Values. If the descriptor construction
fails for any reason, this exception will be thrown.
**See Also:** Cloneable

- equals

```java
public boolean equals​(
Object
o)
```

Compares this descriptor to the given object. The objects are equal if
the given object is also a Descriptor, and if the two Descriptors have
the same field names (possibly differing in case) and the same
associated values. The respective values for a field in the two
Descriptors are equal if the following conditions hold:

- If one value is null then the other must be too.
- If one value is a primitive array then the other must be a primitive
array of the same type with the same elements.
- If one value is an object array then the other must be too and

Arrays.deepEquals

must return true.
- Otherwise

Object.equals(Object)

must return true.

**Specified by:** equals

in interface

Descriptor
**Overrides:** equals

in class

Object
**Parameters:** o

- the object to compare with.
**Returns:** true

if the objects are the same;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this descriptor. The hash
code is computed as the sum of the hash codes for each field in
the descriptor. The hash code of a field with name

n

and value

v

is

n.toLowerCase().hashCode() ^ h

.
Here

h

is the hash code of

v

, computed as
follows:

- If

v

is null then

h

is 0.
- If

v

is a primitive array then

h

is computed using
the appropriate overloading of

java.util.Arrays.hashCode

.
- If

v

is an object array then

h

is computed using

Arrays.deepHashCode

.
- Otherwise

h

is

v.hashCode()

.

**Specified by:** hashCode

in interface

Descriptor
**Overrides:** hashCode

in class

Object
**Returns:** A hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- isValid

```java
public boolean isValid()
throws
RuntimeOperationsException
```

Returns true if all of the fields have legal values given their
names.

This implementation does not support interoperating with a directory
or lookup service. Thus, conforming to the specification, no checking is
done on the

"export"

field.

Otherwise this implementation returns false if:

- name and descriptorType fieldNames are not defined, or
null, or empty, or not String

class, role, getMethod, setMethod fieldNames, if defined,
are null or not String

persistPeriod, currencyTimeLimit, lastUpdatedTimeStamp,
lastReturnedTimeStamp if defined, are null, or not a Numeric
String or not a Numeric Value >= -1

log fieldName, if defined, is null, or not a Boolean or
not a String with value "t", "f", "true", "false". These String
values must not be case sensitive.

visibility fieldName, if defined, is null, or not a
Numeric String or a not Numeric Value >= 1 and <= 4

severity fieldName, if defined, is null, or not a Numeric
String or not a Numeric Value >= 0 and <= 6

persistPolicy fieldName, if defined, is null, or not one of
the following strings:

"OnUpdate", "OnTimer", "NoMoreOftenThan", "OnUnregister", "Always",
"Never". These String values must not be case sensitive.

**Specified by:** isValid

in interface

Descriptor
**Returns:** true if the values are legal.
**Throws:** RuntimeOperationsException

- If the validity checking
fails for any reason, this exception will be thrown.

- toXMLString

```java
public
String
toXMLString()
```

Returns an XML String representing the descriptor.

The format is not defined, but an implementation must
ensure that the string returned by this method can be
used to build an equivalent descriptor when instantiated
using the constructor

DescriptorSupport(String inStr)

.

Fields which are not String objects will have toString()
called on them to create the value. The value will be
enclosed in parentheses. It is not guaranteed that you can
reconstruct these objects unless they have been
specifically set up to support toString() in a meaningful
format and have a matching constructor that accepts a
String in the same format.

If the descriptor is empty the following String is
returned: <Descriptor></Descriptor>

**Returns:** the XML string.
**Throws:** RuntimeOperationsException

- for illegal value for
field Names or field Values. If the XML formatted string
construction fails for any reason, this exception will be
thrown.

- toString

```java
public
String
toString()
```

Returns a human readable string representing the
descriptor. The string will be in the format of
"fieldName=fieldValue,fieldName2=fieldValue2,..."

If there are no fields in the descriptor, then an empty String
is returned.

If a fieldValue is an object then the toString() method is
called on it and its returned value is used as the value for
the field enclosed in parenthesis.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.
**Throws:** RuntimeOperationsException

- for illegal value for
field Names or field Values. If the descriptor string fails
for any reason, this exception will be thrown.

Constructor Detail

- DescriptorSupport

```java
public DescriptorSupport()
```

Descriptor default constructor.
Default initial descriptor size is 20. It will grow as needed.

Note that the created empty descriptor is not a valid descriptor
(the method

isValid

returns

false

)

- DescriptorSupport

```java
public DescriptorSupport​(int initNumFields)
throws
MBeanException
,

RuntimeOperationsException
```

Descriptor constructor. Takes as parameter the initial
capacity of the Map that stores the descriptor fields.
Capacity will grow as needed.

Note that the created empty
descriptor is not a valid descriptor (the method

isValid

returns

false

).

**Parameters:** initNumFields

- The initial capacity of the Map that
stores the descriptor fields.
**Throws:** RuntimeOperationsException

- for illegal value for
initNumFields (<= 0)
**Throws:** MBeanException

- Wraps a distributed communication Exception.

- DescriptorSupport

```java
public DescriptorSupport​(
DescriptorSupport
inDescr)
```

Descriptor constructor taking a Descriptor as parameter.
Creates a new descriptor initialized to the values of the
descriptor passed in parameter.

**Parameters:** inDescr

- the descriptor to be used to initialize the
constructed descriptor. If it is null or contains no descriptor
fields, an empty Descriptor will be created.

- DescriptorSupport

```java
public DescriptorSupport​(
String
inStr)
throws
MBeanException
,

RuntimeOperationsException
,

XMLParseException
```

Descriptor constructor taking an XML String.

The format of the XML string is not defined, but an
implementation must ensure that the string returned by

toXMLString()

on an existing
descriptor can be used to instantiate an equivalent
descriptor using this constructor.

In this implementation, all field values will be created
as Strings. If the field values are not Strings, the
programmer will have to reset or convert these fields
correctly.

**Parameters:** inStr

- An XML-formatted string used to populate this
Descriptor. The format is not defined, but any
implementation must ensure that the string returned by
method

toXMLString

on an existing
descriptor can be used to instantiate an equivalent
descriptor when instantiated using this constructor.
**Throws:** RuntimeOperationsException

- If the String inStr
passed in parameter is null
**Throws:** XMLParseException

- XML parsing problem while parsing
the input String
**Throws:** MBeanException

- Wraps a distributed communication Exception.

- DescriptorSupport

```java
public DescriptorSupport​(
String
[] fieldNames,

Object
[] fieldValues)
throws
RuntimeOperationsException
```

Constructor taking field names and field values. Neither array
can be null.

**Parameters:** fieldNames

- String array of field names. No elements of
this array can be null.
**Parameters:** fieldValues

- Object array of the corresponding field
values. Elements of the array can be null. The

fieldValue

must be valid for the

fieldName

(as defined in method

isValid

)

Note: array sizes of parameters should match. If both arrays
are empty, then an empty descriptor is created.
**Throws:** RuntimeOperationsException

- for illegal value for
field Names or field Values. The array lengths must be equal.
If the descriptor construction fails for any reason, this
exception will be thrown.

- DescriptorSupport

```java
public DescriptorSupport​(
String
... fields)
```

Constructor taking fields in the

fieldName=fieldValue

format.

**Parameters:** fields

- String array with each element containing a
field name and value. If this array is null or empty, then the
default constructor will be executed. Null strings or empty
strings will be ignored.

All field values should be Strings. If the field values are
not Strings, the programmer will have to reset or convert these
fields correctly.

Note: Each string should be of the form

fieldName=fieldValue

. The field name
ends at the first

=

character; for example if the String
is

a=b=c

then the field name is

a

and its value
is

b=c

.
**Throws:** RuntimeOperationsException

- for illegal value for
field Names or field Values. The field must contain an
"=". "=fieldValue", "fieldName", and "fieldValue" are illegal.
FieldName cannot be null. "fieldName=" will cause the value to
be null. If the descriptor construction fails for any reason,
this exception will be thrown.

---

#### Constructor Detail

DescriptorSupport

```java
public DescriptorSupport()
```

Descriptor default constructor.
Default initial descriptor size is 20. It will grow as needed.

Note that the created empty descriptor is not a valid descriptor
(the method

isValid

returns

false

)

---

#### DescriptorSupport

public DescriptorSupport()

Descriptor default constructor.
Default initial descriptor size is 20. It will grow as needed.

Note that the created empty descriptor is not a valid descriptor
(the method

isValid

returns

false

)

DescriptorSupport

```java
public DescriptorSupport​(int initNumFields)
throws
MBeanException
,

RuntimeOperationsException
```

Descriptor constructor. Takes as parameter the initial
capacity of the Map that stores the descriptor fields.
Capacity will grow as needed.

Note that the created empty
descriptor is not a valid descriptor (the method

isValid

returns

false

).

**Parameters:** initNumFields

- The initial capacity of the Map that
stores the descriptor fields.
**Throws:** RuntimeOperationsException

- for illegal value for
initNumFields (<= 0)
**Throws:** MBeanException

- Wraps a distributed communication Exception.

---

#### DescriptorSupport

public DescriptorSupport​(int initNumFields)
throws

MBeanException

,

RuntimeOperationsException

Descriptor constructor. Takes as parameter the initial
capacity of the Map that stores the descriptor fields.
Capacity will grow as needed.

Note that the created empty
descriptor is not a valid descriptor (the method

isValid

returns

false

).

DescriptorSupport

```java
public DescriptorSupport​(
DescriptorSupport
inDescr)
```

Descriptor constructor taking a Descriptor as parameter.
Creates a new descriptor initialized to the values of the
descriptor passed in parameter.

**Parameters:** inDescr

- the descriptor to be used to initialize the
constructed descriptor. If it is null or contains no descriptor
fields, an empty Descriptor will be created.

---

#### DescriptorSupport

public DescriptorSupport​(

DescriptorSupport

inDescr)

Descriptor constructor taking a Descriptor as parameter.
Creates a new descriptor initialized to the values of the
descriptor passed in parameter.

DescriptorSupport

```java
public DescriptorSupport​(
String
inStr)
throws
MBeanException
,

RuntimeOperationsException
,

XMLParseException
```

Descriptor constructor taking an XML String.

The format of the XML string is not defined, but an
implementation must ensure that the string returned by

toXMLString()

on an existing
descriptor can be used to instantiate an equivalent
descriptor using this constructor.

In this implementation, all field values will be created
as Strings. If the field values are not Strings, the
programmer will have to reset or convert these fields
correctly.

**Parameters:** inStr

- An XML-formatted string used to populate this
Descriptor. The format is not defined, but any
implementation must ensure that the string returned by
method

toXMLString

on an existing
descriptor can be used to instantiate an equivalent
descriptor when instantiated using this constructor.
**Throws:** RuntimeOperationsException

- If the String inStr
passed in parameter is null
**Throws:** XMLParseException

- XML parsing problem while parsing
the input String
**Throws:** MBeanException

- Wraps a distributed communication Exception.

---

#### DescriptorSupport

public DescriptorSupport​(

String

inStr)
throws

MBeanException

,

RuntimeOperationsException

,

XMLParseException

Descriptor constructor taking an XML String.

The format of the XML string is not defined, but an
implementation must ensure that the string returned by

toXMLString()

on an existing
descriptor can be used to instantiate an equivalent
descriptor using this constructor.

In this implementation, all field values will be created
as Strings. If the field values are not Strings, the
programmer will have to reset or convert these fields
correctly.

Descriptor constructor taking an XML String.

The format of the XML string is not defined, but an
implementation must ensure that the string returned by

toXMLString()

on an existing
descriptor can be used to instantiate an equivalent
descriptor using this constructor.

In this implementation, all field values will be created
as Strings. If the field values are not Strings, the
programmer will have to reset or convert these fields
correctly.

DescriptorSupport

```java
public DescriptorSupport​(
String
[] fieldNames,

Object
[] fieldValues)
throws
RuntimeOperationsException
```

Constructor taking field names and field values. Neither array
can be null.

**Parameters:** fieldNames

- String array of field names. No elements of
this array can be null.
**Parameters:** fieldValues

- Object array of the corresponding field
values. Elements of the array can be null. The

fieldValue

must be valid for the

fieldName

(as defined in method

isValid

)

Note: array sizes of parameters should match. If both arrays
are empty, then an empty descriptor is created.
**Throws:** RuntimeOperationsException

- for illegal value for
field Names or field Values. The array lengths must be equal.
If the descriptor construction fails for any reason, this
exception will be thrown.

---

#### DescriptorSupport

public DescriptorSupport​(

String

[] fieldNames,

Object

[] fieldValues)
throws

RuntimeOperationsException

Constructor taking field names and field values. Neither array
can be null.

Note: array sizes of parameters should match. If both arrays
are empty, then an empty descriptor is created.

DescriptorSupport

```java
public DescriptorSupport​(
String
... fields)
```

Constructor taking fields in the

fieldName=fieldValue

format.

**Parameters:** fields

- String array with each element containing a
field name and value. If this array is null or empty, then the
default constructor will be executed. Null strings or empty
strings will be ignored.

All field values should be Strings. If the field values are
not Strings, the programmer will have to reset or convert these
fields correctly.

Note: Each string should be of the form

fieldName=fieldValue

. The field name
ends at the first

=

character; for example if the String
is

a=b=c

then the field name is

a

and its value
is

b=c

.
**Throws:** RuntimeOperationsException

- for illegal value for
field Names or field Values. The field must contain an
"=". "=fieldValue", "fieldName", and "fieldValue" are illegal.
FieldName cannot be null. "fieldName=" will cause the value to
be null. If the descriptor construction fails for any reason,
this exception will be thrown.

---

#### DescriptorSupport

public DescriptorSupport​(

String

... fields)

Constructor taking fields in the

fieldName=fieldValue

format.

All field values should be Strings. If the field values are
not Strings, the programmer will have to reset or convert these
fields correctly.

Note: Each string should be of the form

fieldName=fieldValue

. The field name
ends at the first

=

character; for example if the String
is

a=b=c

then the field name is

a

and its value
is

b=c

.

Note: Each string should be of the form

fieldName=fieldValue

. The field name
ends at the first

=

character; for example if the String
is

a=b=c

then the field name is

a

and its value
is

b=c

.

Method Detail

- clone

```java
public
Object
clone()
throws
RuntimeOperationsException
```

Returns a new Descriptor which is a duplicate of the Descriptor.

**Specified by:** clone

in interface

Descriptor
**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** RuntimeOperationsException

- for illegal value for
field Names or field Values. If the descriptor construction
fails for any reason, this exception will be thrown.
**See Also:** Cloneable

- equals

```java
public boolean equals​(
Object
o)
```

Compares this descriptor to the given object. The objects are equal if
the given object is also a Descriptor, and if the two Descriptors have
the same field names (possibly differing in case) and the same
associated values. The respective values for a field in the two
Descriptors are equal if the following conditions hold:

- If one value is null then the other must be too.
- If one value is a primitive array then the other must be a primitive
array of the same type with the same elements.
- If one value is an object array then the other must be too and

Arrays.deepEquals

must return true.
- Otherwise

Object.equals(Object)

must return true.

**Specified by:** equals

in interface

Descriptor
**Overrides:** equals

in class

Object
**Parameters:** o

- the object to compare with.
**Returns:** true

if the objects are the same;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this descriptor. The hash
code is computed as the sum of the hash codes for each field in
the descriptor. The hash code of a field with name

n

and value

v

is

n.toLowerCase().hashCode() ^ h

.
Here

h

is the hash code of

v

, computed as
follows:

- If

v

is null then

h

is 0.
- If

v

is a primitive array then

h

is computed using
the appropriate overloading of

java.util.Arrays.hashCode

.
- If

v

is an object array then

h

is computed using

Arrays.deepHashCode

.
- Otherwise

h

is

v.hashCode()

.

**Specified by:** hashCode

in interface

Descriptor
**Overrides:** hashCode

in class

Object
**Returns:** A hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- isValid

```java
public boolean isValid()
throws
RuntimeOperationsException
```

Returns true if all of the fields have legal values given their
names.

This implementation does not support interoperating with a directory
or lookup service. Thus, conforming to the specification, no checking is
done on the

"export"

field.

Otherwise this implementation returns false if:

- name and descriptorType fieldNames are not defined, or
null, or empty, or not String

class, role, getMethod, setMethod fieldNames, if defined,
are null or not String

persistPeriod, currencyTimeLimit, lastUpdatedTimeStamp,
lastReturnedTimeStamp if defined, are null, or not a Numeric
String or not a Numeric Value >= -1

log fieldName, if defined, is null, or not a Boolean or
not a String with value "t", "f", "true", "false". These String
values must not be case sensitive.

visibility fieldName, if defined, is null, or not a
Numeric String or a not Numeric Value >= 1 and <= 4

severity fieldName, if defined, is null, or not a Numeric
String or not a Numeric Value >= 0 and <= 6

persistPolicy fieldName, if defined, is null, or not one of
the following strings:

"OnUpdate", "OnTimer", "NoMoreOftenThan", "OnUnregister", "Always",
"Never". These String values must not be case sensitive.

**Specified by:** isValid

in interface

Descriptor
**Returns:** true if the values are legal.
**Throws:** RuntimeOperationsException

- If the validity checking
fails for any reason, this exception will be thrown.

- toXMLString

```java
public
String
toXMLString()
```

Returns an XML String representing the descriptor.

The format is not defined, but an implementation must
ensure that the string returned by this method can be
used to build an equivalent descriptor when instantiated
using the constructor

DescriptorSupport(String inStr)

.

Fields which are not String objects will have toString()
called on them to create the value. The value will be
enclosed in parentheses. It is not guaranteed that you can
reconstruct these objects unless they have been
specifically set up to support toString() in a meaningful
format and have a matching constructor that accepts a
String in the same format.

If the descriptor is empty the following String is
returned: <Descriptor></Descriptor>

**Returns:** the XML string.
**Throws:** RuntimeOperationsException

- for illegal value for
field Names or field Values. If the XML formatted string
construction fails for any reason, this exception will be
thrown.

- toString

```java
public
String
toString()
```

Returns a human readable string representing the
descriptor. The string will be in the format of
"fieldName=fieldValue,fieldName2=fieldValue2,..."

If there are no fields in the descriptor, then an empty String
is returned.

If a fieldValue is an object then the toString() method is
called on it and its returned value is used as the value for
the field enclosed in parenthesis.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.
**Throws:** RuntimeOperationsException

- for illegal value for
field Names or field Values. If the descriptor string fails
for any reason, this exception will be thrown.

---

#### Method Detail

clone

```java
public
Object
clone()
throws
RuntimeOperationsException
```

Returns a new Descriptor which is a duplicate of the Descriptor.

**Specified by:** clone

in interface

Descriptor
**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** RuntimeOperationsException

- for illegal value for
field Names or field Values. If the descriptor construction
fails for any reason, this exception will be thrown.
**See Also:** Cloneable

---

#### clone

public

Object

clone()
throws

RuntimeOperationsException

Returns a new Descriptor which is a duplicate of the Descriptor.

equals

```java
public boolean equals​(
Object
o)
```

Compares this descriptor to the given object. The objects are equal if
the given object is also a Descriptor, and if the two Descriptors have
the same field names (possibly differing in case) and the same
associated values. The respective values for a field in the two
Descriptors are equal if the following conditions hold:

- If one value is null then the other must be too.
- If one value is a primitive array then the other must be a primitive
array of the same type with the same elements.
- If one value is an object array then the other must be too and

Arrays.deepEquals

must return true.
- Otherwise

Object.equals(Object)

must return true.

**Specified by:** equals

in interface

Descriptor
**Overrides:** equals

in class

Object
**Parameters:** o

- the object to compare with.
**Returns:** true

if the objects are the same;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Compares this descriptor to the given object. The objects are equal if
the given object is also a Descriptor, and if the two Descriptors have
the same field names (possibly differing in case) and the same
associated values. The respective values for a field in the two
Descriptors are equal if the following conditions hold:

- If one value is null then the other must be too.
- If one value is a primitive array then the other must be a primitive
array of the same type with the same elements.
- If one value is an object array then the other must be too and

Arrays.deepEquals

must return true.
- Otherwise

Object.equals(Object)

must return true.

If one value is null then the other must be too.

If one value is a primitive array then the other must be a primitive
array of the same type with the same elements.

If one value is an object array then the other must be too and

Arrays.deepEquals

must return true.

Otherwise

Object.equals(Object)

must return true.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this descriptor. The hash
code is computed as the sum of the hash codes for each field in
the descriptor. The hash code of a field with name

n

and value

v

is

n.toLowerCase().hashCode() ^ h

.
Here

h

is the hash code of

v

, computed as
follows:

- If

v

is null then

h

is 0.
- If

v

is a primitive array then

h

is computed using
the appropriate overloading of

java.util.Arrays.hashCode

.
- If

v

is an object array then

h

is computed using

Arrays.deepHashCode

.
- Otherwise

h

is

v.hashCode()

.

**Specified by:** hashCode

in interface

Descriptor
**Overrides:** hashCode

in class

Object
**Returns:** A hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this descriptor. The hash
code is computed as the sum of the hash codes for each field in
the descriptor. The hash code of a field with name

n

and value

v

is

n.toLowerCase().hashCode() ^ h

.
Here

h

is the hash code of

v

, computed as
follows:

- If

v

is null then

h

is 0.
- If

v

is a primitive array then

h

is computed using
the appropriate overloading of

java.util.Arrays.hashCode

.
- If

v

is an object array then

h

is computed using

Arrays.deepHashCode

.
- Otherwise

h

is

v.hashCode()

.

Returns the hash code value for this descriptor. The hash
code is computed as the sum of the hash codes for each field in
the descriptor. The hash code of a field with name

n

and value

v

is

n.toLowerCase().hashCode() ^ h

.
Here

h

is the hash code of

v

, computed as
follows:

If

v

is null then

h

is 0.

If

v

is a primitive array then

h

is computed using
the appropriate overloading of

java.util.Arrays.hashCode

.

If

v

is an object array then

h

is computed using

Arrays.deepHashCode

.

Otherwise

h

is

v.hashCode()

.

isValid

```java
public boolean isValid()
throws
RuntimeOperationsException
```

Returns true if all of the fields have legal values given their
names.

This implementation does not support interoperating with a directory
or lookup service. Thus, conforming to the specification, no checking is
done on the

"export"

field.

Otherwise this implementation returns false if:

- name and descriptorType fieldNames are not defined, or
null, or empty, or not String

class, role, getMethod, setMethod fieldNames, if defined,
are null or not String

persistPeriod, currencyTimeLimit, lastUpdatedTimeStamp,
lastReturnedTimeStamp if defined, are null, or not a Numeric
String or not a Numeric Value >= -1

log fieldName, if defined, is null, or not a Boolean or
not a String with value "t", "f", "true", "false". These String
values must not be case sensitive.

visibility fieldName, if defined, is null, or not a
Numeric String or a not Numeric Value >= 1 and <= 4

severity fieldName, if defined, is null, or not a Numeric
String or not a Numeric Value >= 0 and <= 6

persistPolicy fieldName, if defined, is null, or not one of
the following strings:

"OnUpdate", "OnTimer", "NoMoreOftenThan", "OnUnregister", "Always",
"Never". These String values must not be case sensitive.

**Specified by:** isValid

in interface

Descriptor
**Returns:** true if the values are legal.
**Throws:** RuntimeOperationsException

- If the validity checking
fails for any reason, this exception will be thrown.

---

#### isValid

public boolean isValid()
throws

RuntimeOperationsException

Returns true if all of the fields have legal values given their
names.

This implementation does not support interoperating with a directory
or lookup service. Thus, conforming to the specification, no checking is
done on the

"export"

field.

Otherwise this implementation returns false if:

- name and descriptorType fieldNames are not defined, or
null, or empty, or not String

class, role, getMethod, setMethod fieldNames, if defined,
are null or not String

persistPeriod, currencyTimeLimit, lastUpdatedTimeStamp,
lastReturnedTimeStamp if defined, are null, or not a Numeric
String or not a Numeric Value >= -1

log fieldName, if defined, is null, or not a Boolean or
not a String with value "t", "f", "true", "false". These String
values must not be case sensitive.

visibility fieldName, if defined, is null, or not a
Numeric String or a not Numeric Value >= 1 and <= 4

severity fieldName, if defined, is null, or not a Numeric
String or not a Numeric Value >= 0 and <= 6

persistPolicy fieldName, if defined, is null, or not one of
the following strings:

"OnUpdate", "OnTimer", "NoMoreOftenThan", "OnUnregister", "Always",
"Never". These String values must not be case sensitive.

This implementation does not support interoperating with a directory
or lookup service. Thus, conforming to the specification, no checking is
done on the

"export"

field.

Otherwise this implementation returns false if:

- name and descriptorType fieldNames are not defined, or
null, or empty, or not String

class, role, getMethod, setMethod fieldNames, if defined,
are null or not String

persistPeriod, currencyTimeLimit, lastUpdatedTimeStamp,
lastReturnedTimeStamp if defined, are null, or not a Numeric
String or not a Numeric Value >= -1

log fieldName, if defined, is null, or not a Boolean or
not a String with value "t", "f", "true", "false". These String
values must not be case sensitive.

visibility fieldName, if defined, is null, or not a
Numeric String or a not Numeric Value >= 1 and <= 4

severity fieldName, if defined, is null, or not a Numeric
String or not a Numeric Value >= 0 and <= 6

persistPolicy fieldName, if defined, is null, or not one of
the following strings:

"OnUpdate", "OnTimer", "NoMoreOftenThan", "OnUnregister", "Always",
"Never". These String values must not be case sensitive.

Otherwise this implementation returns false if:

- name and descriptorType fieldNames are not defined, or
null, or empty, or not String

class, role, getMethod, setMethod fieldNames, if defined,
are null or not String

persistPeriod, currencyTimeLimit, lastUpdatedTimeStamp,
lastReturnedTimeStamp if defined, are null, or not a Numeric
String or not a Numeric Value >= -1

log fieldName, if defined, is null, or not a Boolean or
not a String with value "t", "f", "true", "false". These String
values must not be case sensitive.

visibility fieldName, if defined, is null, or not a
Numeric String or a not Numeric Value >= 1 and <= 4

severity fieldName, if defined, is null, or not a Numeric
String or not a Numeric Value >= 0 and <= 6

persistPolicy fieldName, if defined, is null, or not one of
the following strings:

"OnUpdate", "OnTimer", "NoMoreOftenThan", "OnUnregister", "Always",
"Never". These String values must not be case sensitive.

name and descriptorType fieldNames are not defined, or
null, or empty, or not String

class, role, getMethod, setMethod fieldNames, if defined,
are null or not String

persistPeriod, currencyTimeLimit, lastUpdatedTimeStamp,
lastReturnedTimeStamp if defined, are null, or not a Numeric
String or not a Numeric Value >= -1

log fieldName, if defined, is null, or not a Boolean or
not a String with value "t", "f", "true", "false". These String
values must not be case sensitive.

visibility fieldName, if defined, is null, or not a
Numeric String or a not Numeric Value >= 1 and <= 4

severity fieldName, if defined, is null, or not a Numeric
String or not a Numeric Value >= 0 and <= 6

persistPolicy fieldName, if defined, is null, or not one of
the following strings:

"OnUpdate", "OnTimer", "NoMoreOftenThan", "OnUnregister", "Always",
"Never". These String values must not be case sensitive.

toXMLString

```java
public
String
toXMLString()
```

Returns an XML String representing the descriptor.

The format is not defined, but an implementation must
ensure that the string returned by this method can be
used to build an equivalent descriptor when instantiated
using the constructor

DescriptorSupport(String inStr)

.

Fields which are not String objects will have toString()
called on them to create the value. The value will be
enclosed in parentheses. It is not guaranteed that you can
reconstruct these objects unless they have been
specifically set up to support toString() in a meaningful
format and have a matching constructor that accepts a
String in the same format.

If the descriptor is empty the following String is
returned: <Descriptor></Descriptor>

**Returns:** the XML string.
**Throws:** RuntimeOperationsException

- for illegal value for
field Names or field Values. If the XML formatted string
construction fails for any reason, this exception will be
thrown.

---

#### toXMLString

public

String

toXMLString()

Returns an XML String representing the descriptor.

The format is not defined, but an implementation must
ensure that the string returned by this method can be
used to build an equivalent descriptor when instantiated
using the constructor

DescriptorSupport(String inStr)

.

Fields which are not String objects will have toString()
called on them to create the value. The value will be
enclosed in parentheses. It is not guaranteed that you can
reconstruct these objects unless they have been
specifically set up to support toString() in a meaningful
format and have a matching constructor that accepts a
String in the same format.

If the descriptor is empty the following String is
returned: <Descriptor></Descriptor>

Returns an XML String representing the descriptor.

The format is not defined, but an implementation must
ensure that the string returned by this method can be
used to build an equivalent descriptor when instantiated
using the constructor

DescriptorSupport(String inStr)

.

Fields which are not String objects will have toString()
called on them to create the value. The value will be
enclosed in parentheses. It is not guaranteed that you can
reconstruct these objects unless they have been
specifically set up to support toString() in a meaningful
format and have a matching constructor that accepts a
String in the same format.

If the descriptor is empty the following String is
returned: <Descriptor></Descriptor>

toString

```java
public
String
toString()
```

Returns a human readable string representing the
descriptor. The string will be in the format of
"fieldName=fieldValue,fieldName2=fieldValue2,..."

If there are no fields in the descriptor, then an empty String
is returned.

If a fieldValue is an object then the toString() method is
called on it and its returned value is used as the value for
the field enclosed in parenthesis.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.
**Throws:** RuntimeOperationsException

- for illegal value for
field Names or field Values. If the descriptor string fails
for any reason, this exception will be thrown.

---

#### toString

public

String

toString()

Returns a human readable string representing the
descriptor. The string will be in the format of
"fieldName=fieldValue,fieldName2=fieldValue2,..."

If there are no fields in the descriptor, then an empty String
is returned.

If a fieldValue is an object then the toString() method is
called on it and its returned value is used as the value for
the field enclosed in parenthesis.

---

