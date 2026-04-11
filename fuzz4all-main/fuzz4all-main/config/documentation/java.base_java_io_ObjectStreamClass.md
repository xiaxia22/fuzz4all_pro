# Class ObjectStreamClass

**Source:** `java.base\java\io\ObjectStreamClass.html`

### Class Description

```java
public class
ObjectStreamClass

extends
Object

implements
Serializable
```

Serialization's descriptor for classes. It contains the name and
serialVersionUID of the class. The ObjectStreamClass for a specific class
loaded in this Java VM can be found/created using the lookup method.

The algorithm to compute the SerialVersionUID is described in

Object Serialization Specification, Section 4.6, Stream Unique Identifiers

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final
ObjectStreamField
[] NO_FIELDS

serialPersistentFields value indicating no serializable fields

---

### Constructor Details

*No entries found.*

### Method Details

#### public static
ObjectStreamClass
lookup​(
Class
<?> cl)

Find the descriptor for a class that can be serialized. Creates an
ObjectStreamClass instance if one does not exist yet for class. Null is
returned if the specified class does not implement java.io.Serializable
or java.io.Externalizable.

**Parameters:**
- cl

- class for which to get the descriptor

**Returns:**
- the class descriptor for the specified class

---

#### public static
ObjectStreamClass
lookupAny​(
Class
<?> cl)

Returns the descriptor for any class, regardless of whether it
implements

Serializable

.

**Parameters:**
- cl

- class for which to get the descriptor

**Returns:**
- the class descriptor for the specified class

**Since:**
- 1.6

---

#### public
String
getName()

Returns the name of the class described by this descriptor.
This method returns the name of the class in the format that
is used by the

Class.getName()

method.

**Returns:**
- a string representing the name of the class

---

#### public long getSerialVersionUID()

Return the serialVersionUID for this class. The serialVersionUID
defines a set of classes all with the same name that have evolved from a
common root class and agree to be serialized and deserialized using a
common format. NonSerializable classes have a serialVersionUID of 0L.

**Returns:**
- the SUID of the class described by this descriptor

---

#### public
Class
<?> forClass()

Return the class in the local VM that this version is mapped to. Null
is returned if there is no corresponding local class.

**Returns:**
- the

Class

instance that this descriptor represents

---

#### public
ObjectStreamField
[] getFields()

Return an array of the fields of this serializable class.

**Returns:**
- an array containing an element for each persistent field of
this class. Returns an array of length zero if there are no
fields.

**Since:**
- 1.2

---

#### public
ObjectStreamField
getField​(
String
name)

Get the field of this class by name.

**Parameters:**
- name

- the name of the data field to look for

**Returns:**
- The ObjectStreamField object of the named field or null if
there is no such named field.

---

#### public
String
toString()

Return a string describing this ObjectStreamClass.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class ObjectStreamClass

java.lang.Object

- java.io.ObjectStreamClass

java.io.ObjectStreamClass

**All Implemented Interfaces:** Serializable

```java
public class
ObjectStreamClass

extends
Object

implements
Serializable
```

Serialization's descriptor for classes. It contains the name and
serialVersionUID of the class. The ObjectStreamClass for a specific class
loaded in this Java VM can be found/created using the lookup method.

The algorithm to compute the SerialVersionUID is described in

Object Serialization Specification, Section 4.6, Stream Unique Identifiers

.

**Since:** 1.1
**See Also:** ObjectStreamField

,

Object Serialization Specification, Section 4, Class Descriptors

,

Serialized Form

public class

ObjectStreamClass

extends

Object

implements

Serializable

Serialization's descriptor for classes. It contains the name and
serialVersionUID of the class. The ObjectStreamClass for a specific class
loaded in this Java VM can be found/created using the lookup method.

The algorithm to compute the SerialVersionUID is described in

Object Serialization Specification, Section 4.6, Stream Unique Identifiers

.

The algorithm to compute the SerialVersionUID is described in

Object Serialization Specification, Section 4.6, Stream Unique Identifiers

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

ObjectStreamField

[]

NO_FIELDS

serialPersistentFields value indicating no serializable fields

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<?>

forClass

()

Return the class in the local VM that this version is mapped to.

ObjectStreamField

getField

​(

String

name)

Get the field of this class by name.

ObjectStreamField

[]

getFields

()

Return an array of the fields of this serializable class.

String

getName

()

Returns the name of the class described by this descriptor.

long

getSerialVersionUID

()

Return the serialVersionUID for this class.

static

ObjectStreamClass

lookup

​(

Class

<?> cl)

Find the descriptor for a class that can be serialized.

static

ObjectStreamClass

lookupAny

​(

Class

<?> cl)

Returns the descriptor for any class, regardless of whether it
implements

Serializable

.

String

toString

()

Return a string describing this ObjectStreamClass.

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

Field Summary

Fields

Modifier and Type

Field

Description

static

ObjectStreamField

[]

NO_FIELDS

serialPersistentFields value indicating no serializable fields

---

#### Field Summary

serialPersistentFields value indicating no serializable fields

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<?>

forClass

()

Return the class in the local VM that this version is mapped to.

ObjectStreamField

getField

​(

String

name)

Get the field of this class by name.

ObjectStreamField

[]

getFields

()

Return an array of the fields of this serializable class.

String

getName

()

Returns the name of the class described by this descriptor.

long

getSerialVersionUID

()

Return the serialVersionUID for this class.

static

ObjectStreamClass

lookup

​(

Class

<?> cl)

Find the descriptor for a class that can be serialized.

static

ObjectStreamClass

lookupAny

​(

Class

<?> cl)

Returns the descriptor for any class, regardless of whether it
implements

Serializable

.

String

toString

()

Return a string describing this ObjectStreamClass.

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

Return the class in the local VM that this version is mapped to.

Get the field of this class by name.

Return an array of the fields of this serializable class.

Returns the name of the class described by this descriptor.

Return the serialVersionUID for this class.

Find the descriptor for a class that can be serialized.

Returns the descriptor for any class, regardless of whether it
implements

Serializable

.

Return a string describing this ObjectStreamClass.

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

============ FIELD DETAIL ===========

- Field Detail

- NO_FIELDS

```java
public static final
ObjectStreamField
[] NO_FIELDS
```

serialPersistentFields value indicating no serializable fields

============ METHOD DETAIL ==========

- Method Detail

- lookup

```java
public static
ObjectStreamClass
lookup​(
Class
<?> cl)
```

Find the descriptor for a class that can be serialized. Creates an
ObjectStreamClass instance if one does not exist yet for class. Null is
returned if the specified class does not implement java.io.Serializable
or java.io.Externalizable.

**Parameters:** cl

- class for which to get the descriptor
**Returns:** the class descriptor for the specified class

- lookupAny

```java
public static
ObjectStreamClass
lookupAny​(
Class
<?> cl)
```

Returns the descriptor for any class, regardless of whether it
implements

Serializable

.

**Parameters:** cl

- class for which to get the descriptor
**Returns:** the class descriptor for the specified class
**Since:** 1.6

- getName

```java
public
String
getName()
```

Returns the name of the class described by this descriptor.
This method returns the name of the class in the format that
is used by the

Class.getName()

method.

**Returns:** a string representing the name of the class

- getSerialVersionUID

```java
public long getSerialVersionUID()
```

Return the serialVersionUID for this class. The serialVersionUID
defines a set of classes all with the same name that have evolved from a
common root class and agree to be serialized and deserialized using a
common format. NonSerializable classes have a serialVersionUID of 0L.

**Returns:** the SUID of the class described by this descriptor

- forClass

```java
public
Class
<?> forClass()
```

Return the class in the local VM that this version is mapped to. Null
is returned if there is no corresponding local class.

**Returns:** the

Class

instance that this descriptor represents

- getFields

```java
public
ObjectStreamField
[] getFields()
```

Return an array of the fields of this serializable class.

**Returns:** an array containing an element for each persistent field of
this class. Returns an array of length zero if there are no
fields.
**Since:** 1.2

- getField

```java
public
ObjectStreamField
getField​(
String
name)
```

Get the field of this class by name.

**Parameters:** name

- the name of the data field to look for
**Returns:** The ObjectStreamField object of the named field or null if
there is no such named field.

- toString

```java
public
String
toString()
```

Return a string describing this ObjectStreamClass.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Field Detail

- NO_FIELDS

```java
public static final
ObjectStreamField
[] NO_FIELDS
```

serialPersistentFields value indicating no serializable fields

---

#### Field Detail

NO_FIELDS

```java
public static final
ObjectStreamField
[] NO_FIELDS
```

serialPersistentFields value indicating no serializable fields

---

#### NO_FIELDS

public static final

ObjectStreamField

[] NO_FIELDS

serialPersistentFields value indicating no serializable fields

Method Detail

- lookup

```java
public static
ObjectStreamClass
lookup​(
Class
<?> cl)
```

Find the descriptor for a class that can be serialized. Creates an
ObjectStreamClass instance if one does not exist yet for class. Null is
returned if the specified class does not implement java.io.Serializable
or java.io.Externalizable.

**Parameters:** cl

- class for which to get the descriptor
**Returns:** the class descriptor for the specified class

- lookupAny

```java
public static
ObjectStreamClass
lookupAny​(
Class
<?> cl)
```

Returns the descriptor for any class, regardless of whether it
implements

Serializable

.

**Parameters:** cl

- class for which to get the descriptor
**Returns:** the class descriptor for the specified class
**Since:** 1.6

- getName

```java
public
String
getName()
```

Returns the name of the class described by this descriptor.
This method returns the name of the class in the format that
is used by the

Class.getName()

method.

**Returns:** a string representing the name of the class

- getSerialVersionUID

```java
public long getSerialVersionUID()
```

Return the serialVersionUID for this class. The serialVersionUID
defines a set of classes all with the same name that have evolved from a
common root class and agree to be serialized and deserialized using a
common format. NonSerializable classes have a serialVersionUID of 0L.

**Returns:** the SUID of the class described by this descriptor

- forClass

```java
public
Class
<?> forClass()
```

Return the class in the local VM that this version is mapped to. Null
is returned if there is no corresponding local class.

**Returns:** the

Class

instance that this descriptor represents

- getFields

```java
public
ObjectStreamField
[] getFields()
```

Return an array of the fields of this serializable class.

**Returns:** an array containing an element for each persistent field of
this class. Returns an array of length zero if there are no
fields.
**Since:** 1.2

- getField

```java
public
ObjectStreamField
getField​(
String
name)
```

Get the field of this class by name.

**Parameters:** name

- the name of the data field to look for
**Returns:** The ObjectStreamField object of the named field or null if
there is no such named field.

- toString

```java
public
String
toString()
```

Return a string describing this ObjectStreamClass.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

lookup

```java
public static
ObjectStreamClass
lookup​(
Class
<?> cl)
```

Find the descriptor for a class that can be serialized. Creates an
ObjectStreamClass instance if one does not exist yet for class. Null is
returned if the specified class does not implement java.io.Serializable
or java.io.Externalizable.

**Parameters:** cl

- class for which to get the descriptor
**Returns:** the class descriptor for the specified class

---

#### lookup

public static

ObjectStreamClass

lookup​(

Class

<?> cl)

Find the descriptor for a class that can be serialized. Creates an
ObjectStreamClass instance if one does not exist yet for class. Null is
returned if the specified class does not implement java.io.Serializable
or java.io.Externalizable.

lookupAny

```java
public static
ObjectStreamClass
lookupAny​(
Class
<?> cl)
```

Returns the descriptor for any class, regardless of whether it
implements

Serializable

.

**Parameters:** cl

- class for which to get the descriptor
**Returns:** the class descriptor for the specified class
**Since:** 1.6

---

#### lookupAny

public static

ObjectStreamClass

lookupAny​(

Class

<?> cl)

Returns the descriptor for any class, regardless of whether it
implements

Serializable

.

getName

```java
public
String
getName()
```

Returns the name of the class described by this descriptor.
This method returns the name of the class in the format that
is used by the

Class.getName()

method.

**Returns:** a string representing the name of the class

---

#### getName

public

String

getName()

Returns the name of the class described by this descriptor.
This method returns the name of the class in the format that
is used by the

Class.getName()

method.

getSerialVersionUID

```java
public long getSerialVersionUID()
```

Return the serialVersionUID for this class. The serialVersionUID
defines a set of classes all with the same name that have evolved from a
common root class and agree to be serialized and deserialized using a
common format. NonSerializable classes have a serialVersionUID of 0L.

**Returns:** the SUID of the class described by this descriptor

---

#### getSerialVersionUID

public long getSerialVersionUID()

Return the serialVersionUID for this class. The serialVersionUID
defines a set of classes all with the same name that have evolved from a
common root class and agree to be serialized and deserialized using a
common format. NonSerializable classes have a serialVersionUID of 0L.

forClass

```java
public
Class
<?> forClass()
```

Return the class in the local VM that this version is mapped to. Null
is returned if there is no corresponding local class.

**Returns:** the

Class

instance that this descriptor represents

---

#### forClass

public

Class

<?> forClass()

Return the class in the local VM that this version is mapped to. Null
is returned if there is no corresponding local class.

getFields

```java
public
ObjectStreamField
[] getFields()
```

Return an array of the fields of this serializable class.

**Returns:** an array containing an element for each persistent field of
this class. Returns an array of length zero if there are no
fields.
**Since:** 1.2

---

#### getFields

public

ObjectStreamField

[] getFields()

Return an array of the fields of this serializable class.

getField

```java
public
ObjectStreamField
getField​(
String
name)
```

Get the field of this class by name.

**Parameters:** name

- the name of the data field to look for
**Returns:** The ObjectStreamField object of the named field or null if
there is no such named field.

---

#### getField

public

ObjectStreamField

getField​(

String

name)

Get the field of this class by name.

toString

```java
public
String
toString()
```

Return a string describing this ObjectStreamClass.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Return a string describing this ObjectStreamClass.

---

