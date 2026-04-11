# Class PropertyDescriptor

**Source:** `java.desktop\java\beans\PropertyDescriptor.html`

### Class Description

```java
public class
PropertyDescriptor

extends
FeatureDescriptor
```

A PropertyDescriptor describes one property that a Java Bean
exports via a pair of accessor methods.

**Direct Known Subclasses:** IndexedPropertyDescriptor

---

### Field Details

*No entries found.*

### Constructor Details

#### public PropertyDescriptor​(
String
propertyName,

Class
<?> beanClass)
throws
IntrospectionException

Constructs a PropertyDescriptor for a property that follows
the standard Java convention by having getFoo and setFoo
accessor methods. Thus if the argument name is "fred", it will
assume that the writer method is "setFred" and the reader method
is "getFred" (or "isFred" for a boolean property). Note that the
property name should start with a lower case character, which will
be capitalized in the method names.

**Parameters:**
- propertyName

- The programmatic name of the property.
- beanClass

- The Class object for the target bean. For
example sun.beans.OurButton.class.

**Throws:**
- IntrospectionException

- if an exception occurs during
introspection.

---

#### public PropertyDescriptor​(
String
propertyName,

Class
<?> beanClass,

String
readMethodName,

String
writeMethodName)
throws
IntrospectionException

This constructor takes the name of a simple property, and method
names for reading and writing the property.

**Parameters:**
- propertyName

- The programmatic name of the property.
- beanClass

- The Class object for the target bean. For
example sun.beans.OurButton.class.
- readMethodName

- The name of the method used for reading the property
value. May be null if the property is write-only.
- writeMethodName

- The name of the method used for writing the property
value. May be null if the property is read-only.

**Throws:**
- IntrospectionException

- if an exception occurs during
introspection.

---

#### public PropertyDescriptor​(
String
propertyName,

Method
readMethod,

Method
writeMethod)
throws
IntrospectionException

This constructor takes the name of a simple property, and Method
objects for reading and writing the property.

**Parameters:**
- propertyName

- The programmatic name of the property.
- readMethod

- The method used for reading the property value.
May be null if the property is write-only.
- writeMethod

- The method used for writing the property value.
May be null if the property is read-only.

**Throws:**
- IntrospectionException

- if an exception occurs during
introspection.

---

### Method Details

#### public
Class
<?> getPropertyType()

Returns the Java type info for the property.
Note that the

Class

object may describe
primitive Java types such as

int

.
This type is returned by the read method
or is used as the parameter type of the write method.
Returns

null

if the type is an indexed property
that does not support non-indexed access.

**Returns:**
- the

Class

object that represents the Java type info,
or

null

if the type cannot be determined

---

#### public
Method
getReadMethod()

Gets the method that should be used to read the property value.

**Returns:**
- The method that should be used to read the property value.
May return null if the property can't be read.

---

#### public void setReadMethod​(
Method
readMethod)
throws
IntrospectionException

Sets the method that should be used to read the property value.

**Parameters:**
- readMethod

- The new read method.

**Throws:**
- IntrospectionException

- if the read method is invalid

**Since:**
- 1.2

---

#### public
Method
getWriteMethod()

Gets the method that should be used to write the property value.

**Returns:**
- The method that should be used to write the property value.
May return null if the property can't be written.

---

#### public void setWriteMethod​(
Method
writeMethod)
throws
IntrospectionException

Sets the method that should be used to write the property value.

**Parameters:**
- writeMethod

- The new write method.

**Throws:**
- IntrospectionException

- if the write method is invalid

**Since:**
- 1.2

---

#### public boolean isBound()

Updates to "bound" properties will cause a "PropertyChange" event to
get fired when the property is changed.

**Returns:**
- True if this is a bound property.

---

#### public void setBound​(boolean bound)

Updates to "bound" properties will cause a "PropertyChange" event to
get fired when the property is changed.

**Parameters:**
- bound

- True if this is a bound property.

---

#### public boolean isConstrained()

Attempted updates to "Constrained" properties will cause a "VetoableChange"
event to get fired when the property is changed.

**Returns:**
- True if this is a constrained property.

---

#### public void setConstrained​(boolean constrained)

Attempted updates to "Constrained" properties will cause a "VetoableChange"
event to get fired when the property is changed.

**Parameters:**
- constrained

- True if this is a constrained property.

---

#### public void setPropertyEditorClass​(
Class
<?> propertyEditorClass)

Normally PropertyEditors will be found using the PropertyEditorManager.
However if for some reason you want to associate a particular
PropertyEditor with a given property, then you can do it with
this method.

**Parameters:**
- propertyEditorClass

- The Class for the desired PropertyEditor.

---

#### public
Class
<?> getPropertyEditorClass()

Gets any explicit PropertyEditor Class that has been registered
for this property.

**Returns:**
- Any explicit PropertyEditor Class that has been registered
for this property. Normally this will return "null",
indicating that no special editor has been registered,
so the PropertyEditorManager should be used to locate
a suitable PropertyEditor.

---

#### public
PropertyEditor
createPropertyEditor​(
Object
bean)

Constructs an instance of a property editor using the current
property editor class.

If the property editor class has a public constructor that takes an
Object argument then it will be invoked using the bean parameter
as the argument. Otherwise, the default constructor will be invoked.

**Parameters:**
- bean

- the source object

**Returns:**
- a property editor instance or null if a property editor has
not been defined or cannot be created

**Since:**
- 1.5

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

Object

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

Object

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

#### Class PropertyDescriptor

java.lang.Object

- java.beans.FeatureDescriptor
- - java.beans.PropertyDescriptor

java.beans.FeatureDescriptor

- java.beans.PropertyDescriptor

java.beans.PropertyDescriptor

**Direct Known Subclasses:** IndexedPropertyDescriptor

```java
public class
PropertyDescriptor

extends
FeatureDescriptor
```

A PropertyDescriptor describes one property that a Java Bean
exports via a pair of accessor methods.

**Since:** 1.1

public class

PropertyDescriptor

extends

FeatureDescriptor

A PropertyDescriptor describes one property that a Java Bean
exports via a pair of accessor methods.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PropertyDescriptor

​(

String

propertyName,

Class

<?> beanClass)

Constructs a PropertyDescriptor for a property that follows
the standard Java convention by having getFoo and setFoo
accessor methods.

PropertyDescriptor

​(

String

propertyName,

Class

<?> beanClass,

String

readMethodName,

String

writeMethodName)

This constructor takes the name of a simple property, and method
names for reading and writing the property.

PropertyDescriptor

​(

String

propertyName,

Method

readMethod,

Method

writeMethod)

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

PropertyEditor

createPropertyEditor

​(

Object

bean)

Constructs an instance of a property editor using the current
property editor class.

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

getPropertyEditorClass

()

Gets any explicit PropertyEditor Class that has been registered
for this property.

Class

<?>

getPropertyType

()

Returns the Java type info for the property.

Method

getReadMethod

()

Gets the method that should be used to read the property value.

Method

getWriteMethod

()

Gets the method that should be used to write the property value.

int

hashCode

()

Returns a hash code value for the object.

boolean

isBound

()

Updates to "bound" properties will cause a "PropertyChange" event to
get fired when the property is changed.

boolean

isConstrained

()

Attempted updates to "Constrained" properties will cause a "VetoableChange"
event to get fired when the property is changed.

void

setBound

​(boolean bound)

Updates to "bound" properties will cause a "PropertyChange" event to
get fired when the property is changed.

void

setConstrained

​(boolean constrained)

Attempted updates to "Constrained" properties will cause a "VetoableChange"
event to get fired when the property is changed.

void

setPropertyEditorClass

​(

Class

<?> propertyEditorClass)

Normally PropertyEditors will be found using the PropertyEditorManager.

void

setReadMethod

​(

Method

readMethod)

Sets the method that should be used to read the property value.

void

setWriteMethod

​(

Method

writeMethod)

Sets the method that should be used to write the property value.

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

PropertyDescriptor

​(

String

propertyName,

Class

<?> beanClass)

Constructs a PropertyDescriptor for a property that follows
the standard Java convention by having getFoo and setFoo
accessor methods.

PropertyDescriptor

​(

String

propertyName,

Class

<?> beanClass,

String

readMethodName,

String

writeMethodName)

This constructor takes the name of a simple property, and method
names for reading and writing the property.

PropertyDescriptor

​(

String

propertyName,

Method

readMethod,

Method

writeMethod)

This constructor takes the name of a simple property, and Method
objects for reading and writing the property.

---

#### Constructor Summary

Constructs a PropertyDescriptor for a property that follows
the standard Java convention by having getFoo and setFoo
accessor methods.

This constructor takes the name of a simple property, and method
names for reading and writing the property.

This constructor takes the name of a simple property, and Method
objects for reading and writing the property.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

PropertyEditor

createPropertyEditor

​(

Object

bean)

Constructs an instance of a property editor using the current
property editor class.

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

getPropertyEditorClass

()

Gets any explicit PropertyEditor Class that has been registered
for this property.

Class

<?>

getPropertyType

()

Returns the Java type info for the property.

Method

getReadMethod

()

Gets the method that should be used to read the property value.

Method

getWriteMethod

()

Gets the method that should be used to write the property value.

int

hashCode

()

Returns a hash code value for the object.

boolean

isBound

()

Updates to "bound" properties will cause a "PropertyChange" event to
get fired when the property is changed.

boolean

isConstrained

()

Attempted updates to "Constrained" properties will cause a "VetoableChange"
event to get fired when the property is changed.

void

setBound

​(boolean bound)

Updates to "bound" properties will cause a "PropertyChange" event to
get fired when the property is changed.

void

setConstrained

​(boolean constrained)

Attempted updates to "Constrained" properties will cause a "VetoableChange"
event to get fired when the property is changed.

void

setPropertyEditorClass

​(

Class

<?> propertyEditorClass)

Normally PropertyEditors will be found using the PropertyEditorManager.

void

setReadMethod

​(

Method

readMethod)

Sets the method that should be used to read the property value.

void

setWriteMethod

​(

Method

writeMethod)

Sets the method that should be used to write the property value.

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

Constructs an instance of a property editor using the current
property editor class.

Compares this

PropertyDescriptor

against the specified object.

Gets any explicit PropertyEditor Class that has been registered
for this property.

Returns the Java type info for the property.

Gets the method that should be used to read the property value.

Gets the method that should be used to write the property value.

Returns a hash code value for the object.

Updates to "bound" properties will cause a "PropertyChange" event to
get fired when the property is changed.

Attempted updates to "Constrained" properties will cause a "VetoableChange"
event to get fired when the property is changed.

Normally PropertyEditors will be found using the PropertyEditorManager.

Sets the method that should be used to read the property value.

Sets the method that should be used to write the property value.

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

- PropertyDescriptor

```java
public PropertyDescriptor​(
String
propertyName,

Class
<?> beanClass)
throws
IntrospectionException
```

Constructs a PropertyDescriptor for a property that follows
the standard Java convention by having getFoo and setFoo
accessor methods. Thus if the argument name is "fred", it will
assume that the writer method is "setFred" and the reader method
is "getFred" (or "isFred" for a boolean property). Note that the
property name should start with a lower case character, which will
be capitalized in the method names.

**Parameters:** propertyName

- The programmatic name of the property.
**Parameters:** beanClass

- The Class object for the target bean. For
example sun.beans.OurButton.class.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

- PropertyDescriptor

```java
public PropertyDescriptor​(
String
propertyName,

Class
<?> beanClass,

String
readMethodName,

String
writeMethodName)
throws
IntrospectionException
```

This constructor takes the name of a simple property, and method
names for reading and writing the property.

**Parameters:** propertyName

- The programmatic name of the property.
**Parameters:** beanClass

- The Class object for the target bean. For
example sun.beans.OurButton.class.
**Parameters:** readMethodName

- The name of the method used for reading the property
value. May be null if the property is write-only.
**Parameters:** writeMethodName

- The name of the method used for writing the property
value. May be null if the property is read-only.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

- PropertyDescriptor

```java
public PropertyDescriptor​(
String
propertyName,

Method
readMethod,

Method
writeMethod)
throws
IntrospectionException
```

This constructor takes the name of a simple property, and Method
objects for reading and writing the property.

**Parameters:** propertyName

- The programmatic name of the property.
**Parameters:** readMethod

- The method used for reading the property value.
May be null if the property is write-only.
**Parameters:** writeMethod

- The method used for writing the property value.
May be null if the property is read-only.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

============ METHOD DETAIL ==========

- Method Detail

- getPropertyType

```java
public
Class
<?> getPropertyType()
```

Returns the Java type info for the property.
Note that the

Class

object may describe
primitive Java types such as

int

.
This type is returned by the read method
or is used as the parameter type of the write method.
Returns

null

if the type is an indexed property
that does not support non-indexed access.

**Returns:** the

Class

object that represents the Java type info,
or

null

if the type cannot be determined

- getReadMethod

```java
public
Method
getReadMethod()
```

Gets the method that should be used to read the property value.

**Returns:** The method that should be used to read the property value.
May return null if the property can't be read.

- setReadMethod

```java
public void setReadMethod​(
Method
readMethod)
throws
IntrospectionException
```

Sets the method that should be used to read the property value.

**Parameters:** readMethod

- The new read method.
**Throws:** IntrospectionException

- if the read method is invalid
**Since:** 1.2

- getWriteMethod

```java
public
Method
getWriteMethod()
```

Gets the method that should be used to write the property value.

**Returns:** The method that should be used to write the property value.
May return null if the property can't be written.

- setWriteMethod

```java
public void setWriteMethod​(
Method
writeMethod)
throws
IntrospectionException
```

Sets the method that should be used to write the property value.

**Parameters:** writeMethod

- The new write method.
**Throws:** IntrospectionException

- if the write method is invalid
**Since:** 1.2

- isBound

```java
public boolean isBound()
```

Updates to "bound" properties will cause a "PropertyChange" event to
get fired when the property is changed.

**Returns:** True if this is a bound property.

- setBound

```java
public void setBound​(boolean bound)
```

Updates to "bound" properties will cause a "PropertyChange" event to
get fired when the property is changed.

**Parameters:** bound

- True if this is a bound property.

- isConstrained

```java
public boolean isConstrained()
```

Attempted updates to "Constrained" properties will cause a "VetoableChange"
event to get fired when the property is changed.

**Returns:** True if this is a constrained property.

- setConstrained

```java
public void setConstrained​(boolean constrained)
```

Attempted updates to "Constrained" properties will cause a "VetoableChange"
event to get fired when the property is changed.

**Parameters:** constrained

- True if this is a constrained property.

- setPropertyEditorClass

```java
public void setPropertyEditorClass​(
Class
<?> propertyEditorClass)
```

Normally PropertyEditors will be found using the PropertyEditorManager.
However if for some reason you want to associate a particular
PropertyEditor with a given property, then you can do it with
this method.

**Parameters:** propertyEditorClass

- The Class for the desired PropertyEditor.

- getPropertyEditorClass

```java
public
Class
<?> getPropertyEditorClass()
```

Gets any explicit PropertyEditor Class that has been registered
for this property.

**Returns:** Any explicit PropertyEditor Class that has been registered
for this property. Normally this will return "null",
indicating that no special editor has been registered,
so the PropertyEditorManager should be used to locate
a suitable PropertyEditor.

- createPropertyEditor

```java
public
PropertyEditor
createPropertyEditor​(
Object
bean)
```

Constructs an instance of a property editor using the current
property editor class.

If the property editor class has a public constructor that takes an
Object argument then it will be invoked using the bean parameter
as the argument. Otherwise, the default constructor will be invoked.

**Parameters:** bean

- the source object
**Returns:** a property editor instance or null if a property editor has
not been defined or cannot be created
**Since:** 1.5

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

Object
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

Object
**Returns:** a hash code value for this object.
**Since:** 1.5
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- PropertyDescriptor

```java
public PropertyDescriptor​(
String
propertyName,

Class
<?> beanClass)
throws
IntrospectionException
```

Constructs a PropertyDescriptor for a property that follows
the standard Java convention by having getFoo and setFoo
accessor methods. Thus if the argument name is "fred", it will
assume that the writer method is "setFred" and the reader method
is "getFred" (or "isFred" for a boolean property). Note that the
property name should start with a lower case character, which will
be capitalized in the method names.

**Parameters:** propertyName

- The programmatic name of the property.
**Parameters:** beanClass

- The Class object for the target bean. For
example sun.beans.OurButton.class.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

- PropertyDescriptor

```java
public PropertyDescriptor​(
String
propertyName,

Class
<?> beanClass,

String
readMethodName,

String
writeMethodName)
throws
IntrospectionException
```

This constructor takes the name of a simple property, and method
names for reading and writing the property.

**Parameters:** propertyName

- The programmatic name of the property.
**Parameters:** beanClass

- The Class object for the target bean. For
example sun.beans.OurButton.class.
**Parameters:** readMethodName

- The name of the method used for reading the property
value. May be null if the property is write-only.
**Parameters:** writeMethodName

- The name of the method used for writing the property
value. May be null if the property is read-only.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

- PropertyDescriptor

```java
public PropertyDescriptor​(
String
propertyName,

Method
readMethod,

Method
writeMethod)
throws
IntrospectionException
```

This constructor takes the name of a simple property, and Method
objects for reading and writing the property.

**Parameters:** propertyName

- The programmatic name of the property.
**Parameters:** readMethod

- The method used for reading the property value.
May be null if the property is write-only.
**Parameters:** writeMethod

- The method used for writing the property value.
May be null if the property is read-only.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

---

#### Constructor Detail

PropertyDescriptor

```java
public PropertyDescriptor​(
String
propertyName,

Class
<?> beanClass)
throws
IntrospectionException
```

Constructs a PropertyDescriptor for a property that follows
the standard Java convention by having getFoo and setFoo
accessor methods. Thus if the argument name is "fred", it will
assume that the writer method is "setFred" and the reader method
is "getFred" (or "isFred" for a boolean property). Note that the
property name should start with a lower case character, which will
be capitalized in the method names.

**Parameters:** propertyName

- The programmatic name of the property.
**Parameters:** beanClass

- The Class object for the target bean. For
example sun.beans.OurButton.class.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

---

#### PropertyDescriptor

public PropertyDescriptor​(

String

propertyName,

Class

<?> beanClass)
throws

IntrospectionException

Constructs a PropertyDescriptor for a property that follows
the standard Java convention by having getFoo and setFoo
accessor methods. Thus if the argument name is "fred", it will
assume that the writer method is "setFred" and the reader method
is "getFred" (or "isFred" for a boolean property). Note that the
property name should start with a lower case character, which will
be capitalized in the method names.

PropertyDescriptor

```java
public PropertyDescriptor​(
String
propertyName,

Class
<?> beanClass,

String
readMethodName,

String
writeMethodName)
throws
IntrospectionException
```

This constructor takes the name of a simple property, and method
names for reading and writing the property.

**Parameters:** propertyName

- The programmatic name of the property.
**Parameters:** beanClass

- The Class object for the target bean. For
example sun.beans.OurButton.class.
**Parameters:** readMethodName

- The name of the method used for reading the property
value. May be null if the property is write-only.
**Parameters:** writeMethodName

- The name of the method used for writing the property
value. May be null if the property is read-only.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

---

#### PropertyDescriptor

public PropertyDescriptor​(

String

propertyName,

Class

<?> beanClass,

String

readMethodName,

String

writeMethodName)
throws

IntrospectionException

This constructor takes the name of a simple property, and method
names for reading and writing the property.

PropertyDescriptor

```java
public PropertyDescriptor​(
String
propertyName,

Method
readMethod,

Method
writeMethod)
throws
IntrospectionException
```

This constructor takes the name of a simple property, and Method
objects for reading and writing the property.

**Parameters:** propertyName

- The programmatic name of the property.
**Parameters:** readMethod

- The method used for reading the property value.
May be null if the property is write-only.
**Parameters:** writeMethod

- The method used for writing the property value.
May be null if the property is read-only.
**Throws:** IntrospectionException

- if an exception occurs during
introspection.

---

#### PropertyDescriptor

public PropertyDescriptor​(

String

propertyName,

Method

readMethod,

Method

writeMethod)
throws

IntrospectionException

This constructor takes the name of a simple property, and Method
objects for reading and writing the property.

Method Detail

- getPropertyType

```java
public
Class
<?> getPropertyType()
```

Returns the Java type info for the property.
Note that the

Class

object may describe
primitive Java types such as

int

.
This type is returned by the read method
or is used as the parameter type of the write method.
Returns

null

if the type is an indexed property
that does not support non-indexed access.

**Returns:** the

Class

object that represents the Java type info,
or

null

if the type cannot be determined

- getReadMethod

```java
public
Method
getReadMethod()
```

Gets the method that should be used to read the property value.

**Returns:** The method that should be used to read the property value.
May return null if the property can't be read.

- setReadMethod

```java
public void setReadMethod​(
Method
readMethod)
throws
IntrospectionException
```

Sets the method that should be used to read the property value.

**Parameters:** readMethod

- The new read method.
**Throws:** IntrospectionException

- if the read method is invalid
**Since:** 1.2

- getWriteMethod

```java
public
Method
getWriteMethod()
```

Gets the method that should be used to write the property value.

**Returns:** The method that should be used to write the property value.
May return null if the property can't be written.

- setWriteMethod

```java
public void setWriteMethod​(
Method
writeMethod)
throws
IntrospectionException
```

Sets the method that should be used to write the property value.

**Parameters:** writeMethod

- The new write method.
**Throws:** IntrospectionException

- if the write method is invalid
**Since:** 1.2

- isBound

```java
public boolean isBound()
```

Updates to "bound" properties will cause a "PropertyChange" event to
get fired when the property is changed.

**Returns:** True if this is a bound property.

- setBound

```java
public void setBound​(boolean bound)
```

Updates to "bound" properties will cause a "PropertyChange" event to
get fired when the property is changed.

**Parameters:** bound

- True if this is a bound property.

- isConstrained

```java
public boolean isConstrained()
```

Attempted updates to "Constrained" properties will cause a "VetoableChange"
event to get fired when the property is changed.

**Returns:** True if this is a constrained property.

- setConstrained

```java
public void setConstrained​(boolean constrained)
```

Attempted updates to "Constrained" properties will cause a "VetoableChange"
event to get fired when the property is changed.

**Parameters:** constrained

- True if this is a constrained property.

- setPropertyEditorClass

```java
public void setPropertyEditorClass​(
Class
<?> propertyEditorClass)
```

Normally PropertyEditors will be found using the PropertyEditorManager.
However if for some reason you want to associate a particular
PropertyEditor with a given property, then you can do it with
this method.

**Parameters:** propertyEditorClass

- The Class for the desired PropertyEditor.

- getPropertyEditorClass

```java
public
Class
<?> getPropertyEditorClass()
```

Gets any explicit PropertyEditor Class that has been registered
for this property.

**Returns:** Any explicit PropertyEditor Class that has been registered
for this property. Normally this will return "null",
indicating that no special editor has been registered,
so the PropertyEditorManager should be used to locate
a suitable PropertyEditor.

- createPropertyEditor

```java
public
PropertyEditor
createPropertyEditor​(
Object
bean)
```

Constructs an instance of a property editor using the current
property editor class.

If the property editor class has a public constructor that takes an
Object argument then it will be invoked using the bean parameter
as the argument. Otherwise, the default constructor will be invoked.

**Parameters:** bean

- the source object
**Returns:** a property editor instance or null if a property editor has
not been defined or cannot be created
**Since:** 1.5

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

Object
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

Object
**Returns:** a hash code value for this object.
**Since:** 1.5
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

getPropertyType

```java
public
Class
<?> getPropertyType()
```

Returns the Java type info for the property.
Note that the

Class

object may describe
primitive Java types such as

int

.
This type is returned by the read method
or is used as the parameter type of the write method.
Returns

null

if the type is an indexed property
that does not support non-indexed access.

**Returns:** the

Class

object that represents the Java type info,
or

null

if the type cannot be determined

---

#### getPropertyType

public

Class

<?> getPropertyType()

Returns the Java type info for the property.
Note that the

Class

object may describe
primitive Java types such as

int

.
This type is returned by the read method
or is used as the parameter type of the write method.
Returns

null

if the type is an indexed property
that does not support non-indexed access.

getReadMethod

```java
public
Method
getReadMethod()
```

Gets the method that should be used to read the property value.

**Returns:** The method that should be used to read the property value.
May return null if the property can't be read.

---

#### getReadMethod

public

Method

getReadMethod()

Gets the method that should be used to read the property value.

setReadMethod

```java
public void setReadMethod​(
Method
readMethod)
throws
IntrospectionException
```

Sets the method that should be used to read the property value.

**Parameters:** readMethod

- The new read method.
**Throws:** IntrospectionException

- if the read method is invalid
**Since:** 1.2

---

#### setReadMethod

public void setReadMethod​(

Method

readMethod)
throws

IntrospectionException

Sets the method that should be used to read the property value.

getWriteMethod

```java
public
Method
getWriteMethod()
```

Gets the method that should be used to write the property value.

**Returns:** The method that should be used to write the property value.
May return null if the property can't be written.

---

#### getWriteMethod

public

Method

getWriteMethod()

Gets the method that should be used to write the property value.

setWriteMethod

```java
public void setWriteMethod​(
Method
writeMethod)
throws
IntrospectionException
```

Sets the method that should be used to write the property value.

**Parameters:** writeMethod

- The new write method.
**Throws:** IntrospectionException

- if the write method is invalid
**Since:** 1.2

---

#### setWriteMethod

public void setWriteMethod​(

Method

writeMethod)
throws

IntrospectionException

Sets the method that should be used to write the property value.

isBound

```java
public boolean isBound()
```

Updates to "bound" properties will cause a "PropertyChange" event to
get fired when the property is changed.

**Returns:** True if this is a bound property.

---

#### isBound

public boolean isBound()

Updates to "bound" properties will cause a "PropertyChange" event to
get fired when the property is changed.

setBound

```java
public void setBound​(boolean bound)
```

Updates to "bound" properties will cause a "PropertyChange" event to
get fired when the property is changed.

**Parameters:** bound

- True if this is a bound property.

---

#### setBound

public void setBound​(boolean bound)

Updates to "bound" properties will cause a "PropertyChange" event to
get fired when the property is changed.

isConstrained

```java
public boolean isConstrained()
```

Attempted updates to "Constrained" properties will cause a "VetoableChange"
event to get fired when the property is changed.

**Returns:** True if this is a constrained property.

---

#### isConstrained

public boolean isConstrained()

Attempted updates to "Constrained" properties will cause a "VetoableChange"
event to get fired when the property is changed.

setConstrained

```java
public void setConstrained​(boolean constrained)
```

Attempted updates to "Constrained" properties will cause a "VetoableChange"
event to get fired when the property is changed.

**Parameters:** constrained

- True if this is a constrained property.

---

#### setConstrained

public void setConstrained​(boolean constrained)

Attempted updates to "Constrained" properties will cause a "VetoableChange"
event to get fired when the property is changed.

setPropertyEditorClass

```java
public void setPropertyEditorClass​(
Class
<?> propertyEditorClass)
```

Normally PropertyEditors will be found using the PropertyEditorManager.
However if for some reason you want to associate a particular
PropertyEditor with a given property, then you can do it with
this method.

**Parameters:** propertyEditorClass

- The Class for the desired PropertyEditor.

---

#### setPropertyEditorClass

public void setPropertyEditorClass​(

Class

<?> propertyEditorClass)

Normally PropertyEditors will be found using the PropertyEditorManager.
However if for some reason you want to associate a particular
PropertyEditor with a given property, then you can do it with
this method.

getPropertyEditorClass

```java
public
Class
<?> getPropertyEditorClass()
```

Gets any explicit PropertyEditor Class that has been registered
for this property.

**Returns:** Any explicit PropertyEditor Class that has been registered
for this property. Normally this will return "null",
indicating that no special editor has been registered,
so the PropertyEditorManager should be used to locate
a suitable PropertyEditor.

---

#### getPropertyEditorClass

public

Class

<?> getPropertyEditorClass()

Gets any explicit PropertyEditor Class that has been registered
for this property.

createPropertyEditor

```java
public
PropertyEditor
createPropertyEditor​(
Object
bean)
```

Constructs an instance of a property editor using the current
property editor class.

If the property editor class has a public constructor that takes an
Object argument then it will be invoked using the bean parameter
as the argument. Otherwise, the default constructor will be invoked.

**Parameters:** bean

- the source object
**Returns:** a property editor instance or null if a property editor has
not been defined or cannot be created
**Since:** 1.5

---

#### createPropertyEditor

public

PropertyEditor

createPropertyEditor​(

Object

bean)

Constructs an instance of a property editor using the current
property editor class.

If the property editor class has a public constructor that takes an
Object argument then it will be invoked using the bean parameter
as the argument. Otherwise, the default constructor will be invoked.

If the property editor class has a public constructor that takes an
Object argument then it will be invoked using the bean parameter
as the argument. Otherwise, the default constructor will be invoked.

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

Object
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

Object
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

