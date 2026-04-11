# Class Manifest

**Source:** `java.base\java\util\jar\Manifest.html`

### Class Description

```java
public class
Manifest

extends
Object

implements
Cloneable
```

The Manifest class is used to maintain Manifest entry names and their
associated Attributes. There are main Manifest Attributes as well as
per-entry Attributes. For information on the Manifest format, please
see the

Manifest format specification

.

**All Implemented Interfaces:** Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public Manifest()

Constructs a new, empty Manifest.

---

#### public Manifest​(
InputStream
is)
throws
IOException

Constructs a new Manifest from the specified input stream.

**Parameters:**
- is

- the input stream containing manifest data

**Throws:**
- IOException

- if an I/O error has occurred

---

#### public Manifest​(
Manifest
man)

Constructs a new Manifest that is a copy of the specified Manifest.

**Parameters:**
- man

- the Manifest to copy

---

### Method Details

#### public
Attributes
getMainAttributes()

Returns the main Attributes for the Manifest.

**Returns:**
- the main Attributes for the Manifest

---

#### public
Map
<
String
,​
Attributes
> getEntries()

Returns a Map of the entries contained in this Manifest. Each entry
is represented by a String name (key) and associated Attributes (value).
The Map permits the

null

key, but no entry with a null key is
created by

read(java.io.InputStream)

, nor is such an entry written by using

write(java.io.OutputStream)

.

**Returns:**
- a Map of the entries contained in this Manifest

---

#### public
Attributes
getAttributes​(
String
name)

Returns the Attributes for the specified entry name.
This method is defined as:

```java
return (Attributes)getEntries().get(name)
```

Though

null

is a valid

name

, when

getAttributes(null)

is invoked on a

Manifest

obtained from a jar file,

null

will be returned. While jar
files themselves do not allow

null

-named attributes, it is
possible to invoke

getEntries()

on a

Manifest

, and
on that result, invoke

put

with a null key and an
arbitrary value. Subsequent invocations of

getAttributes(null)

will return the just-

put

value.

Note that this method does not return the manifest's main attributes;
see

getMainAttributes()

.

**Parameters:**
- name

- entry name

**Returns:**
- the Attributes for the specified entry name

---

#### public void clear()

Clears the main Attributes as well as the entries in this Manifest.

---

#### public void write​(
OutputStream
out)
throws
IOException

Writes the Manifest to the specified OutputStream.
Attributes.Name.MANIFEST_VERSION must be set in
MainAttributes prior to invoking this method.

**Parameters:**
- out

- the output stream

**Throws:**
- IOException

- if an I/O error has occurred

**See Also:**
- getMainAttributes()

---

#### public void read​(
InputStream
is)
throws
IOException

Reads the Manifest from the specified InputStream. The entry
names and attributes read will be merged in with the current
manifest entries.

**Parameters:**
- is

- the input stream

**Throws:**
- IOException

- if an I/O error has occurred

---

#### public boolean equals​(
Object
o)

Returns true if the specified Object is also a Manifest and has
the same main Attributes and entries.

**Overrides:**
- equals

in class

Object

**Parameters:**
- o

- the object to be compared

**Returns:**
- true if the specified Object is also a Manifest and has
the same main Attributes and entries

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code for this Manifest.

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
Object
clone()

Returns a shallow copy of this Manifest. The shallow copy is
implemented as follows:

```java
public Object clone() { return new Manifest(this); }
```

**Overrides:**
- clone

in class

Object

**Returns:**
- a shallow copy of this Manifest

**See Also:**
- Cloneable

---

### Additional Sections

#### Class Manifest

java.lang.Object

- java.util.jar.Manifest

java.util.jar.Manifest

**All Implemented Interfaces:** Cloneable

```java
public class
Manifest

extends
Object

implements
Cloneable
```

The Manifest class is used to maintain Manifest entry names and their
associated Attributes. There are main Manifest Attributes as well as
per-entry Attributes. For information on the Manifest format, please
see the

Manifest format specification

.

**Since:** 1.2
**See Also:** Attributes

public class

Manifest

extends

Object

implements

Cloneable

The Manifest class is used to maintain Manifest entry names and their
associated Attributes. There are main Manifest Attributes as well as
per-entry Attributes. For information on the Manifest format, please
see the

Manifest format specification

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Manifest

()

Constructs a new, empty Manifest.

Manifest

​(

InputStream

is)

Constructs a new Manifest from the specified input stream.

Manifest

​(

Manifest

man)

Constructs a new Manifest that is a copy of the specified Manifest.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

clear

()

Clears the main Attributes as well as the entries in this Manifest.

Object

clone

()

Returns a shallow copy of this Manifest.

boolean

equals

​(

Object

o)

Returns true if the specified Object is also a Manifest and has
the same main Attributes and entries.

Attributes

getAttributes

​(

String

name)

Returns the Attributes for the specified entry name.

Map

<

String

,​

Attributes

>

getEntries

()

Returns a Map of the entries contained in this Manifest.

Attributes

getMainAttributes

()

Returns the main Attributes for the Manifest.

int

hashCode

()

Returns the hash code for this Manifest.

void

read

​(

InputStream

is)

Reads the Manifest from the specified InputStream.

void

write

​(

OutputStream

out)

Writes the Manifest to the specified OutputStream.

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

Manifest

()

Constructs a new, empty Manifest.

Manifest

​(

InputStream

is)

Constructs a new Manifest from the specified input stream.

Manifest

​(

Manifest

man)

Constructs a new Manifest that is a copy of the specified Manifest.

---

#### Constructor Summary

Constructs a new, empty Manifest.

Constructs a new Manifest from the specified input stream.

Constructs a new Manifest that is a copy of the specified Manifest.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

clear

()

Clears the main Attributes as well as the entries in this Manifest.

Object

clone

()

Returns a shallow copy of this Manifest.

boolean

equals

​(

Object

o)

Returns true if the specified Object is also a Manifest and has
the same main Attributes and entries.

Attributes

getAttributes

​(

String

name)

Returns the Attributes for the specified entry name.

Map

<

String

,​

Attributes

>

getEntries

()

Returns a Map of the entries contained in this Manifest.

Attributes

getMainAttributes

()

Returns the main Attributes for the Manifest.

int

hashCode

()

Returns the hash code for this Manifest.

void

read

​(

InputStream

is)

Reads the Manifest from the specified InputStream.

void

write

​(

OutputStream

out)

Writes the Manifest to the specified OutputStream.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Clears the main Attributes as well as the entries in this Manifest.

Returns a shallow copy of this Manifest.

Returns true if the specified Object is also a Manifest and has
the same main Attributes and entries.

Returns the Attributes for the specified entry name.

Returns a Map of the entries contained in this Manifest.

Returns the main Attributes for the Manifest.

Returns the hash code for this Manifest.

Reads the Manifest from the specified InputStream.

Writes the Manifest to the specified OutputStream.

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

- Manifest

```java
public Manifest()
```

Constructs a new, empty Manifest.

- Manifest

```java
public Manifest​(
InputStream
is)
throws
IOException
```

Constructs a new Manifest from the specified input stream.

**Parameters:** is

- the input stream containing manifest data
**Throws:** IOException

- if an I/O error has occurred

- Manifest

```java
public Manifest​(
Manifest
man)
```

Constructs a new Manifest that is a copy of the specified Manifest.

**Parameters:** man

- the Manifest to copy

============ METHOD DETAIL ==========

- Method Detail

- getMainAttributes

```java
public
Attributes
getMainAttributes()
```

Returns the main Attributes for the Manifest.

**Returns:** the main Attributes for the Manifest

- getEntries

```java
public
Map
<
String
,​
Attributes
> getEntries()
```

Returns a Map of the entries contained in this Manifest. Each entry
is represented by a String name (key) and associated Attributes (value).
The Map permits the

null

key, but no entry with a null key is
created by

read(java.io.InputStream)

, nor is such an entry written by using

write(java.io.OutputStream)

.

**Returns:** a Map of the entries contained in this Manifest

- getAttributes

```java
public
Attributes
getAttributes​(
String
name)
```

Returns the Attributes for the specified entry name.
This method is defined as:

```java
return (Attributes)getEntries().get(name)
```

Though

null

is a valid

name

, when

getAttributes(null)

is invoked on a

Manifest

obtained from a jar file,

null

will be returned. While jar
files themselves do not allow

null

-named attributes, it is
possible to invoke

getEntries()

on a

Manifest

, and
on that result, invoke

put

with a null key and an
arbitrary value. Subsequent invocations of

getAttributes(null)

will return the just-

put

value.

Note that this method does not return the manifest's main attributes;
see

getMainAttributes()

.

**Parameters:** name

- entry name
**Returns:** the Attributes for the specified entry name

- clear

```java
public void clear()
```

Clears the main Attributes as well as the entries in this Manifest.

- write

```java
public void write​(
OutputStream
out)
throws
IOException
```

Writes the Manifest to the specified OutputStream.
Attributes.Name.MANIFEST_VERSION must be set in
MainAttributes prior to invoking this method.

**Parameters:** out

- the output stream
**Throws:** IOException

- if an I/O error has occurred
**See Also:** getMainAttributes()

- read

```java
public void read​(
InputStream
is)
throws
IOException
```

Reads the Manifest from the specified InputStream. The entry
names and attributes read will be merged in with the current
manifest entries.

**Parameters:** is

- the input stream
**Throws:** IOException

- if an I/O error has occurred

- equals

```java
public boolean equals​(
Object
o)
```

Returns true if the specified Object is also a Manifest and has
the same main Attributes and entries.

**Overrides:** equals

in class

Object
**Parameters:** o

- the object to be compared
**Returns:** true if the specified Object is also a Manifest and has
the same main Attributes and entries
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code for this Manifest.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- clone

```java
public
Object
clone()
```

Returns a shallow copy of this Manifest. The shallow copy is
implemented as follows:

```java
public Object clone() { return new Manifest(this); }
```

**Overrides:** clone

in class

Object
**Returns:** a shallow copy of this Manifest
**See Also:** Cloneable

Constructor Detail

- Manifest

```java
public Manifest()
```

Constructs a new, empty Manifest.

- Manifest

```java
public Manifest​(
InputStream
is)
throws
IOException
```

Constructs a new Manifest from the specified input stream.

**Parameters:** is

- the input stream containing manifest data
**Throws:** IOException

- if an I/O error has occurred

- Manifest

```java
public Manifest​(
Manifest
man)
```

Constructs a new Manifest that is a copy of the specified Manifest.

**Parameters:** man

- the Manifest to copy

---

#### Constructor Detail

Manifest

```java
public Manifest()
```

Constructs a new, empty Manifest.

---

#### Manifest

public Manifest()

Constructs a new, empty Manifest.

Manifest

```java
public Manifest​(
InputStream
is)
throws
IOException
```

Constructs a new Manifest from the specified input stream.

**Parameters:** is

- the input stream containing manifest data
**Throws:** IOException

- if an I/O error has occurred

---

#### Manifest

public Manifest​(

InputStream

is)
throws

IOException

Constructs a new Manifest from the specified input stream.

Manifest

```java
public Manifest​(
Manifest
man)
```

Constructs a new Manifest that is a copy of the specified Manifest.

**Parameters:** man

- the Manifest to copy

---

#### Manifest

public Manifest​(

Manifest

man)

Constructs a new Manifest that is a copy of the specified Manifest.

Method Detail

- getMainAttributes

```java
public
Attributes
getMainAttributes()
```

Returns the main Attributes for the Manifest.

**Returns:** the main Attributes for the Manifest

- getEntries

```java
public
Map
<
String
,​
Attributes
> getEntries()
```

Returns a Map of the entries contained in this Manifest. Each entry
is represented by a String name (key) and associated Attributes (value).
The Map permits the

null

key, but no entry with a null key is
created by

read(java.io.InputStream)

, nor is such an entry written by using

write(java.io.OutputStream)

.

**Returns:** a Map of the entries contained in this Manifest

- getAttributes

```java
public
Attributes
getAttributes​(
String
name)
```

Returns the Attributes for the specified entry name.
This method is defined as:

```java
return (Attributes)getEntries().get(name)
```

Though

null

is a valid

name

, when

getAttributes(null)

is invoked on a

Manifest

obtained from a jar file,

null

will be returned. While jar
files themselves do not allow

null

-named attributes, it is
possible to invoke

getEntries()

on a

Manifest

, and
on that result, invoke

put

with a null key and an
arbitrary value. Subsequent invocations of

getAttributes(null)

will return the just-

put

value.

Note that this method does not return the manifest's main attributes;
see

getMainAttributes()

.

**Parameters:** name

- entry name
**Returns:** the Attributes for the specified entry name

- clear

```java
public void clear()
```

Clears the main Attributes as well as the entries in this Manifest.

- write

```java
public void write​(
OutputStream
out)
throws
IOException
```

Writes the Manifest to the specified OutputStream.
Attributes.Name.MANIFEST_VERSION must be set in
MainAttributes prior to invoking this method.

**Parameters:** out

- the output stream
**Throws:** IOException

- if an I/O error has occurred
**See Also:** getMainAttributes()

- read

```java
public void read​(
InputStream
is)
throws
IOException
```

Reads the Manifest from the specified InputStream. The entry
names and attributes read will be merged in with the current
manifest entries.

**Parameters:** is

- the input stream
**Throws:** IOException

- if an I/O error has occurred

- equals

```java
public boolean equals​(
Object
o)
```

Returns true if the specified Object is also a Manifest and has
the same main Attributes and entries.

**Overrides:** equals

in class

Object
**Parameters:** o

- the object to be compared
**Returns:** true if the specified Object is also a Manifest and has
the same main Attributes and entries
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code for this Manifest.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- clone

```java
public
Object
clone()
```

Returns a shallow copy of this Manifest. The shallow copy is
implemented as follows:

```java
public Object clone() { return new Manifest(this); }
```

**Overrides:** clone

in class

Object
**Returns:** a shallow copy of this Manifest
**See Also:** Cloneable

---

#### Method Detail

getMainAttributes

```java
public
Attributes
getMainAttributes()
```

Returns the main Attributes for the Manifest.

**Returns:** the main Attributes for the Manifest

---

#### getMainAttributes

public

Attributes

getMainAttributes()

Returns the main Attributes for the Manifest.

getEntries

```java
public
Map
<
String
,​
Attributes
> getEntries()
```

Returns a Map of the entries contained in this Manifest. Each entry
is represented by a String name (key) and associated Attributes (value).
The Map permits the

null

key, but no entry with a null key is
created by

read(java.io.InputStream)

, nor is such an entry written by using

write(java.io.OutputStream)

.

**Returns:** a Map of the entries contained in this Manifest

---

#### getEntries

public

Map

<

String

,​

Attributes

> getEntries()

Returns a Map of the entries contained in this Manifest. Each entry
is represented by a String name (key) and associated Attributes (value).
The Map permits the

null

key, but no entry with a null key is
created by

read(java.io.InputStream)

, nor is such an entry written by using

write(java.io.OutputStream)

.

getAttributes

```java
public
Attributes
getAttributes​(
String
name)
```

Returns the Attributes for the specified entry name.
This method is defined as:

```java
return (Attributes)getEntries().get(name)
```

Though

null

is a valid

name

, when

getAttributes(null)

is invoked on a

Manifest

obtained from a jar file,

null

will be returned. While jar
files themselves do not allow

null

-named attributes, it is
possible to invoke

getEntries()

on a

Manifest

, and
on that result, invoke

put

with a null key and an
arbitrary value. Subsequent invocations of

getAttributes(null)

will return the just-

put

value.

Note that this method does not return the manifest's main attributes;
see

getMainAttributes()

.

**Parameters:** name

- entry name
**Returns:** the Attributes for the specified entry name

---

#### getAttributes

public

Attributes

getAttributes​(

String

name)

Returns the Attributes for the specified entry name.
This method is defined as:

```java
return (Attributes)getEntries().get(name)
```

Though

null

is a valid

name

, when

getAttributes(null)

is invoked on a

Manifest

obtained from a jar file,

null

will be returned. While jar
files themselves do not allow

null

-named attributes, it is
possible to invoke

getEntries()

on a

Manifest

, and
on that result, invoke

put

with a null key and an
arbitrary value. Subsequent invocations of

getAttributes(null)

will return the just-

put

value.

Note that this method does not return the manifest's main attributes;
see

getMainAttributes()

.

return (Attributes)getEntries().get(name)

Note that this method does not return the manifest's main attributes;
see

getMainAttributes()

.

clear

```java
public void clear()
```

Clears the main Attributes as well as the entries in this Manifest.

---

#### clear

public void clear()

Clears the main Attributes as well as the entries in this Manifest.

write

```java
public void write​(
OutputStream
out)
throws
IOException
```

Writes the Manifest to the specified OutputStream.
Attributes.Name.MANIFEST_VERSION must be set in
MainAttributes prior to invoking this method.

**Parameters:** out

- the output stream
**Throws:** IOException

- if an I/O error has occurred
**See Also:** getMainAttributes()

---

#### write

public void write​(

OutputStream

out)
throws

IOException

Writes the Manifest to the specified OutputStream.
Attributes.Name.MANIFEST_VERSION must be set in
MainAttributes prior to invoking this method.

read

```java
public void read​(
InputStream
is)
throws
IOException
```

Reads the Manifest from the specified InputStream. The entry
names and attributes read will be merged in with the current
manifest entries.

**Parameters:** is

- the input stream
**Throws:** IOException

- if an I/O error has occurred

---

#### read

public void read​(

InputStream

is)
throws

IOException

Reads the Manifest from the specified InputStream. The entry
names and attributes read will be merged in with the current
manifest entries.

equals

```java
public boolean equals​(
Object
o)
```

Returns true if the specified Object is also a Manifest and has
the same main Attributes and entries.

**Overrides:** equals

in class

Object
**Parameters:** o

- the object to be compared
**Returns:** true if the specified Object is also a Manifest and has
the same main Attributes and entries
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Returns true if the specified Object is also a Manifest and has
the same main Attributes and entries.

hashCode

```java
public int hashCode()
```

Returns the hash code for this Manifest.

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

Returns the hash code for this Manifest.

clone

```java
public
Object
clone()
```

Returns a shallow copy of this Manifest. The shallow copy is
implemented as follows:

```java
public Object clone() { return new Manifest(this); }
```

**Overrides:** clone

in class

Object
**Returns:** a shallow copy of this Manifest
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Returns a shallow copy of this Manifest. The shallow copy is
implemented as follows:

```java
public Object clone() { return new Manifest(this); }
```

public Object clone() { return new Manifest(this); }

---

