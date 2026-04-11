# Class IndexedPropertyDescriptor

**Source:** `java.desktop\java\beans\IndexedPropertyDescriptor.html`

### Class Description

```java
public class
IndexedPropertyDescriptor

extends
PropertyDescriptor
```

An IndexedPropertyDescriptor describes a property that acts like an
array and has an indexed read and/or indexed write method to access
specific elements of the array.

An indexed property may also provide simple non-indexed read and write
methods. If these are present, they read and write arrays of the type
returned by the indexed read method.

**Since:** 1.1

---

### Field Details

*No entries found.*

### Constructor Details

#### public IndexedPropertyDescriptor​(
String
propertyName,

Class
<?> beanClass)
throws
IntrospectionException

This constructor constructs an IndexedPropertyDescriptor for a property
that follows the standard Java conventions by having getFoo and setFoo
accessor methods, for both indexed access and array access.

Thus if the argument name is "fred", it will assume that there
is an indexed reader method "getFred", a non-indexed (array) reader
method also called "getFred", an indexed writer method "setFred",
and finally a non-indexed writer method "setFred".

**Parameters:**
- propertyName

- The programmatic name of the property.
- beanClass

- The Class object for the target bean.

**Throws:**
- IntrospectionException

- if an exception occurs during
introspection.

---

#### public IndexedPropertyDescriptor​(
String
propertyName,

Class
<?> beanClass,

String
readMethodName,

String
writeMethodName,

String
indexedReadMethodName,

String
indexedWriteMethodName)
throws
IntrospectionException

This constructor takes the name of a simple property, and method
names for reading and writing the property, both indexed
and non-indexed.

**Parameters:**
- propertyName

- The programmatic name of the property.
- beanClass

- The Class object for the target bean.
- readMethodName

- The name of the method used for reading the property
values as an array. May be null if the property is write-only
or must be indexed.
- writeMethodName

- The name of the method used for writing the property
values as an array. May be null if the property is read-only
or must be indexed.
- indexedReadMethodName

- The name of the method used for reading
an indexed property value.
May be null if the property is write-only.
- indexedWriteMethodName

- The name of the method used for writing
an indexed property value.
May be null if the property is read-only.

**Throws:**
- IntrospectionException

- if an exception occurs during
introspection.

---

#### public IndexedPropertyDescriptor​(
String
propertyName,

Method
readMethod,

Method
writeMethod,

Method
indexedReadMethod,

Method
indexedWriteMethod)
throws
IntrospectionException

This constructor takes the name of a simple property, and Method
objects for reading and writing the property.

**Parameters:**
- propertyName

- The programmatic name of the property.
- readMethod

- The method used for reading the property values as an array.
May be null if the property is write-only or must be indexed.
- writeMethod

- The method used for writing the property values as an array.
May be null if the property is read-only or must be indexed.
- indexedReadMethod

- The method used for reading an indexed property value.
May be null if the property is write-only.
- indexedWriteMethod

- The method used for writing an indexed property value.
May be null if the property is read-only.

**Throws:**
- IntrospectionException

- if an exception occurs during
introspection.

---

### Method Details

#### public
Method
getIndexedReadMethod()

Gets the method that should be used to read an indexed
property value.

**Returns:**
- The method that should be used to read an indexed
property value.
May return null if the property isn't indexed or is write-only.

---

#### public void setIndexedReadMethod​(
Method
readMethod)
throws
IntrospectionException

Sets the method that should be used to read an indexed property value.

**Parameters:**
- readMethod

- The new indexed read method.

**Throws:**
- IntrospectionException

- if an exception occurs during
introspection.

**Since:**
- 1.2

---

#### public
Method
getIndexedWriteMethod()

Gets the method that should be used to write an indexed property value.

**Returns:**
- The method that should be used to write an indexed
property value.
May return null if the property isn't indexed or is read-only.

---

#### public void setIndexedWriteMethod​(
Method
writeMethod)
throws
IntrospectionException

Sets the method that should be used to write an indexed property value.

**Parameters:**
- writeMethod

- The new indexed write method.

**Throws:**
- IntrospectionException

- if an exception occurs during
introspection.

**Since:**
- 1.2

---

#### public
Class
<?> getIndexedPropertyType()

Returns the Java type info for the indexed property.
Note that the

Class

object may describe
primitive Java types such as

int

.
This type is returned by the indexed read method
or is used as the parameter type of the indexed write method.

**Returns:**
- the

Class

object that represents the Java type info,
or

null

if the type cannot be determined

---

#### public boolean equals​(
Object
obj)

Compares this

PropertyDescriptor

against the specified object.
Returns true if the objects are the same. Two

PropertyDescriptor

s
are the same if the read, write, property types, property editor and
flags are equivalent.

**Overrides:**
- equals

in class

PropertyDescriptor

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true

if this object is the same as the obj
argument;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

**Since:**
- 1.4

---

#### public int hashCode()

Returns a hash code value for the object.
See

Object.hashCode()

for a complete description.

**Overrides:**
- hashCode

in class

PropertyDescriptor

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

**Since:**
- 1.5

---

### Additional Sections

#### Class IndexedPropertyDescriptor

java.lang.Object

- java.beans.FeatureDescriptor
- - java.beans.PropertyDescriptor
- - java.beans.IndexedPropertyDescriptor

java.beans.FeatureDescriptor

- java.beans.PropertyDescriptor
- - java.beans.IndexedPropertyDescriptor

java.beans.PropertyDescriptor

- java.beans.IndexedPropertyDescriptor

java.beans.IndexedPropertyDescriptor

```java
public class
IndexedPropertyDescriptor

extends
PropertyDescriptor
```

An IndexedPropertyDescriptor describes a property that acts like an
array and has an indexed read and/or indexed write method to access
specific elements of the array.

An indexed property may also provide simple non-indexed read and write
methods. If these are present, they read and write arrays of the type
returned by the indexed read method.

**Since:** 1.1

public class

IndexedPropertyDescriptor

extends

PropertyDescriptor

An IndexedPropertyDescriptor describes a property that acts like an
array and has an indexed read and/or indexed write method to access
specific elements of the array.

An indexed property may also provide simple non-indexed read and write
methods. If these are present, they read and write arrays of the type
returned by the indexed read method.

An indexed property may also provide simple non-indexed read and write
methods. If these are present, they read and write arrays of the type
returned by the indexed read method.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

IndexedPropertyDescriptor

​(

String

propertyName,

Class

<?> beanClass)

This constructor constructs an IndexedPropertyDescriptor for a property
that follows the standard Java conventions by having getFoo and setFoo
accessor methods, for both indexed access and array access.

IndexedPropertyDescriptor

​(

String

propertyName,

Class

<?> beanClass,

String

readMethodName,

String

writeMethodName,

String

indexedReadMethodName,

String

indexedWriteMethodName)

This constructor takes the name of a simple property, and method
names for reading and writing the property, both indexed
and non-indexed.

IndexedPropertyDescriptor

​(

String

propertyName,

Method

readMethod,

Method

writeMethod,

Method

indexedReadMethod,

Method

indexedWriteMethod)

This constructor takes the name of a simple property, and Method
objects for reading and writing the property.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares this

PropertyDescriptor

against the specified object.

Class

<?>

getIndexedPropertyType

()

Returns the Java type info for the indexed property.

Method

getIndexedReadMethod

()

Gets the method that should be used to read an indexed
property value.

Method

getIndexedWriteMethod

()

Gets the method that should be used to write an indexed property value.

int

hashCode

()

Returns a hash code value for the object.

void

setIndexedReadMethod

​(

Method

readMethod)

Sets the method that should be used to read an indexed property value.

void

setIndexedWriteMethod

​(

Method

writeMethod)

Sets the method that should be used to write an indexed property value.

- Methods declared in class java.beans.

PropertyDescriptor

createPropertyEditor

,

getPropertyEditorClass

,

getPropertyType

,

getReadMethod

,

getWriteMethod

,

isBound

,

isConstrained

,

setBound

,

setConstrained

,

setPropertyEditorClass

,

setReadMethod

,

setWriteMethod

- Methods declared in class java.beans.

FeatureDescriptor

attributeNames

,

getDisplayName

,

getName

,

getShortDescription

,

getValue

,

isExpert

,

isHidden

,

isPreferred

,

setDisplayName

,

setExpert

,

setHidden

,

setName

,

setPreferred

,

setShortDescription

,

setValue

,

toString

- Methods declared in class java.lang.

Object

clone

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

Constructor

Description

IndexedPropertyDescriptor

​(

String

propertyName,

Class

<?> beanClass)

This constructor constructs an IndexedPropertyDescriptor for a property
that follows the standard Java conventions by having getFoo and setFoo
accessor methods, for both indexed access and array access.

IndexedPropertyDescriptor

​(

String

propertyName,

Class

<?> beanClass,

String

readMethodName,

String

writeMethodName,

String

indexedReadMethodName,

String

indexedWriteMethodName)

This constructor takes the name of a simple property, and method
names for reading and writing the property, both indexed
and non-indexed.

IndexedPropertyDescriptor

​(

String

propertyName,

Method

readMethod,

Method

writeMethod,

Method

indexedReadMethod,

Method

indexedWriteMethod)

This constructor takes the name of a simple property, and Method
objects for reading and writing the property.

---

#### Constructor Summary

This constructor constructs an IndexedPropertyDescriptor for a property
that follows the standard Java conventions by having getFoo and setFoo
accessor methods, for both indexed access and array access.

This constructor takes the name of a simple property, and method
names for reading and writing the property, both indexed
and non-indexed.

This constructor takes the name of a simple property, and Method
objects for reading and writing the property.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares this

PropertyDescriptor

against the specified object.

Class

<?>

getIndexedPropertyType

()

Returns the Java type info for the indexed property.

Method

getIndexedReadMethod

()

Gets the method that should be used to read an indexed
property value.

Method

getIndexedWriteMethod

()

Gets the method that should be used to write an indexed property value.

int

hashCode

()

Returns a hash code value for the object.

void

setIndexedReadMethod

​(

Method

readMethod)

Sets the method that should be used to read an indexed property value.

void

setIndexedWriteMethod

​(

Method

writeMethod)

Sets the method that should be used to write an indexed property value.

- Methods declared in class java.beans.

PropertyDescriptor

createPropertyEditor

,

getPropertyEditorClass

,

getPropertyType

,

getReadMethod

,

getWriteMethod

,

isBound

,

isConstrained

,

setBound

,

setConstrained

,

setPropertyEditorClass

,

setReadMethod

,

setWriteMethod

- Methods declared in class java.beans.

FeatureDescriptor

attributeNames

,

getDisplayName

,

getName

,

getShortDescription

,

getValue

,

isExpert

,

isHidden

,

isPreferred

,

setDisplayName

,

setExpert

,

setHidden

,

setName

,

setPreferred

,

setShortDescription

,

setValue

,

toString

- Methods declared in class java.lang.

Object

clone

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

Compares this

PropertyDescriptor

against the specified object.

Returns the Java type info for the indexed property.

Gets the method that should be used to read an indexed
property value.

Gets the method that should be used to write an indexed property value.

Returns a hash code value for the object.

Sets the method that should be used to read an indexed property value.

Sets the method that should be used to write an indexed property value.

Methods declared in class java.beans.

PropertyDescriptor

createPropertyEditor

,

getPropertyEditorClass

,

getPropertyType

,

getReadMethod

,

getWriteMethod

,

isBound

,

isConstrained

,

setBound

,

setConstrained

,

setPropertyEditorClass

,

setReadMethod

,

setWriteMethod

---

#### Methods declared in class java.beans. PropertyDescriptor

Methods declared in class java.beans.

FeatureDescriptor

attributeNames

,

getDisplayName

,

getName

,

getShortDescription

,

getValue

,

isExpert

,

isHidden

,

isPreferred

,

setDisplayName

,

setExpert

,

setHidden

,

setName

,

setPreferred

,

setShortDescription

,

setValue

,

toString

---

#### Methods declared in class java.beans. FeatureDescriptor

Methods declared in class java.lang.

Object

clone

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

- IndexedPropertyDescriptor

```java
public IndexedPropertyDescriptor​(
String
propertyName,

Class
<?> beanClass)
throws
IntrospectionException
```

This constructor constructs an IndexedPropertyDescriptor for a property
that follows the standard Java conventions by having getFoo and setFoo
accessor methods, for both indexed access and array access.

Thus if the argument name is "fred", it will assume that there
is an indexed reader method "getFred", a non-indexed (array) reader
method also called "getFred", an indexed writer method "setFred",
and finally a non-indexed writer method "setFred".

**Parameters:** propertyName

- The programmatic name of the property.
**Parameters:** beanClass

- The Class object for the target bean.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

- IndexedPropertyDescriptor

```java
public IndexedPropertyDescriptor​(
String
propertyName,

Class
<?> beanClass,

String
readMethodName,

String
writeMethodName,

String
indexedReadMethodName,

String
indexedWriteMethodName)
throws
IntrospectionException
```

This constructor takes the name of a simple property, and method
names for reading and writing the property, both indexed
and non-indexed.

**Parameters:** propertyName

- The programmatic name of the property.
**Parameters:** beanClass

- The Class object for the target bean.
**Parameters:** readMethodName

- The name of the method used for reading the property
values as an array. May be null if the property is write-only
or must be indexed.
**Parameters:** writeMethodName

- The name of the method used for writing the property
values as an array. May be null if the property is read-only
or must be indexed.
**Parameters:** indexedReadMethodName

- The name of the method used for reading
an indexed property value.
May be null if the property is write-only.
**Parameters:** indexedWriteMethodName

- The name of the method used for writing
an indexed property value.
May be null if the property is read-only.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

- IndexedPropertyDescriptor

```java
public IndexedPropertyDescriptor​(
String
propertyName,

Method
readMethod,

Method
writeMethod,

Method
indexedReadMethod,

Method
indexedWriteMethod)
throws
IntrospectionException
```

This constructor takes the name of a simple property, and Method
objects for reading and writing the property.

**Parameters:** propertyName

- The programmatic name of the property.
**Parameters:** readMethod

- The method used for reading the property values as an array.
May be null if the property is write-only or must be indexed.
**Parameters:** writeMethod

- The method used for writing the property values as an array.
May be null if the property is read-only or must be indexed.
**Parameters:** indexedReadMethod

- The method used for reading an indexed property value.
May be null if the property is write-only.
**Parameters:** indexedWriteMethod

- The method used for writing an indexed property value.
May be null if the property is read-only.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

============ METHOD DETAIL ==========

- Method Detail

- getIndexedReadMethod

```java
public
Method
getIndexedReadMethod()
```

Gets the method that should be used to read an indexed
property value.

**Returns:** The method that should be used to read an indexed
property value.
May return null if the property isn't indexed or is write-only.

- setIndexedReadMethod

```java
public void setIndexedReadMethod​(
Method
readMethod)
throws
IntrospectionException
```

Sets the method that should be used to read an indexed property value.

**Parameters:** readMethod

- The new indexed read method.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.
**Since:** 1.2

- getIndexedWriteMethod

```java
public
Method
getIndexedWriteMethod()
```

Gets the method that should be used to write an indexed property value.

**Returns:** The method that should be used to write an indexed
property value.
May return null if the property isn't indexed or is read-only.

- setIndexedWriteMethod

```java
public void setIndexedWriteMethod​(
Method
writeMethod)
throws
IntrospectionException
```

Sets the method that should be used to write an indexed property value.

**Parameters:** writeMethod

- The new indexed write method.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.
**Since:** 1.2

- getIndexedPropertyType

```java
public
Class
<?> getIndexedPropertyType()
```

Returns the Java type info for the indexed property.
Note that the

Class

object may describe
primitive Java types such as

int

.
This type is returned by the indexed read method
or is used as the parameter type of the indexed write method.

**Returns:** the

Class

object that represents the Java type info,
or

null

if the type cannot be determined

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this

PropertyDescriptor

against the specified object.
Returns true if the objects are the same. Two

PropertyDescriptor

s
are the same if the read, write, property types, property editor and
flags are equivalent.

**Overrides:** equals

in class

PropertyDescriptor
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**Since:** 1.4
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for the object.
See

Object.hashCode()

for a complete description.

**Overrides:** hashCode

in class

PropertyDescriptor
**Returns:** a hash code value for this object.
**Since:** 1.5
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- IndexedPropertyDescriptor

```java
public IndexedPropertyDescriptor​(
String
propertyName,

Class
<?> beanClass)
throws
IntrospectionException
```

This constructor constructs an IndexedPropertyDescriptor for a property
that follows the standard Java conventions by having getFoo and setFoo
accessor methods, for both indexed access and array access.

Thus if the argument name is "fred", it will assume that there
is an indexed reader method "getFred", a non-indexed (array) reader
method also called "getFred", an indexed writer method "setFred",
and finally a non-indexed writer method "setFred".

**Parameters:** propertyName

- The programmatic name of the property.
**Parameters:** beanClass

- The Class object for the target bean.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

- IndexedPropertyDescriptor

```java
public IndexedPropertyDescriptor​(
String
propertyName,

Class
<?> beanClass,

String
readMethodName,

String
writeMethodName,

String
indexedReadMethodName,

String
indexedWriteMethodName)
throws
IntrospectionException
```

This constructor takes the name of a simple property, and method
names for reading and writing the property, both indexed
and non-indexed.

**Parameters:** propertyName

- The programmatic name of the property.
**Parameters:** beanClass

- The Class object for the target bean.
**Parameters:** readMethodName

- The name of the method used for reading the property
values as an array. May be null if the property is write-only
or must be indexed.
**Parameters:** writeMethodName

- The name of the method used for writing the property
values as an array. May be null if the property is read-only
or must be indexed.
**Parameters:** indexedReadMethodName

- The name of the method used for reading
an indexed property value.
May be null if the property is write-only.
**Parameters:** indexedWriteMethodName

- The name of the method used for writing
an indexed property value.
May be null if the property is read-only.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

- IndexedPropertyDescriptor

```java
public IndexedPropertyDescriptor​(
String
propertyName,

Method
readMethod,

Method
writeMethod,

Method
indexedReadMethod,

Method
indexedWriteMethod)
throws
IntrospectionException
```

This constructor takes the name of a simple property, and Method
objects for reading and writing the property.

**Parameters:** propertyName

- The programmatic name of the property.
**Parameters:** readMethod

- The method used for reading the property values as an array.
May be null if the property is write-only or must be indexed.
**Parameters:** writeMethod

- The method used for writing the property values as an array.
May be null if the property is read-only or must be indexed.
**Parameters:** indexedReadMethod

- The method used for reading an indexed property value.
May be null if the property is write-only.
**Parameters:** indexedWriteMethod

- The method used for writing an indexed property value.
May be null if the property is read-only.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

---

#### Constructor Detail

IndexedPropertyDescriptor

```java
public IndexedPropertyDescriptor​(
String
propertyName,

Class
<?> beanClass)
throws
IntrospectionException
```

This constructor constructs an IndexedPropertyDescriptor for a property
that follows the standard Java conventions by having getFoo and setFoo
accessor methods, for both indexed access and array access.

Thus if the argument name is "fred", it will assume that there
is an indexed reader method "getFred", a non-indexed (array) reader
method also called "getFred", an indexed writer method "setFred",
and finally a non-indexed writer method "setFred".

**Parameters:** propertyName

- The programmatic name of the property.
**Parameters:** beanClass

- The Class object for the target bean.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

---

#### IndexedPropertyDescriptor

public IndexedPropertyDescriptor​(

String

propertyName,

Class

<?> beanClass)
throws

IntrospectionException

This constructor constructs an IndexedPropertyDescriptor for a property
that follows the standard Java conventions by having getFoo and setFoo
accessor methods, for both indexed access and array access.

Thus if the argument name is "fred", it will assume that there
is an indexed reader method "getFred", a non-indexed (array) reader
method also called "getFred", an indexed writer method "setFred",
and finally a non-indexed writer method "setFred".

Thus if the argument name is "fred", it will assume that there
is an indexed reader method "getFred", a non-indexed (array) reader
method also called "getFred", an indexed writer method "setFred",
and finally a non-indexed writer method "setFred".

IndexedPropertyDescriptor

```java
public IndexedPropertyDescriptor​(
String
propertyName,

Class
<?> beanClass,

String
readMethodName,

String
writeMethodName,

String
indexedReadMethodName,

String
indexedWriteMethodName)
throws
IntrospectionException
```

This constructor takes the name of a simple property, and method
names for reading and writing the property, both indexed
and non-indexed.

**Parameters:** propertyName

- The programmatic name of the property.
**Parameters:** beanClass

- The Class object for the target bean.
**Parameters:** readMethodName

- The name of the method used for reading the property
values as an array. May be null if the property is write-only
or must be indexed.
**Parameters:** writeMethodName

- The name of the method used for writing the property
values as an array. May be null if the property is read-only
or must be indexed.
**Parameters:** indexedReadMethodName

- The name of the method used for reading
an indexed property value.
May be null if the property is write-only.
**Parameters:** indexedWriteMethodName

- The name of the method used for writing
an indexed property value.
May be null if the property is read-only.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

---

#### IndexedPropertyDescriptor

public IndexedPropertyDescriptor​(

String

propertyName,

Class

<?> beanClass,

String

readMethodName,

String

writeMethodName,

String

indexedReadMethodName,

String

indexedWriteMethodName)
throws

IntrospectionException

This constructor takes the name of a simple property, and method
names for reading and writing the property, both indexed
and non-indexed.

IndexedPropertyDescriptor

```java
public IndexedPropertyDescriptor​(
String
propertyName,

Method
readMethod,

Method
writeMethod,

Method
indexedReadMethod,

Method
indexedWriteMethod)
throws
IntrospectionException
```

This constructor takes the name of a simple property, and Method
objects for reading and writing the property.

**Parameters:** propertyName

- The programmatic name of the property.
**Parameters:** readMethod

- The method used for reading the property values as an array.
May be null if the property is write-only or must be indexed.
**Parameters:** writeMethod

- The method used for writing the property values as an array.
May be null if the property is read-only or must be indexed.
**Parameters:** indexedReadMethod

- The method used for reading an indexed property value.
May be null if the property is write-only.
**Parameters:** indexedWriteMethod

- The method used for writing an indexed property value.
May be null if the property is read-only.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

---

#### IndexedPropertyDescriptor

public IndexedPropertyDescriptor​(

String

propertyName,

Method

readMethod,

Method

writeMethod,

Method

indexedReadMethod,

Method

indexedWriteMethod)
throws

IntrospectionException

This constructor takes the name of a simple property, and Method
objects for reading and writing the property.

Method Detail

- getIndexedReadMethod

```java
public
Method
getIndexedReadMethod()
```

Gets the method that should be used to read an indexed
property value.

**Returns:** The method that should be used to read an indexed
property value.
May return null if the property isn't indexed or is write-only.

- setIndexedReadMethod

```java
public void setIndexedReadMethod​(
Method
readMethod)
throws
IntrospectionException
```

Sets the method that should be used to read an indexed property value.

**Parameters:** readMethod

- The new indexed read method.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.
**Since:** 1.2

- getIndexedWriteMethod

```java
public
Method
getIndexedWriteMethod()
```

Gets the method that should be used to write an indexed property value.

**Returns:** The method that should be used to write an indexed
property value.
May return null if the property isn't indexed or is read-only.

- setIndexedWriteMethod

```java
public void setIndexedWriteMethod​(
Method
writeMethod)
throws
IntrospectionException
```

Sets the method that should be used to write an indexed property value.

**Parameters:** writeMethod

- The new indexed write method.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.
**Since:** 1.2

- getIndexedPropertyType

```java
public
Class
<?> getIndexedPropertyType()
```

Returns the Java type info for the indexed property.
Note that the

Class

object may describe
primitive Java types such as

int

.
This type is returned by the indexed read method
or is used as the parameter type of the indexed write method.

**Returns:** the

Class

object that represents the Java type info,
or

null

if the type cannot be determined

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this

PropertyDescriptor

against the specified object.
Returns true if the objects are the same. Two

PropertyDescriptor

s
are the same if the read, write, property types, property editor and
flags are equivalent.

**Overrides:** equals

in class

PropertyDescriptor
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**Since:** 1.4
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for the object.
See

Object.hashCode()

for a complete description.

**Overrides:** hashCode

in class

PropertyDescriptor
**Returns:** a hash code value for this object.
**Since:** 1.5
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

getIndexedReadMethod

```java
public
Method
getIndexedReadMethod()
```

Gets the method that should be used to read an indexed
property value.

**Returns:** The method that should be used to read an indexed
property value.
May return null if the property isn't indexed or is write-only.

---

#### getIndexedReadMethod

public

Method

getIndexedReadMethod()

Gets the method that should be used to read an indexed
property value.

setIndexedReadMethod

```java
public void setIndexedReadMethod​(
Method
readMethod)
throws
IntrospectionException
```

Sets the method that should be used to read an indexed property value.

**Parameters:** readMethod

- The new indexed read method.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.
**Since:** 1.2

---

#### setIndexedReadMethod

public void setIndexedReadMethod​(

Method

readMethod)
throws

IntrospectionException

Sets the method that should be used to read an indexed property value.

getIndexedWriteMethod

```java
public
Method
getIndexedWriteMethod()
```

Gets the method that should be used to write an indexed property value.

**Returns:** The method that should be used to write an indexed
property value.
May return null if the property isn't indexed or is read-only.

---

#### getIndexedWriteMethod

public

Method

getIndexedWriteMethod()

Gets the method that should be used to write an indexed property value.

setIndexedWriteMethod

```java
public void setIndexedWriteMethod​(
Method
writeMethod)
throws
IntrospectionException
```

Sets the method that should be used to write an indexed property value.

**Parameters:** writeMethod

- The new indexed write method.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.
**Since:** 1.2

---

#### setIndexedWriteMethod

public void setIndexedWriteMethod​(

Method

writeMethod)
throws

IntrospectionException

Sets the method that should be used to write an indexed property value.

getIndexedPropertyType

```java
public
Class
<?> getIndexedPropertyType()
```

Returns the Java type info for the indexed property.
Note that the

Class

object may describe
primitive Java types such as

int

.
This type is returned by the indexed read method
or is used as the parameter type of the indexed write method.

**Returns:** the

Class

object that represents the Java type info,
or

null

if the type cannot be determined

---

#### getIndexedPropertyType

public

Class

<?> getIndexedPropertyType()

Returns the Java type info for the indexed property.
Note that the

Class

object may describe
primitive Java types such as

int

.
This type is returned by the indexed read method
or is used as the parameter type of the indexed write method.

equals

```java
public boolean equals​(
Object
obj)
```

Compares this

PropertyDescriptor

against the specified object.
Returns true if the objects are the same. Two

PropertyDescriptor

s
are the same if the read, write, property types, property editor and
flags are equivalent.

**Overrides:** equals

in class

PropertyDescriptor
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**Since:** 1.4
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares this

PropertyDescriptor

against the specified object.
Returns true if the objects are the same. Two

PropertyDescriptor

s
are the same if the read, write, property types, property editor and
flags are equivalent.

hashCode

```java
public int hashCode()
```

Returns a hash code value for the object.
See

Object.hashCode()

for a complete description.

**Overrides:** hashCode

in class

PropertyDescriptor
**Returns:** a hash code value for this object.
**Since:** 1.5
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code value for the object.
See

Object.hashCode()

for a complete description.

---

