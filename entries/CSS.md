**Cascading Style Sheets (CSS)** is a stylesheet language used to describe the presentation of a document written in HTML or XML. CSS describes how elements should be rendered on screen, on paper, in speech, or on other media.



## History



CSS was first proposed by **H�kon Wium Lie** on October 10, 1994. At the time, Lie was working with Tim Berners-Lee at CERN. The proposal was made to provide a standard way to style web documents, separating content from presentation.



The first CSS specification, CSS1, became a W3C Recommendation in December 1996. This was followed by CSS2 in 1998, and CSS3, which is divided into modules, began development in 1999.



## Syntax



CSS rules consist of a selector and a declaration block:



```css

selector {

    property: value;

    another-property: another-value;

}

```



### Selectors



CSS selectors are used to target HTML elements:



- **Element Selector**: `p { color: blue; }`

- **Class Selector**: `.my-class { font-size: 16px; }`

- **ID Selector**: `#my-id { background: yellow; }`

- **Attribute Selector**: `input[type="text"] { border: 1px solid; }`



## Box Model



The CSS box model describes the rectangular boxes generated for elements. Each box consists of:



1. **Content** - The actual content of the element

2. **Padding** - Space between content and border

3. **Border** - A border surrounding the padding

4. **Margin** - Space outside the border



## Flexbox



Flexbox is a one-dimensional layout method for arranging items in rows or columns. It makes it easier to design flexible responsive layout structures.



```css

.container {

    display: flex;

    justify-content: space-between;

    align-items: center;

}

```



## Grid Layout



CSS Grid Layout is a two-dimensional layout system for the web. It lets you layout content in rows and columns, and provides many features to make building complex layouts straightforward.



```css

.grid-container {

    display: grid;

    grid-template-columns: repeat(3, 1fr);

    gap: 20px;

}

```



## Responsive Design



CSS enables responsive web design through media queries, which apply different styles based on device characteristics:



```css

@media (max-width: 768px) {

    .sidebar {

        display: none;

    }

}

```



## Modern Features



Modern CSS includes powerful features like:



- **CSS Variables (Custom Properties)** for reusable values

- **CSS Animations** for creating smooth transitions

- **CSS Transforms** for rotating, scaling, and skewing elements

- **CSS Filters** for visual effects like blur and brightness



CSS continues to evolve with new features being added regularly to make web styling more powerful and efficient.



see more about CSS here: https://www.w3schools.com/css/