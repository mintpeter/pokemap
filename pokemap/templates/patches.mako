<table>
    <thead>
        <tr>
            <th>Generation ID</th>
            <th>Route ID</th>
            <th>Type ID</th>
        </tr>
    </thead>
    <tbody>
%for patch in patches:
        <tr>
            <td>${patch.genid}</td>
            <td>${patch.routeid}</td>
            <td>${patch.typeid}</td>
        </tr>
%endfor
    </tbody>
</table>
