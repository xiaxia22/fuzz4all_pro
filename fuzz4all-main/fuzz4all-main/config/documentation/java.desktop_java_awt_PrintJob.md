# Class PrintJob

**Source:** `java.desktop\java\awt\PrintJob.html`

### Class Description

```java
public abstract class
PrintJob

extends
Object
```

An abstract class which initiates and executes a print job.
It provides access to a print graphics object which renders
to an appropriate print device.

**See Also:** Toolkit.getPrintJob(java.awt.Frame, java.lang.String, java.util.Properties)

---

### Field Details

*No entries found.*

### Constructor Details

#### public PrintJob()

*No description found.*

---

### Method Details

#### public abstract
Graphics
getGraphics()

Gets a Graphics object that will draw to the next page.
The page is sent to the printer when the graphics
object is disposed. This graphics object will also implement
the PrintGraphics interface.

**Returns:**
- the graphics context for printing the next page

**See Also:**
- PrintGraphics

---

#### public abstract
Dimension
getPageDimension()

Returns the dimensions of the page in pixels.
The resolution of the page is chosen so that it
is similar to the screen resolution.

**Returns:**
- the page dimension

---

#### public abstract int getPageResolution()

Returns the resolution of the page in pixels per inch.
Note that this doesn't have to correspond to the physical
resolution of the printer.

**Returns:**
- the page resolution

---

#### public abstract boolean lastPageFirst()

Returns true if the last page will be printed first.

**Returns:**
- true

if the last page will be printed first;
otherwise

false

---

#### public abstract void end()

Ends the print job and does any necessary cleanup.

---

#### @Deprecated
(
since
="9")
public void finalize()

Ends this print job once it is no longer referenced.

**Overrides:**
- finalize

in class

Object

**See Also:**
- end()

---

### Additional Sections

#### Class PrintJob

java.lang.Object

- java.awt.PrintJob

java.awt.PrintJob

```java
public abstract class
PrintJob

extends
Object
```

An abstract class which initiates and executes a print job.
It provides access to a print graphics object which renders
to an appropriate print device.

**See Also:** Toolkit.getPrintJob(java.awt.Frame, java.lang.String, java.util.Properties)

public abstract class

PrintJob

extends

Object

An abstract class which initiates and executes a print job.
It provides access to a print graphics object which renders
to an appropriate print device.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PrintJob

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

abstract void

end

()

Ends the print job and does any necessary cleanup.

void

finalize

()

Deprecated.

The

finalize

method has been deprecated.

abstract

Graphics

getGraphics

()

Gets a Graphics object that will draw to the next page.

abstract

Dimension

getPageDimension

()

Returns the dimensions of the page in pixels.

abstract int

getPageResolution

()

Returns the resolution of the page in pixels per inch.

abstract boolean

lastPageFirst

()

Returns true if the last page will be printed first.

- Methods declared in class java.lang.

Object

clone

,

equals

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

Constructor Summary

Constructors

Constructor

Description

PrintJob

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

abstract void

end

()

Ends the print job and does any necessary cleanup.

void

finalize

()

Deprecated.

The

finalize

method has been deprecated.

abstract

Graphics

getGraphics

()

Gets a Graphics object that will draw to the next page.

abstract

Dimension

getPageDimension

()

Returns the dimensions of the page in pixels.

abstract int

getPageResolution

()

Returns the resolution of the page in pixels per inch.

abstract boolean

lastPageFirst

()

Returns true if the last page will be printed first.

- Methods declared in class java.lang.

Object

clone

,

equals

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

Ends the print job and does any necessary cleanup.

Deprecated.

The

finalize

method has been deprecated.

Gets a Graphics object that will draw to the next page.

Returns the dimensions of the page in pixels.

Returns the resolution of the page in pixels per inch.

Returns true if the last page will be printed first.

Methods declared in class java.lang.

Object

clone

,

equals

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

- PrintJob

```java
public PrintJob()
```

============ METHOD DETAIL ==========

- Method Detail

- getGraphics

```java
public abstract
Graphics
getGraphics()
```

Gets a Graphics object that will draw to the next page.
The page is sent to the printer when the graphics
object is disposed. This graphics object will also implement
the PrintGraphics interface.

**Returns:** the graphics context for printing the next page
**See Also:** PrintGraphics

- getPageDimension

```java
public abstract
Dimension
getPageDimension()
```

Returns the dimensions of the page in pixels.
The resolution of the page is chosen so that it
is similar to the screen resolution.

**Returns:** the page dimension

- getPageResolution

```java
public abstract int getPageResolution()
```

Returns the resolution of the page in pixels per inch.
Note that this doesn't have to correspond to the physical
resolution of the printer.

**Returns:** the page resolution

- lastPageFirst

```java
public abstract boolean lastPageFirst()
```

Returns true if the last page will be printed first.

**Returns:** true

if the last page will be printed first;
otherwise

false

- end

```java
public abstract void end()
```

Ends the print job and does any necessary cleanup.

- finalize

```java
@Deprecated
(
since
="9")
public void finalize()
```

Deprecated.

The

finalize

method has been deprecated.
Subclasses that override

finalize

in order to perform cleanup
should be modified to use alternative cleanup mechanisms and
to remove the overriding

finalize

method.
When overriding the

finalize

method, its implementation must explicitly
ensure that

super.finalize()

is invoked as described in

Object.finalize()

.
See the specification for

Object.finalize()

for further
information about migration options.

Ends this print job once it is no longer referenced.

**Overrides:** finalize

in class

Object
**See Also:** end()

Constructor Detail

- PrintJob

```java
public PrintJob()
```

---

#### Constructor Detail

PrintJob

```java
public PrintJob()
```

---

#### PrintJob

public PrintJob()

Method Detail

- getGraphics

```java
public abstract
Graphics
getGraphics()
```

Gets a Graphics object that will draw to the next page.
The page is sent to the printer when the graphics
object is disposed. This graphics object will also implement
the PrintGraphics interface.

**Returns:** the graphics context for printing the next page
**See Also:** PrintGraphics

- getPageDimension

```java
public abstract
Dimension
getPageDimension()
```

Returns the dimensions of the page in pixels.
The resolution of the page is chosen so that it
is similar to the screen resolution.

**Returns:** the page dimension

- getPageResolution

```java
public abstract int getPageResolution()
```

Returns the resolution of the page in pixels per inch.
Note that this doesn't have to correspond to the physical
resolution of the printer.

**Returns:** the page resolution

- lastPageFirst

```java
public abstract boolean lastPageFirst()
```

Returns true if the last page will be printed first.

**Returns:** true

if the last page will be printed first;
otherwise

false

- end

```java
public abstract void end()
```

Ends the print job and does any necessary cleanup.

- finalize

```java
@Deprecated
(
since
="9")
public void finalize()
```

Deprecated.

The

finalize

method has been deprecated.
Subclasses that override

finalize

in order to perform cleanup
should be modified to use alternative cleanup mechanisms and
to remove the overriding

finalize

method.
When overriding the

finalize

method, its implementation must explicitly
ensure that

super.finalize()

is invoked as described in

Object.finalize()

.
See the specification for

Object.finalize()

for further
information about migration options.

Ends this print job once it is no longer referenced.

**Overrides:** finalize

in class

Object
**See Also:** end()

---

#### Method Detail

getGraphics

```java
public abstract
Graphics
getGraphics()
```

Gets a Graphics object that will draw to the next page.
The page is sent to the printer when the graphics
object is disposed. This graphics object will also implement
the PrintGraphics interface.

**Returns:** the graphics context for printing the next page
**See Also:** PrintGraphics

---

#### getGraphics

public abstract

Graphics

getGraphics()

Gets a Graphics object that will draw to the next page.
The page is sent to the printer when the graphics
object is disposed. This graphics object will also implement
the PrintGraphics interface.

getPageDimension

```java
public abstract
Dimension
getPageDimension()
```

Returns the dimensions of the page in pixels.
The resolution of the page is chosen so that it
is similar to the screen resolution.

**Returns:** the page dimension

---

#### getPageDimension

public abstract

Dimension

getPageDimension()

Returns the dimensions of the page in pixels.
The resolution of the page is chosen so that it
is similar to the screen resolution.

getPageResolution

```java
public abstract int getPageResolution()
```

Returns the resolution of the page in pixels per inch.
Note that this doesn't have to correspond to the physical
resolution of the printer.

**Returns:** the page resolution

---

#### getPageResolution

public abstract int getPageResolution()

Returns the resolution of the page in pixels per inch.
Note that this doesn't have to correspond to the physical
resolution of the printer.

lastPageFirst

```java
public abstract boolean lastPageFirst()
```

Returns true if the last page will be printed first.

**Returns:** true

if the last page will be printed first;
otherwise

false

---

#### lastPageFirst

public abstract boolean lastPageFirst()

Returns true if the last page will be printed first.

end

```java
public abstract void end()
```

Ends the print job and does any necessary cleanup.

---

#### end

public abstract void end()

Ends the print job and does any necessary cleanup.

finalize

```java
@Deprecated
(
since
="9")
public void finalize()
```

Deprecated.

The

finalize

method has been deprecated.
Subclasses that override

finalize

in order to perform cleanup
should be modified to use alternative cleanup mechanisms and
to remove the overriding

finalize

method.
When overriding the

finalize

method, its implementation must explicitly
ensure that

super.finalize()

is invoked as described in

Object.finalize()

.
See the specification for

Object.finalize()

for further
information about migration options.

Ends this print job once it is no longer referenced.

**Overrides:** finalize

in class

Object
**See Also:** end()

---

#### finalize

@Deprecated

(

since

="9")
public void finalize()

Ends this print job once it is no longer referenced.

---

