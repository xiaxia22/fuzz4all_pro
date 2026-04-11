# Class ListResourceBundle

**Source:** `java.base\java\util\ListResourceBundle.html`

### Class Description

```java
public abstract class
ListResourceBundle

extends
ResourceBundle
```

ListResourceBundle

is an abstract subclass of

ResourceBundle

that manages resources for a locale
in a convenient and easy to use list. See

ResourceBundle

for
more information about resource bundles in general.

Subclasses must override

getContents

and provide an array,
where each item in the array is a pair of objects.
The first element of each pair is the key, which must be a

String

, and the second element is the value associated with
that key.

The following

example

shows two members of a resource
bundle family with the base name "MyResources".
"MyResources" is the default member of the bundle family, and
"MyResources_fr" is the French member.
These members are based on

ListResourceBundle

(a related

example

shows
how you can add a bundle to this family that's based on a properties file).
The keys in this example are of the form "s1" etc. The actual
keys are entirely up to your choice, so long as they are the same as
the keys you use in your program to retrieve the objects from the bundle.
Keys are case-sensitive.

```java
public class MyResources extends ListResourceBundle {
protected Object[][] getContents() {
return new Object[][] {
// LOCALIZE THIS
{"s1", "The disk \"{1}\" contains {0}."}, // MessageFormat pattern
{"s2", "1"}, // location of {0} in pattern
{"s3", "My Disk"}, // sample disk name
{"s4", "no files"}, // first ChoiceFormat choice
{"s5", "one file"}, // second ChoiceFormat choice
{"s6", "{0,number} files"}, // third ChoiceFormat choice
{"s7", "3 Mar 96"}, // sample date
{"s8", new Dimension(1,5)} // real object, not just string
// END OF MATERIAL TO LOCALIZE
};
}
}

public class MyResources_fr extends ListResourceBundle {
protected Object[][] getContents() {
return new Object[][] {
// LOCALIZE THIS
{"s1", "Le disque \"{1}\" {0}."}, // MessageFormat pattern
{"s2", "1"}, // location of {0} in pattern
{"s3", "Mon disque"}, // sample disk name
{"s4", "ne contient pas de fichiers"}, // first ChoiceFormat choice
{"s5", "contient un fichier"}, // second ChoiceFormat choice
{"s6", "contient {0,number} fichiers"}, // third ChoiceFormat choice
{"s7", "3 mars 1996"}, // sample date
{"s8", new Dimension(1,3)} // real object, not just string
// END OF MATERIAL TO LOCALIZE
};
}
}
```

The implementation of a

ListResourceBundle

subclass must be thread-safe
if it's simultaneously used by multiple threads. The default implementations
of the methods in this class are thread-safe.

**Direct Known Subclasses:** AccessibleResourceBundle

---

### Field Details

*No entries found.*

### Constructor Details

#### public ListResourceBundle()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

### Method Details

#### public
Enumeration
<
String
> getKeys()

Returns an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.

**Specified by:**
- getKeys

in class

ResourceBundle

**Returns:**
- an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.

**See Also:**
- ResourceBundle.keySet()

---

#### protected
Set
<
String
> handleKeySet()

Returns a

Set

of the keys contained

only

in this

ResourceBundle

.

**Overrides:**
- handleKeySet

in class

ResourceBundle

**Returns:**
- a

Set

of the keys contained only in this

ResourceBundle

**See Also:**
- ResourceBundle.keySet()

**Since:**
- 1.6

---

#### protected abstract
Object
[][] getContents()

Returns an array in which each item is a pair of objects in an

Object

array. The first element of each pair is
the key, which must be a

String

, and the second
element is the value associated with that key. See the class
description for details.

**Returns:**
- an array of an

Object

array representing a
key-value pair.

---

### Additional Sections

#### Class ListResourceBundle

java.lang.Object

- java.util.ResourceBundle
- - java.util.ListResourceBundle

java.util.ResourceBundle

- java.util.ListResourceBundle

java.util.ListResourceBundle

**Direct Known Subclasses:** AccessibleResourceBundle

```java
public abstract class
ListResourceBundle

extends
ResourceBundle
```

ListResourceBundle

is an abstract subclass of

ResourceBundle

that manages resources for a locale
in a convenient and easy to use list. See

ResourceBundle

for
more information about resource bundles in general.

Subclasses must override

getContents

and provide an array,
where each item in the array is a pair of objects.
The first element of each pair is the key, which must be a

String

, and the second element is the value associated with
that key.

The following

example

shows two members of a resource
bundle family with the base name "MyResources".
"MyResources" is the default member of the bundle family, and
"MyResources_fr" is the French member.
These members are based on

ListResourceBundle

(a related

example

shows
how you can add a bundle to this family that's based on a properties file).
The keys in this example are of the form "s1" etc. The actual
keys are entirely up to your choice, so long as they are the same as
the keys you use in your program to retrieve the objects from the bundle.
Keys are case-sensitive.

```java
public class MyResources extends ListResourceBundle {
protected Object[][] getContents() {
return new Object[][] {
// LOCALIZE THIS
{"s1", "The disk \"{1}\" contains {0}."}, // MessageFormat pattern
{"s2", "1"}, // location of {0} in pattern
{"s3", "My Disk"}, // sample disk name
{"s4", "no files"}, // first ChoiceFormat choice
{"s5", "one file"}, // second ChoiceFormat choice
{"s6", "{0,number} files"}, // third ChoiceFormat choice
{"s7", "3 Mar 96"}, // sample date
{"s8", new Dimension(1,5)} // real object, not just string
// END OF MATERIAL TO LOCALIZE
};
}
}

public class MyResources_fr extends ListResourceBundle {
protected Object[][] getContents() {
return new Object[][] {
// LOCALIZE THIS
{"s1", "Le disque \"{1}\" {0}."}, // MessageFormat pattern
{"s2", "1"}, // location of {0} in pattern
{"s3", "Mon disque"}, // sample disk name
{"s4", "ne contient pas de fichiers"}, // first ChoiceFormat choice
{"s5", "contient un fichier"}, // second ChoiceFormat choice
{"s6", "contient {0,number} fichiers"}, // third ChoiceFormat choice
{"s7", "3 mars 1996"}, // sample date
{"s8", new Dimension(1,3)} // real object, not just string
// END OF MATERIAL TO LOCALIZE
};
}
}
```

The implementation of a

ListResourceBundle

subclass must be thread-safe
if it's simultaneously used by multiple threads. The default implementations
of the methods in this class are thread-safe.

**Since:** 1.1
**See Also:** ResourceBundle

,

PropertyResourceBundle

public abstract class

ListResourceBundle

extends

ResourceBundle

ListResourceBundle

is an abstract subclass of

ResourceBundle

that manages resources for a locale
in a convenient and easy to use list. See

ResourceBundle

for
more information about resource bundles in general.

Subclasses must override

getContents

and provide an array,
where each item in the array is a pair of objects.
The first element of each pair is the key, which must be a

String

, and the second element is the value associated with
that key.

The following

example

shows two members of a resource
bundle family with the base name "MyResources".
"MyResources" is the default member of the bundle family, and
"MyResources_fr" is the French member.
These members are based on

ListResourceBundle

(a related

example

shows
how you can add a bundle to this family that's based on a properties file).
The keys in this example are of the form "s1" etc. The actual
keys are entirely up to your choice, so long as they are the same as
the keys you use in your program to retrieve the objects from the bundle.
Keys are case-sensitive.

```java
public class MyResources extends ListResourceBundle {
protected Object[][] getContents() {
return new Object[][] {
// LOCALIZE THIS
{"s1", "The disk \"{1}\" contains {0}."}, // MessageFormat pattern
{"s2", "1"}, // location of {0} in pattern
{"s3", "My Disk"}, // sample disk name
{"s4", "no files"}, // first ChoiceFormat choice
{"s5", "one file"}, // second ChoiceFormat choice
{"s6", "{0,number} files"}, // third ChoiceFormat choice
{"s7", "3 Mar 96"}, // sample date
{"s8", new Dimension(1,5)} // real object, not just string
// END OF MATERIAL TO LOCALIZE
};
}
}

public class MyResources_fr extends ListResourceBundle {
protected Object[][] getContents() {
return new Object[][] {
// LOCALIZE THIS
{"s1", "Le disque \"{1}\" {0}."}, // MessageFormat pattern
{"s2", "1"}, // location of {0} in pattern
{"s3", "Mon disque"}, // sample disk name
{"s4", "ne contient pas de fichiers"}, // first ChoiceFormat choice
{"s5", "contient un fichier"}, // second ChoiceFormat choice
{"s6", "contient {0,number} fichiers"}, // third ChoiceFormat choice
{"s7", "3 mars 1996"}, // sample date
{"s8", new Dimension(1,3)} // real object, not just string
// END OF MATERIAL TO LOCALIZE
};
}
}
```

The implementation of a

ListResourceBundle

subclass must be thread-safe
if it's simultaneously used by multiple threads. The default implementations
of the methods in this class are thread-safe.

Subclasses must override

getContents

and provide an array,
where each item in the array is a pair of objects.
The first element of each pair is the key, which must be a

String

, and the second element is the value associated with
that key.

The following

example

shows two members of a resource
bundle family with the base name "MyResources".
"MyResources" is the default member of the bundle family, and
"MyResources_fr" is the French member.
These members are based on

ListResourceBundle

(a related

example

shows
how you can add a bundle to this family that's based on a properties file).
The keys in this example are of the form "s1" etc. The actual
keys are entirely up to your choice, so long as they are the same as
the keys you use in your program to retrieve the objects from the bundle.
Keys are case-sensitive.

```java
public class MyResources extends ListResourceBundle {
protected Object[][] getContents() {
return new Object[][] {
// LOCALIZE THIS
{"s1", "The disk \"{1}\" contains {0}."}, // MessageFormat pattern
{"s2", "1"}, // location of {0} in pattern
{"s3", "My Disk"}, // sample disk name
{"s4", "no files"}, // first ChoiceFormat choice
{"s5", "one file"}, // second ChoiceFormat choice
{"s6", "{0,number} files"}, // third ChoiceFormat choice
{"s7", "3 Mar 96"}, // sample date
{"s8", new Dimension(1,5)} // real object, not just string
// END OF MATERIAL TO LOCALIZE
};
}
}

public class MyResources_fr extends ListResourceBundle {
protected Object[][] getContents() {
return new Object[][] {
// LOCALIZE THIS
{"s1", "Le disque \"{1}\" {0}."}, // MessageFormat pattern
{"s2", "1"}, // location of {0} in pattern
{"s3", "Mon disque"}, // sample disk name
{"s4", "ne contient pas de fichiers"}, // first ChoiceFormat choice
{"s5", "contient un fichier"}, // second ChoiceFormat choice
{"s6", "contient {0,number} fichiers"}, // third ChoiceFormat choice
{"s7", "3 mars 1996"}, // sample date
{"s8", new Dimension(1,3)} // real object, not just string
// END OF MATERIAL TO LOCALIZE
};
}
}
```

The implementation of a

ListResourceBundle

subclass must be thread-safe
if it's simultaneously used by multiple threads. The default implementations
of the methods in this class are thread-safe.

The following

example

shows two members of a resource
bundle family with the base name "MyResources".
"MyResources" is the default member of the bundle family, and
"MyResources_fr" is the French member.
These members are based on

ListResourceBundle

(a related

example

shows
how you can add a bundle to this family that's based on a properties file).
The keys in this example are of the form "s1" etc. The actual
keys are entirely up to your choice, so long as they are the same as
the keys you use in your program to retrieve the objects from the bundle.
Keys are case-sensitive.

```java
public class MyResources extends ListResourceBundle {
protected Object[][] getContents() {
return new Object[][] {
// LOCALIZE THIS
{"s1", "The disk \"{1}\" contains {0}."}, // MessageFormat pattern
{"s2", "1"}, // location of {0} in pattern
{"s3", "My Disk"}, // sample disk name
{"s4", "no files"}, // first ChoiceFormat choice
{"s5", "one file"}, // second ChoiceFormat choice
{"s6", "{0,number} files"}, // third ChoiceFormat choice
{"s7", "3 Mar 96"}, // sample date
{"s8", new Dimension(1,5)} // real object, not just string
// END OF MATERIAL TO LOCALIZE
};
}
}

public class MyResources_fr extends ListResourceBundle {
protected Object[][] getContents() {
return new Object[][] {
// LOCALIZE THIS
{"s1", "Le disque \"{1}\" {0}."}, // MessageFormat pattern
{"s2", "1"}, // location of {0} in pattern
{"s3", "Mon disque"}, // sample disk name
{"s4", "ne contient pas de fichiers"}, // first ChoiceFormat choice
{"s5", "contient un fichier"}, // second ChoiceFormat choice
{"s6", "contient {0,number} fichiers"}, // third ChoiceFormat choice
{"s7", "3 mars 1996"}, // sample date
{"s8", new Dimension(1,3)} // real object, not just string
// END OF MATERIAL TO LOCALIZE
};
}
}
```

The implementation of a

ListResourceBundle

subclass must be thread-safe
if it's simultaneously used by multiple threads. The default implementations
of the methods in this class are thread-safe.

public class MyResources extends ListResourceBundle {
protected Object[][] getContents() {
return new Object[][] {
// LOCALIZE THIS
{"s1", "The disk \"{1}\" contains {0}."}, // MessageFormat pattern
{"s2", "1"}, // location of {0} in pattern
{"s3", "My Disk"}, // sample disk name
{"s4", "no files"}, // first ChoiceFormat choice
{"s5", "one file"}, // second ChoiceFormat choice
{"s6", "{0,number} files"}, // third ChoiceFormat choice
{"s7", "3 Mar 96"}, // sample date
{"s8", new Dimension(1,5)} // real object, not just string
// END OF MATERIAL TO LOCALIZE
};
}
}

public class MyResources_fr extends ListResourceBundle {
protected Object[][] getContents() {
return new Object[][] {
// LOCALIZE THIS
{"s1", "Le disque \"{1}\" {0}."}, // MessageFormat pattern
{"s2", "1"}, // location of {0} in pattern
{"s3", "Mon disque"}, // sample disk name
{"s4", "ne contient pas de fichiers"}, // first ChoiceFormat choice
{"s5", "contient un fichier"}, // second ChoiceFormat choice
{"s6", "contient {0,number} fichiers"}, // third ChoiceFormat choice
{"s7", "3 mars 1996"}, // sample date
{"s8", new Dimension(1,3)} // real object, not just string
// END OF MATERIAL TO LOCALIZE
};
}
}

The implementation of a

ListResourceBundle

subclass must be thread-safe
if it's simultaneously used by multiple threads. The default implementations
of the methods in this class are thread-safe.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class java.util.

ResourceBundle

ResourceBundle.Control

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.util.

ResourceBundle

parent

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ListResourceBundle

()

Sole constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected abstract

Object

[][]

getContents

()

Returns an array in which each item is a pair of objects in an

Object

array.

Enumeration

<

String

>

getKeys

()

Returns an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.

protected

Set

<

String

>

handleKeySet

()

Returns a

Set

of the keys contained

only

in this

ResourceBundle

.

- Methods declared in class java.util.

ResourceBundle

clearCache

,

clearCache

,

containsKey

,

getBaseBundleName

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getLocale

,

getObject

,

getString

,

getStringArray

,

handleGetObject

,

keySet

,

setParent

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

Nested Class Summary

- Nested classes/interfaces declared in class java.util.

ResourceBundle

ResourceBundle.Control

---

#### Nested Class Summary

Nested classes/interfaces declared in class java.util.

ResourceBundle

ResourceBundle.Control

---

#### Nested classes/interfaces declared in class java.util. ResourceBundle

Field Summary

- Fields declared in class java.util.

ResourceBundle

parent

---

#### Field Summary

Fields declared in class java.util.

ResourceBundle

parent

---

#### Fields declared in class java.util. ResourceBundle

Constructor Summary

Constructors

Constructor

Description

ListResourceBundle

()

Sole constructor.

---

#### Constructor Summary

Sole constructor.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected abstract

Object

[][]

getContents

()

Returns an array in which each item is a pair of objects in an

Object

array.

Enumeration

<

String

>

getKeys

()

Returns an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.

protected

Set

<

String

>

handleKeySet

()

Returns a

Set

of the keys contained

only

in this

ResourceBundle

.

- Methods declared in class java.util.

ResourceBundle

clearCache

,

clearCache

,

containsKey

,

getBaseBundleName

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getLocale

,

getObject

,

getString

,

getStringArray

,

handleGetObject

,

keySet

,

setParent

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

Returns an array in which each item is a pair of objects in an

Object

array.

Returns an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.

Returns a

Set

of the keys contained

only

in this

ResourceBundle

.

Methods declared in class java.util.

ResourceBundle

clearCache

,

clearCache

,

containsKey

,

getBaseBundleName

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getBundle

,

getLocale

,

getObject

,

getString

,

getStringArray

,

handleGetObject

,

keySet

,

setParent

---

#### Methods declared in class java.util. ResourceBundle

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

- ListResourceBundle

```java
public ListResourceBundle()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

============ METHOD DETAIL ==========

- Method Detail

- getKeys

```java
public
Enumeration
<
String
> getKeys()
```

Returns an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.

**Specified by:** getKeys

in class

ResourceBundle
**Returns:** an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.
**See Also:** ResourceBundle.keySet()

- handleKeySet

```java
protected
Set
<
String
> handleKeySet()
```

Returns a

Set

of the keys contained

only

in this

ResourceBundle

.

**Overrides:** handleKeySet

in class

ResourceBundle
**Returns:** a

Set

of the keys contained only in this

ResourceBundle
**Since:** 1.6
**See Also:** ResourceBundle.keySet()

- getContents

```java
protected abstract
Object
[][] getContents()
```

Returns an array in which each item is a pair of objects in an

Object

array. The first element of each pair is
the key, which must be a

String

, and the second
element is the value associated with that key. See the class
description for details.

**Returns:** an array of an

Object

array representing a
key-value pair.

Constructor Detail

- ListResourceBundle

```java
public ListResourceBundle()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### Constructor Detail

ListResourceBundle

```java
public ListResourceBundle()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### ListResourceBundle

public ListResourceBundle()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

Method Detail

- getKeys

```java
public
Enumeration
<
String
> getKeys()
```

Returns an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.

**Specified by:** getKeys

in class

ResourceBundle
**Returns:** an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.
**See Also:** ResourceBundle.keySet()

- handleKeySet

```java
protected
Set
<
String
> handleKeySet()
```

Returns a

Set

of the keys contained

only

in this

ResourceBundle

.

**Overrides:** handleKeySet

in class

ResourceBundle
**Returns:** a

Set

of the keys contained only in this

ResourceBundle
**Since:** 1.6
**See Also:** ResourceBundle.keySet()

- getContents

```java
protected abstract
Object
[][] getContents()
```

Returns an array in which each item is a pair of objects in an

Object

array. The first element of each pair is
the key, which must be a

String

, and the second
element is the value associated with that key. See the class
description for details.

**Returns:** an array of an

Object

array representing a
key-value pair.

---

#### Method Detail

getKeys

```java
public
Enumeration
<
String
> getKeys()
```

Returns an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.

**Specified by:** getKeys

in class

ResourceBundle
**Returns:** an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.
**See Also:** ResourceBundle.keySet()

---

#### getKeys

public

Enumeration

<

String

> getKeys()

Returns an

Enumeration

of the keys contained in
this

ResourceBundle

and its parent bundles.

handleKeySet

```java
protected
Set
<
String
> handleKeySet()
```

Returns a

Set

of the keys contained

only

in this

ResourceBundle

.

**Overrides:** handleKeySet

in class

ResourceBundle
**Returns:** a

Set

of the keys contained only in this

ResourceBundle
**Since:** 1.6
**See Also:** ResourceBundle.keySet()

---

#### handleKeySet

protected

Set

<

String

> handleKeySet()

Returns a

Set

of the keys contained

only

in this

ResourceBundle

.

getContents

```java
protected abstract
Object
[][] getContents()
```

Returns an array in which each item is a pair of objects in an

Object

array. The first element of each pair is
the key, which must be a

String

, and the second
element is the value associated with that key. See the class
description for details.

**Returns:** an array of an

Object

array representing a
key-value pair.

---

#### getContents

protected abstract

Object

[][] getContents()

Returns an array in which each item is a pair of objects in an

Object

array. The first element of each pair is
the key, which must be a

String

, and the second
element is the value associated with that key. See the class
description for details.

---

