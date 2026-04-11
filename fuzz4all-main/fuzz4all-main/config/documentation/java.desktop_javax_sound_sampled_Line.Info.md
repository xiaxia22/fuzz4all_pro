# Class Line.Info

**Source:** `java.desktop\javax\sound\sampled\Line.Info.html`

### Class Description

```java
public static class
Line.Info

extends
Object
```

A

Line.Info

object contains information about a line. The only
information provided by

Line.Info

itself is the Java class of the
line. A subclass of

Line.Info

adds other kinds of information
about the line. This additional information depends on which

Line

subinterface is implemented by the kind of line that the

Line.Info

subclass describes.

A

Line.Info

can be retrieved using various methods of the

Line

,

Mixer

, and

AudioSystem

interfaces. Other
such methods let you pass a

Line.Info

as an argument, to learn
whether lines matching the specified configuration are available and to
obtain them.

**Direct Known Subclasses:** DataLine.Info

,

Port.Info

---

### Field Details

*No entries found.*

### Constructor Details

#### public Info​(
Class
<?> lineClass)

Constructs an info object that describes a line of the specified
class. This constructor is typically used by an application to
describe a desired line.

**Parameters:**
- lineClass

- the class of the line that the new

Line.Info

object describes

---

### Method Details

#### public
Class
<?> getLineClass()

Obtains the class of the line that this

Line.Info

object
describes.

**Returns:**
- the described line's class

---

#### public boolean matches​(
Line.Info
info)

Indicates whether the specified info object matches this one. To
match, the specified object must be identical to or a special case of
this one. The specified info object must be either an instance of the
same class as this one, or an instance of a sub-type of this one. In
addition, the attributes of the specified object must be compatible
with the capabilities of this one. Specifically, the routing
configuration for the specified info object must be compatible with
that of this one. Subclasses may add other criteria to determine
whether the two objects match.

**Parameters:**
- info

- the info object which is being compared to this one

**Returns:**
- true

if the specified object matches this one,

false

otherwise

---

#### public
String
toString()

Obtains a textual description of the line info.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string description

---

### Additional Sections

#### Class Line.Info

java.lang.Object

- javax.sound.sampled.Line.Info

javax.sound.sampled.Line.Info

**Direct Known Subclasses:** DataLine.Info

,

Port.Info

**Enclosing interface:** Line

```java
public static class
Line.Info

extends
Object
```

A

Line.Info

object contains information about a line. The only
information provided by

Line.Info

itself is the Java class of the
line. A subclass of

Line.Info

adds other kinds of information
about the line. This additional information depends on which

Line

subinterface is implemented by the kind of line that the

Line.Info

subclass describes.

A

Line.Info

can be retrieved using various methods of the

Line

,

Mixer

, and

AudioSystem

interfaces. Other
such methods let you pass a

Line.Info

as an argument, to learn
whether lines matching the specified configuration are available and to
obtain them.

**Since:** 1.3
**See Also:** Line.getLineInfo()

,

Mixer.getSourceLineInfo()

,

Mixer.getTargetLineInfo()

,

Mixer.getLine(Line.Info)

,

Mixer.getSourceLineInfo(Line.Info)

,

Mixer.getTargetLineInfo(Line.Info)

,

Mixer.isLineSupported(Line.Info)

,

AudioSystem.getLine(Line.Info)

,

AudioSystem.getSourceLineInfo(Line.Info)

,

AudioSystem.getTargetLineInfo(Line.Info)

,

AudioSystem.isLineSupported(Line.Info)

public static class

Line.Info

extends

Object

A

Line.Info

object contains information about a line. The only
information provided by

Line.Info

itself is the Java class of the
line. A subclass of

Line.Info

adds other kinds of information
about the line. This additional information depends on which

Line

subinterface is implemented by the kind of line that the

Line.Info

subclass describes.

A

Line.Info

can be retrieved using various methods of the

Line

,

Mixer

, and

AudioSystem

interfaces. Other
such methods let you pass a

Line.Info

as an argument, to learn
whether lines matching the specified configuration are available and to
obtain them.

A

Line.Info

can be retrieved using various methods of the

Line

,

Mixer

, and

AudioSystem

interfaces. Other
such methods let you pass a

Line.Info

as an argument, to learn
whether lines matching the specified configuration are available and to
obtain them.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Info

​(

Class

<?> lineClass)

Constructs an info object that describes a line of the specified
class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<?>

getLineClass

()

Obtains the class of the line that this

Line.Info

object
describes.

boolean

matches

​(

Line.Info

info)

Indicates whether the specified info object matches this one.

String

toString

()

Obtains a textual description of the line info.

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

Constructor Summary

Constructors

Constructor

Description

Info

​(

Class

<?> lineClass)

Constructs an info object that describes a line of the specified
class.

---

#### Constructor Summary

Constructs an info object that describes a line of the specified
class.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<?>

getLineClass

()

Obtains the class of the line that this

Line.Info

object
describes.

boolean

matches

​(

Line.Info

info)

Indicates whether the specified info object matches this one.

String

toString

()

Obtains a textual description of the line info.

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

Obtains the class of the line that this

Line.Info

object
describes.

Indicates whether the specified info object matches this one.

Obtains a textual description of the line info.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Info

```java
public Info​(
Class
<?> lineClass)
```

Constructs an info object that describes a line of the specified
class. This constructor is typically used by an application to
describe a desired line.

**Parameters:** lineClass

- the class of the line that the new

Line.Info

object describes

============ METHOD DETAIL ==========

- Method Detail

- getLineClass

```java
public
Class
<?> getLineClass()
```

Obtains the class of the line that this

Line.Info

object
describes.

**Returns:** the described line's class

- matches

```java
public boolean matches​(
Line.Info
info)
```

Indicates whether the specified info object matches this one. To
match, the specified object must be identical to or a special case of
this one. The specified info object must be either an instance of the
same class as this one, or an instance of a sub-type of this one. In
addition, the attributes of the specified object must be compatible
with the capabilities of this one. Specifically, the routing
configuration for the specified info object must be compatible with
that of this one. Subclasses may add other criteria to determine
whether the two objects match.

**Parameters:** info

- the info object which is being compared to this one
**Returns:** true

if the specified object matches this one,

false

otherwise

- toString

```java
public
String
toString()
```

Obtains a textual description of the line info.

**Overrides:** toString

in class

Object
**Returns:** a string description

Constructor Detail

- Info

```java
public Info​(
Class
<?> lineClass)
```

Constructs an info object that describes a line of the specified
class. This constructor is typically used by an application to
describe a desired line.

**Parameters:** lineClass

- the class of the line that the new

Line.Info

object describes

---

#### Constructor Detail

Info

```java
public Info​(
Class
<?> lineClass)
```

Constructs an info object that describes a line of the specified
class. This constructor is typically used by an application to
describe a desired line.

**Parameters:** lineClass

- the class of the line that the new

Line.Info

object describes

---

#### Info

public Info​(

Class

<?> lineClass)

Constructs an info object that describes a line of the specified
class. This constructor is typically used by an application to
describe a desired line.

Method Detail

- getLineClass

```java
public
Class
<?> getLineClass()
```

Obtains the class of the line that this

Line.Info

object
describes.

**Returns:** the described line's class

- matches

```java
public boolean matches​(
Line.Info
info)
```

Indicates whether the specified info object matches this one. To
match, the specified object must be identical to or a special case of
this one. The specified info object must be either an instance of the
same class as this one, or an instance of a sub-type of this one. In
addition, the attributes of the specified object must be compatible
with the capabilities of this one. Specifically, the routing
configuration for the specified info object must be compatible with
that of this one. Subclasses may add other criteria to determine
whether the two objects match.

**Parameters:** info

- the info object which is being compared to this one
**Returns:** true

if the specified object matches this one,

false

otherwise

- toString

```java
public
String
toString()
```

Obtains a textual description of the line info.

**Overrides:** toString

in class

Object
**Returns:** a string description

---

#### Method Detail

getLineClass

```java
public
Class
<?> getLineClass()
```

Obtains the class of the line that this

Line.Info

object
describes.

**Returns:** the described line's class

---

#### getLineClass

public

Class

<?> getLineClass()

Obtains the class of the line that this

Line.Info

object
describes.

matches

```java
public boolean matches​(
Line.Info
info)
```

Indicates whether the specified info object matches this one. To
match, the specified object must be identical to or a special case of
this one. The specified info object must be either an instance of the
same class as this one, or an instance of a sub-type of this one. In
addition, the attributes of the specified object must be compatible
with the capabilities of this one. Specifically, the routing
configuration for the specified info object must be compatible with
that of this one. Subclasses may add other criteria to determine
whether the two objects match.

**Parameters:** info

- the info object which is being compared to this one
**Returns:** true

if the specified object matches this one,

false

otherwise

---

#### matches

public boolean matches​(

Line.Info

info)

Indicates whether the specified info object matches this one. To
match, the specified object must be identical to or a special case of
this one. The specified info object must be either an instance of the
same class as this one, or an instance of a sub-type of this one. In
addition, the attributes of the specified object must be compatible
with the capabilities of this one. Specifically, the routing
configuration for the specified info object must be compatible with
that of this one. Subclasses may add other criteria to determine
whether the two objects match.

toString

```java
public
String
toString()
```

Obtains a textual description of the line info.

**Overrides:** toString

in class

Object
**Returns:** a string description

---

#### toString

public

String

toString()

Obtains a textual description of the line info.

---

