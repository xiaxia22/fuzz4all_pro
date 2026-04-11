# Interface Externalizable

**Source:** `java.base\java\io\Externalizable.html`

### Class Description

```java
public interface
Externalizable

extends
Serializable
```

Only the identity of the class of an Externalizable instance is
written in the serialization stream and it is the responsibility
of the class to save and restore the contents of its instances.

The writeExternal and readExternal methods of the Externalizable
interface are implemented by a class to give the class complete
control over the format and contents of the stream for an object
and its supertypes. These methods must explicitly
coordinate with the supertype to save its state. These methods supersede
customized implementations of writeObject and readObject methods.

Object Serialization uses the Serializable and Externalizable
interfaces. Object persistence mechanisms can use them as well. Each
object to be stored is tested for the Externalizable interface. If
the object supports Externalizable, the writeExternal method is called. If the
object does not support Externalizable and does implement
Serializable, the object is saved using
ObjectOutputStream.

When an Externalizable object is
reconstructed, an instance is created using the public no-arg
constructor, then the readExternal method called. Serializable
objects are restored by reading them from an ObjectInputStream.

An Externalizable instance can designate a substitution object via
the writeReplace and readResolve methods documented in the Serializable
interface.

**All Superinterfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void writeExternal​(
ObjectOutput
out)
throws
IOException

The object implements the writeExternal method to save its contents
by calling the methods of DataOutput for its primitive values or
calling the writeObject method of ObjectOutput for objects, strings,
and arrays.

**Parameters:**
- out

- the stream to write the object to

**Throws:**
- IOException

- Includes any I/O exceptions that may occur

---

#### void readExternal​(
ObjectInput
in)
throws
IOException
,

ClassNotFoundException

The object implements the readExternal method to restore its
contents by calling the methods of DataInput for primitive
types and readObject for objects, strings and arrays. The
readExternal method must read the values in the same sequence
and with the same types as were written by writeExternal.

**Parameters:**
- in

- the stream to read data from in order to restore the object

**Throws:**
- IOException

- if I/O errors occur
- ClassNotFoundException

- If the class for an object being
restored cannot be found.

---

### Additional Sections

#### Interface Externalizable

**All Superinterfaces:** Serializable

**All Known Subinterfaces:** RemoteRef

,

ServerRef

**All Known Implementing Classes:** DataFlavor

,

MLet

,

PrivateMLet

```java
public interface
Externalizable

extends
Serializable
```

Only the identity of the class of an Externalizable instance is
written in the serialization stream and it is the responsibility
of the class to save and restore the contents of its instances.

The writeExternal and readExternal methods of the Externalizable
interface are implemented by a class to give the class complete
control over the format and contents of the stream for an object
and its supertypes. These methods must explicitly
coordinate with the supertype to save its state. These methods supersede
customized implementations of writeObject and readObject methods.

Object Serialization uses the Serializable and Externalizable
interfaces. Object persistence mechanisms can use them as well. Each
object to be stored is tested for the Externalizable interface. If
the object supports Externalizable, the writeExternal method is called. If the
object does not support Externalizable and does implement
Serializable, the object is saved using
ObjectOutputStream.

When an Externalizable object is
reconstructed, an instance is created using the public no-arg
constructor, then the readExternal method called. Serializable
objects are restored by reading them from an ObjectInputStream.

An Externalizable instance can designate a substitution object via
the writeReplace and readResolve methods documented in the Serializable
interface.

**Since:** 1.1
**See Also:** ObjectOutputStream

,

ObjectInputStream

,

ObjectOutput

,

ObjectInput

,

Serializable

public interface

Externalizable

extends

Serializable

Only the identity of the class of an Externalizable instance is
written in the serialization stream and it is the responsibility
of the class to save and restore the contents of its instances.

The writeExternal and readExternal methods of the Externalizable
interface are implemented by a class to give the class complete
control over the format and contents of the stream for an object
and its supertypes. These methods must explicitly
coordinate with the supertype to save its state. These methods supersede
customized implementations of writeObject and readObject methods.

Object Serialization uses the Serializable and Externalizable
interfaces. Object persistence mechanisms can use them as well. Each
object to be stored is tested for the Externalizable interface. If
the object supports Externalizable, the writeExternal method is called. If the
object does not support Externalizable and does implement
Serializable, the object is saved using
ObjectOutputStream.

When an Externalizable object is
reconstructed, an instance is created using the public no-arg
constructor, then the readExternal method called. Serializable
objects are restored by reading them from an ObjectInputStream.

An Externalizable instance can designate a substitution object via
the writeReplace and readResolve methods documented in the Serializable
interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

readExternal

​(

ObjectInput

in)

The object implements the readExternal method to restore its
contents by calling the methods of DataInput for primitive
types and readObject for objects, strings and arrays.

void

writeExternal

​(

ObjectOutput

out)

The object implements the writeExternal method to save its contents
by calling the methods of DataOutput for its primitive values or
calling the writeObject method of ObjectOutput for objects, strings,
and arrays.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

readExternal

​(

ObjectInput

in)

The object implements the readExternal method to restore its
contents by calling the methods of DataInput for primitive
types and readObject for objects, strings and arrays.

void

writeExternal

​(

ObjectOutput

out)

The object implements the writeExternal method to save its contents
by calling the methods of DataOutput for its primitive values or
calling the writeObject method of ObjectOutput for objects, strings,
and arrays.

---

#### Method Summary

The object implements the readExternal method to restore its
contents by calling the methods of DataInput for primitive
types and readObject for objects, strings and arrays.

The object implements the writeExternal method to save its contents
by calling the methods of DataOutput for its primitive values or
calling the writeObject method of ObjectOutput for objects, strings,
and arrays.

============ METHOD DETAIL ==========

- Method Detail

- writeExternal

```java
void writeExternal​(
ObjectOutput
out)
throws
IOException
```

The object implements the writeExternal method to save its contents
by calling the methods of DataOutput for its primitive values or
calling the writeObject method of ObjectOutput for objects, strings,
and arrays.

**Parameters:** out

- the stream to write the object to
**Throws:** IOException

- Includes any I/O exceptions that may occur

- readExternal

```java
void readExternal​(
ObjectInput
in)
throws
IOException
,

ClassNotFoundException
```

The object implements the readExternal method to restore its
contents by calling the methods of DataInput for primitive
types and readObject for objects, strings and arrays. The
readExternal method must read the values in the same sequence
and with the same types as were written by writeExternal.

**Parameters:** in

- the stream to read data from in order to restore the object
**Throws:** IOException

- if I/O errors occur
**Throws:** ClassNotFoundException

- If the class for an object being
restored cannot be found.

Method Detail

- writeExternal

```java
void writeExternal​(
ObjectOutput
out)
throws
IOException
```

The object implements the writeExternal method to save its contents
by calling the methods of DataOutput for its primitive values or
calling the writeObject method of ObjectOutput for objects, strings,
and arrays.

**Parameters:** out

- the stream to write the object to
**Throws:** IOException

- Includes any I/O exceptions that may occur

- readExternal

```java
void readExternal​(
ObjectInput
in)
throws
IOException
,

ClassNotFoundException
```

The object implements the readExternal method to restore its
contents by calling the methods of DataInput for primitive
types and readObject for objects, strings and arrays. The
readExternal method must read the values in the same sequence
and with the same types as were written by writeExternal.

**Parameters:** in

- the stream to read data from in order to restore the object
**Throws:** IOException

- if I/O errors occur
**Throws:** ClassNotFoundException

- If the class for an object being
restored cannot be found.

---

#### Method Detail

writeExternal

```java
void writeExternal​(
ObjectOutput
out)
throws
IOException
```

The object implements the writeExternal method to save its contents
by calling the methods of DataOutput for its primitive values or
calling the writeObject method of ObjectOutput for objects, strings,
and arrays.

**Parameters:** out

- the stream to write the object to
**Throws:** IOException

- Includes any I/O exceptions that may occur

---

#### writeExternal

void writeExternal​(

ObjectOutput

out)
throws

IOException

The object implements the writeExternal method to save its contents
by calling the methods of DataOutput for its primitive values or
calling the writeObject method of ObjectOutput for objects, strings,
and arrays.

readExternal

```java
void readExternal​(
ObjectInput
in)
throws
IOException
,

ClassNotFoundException
```

The object implements the readExternal method to restore its
contents by calling the methods of DataInput for primitive
types and readObject for objects, strings and arrays. The
readExternal method must read the values in the same sequence
and with the same types as were written by writeExternal.

**Parameters:** in

- the stream to read data from in order to restore the object
**Throws:** IOException

- if I/O errors occur
**Throws:** ClassNotFoundException

- If the class for an object being
restored cannot be found.

---

#### readExternal

void readExternal​(

ObjectInput

in)
throws

IOException

,

ClassNotFoundException

The object implements the readExternal method to restore its
contents by calling the methods of DataInput for primitive
types and readObject for objects, strings and arrays. The
readExternal method must read the values in the same sequence
and with the same types as were written by writeExternal.

---

