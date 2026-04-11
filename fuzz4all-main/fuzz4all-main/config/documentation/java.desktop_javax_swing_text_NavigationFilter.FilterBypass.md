# Class NavigationFilter.FilterBypass

**Source:** `java.desktop\javax\swing\text\NavigationFilter.FilterBypass.html`

### Class Description

```java
public abstract static class
NavigationFilter.FilterBypass

extends
Object
```

Used as a way to circumvent calling back into the caret to
position the cursor. Caret implementations that wish to support
a NavigationFilter must provide an implementation that will
not callback into the NavigationFilter.

**Enclosing class:** NavigationFilter

---

### Field Details

*No entries found.*

### Constructor Details

#### public FilterBypass()

*No description found.*

---

### Method Details

#### public abstract
Caret
getCaret()

Returns the Caret that is changing.

**Returns:**
- Caret that is changing

---

#### public abstract void setDot​(int dot,

Position.Bias
bias)

Sets the caret location, bypassing the NavigationFilter.

**Parameters:**
- dot

- the position >= 0
- bias

- Bias to place the dot at

---

#### public abstract void moveDot​(int dot,

Position.Bias
bias)

Moves the caret location, bypassing the NavigationFilter.

**Parameters:**
- dot

- the position >= 0
- bias

- Bias for new location

---

### Additional Sections

#### Class NavigationFilter.FilterBypass

java.lang.Object

- javax.swing.text.NavigationFilter.FilterBypass

javax.swing.text.NavigationFilter.FilterBypass

**Enclosing class:** NavigationFilter

```java
public abstract static class
NavigationFilter.FilterBypass

extends
Object
```

Used as a way to circumvent calling back into the caret to
position the cursor. Caret implementations that wish to support
a NavigationFilter must provide an implementation that will
not callback into the NavigationFilter.

**Since:** 1.4

public abstract static class

NavigationFilter.FilterBypass

extends

Object

Used as a way to circumvent calling back into the caret to
position the cursor. Caret implementations that wish to support
a NavigationFilter must provide an implementation that will
not callback into the NavigationFilter.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FilterBypass

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Caret

getCaret

()

Returns the Caret that is changing.

abstract void

moveDot

​(int dot,

Position.Bias

bias)

Moves the caret location, bypassing the NavigationFilter.

abstract void

setDot

​(int dot,

Position.Bias

bias)

Sets the caret location, bypassing the NavigationFilter.

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

Constructor Summary

Constructors

Constructor

Description

FilterBypass

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Caret

getCaret

()

Returns the Caret that is changing.

abstract void

moveDot

​(int dot,

Position.Bias

bias)

Moves the caret location, bypassing the NavigationFilter.

abstract void

setDot

​(int dot,

Position.Bias

bias)

Sets the caret location, bypassing the NavigationFilter.

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

Returns the Caret that is changing.

Moves the caret location, bypassing the NavigationFilter.

Sets the caret location, bypassing the NavigationFilter.

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

- FilterBypass

```java
public FilterBypass()
```

============ METHOD DETAIL ==========

- Method Detail

- getCaret

```java
public abstract
Caret
getCaret()
```

Returns the Caret that is changing.

**Returns:** Caret that is changing

- setDot

```java
public abstract void setDot​(int dot,

Position.Bias
bias)
```

Sets the caret location, bypassing the NavigationFilter.

**Parameters:** dot

- the position >= 0
**Parameters:** bias

- Bias to place the dot at

- moveDot

```java
public abstract void moveDot​(int dot,

Position.Bias
bias)
```

Moves the caret location, bypassing the NavigationFilter.

**Parameters:** dot

- the position >= 0
**Parameters:** bias

- Bias for new location

Constructor Detail

- FilterBypass

```java
public FilterBypass()
```

---

#### Constructor Detail

FilterBypass

```java
public FilterBypass()
```

---

#### FilterBypass

public FilterBypass()

Method Detail

- getCaret

```java
public abstract
Caret
getCaret()
```

Returns the Caret that is changing.

**Returns:** Caret that is changing

- setDot

```java
public abstract void setDot​(int dot,

Position.Bias
bias)
```

Sets the caret location, bypassing the NavigationFilter.

**Parameters:** dot

- the position >= 0
**Parameters:** bias

- Bias to place the dot at

- moveDot

```java
public abstract void moveDot​(int dot,

Position.Bias
bias)
```

Moves the caret location, bypassing the NavigationFilter.

**Parameters:** dot

- the position >= 0
**Parameters:** bias

- Bias for new location

---

#### Method Detail

getCaret

```java
public abstract
Caret
getCaret()
```

Returns the Caret that is changing.

**Returns:** Caret that is changing

---

#### getCaret

public abstract

Caret

getCaret()

Returns the Caret that is changing.

setDot

```java
public abstract void setDot​(int dot,

Position.Bias
bias)
```

Sets the caret location, bypassing the NavigationFilter.

**Parameters:** dot

- the position >= 0
**Parameters:** bias

- Bias to place the dot at

---

#### setDot

public abstract void setDot​(int dot,

Position.Bias

bias)

Sets the caret location, bypassing the NavigationFilter.

moveDot

```java
public abstract void moveDot​(int dot,

Position.Bias
bias)
```

Moves the caret location, bypassing the NavigationFilter.

**Parameters:** dot

- the position >= 0
**Parameters:** bias

- Bias for new location

---

#### moveDot

public abstract void moveDot​(int dot,

Position.Bias

bias)

Moves the caret location, bypassing the NavigationFilter.

---

