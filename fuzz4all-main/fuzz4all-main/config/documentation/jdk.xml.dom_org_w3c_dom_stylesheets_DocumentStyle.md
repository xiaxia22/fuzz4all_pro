# Interface DocumentStyle

**Source:** `jdk.xml.dom\org\w3c\dom\stylesheets\DocumentStyle.html`

### Class Description

```java
public interface
DocumentStyle
```

The

DocumentStyle

interface provides a mechanism by which the
style sheets embedded in a document can be retrieved. The expectation is
that an instance of the

DocumentStyle

interface can be
obtained by using binding-specific casting methods on an instance of the

Document

interface.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**All Known Subinterfaces:** DocumentCSS

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### StyleSheetList
getStyleSheets()

A list containing all the style sheets explicitly linked into or
embedded in a document. For HTML documents, this includes external
style sheets, included via the HTML LINK element, and inline STYLE
elements. In XML, this includes external style sheets, included via
style sheet processing instructions (see [XML StyleSheet]).

---

### Additional Sections

#### Interface DocumentStyle

**All Known Subinterfaces:** DocumentCSS

```java
public interface
DocumentStyle
```

The

DocumentStyle

interface provides a mechanism by which the
style sheets embedded in a document can be retrieved. The expectation is
that an instance of the

DocumentStyle

interface can be
obtained by using binding-specific casting methods on an instance of the

Document

interface.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

public interface

DocumentStyle

The

DocumentStyle

interface provides a mechanism by which the
style sheets embedded in a document can be retrieved. The expectation is
that an instance of the

DocumentStyle

interface can be
obtained by using binding-specific casting methods on an instance of the

Document

interface.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

StyleSheetList

getStyleSheets

()

A list containing all the style sheets explicitly linked into or
embedded in a document.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

StyleSheetList

getStyleSheets

()

A list containing all the style sheets explicitly linked into or
embedded in a document.

---

#### Method Summary

A list containing all the style sheets explicitly linked into or
embedded in a document.

============ METHOD DETAIL ==========

- Method Detail

- getStyleSheets

```java
StyleSheetList
getStyleSheets()
```

A list containing all the style sheets explicitly linked into or
embedded in a document. For HTML documents, this includes external
style sheets, included via the HTML LINK element, and inline STYLE
elements. In XML, this includes external style sheets, included via
style sheet processing instructions (see [XML StyleSheet]).

Method Detail

- getStyleSheets

```java
StyleSheetList
getStyleSheets()
```

A list containing all the style sheets explicitly linked into or
embedded in a document. For HTML documents, this includes external
style sheets, included via the HTML LINK element, and inline STYLE
elements. In XML, this includes external style sheets, included via
style sheet processing instructions (see [XML StyleSheet]).

---

#### Method Detail

getStyleSheets

```java
StyleSheetList
getStyleSheets()
```

A list containing all the style sheets explicitly linked into or
embedded in a document. For HTML documents, this includes external
style sheets, included via the HTML LINK element, and inline STYLE
elements. In XML, this includes external style sheets, included via
style sheet processing instructions (see [XML StyleSheet]).

---

#### getStyleSheets

StyleSheetList

getStyleSheets()

A list containing all the style sheets explicitly linked into or
embedded in a document. For HTML documents, this includes external
style sheets, included via the HTML LINK element, and inline STYLE
elements. In XML, this includes external style sheets, included via
style sheet processing instructions (see [XML StyleSheet]).

---

