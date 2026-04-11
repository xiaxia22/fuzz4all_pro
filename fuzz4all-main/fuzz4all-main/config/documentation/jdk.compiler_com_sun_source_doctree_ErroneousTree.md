# Interface ErroneousTree

**Source:** `jdk.compiler\com\sun\source\doctree\ErroneousTree.html`

### Class Description

```java
public interface
ErroneousTree

extends
TextTree
```

A tree node to stand in for a malformed text

**All Superinterfaces:** DocTree

,

TextTree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Diagnostic
<
JavaFileObject
> getDiagnostic()

Returns a diagnostic object giving details about
the reason the body text is in error.

**Returns:**
- a diagnostic

---

### Additional Sections

#### Interface ErroneousTree

**All Superinterfaces:** DocTree

,

TextTree

```java
public interface
ErroneousTree

extends
TextTree
```

A tree node to stand in for a malformed text

**Since:** 1.8

public interface

ErroneousTree

extends

TextTree

A tree node to stand in for a malformed text

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface com.sun.source.doctree.

DocTree

DocTree.Kind

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Diagnostic

<

JavaFileObject

>

getDiagnostic

()

Returns a diagnostic object giving details about
the reason the body text is in error.

- Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

- Methods declared in interface com.sun.source.doctree.

TextTree

getBody

Nested Class Summary

- Nested classes/interfaces declared in interface com.sun.source.doctree.

DocTree

DocTree.Kind

---

#### Nested Class Summary

Nested classes/interfaces declared in interface com.sun.source.doctree.

DocTree

DocTree.Kind

---

#### Nested classes/interfaces declared in interface com.sun.source.doctree. DocTree

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Diagnostic

<

JavaFileObject

>

getDiagnostic

()

Returns a diagnostic object giving details about
the reason the body text is in error.

- Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

- Methods declared in interface com.sun.source.doctree.

TextTree

getBody

---

#### Method Summary

Returns a diagnostic object giving details about
the reason the body text is in error.

Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.doctree. DocTree

Methods declared in interface com.sun.source.doctree.

TextTree

getBody

---

#### Methods declared in interface com.sun.source.doctree. TextTree

============ METHOD DETAIL ==========

- Method Detail

- getDiagnostic

```java
Diagnostic
<
JavaFileObject
> getDiagnostic()
```

Returns a diagnostic object giving details about
the reason the body text is in error.

**Returns:** a diagnostic

Method Detail

- getDiagnostic

```java
Diagnostic
<
JavaFileObject
> getDiagnostic()
```

Returns a diagnostic object giving details about
the reason the body text is in error.

**Returns:** a diagnostic

---

#### Method Detail

getDiagnostic

```java
Diagnostic
<
JavaFileObject
> getDiagnostic()
```

Returns a diagnostic object giving details about
the reason the body text is in error.

**Returns:** a diagnostic

---

#### getDiagnostic

Diagnostic

<

JavaFileObject

> getDiagnostic()

Returns a diagnostic object giving details about
the reason the body text is in error.

---

