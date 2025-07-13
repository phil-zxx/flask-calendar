from frontend import app
from utils.CellTable import Cell, Table
from utils.Date import Date
from flask import render_template, request


@app.route('/')
def route_calendar():
    print("Calendar route accessed")
    year = request.args.get('year', Date.Today().year, type=int)
    view_type = int(request.args.get('type', '1'))

    first_weekday = Date(year, 1, 1).weekday()
    if view_type == 1:
        lengths = [max([((Date(year, month, 1).weekday() - first_weekday) % 7) + 1 + Date.get_days_in_month(year, month) for month in range(1, 13)]) for first_weekday in range(7)]
    elif view_type == 2:
        lengths = [31]  # Day layout aligned from 1st day of the month
    elif view_type == 3:
        lengths = [31]  # Day layout aligned from last day of the month
    else:
        raise ValueError(f"Invalid view type ({view_type})")

    days_in_row  = lengths[min(range(len(lengths)), key=lambda i: lengths[i])]

    headers = [Cell(str(year), "th", "border-end text-center")]
    for idx in range(days_in_row):
        if view_type == 1:
            weekday    = (first_weekday + idx) % 7
            day_name   = Date.get_weekday_name(weekday)
            class_name = "text-secondary bg-secondary-subtle" if day_name in ["Sat", "Sun"] else ""
            headers.append(Cell(day_name, "th", f"text-center {class_name}"))
        elif view_type == 2:
            headers.append(Cell(idx + 1, "th", "text-center px-2"))
        elif view_type == 3:
            headers.append(Cell(idx + 1, "th", "text-center px-2"))
        else:
            raise ValueError(f"Invalid view type ({view_type})")

    today = Date.Today()
    rows = []
    for month in range(1, 13):
        row           = [Cell(f"{Date.get_month_name(month)} / {month} / {Date.get_future_month_name(month)}", "th", "border-end" + (" bg-primary-subtle text-primary" if month % 3 == 0 else ""), "padding-left: 0.6em!important;padding-right: 0.6em!important;")]
        days_in_month = Date.get_days_in_month(year, month)
        weekday       = Date(year, month, 1).weekday()
        if view_type == 1:
            offset = (weekday - first_weekday) % 7
        elif view_type == 2:
            offset = 0
        elif view_type == 3:
            offset = days_in_row - days_in_month
        else:
            raise ValueError(f"Invalid view type ({view_type})")

        for _ in range(offset):
            row.append(Cell("", "td", ""))

        for day in range(1, days_in_month + 1):
            d = Date(year, month, day)
            is_today = d == today
            is_imm   = d.is_IMM()
            class_name = ""
            if is_today:
                class_name += "border border-danger border-2 "
            if is_imm:
                class_name += "text-primary bg-primary-subtle "

            class_name += "text-secondary bg-secondary-subtle" if Date(year, month, day).get_day_of_week() in ["Sat", "Sun"] else ""
            # data_html += f"<td class=\"text-center {class_name}\">{day}</td>"
            row.append(Cell(str(day), "td", f"text-center {class_name}"))

        rows.append(row)

        for _ in range(days_in_row - (offset + days_in_month)):
            row.append(Cell("", "td", ""))

    extra_cell_class = "px-1 py-2 align-middle"
    table_html = Table(
        headers=headers,
        rows=rows,
        class_name="table table-hover font-monospace",
        styles="width:0em;white-space: nowrap;"
    ).to_html(extra_cell_class)

    return render_template('layout.html', content=table_html)
