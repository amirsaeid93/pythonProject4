  const listItems = [
    'First item',
    'Second item',
    'Third item'
  ];

  const ul = document.createElement('ul');

  listItems.forEach((item, index) => {
    const li = document.createElement('li');
    li.textContent = item;
    if (index === 1) {
      li.classList.add('my-item');
    }
    ul.appendChild(li);
  });

  const targetElement = document.getElementById('target');

  targetElement.appendChild(ul);